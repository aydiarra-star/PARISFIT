"""Phase28 read-only preflight. No key discovery, encryption, uploads, ref changes or deletion."""
from pathlib import Path
import json,hashlib,tarfile,csv,subprocess,os,datetime,re
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase28';D.mkdir(exist_ok=True)
def read(p):return json.loads((R/p).read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def save(n,v):(D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def table(n,rows,fields):
 with (D/n).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
reg=read('docs/coach/phase26/archive-register.json');seal=read('docs/coach/phase26/evidence-seal.json')
archives=[{'path':r['archive'],'bytes':r['bytes'],'sha256':r['sha256']} for r in reg['archives']]+[{'path':seal['path'],'bytes':seal['bytes'],'sha256':seal['sha256']}]
for a in archives:
 p=R/a['path'];assert p.is_file(),a['path'];assert p.stat().st_size==a['bytes'] and sha(p)==a['sha256'];a['sha256Verified']=True
rows=read('docs/coach/phase26/backup-file-manifest.json');assert len(rows)==1783
for name in ['project.tar.gz','working-data.tar.gz']:
 expected={r['path']:r for r in rows if r['archive']==name};seen=set()
 with tarfile.open(R/'.cache/phase26-work/backups'/name) as t:
  for m in t:
   assert m.isfile() and m.name in expected and m.name not in seen;seen.add(m.name);r=expected[m.name];assert m.size==r['bytes'];assert hashlib.sha256(t.extractfile(m).read()).hexdigest()==r['sha256']
 assert seen==set(expected)
# Re-check the independently restored Phase26 Git object store, not a post-encryption restore.
objects=read('docs/coach/phase26/git-object-manifest.json');assert len(objects)==1779
store=R/'.cache/phase26-work/restored/objects';assert store.is_dir();assert not (store/'info/alternates').exists()
env=dict(os.environ,GIT_OBJECT_DIRECTORY=str(store),GIT_ALTERNATE_OBJECT_DIRECTORIES='');proc=subprocess.Popen(['git','cat-file','--batch'],cwd=R,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
for oid,r in objects.items():
 proc.stdin.write((oid+'\n').encode());proc.stdin.flush();meta=proc.stdout.readline().decode().split();assert len(meta)==3 and meta[1]==r['type'] and int(meta[2])==r['bytes'];data=proc.stdout.read(int(meta[2]));proc.stdout.read(1);assert hashlib.sha256(data).hexdigest()==r['sha256']
proc.stdin.close();assert proc.wait()==0
# Evidence tar is supplemental to the 1783-file scope.
with tarfile.open(R/seal['path']) as t:
 ms=t.getmembers();assert len(ms)==seal['fileCount'];expected={r['path']:r for r in seal['files']};assert set(m.name for m in ms)==set(expected)
 for m in ms:assert m.isfile() and hashlib.sha256(t.extractfile(m).read()).hexdigest()==expected[m.name]['sha256']
assert all(sha(R/r['path'])==r['sha256'] for r in rows)
table('input-files.csv',rows,['path','bytes','sha256','archive']);table('input-git-objects.csv',[{'gitObject':oid,**r} for oid,r in objects.items()],['gitObject','type','bytes','sha256'])
# Exact existing publication artifact, no rebuild (which would delete its old directory).
public=read('docs/coach/phase25/publication-verification.json')['files'];P=R/'.cache/public';actual=sorted(str(p.relative_to(P)) for p in P.rglob('*') if p.is_file());assert actual==sorted(r['path'] for r in public)
patterns=[rb'AGE-SECRET-KEY-1[0-9A-Z]{50,}',rb'\bgh[pousr]_[A-Za-z0-9]{30,}\b',rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
for r in public:
 p=P/r['path'];assert sha(p)==r['sha256'];assert not any(re.search(pat,p.read_bytes()) for pat in patterns)
# Archive metadata only; no real key supplied or confirmed by owner.
result={'status':'BLOCKED_OWNER_KEY_MISSING','createdAtObservedUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':'Phase26 archives exclusively','archives':archives,'filesInTarVerified':len(rows),'gitObjectsInExistingPhase26RestoreVerified':len(objects),'supplementalEvidenceFilesVerified':seal['fileCount'],'publicArtifactFilesUnchanged':len(public),'knownSecretPatternsInPublicArtifact':0,'completeSecretAudit':False,'productionRecipientConfirmed':False,'keySearchedOrRead':False,'encryptionPerformed':False,'ciphertextVolumesCreated':0,'phase28PostEncryptionRestorePerformed':False,'missingActionsArtifacts':216,'artifactsBasis':'Phase26 metadata and failed download attempts; no new retrieval','sourceFilesUnchanged':True,'branch':subprocess.check_output(['git','branch','--show-current'],cwd=R).decode().strip(),'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()}
save('preflight-result.json',result);print(json.dumps(result,indent=2))
