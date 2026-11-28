"""Read-only bounded inventory: fetched refs + project worktree/cache, no credentials read."""
from pathlib import Path
import subprocess,json,csv,hashlib,struct,collections,re
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase25';D.mkdir(exist_ok=True)
def git(*args):return subprocess.check_output(['git',*args],cwd=R)
def sha(b):return hashlib.sha256(b).hexdigest()
def write(name,data):(D/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
def csvwrite(name,rows,cols):
 with (D/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
def category(p):
 e=Path(p).suffix.lower()
 if e in ['.glb','.gltf']:return '3d-model'
 if e in ['.bvh','.c3d','.trc','.mot','.sto','.amc','.asf','.fbx','.osim','.vsk']:return 'capture-or-biomechanical-model'
 if e in ['.mp4','.webm','.mov','.avi']:return 'video'
 if e in ['.zip','.gz','.tgz','.tar','.7z']:return 'archive-needs-nested-review'
 if p.startswith(('tools/','tests/')) or (e=='.html' and p!='index.html'):return 'diagnostic-or-test-tool'
 if p.startswith(('docs/','.cache/')):return 'report-evidence-or-working-data'
 return 'application-or-infrastructure'
def glb(b):
 if b[:4]!=b'glTF':return None
 try:
  n=struct.unpack_from('<I',b,12)[0];g=json.loads(b[20:20+n]);return {'animationCount':len(g.get('animations',[])),'clipNames':[a.get('name') for a in g.get('animations',[])],'accessors':len(g.get('accessors',[]))}
 except Exception:return {'parseError':True}
# Snapshot pre-existing files. Exclude dependencies, Git metadata, our own outputs, generated backup.
rows=[];skip={'.git','node_modules','.venv','__pycache__'}
import os
for root,dirs,files in os.walk(R):
 dirs[:]=[d for d in dirs if d not in skip and not (Path(root)/d).relative_to(R).as_posix().startswith(('.cache/phase25','docs/coach/phase25','tools/confidentiality-audit'))]
 for name in files:
  p=Path(root)/name
  if p.is_symlink():continue
  rel=p.relative_to(R).as_posix();b=p.read_bytes();rows.append({'path':rel,'bytes':len(b),'sha256':sha(b),'category':category(rel),'scope':'ignored-cache' if rel.startswith('.cache/') else 'project-worktree','glb':glb(b)})
rows.sort(key=lambda x:x['path']);write('worktree-inventory.json',rows)
commits=git('rev-list','--all').decode().splitlines();pairs={};trees={}
for commit in commits:
 entries=[]
 for rec in git('ls-tree','-rz',commit).split(b'\0'):
  if not rec:continue
  head,p=rec.split(b'\t',1);mode,typ,oid=head.decode().split();p=p.decode()
  if typ!='blob':continue
  entries.append((p,oid));q=pairs.setdefault((p,oid),{'path':p,'gitBlob':oid,'category':category(p),'commitCount':0,'exampleCommit':commit});q['commitCount']+=1
 trees[commit]=entries
# Hash each unique blob and scan textual content with values never emitted.
patterns={'private-key':rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----','github-token':rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b','aws-key':rb'\bAKIA[0-9A-Z]{16}\b','email':rb'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}','credential-assignment':rb'(?i)(?:password|api_key|access_token|secret)\s*[:=]\s*[\x22\x27][^\x22\x27\s]{8,}[\x22\x27]'}
objects={};findings=[];proc=subprocess.Popen(['git','cat-file','--batch'],cwd=R,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
for oid in sorted({x[1] for x in pairs}):
 proc.stdin.write((oid+'\n').encode());proc.stdin.flush();head=proc.stdout.readline().decode().split();b=proc.stdout.read(int(head[2]));proc.stdout.read(1)
 objects[oid]={'bytes':len(b),'sha256':sha(b),'glb':glb(b),'lfsPointer':b.startswith(b'version https://git-lfs.github.com/spec/v1')}
 if b'\0' not in b:
  for kind,pattern in patterns.items():
   count=len(re.findall(pattern,b))
   if count:findings.append({'gitBlob':oid,'type':kind,'count':count,'paths':[p for p,o in pairs if o==oid]})
proc.stdin.close();proc.wait()
for q in pairs.values():q.update(objects[q['gitBlob']])
write('history-inventory.json',sorted(pairs.values(),key=lambda x:(x['path'],x['gitBlob'])))
refs=[]
for line in git('for-each-ref','--format=%(objectname) %(refname)').decode().splitlines():
 oid,ref=line.split(' ',1);commit=git('rev-parse',ref+'^{commit}').decode().strip();entries=trees[commit];counts=collections.Counter(category(p) for p,o in entries)
 refs.append({'ref':ref,'commit':commit,'files':len(entries),'categories':dict(counts),'animatedGLBs':[p for p,o in entries if (objects[o]['glb'] or {}).get('animationCount',0)>0],'captureFiles':[p for p,o in entries if category(p)=='capture-or-biomechanical-model']})
write('refs-exposure.json',refs);write('sensitivity-findings.json',{'scope':'all reachable textual Git blobs; values intentionally omitted','findings':findings,'binarySemanticReview':'not performed; no assertion of absence of personal data'})
summary={'commits':len(commits),'refs':len(refs),'remoteBranches':sum(x['ref'].startswith('refs/remotes/origin/') and not x['ref'].endswith('/HEAD') for x in refs),'tags':sum(x['ref'].startswith('refs/tags/') for x in refs),'uniqueGitBlobs':len(objects),'pathBlobVersions':len(pairs),'historicalCategories':dict(collections.Counter(q['category'] for q in pairs.values())),'worktreeFiles':len(rows),'worktreeBytes':sum(x['bytes'] for x in rows),'worktreeCategories':dict(collections.Counter(x['category'] for x in rows)),'animatedGLBVersions':sum((x['glb'] or {}).get('animationCount',0)>0 for x in objects.values()),'lfsPointers':sum(x['lfsPointer'] for x in objects.values()),'secretPatternCounts':dict(collections.Counter(x['type'] for x in findings))}
write('inventory-summary.json',summary);print(json.dumps(summary,indent=2))
