"""Create local-only backups and restore WITHOUT initializing a repo or changing branches/refs.
No network, uploads, deletions, credential files, or history rewriting. Refuses overwrites.
"""
from pathlib import Path,PurePosixPath
import os,json,hashlib,subprocess,tarfile,datetime,re
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase26';B=R/'.cache/phase26-work/backups';T=R/'.cache/phase26-work/restored'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def save(n,v):(D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def git(*a,env=None,input=None):return subprocess.check_output(['git',*a],cwd=R,env=env,input=input,stderr=subprocess.PIPE)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
B.mkdir(parents=True,exist_ok=False);T.mkdir(parents=True,exist_ok=False)
# Project content + caches, keeping previous reports and dirty/untracked work, excluding secrets/config.
rows=[];excluded=[]
for root,dirs,files in os.walk(R):
 keep=[]
 for d in dirs:
  rel=(Path(root)/d).relative_to(R).as_posix()
  if d in ['.git','node_modules','.venv','__pycache__'] or rel.startswith(('.cache/phase25-backup','.cache/phase26-work','docs/coach/phase26')):excluded.append(rel+'/');continue
  keep.append(d)
 dirs[:]=keep
 for f in files:
  p=Path(root)/f;rel=p.relative_to(R).as_posix()
  if p.is_symlink() or f in ['.env','.netrc','.git-credentials'] or f.startswith('.env.'):
   excluded.append(rel);continue
  rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p),'archive':'working-data.tar.gz' if rel.startswith('.cache/') else 'project.tar.gz'})
rows.sort(key=lambda r:r['path']);save('backup-file-manifest.json',rows);save('exclusions.json',sorted(excluded))
refs=git('for-each-ref','--format=%(objectname) %(refname)').decode().splitlines();save('refs-manifest.json',refs)
reports=[]
for name in ['project.tar.gz','working-data.tar.gz']:
 selected=[r for r in rows if r['archive']==name];p=B/name;created=now()
 with tarfile.open(p,'x:gz',compresslevel=1) as tar:
  for r in selected:tar.add(R/r['path'],arcname=r['path'],recursive=False)
 # Actual isolated disk restoration, refusing links and traversal.
 with tarfile.open(p,'r:gz') as tar:
  members=tar.getmembers();assert len(members)==len(selected)
  for m in members:
   rel=PurePosixPath(m.name);assert m.isfile() and not rel.is_absolute() and '..' not in rel.parts
   dest=T/'files'/m.name;dest.parent.mkdir(parents=True,exist_ok=True)
   with dest.open('xb') as out:out.write(tar.extractfile(m).read())
 assert all(sha(T/'files'/r['path'])==r['sha256'] for r in selected)
 reports.append({'archive':str(p.relative_to(R)),'createdAtObservedUTC':created,'bytes':p.stat().st_size,'fileCount':len(selected),'sha256':sha(p),'restore':'PASS','restoredFileCount':len(selected)})
created=now();bundle=B/'history.bundle';git('bundle','create',str(bundle),'--all');verify=git('bundle','verify',str(bundle)).decode();heads=git('bundle','list-heads',str(bundle)).decode().splitlines()
# Load ONLY bundle pack into an isolated object store, never create or checkout another repository.
objects=T/'objects';objects.mkdir();env=dict(os.environ,GIT_OBJECT_DIRECTORY=str(objects),GIT_ALTERNATE_OBJECT_DIRECTORIES='')
with bundle.open('rb') as f:
 header=[]
 while True:
  line=f.readline()
  if not line.strip():break
  header.append(line)
 pack=f.read()
packResult=git('index-pack','--stdin','--strict',env=env,input=pack).decode().strip()
head=git('rev-parse','HEAD').decode().strip()
sourceObjects=git('rev-list','--objects','--all','--no-object-names').decode().splitlines();unique=sorted(set(sourceObjects))
# Batch raw object SHA256 comparison source versus restored store, including commits/trees/blobs.
def object_hashes(env):
 proc=subprocess.Popen(['git','cat-file','--batch'],cwd=R,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE);out={}
 for oid in unique:
  proc.stdin.write((oid+'\n').encode());proc.stdin.flush();meta=proc.stdout.readline().decode().split();assert len(meta)==3,meta
  data=proc.stdout.read(int(meta[2]));proc.stdout.read(1);out[oid]={'type':meta[1],'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
 proc.stdin.close();assert proc.wait()==0;return out
original=object_hashes(None);restored=object_hashes(env);assert original==restored
# Every recorded ref target exists from the isolated store, independent of source objects.
for line in heads:
 oid,ref=line.split(' ',1);assert git('cat-file','-t',oid,env=env).strip() in [b'commit',b'tag']
commits=git('rev-list','--all').decode().splitlines();assert all(restored[c]['type']=='commit' for c in commits)
# Reconstruct committed files from isolated Git objects; no checkout or new branch.
committed=T/'committed-head';committed.mkdir();raw=git('archive',head,env=env);(T/'committed-head.tar').write_bytes(raw)
with tarfile.open(T/'committed-head.tar') as tar:
 for m in tar:
  if m.isdir():continue
  rel=PurePosixPath(m.name);assert m.isfile() and not rel.is_absolute() and '..' not in rel.parts
  p=committed/m.name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(tar.extractfile(m).read())
assert not (objects/'info/alternates').exists()
reports.append({'archive':str(bundle.relative_to(R)),'createdAtObservedUTC':created,'bytes':bundle.stat().st_size,'fileCount':sum(p.is_file() for p in committed.rglob('*')),'fileCountMeaning':'files at HEAD; full history measured separately in objects and path versions','sha256':sha(bundle),'restore':'PASS','refsIncludingHEAD':len(heads),'commits':len(commits),'gitObjectsVerified':len(restored),'gitBlobsVerified':sum(x['type']=='blob' for x in restored.values()),'indexPackStrict':packResult})
save('git-object-manifest.json',original);save('archive-register.json',{'sessionDate':'2026-11-27','clockNotice':'Observed sandbox UTC clock reports 2026-11-28; timestamps are retained without claiming session date equivalence.','archives':reports,'durable':False,'uploaded':False,'isolatedRestoreDirectory':str(T.relative_to(R)),'gitObjectStoreIndependent':True,'sourceRefsUnchanged':refs==git('for-each-ref','--format=%(objectname) %(refname)').decode().splitlines(),'sourceFilesUnmodified':all(sha(R/r['path'])==r['sha256'] for r in rows)})
print(json.dumps(reports,indent=2))
