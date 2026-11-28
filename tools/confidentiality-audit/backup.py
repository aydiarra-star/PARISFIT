"""Local-only safety copy; never a durable/offsite backup claim. Does not remove originals."""
from pathlib import Path
import json,hashlib,tarfile,subprocess
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase25';B=R/'.cache/phase25-backup';B.mkdir(exist_ok=True)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
rows=json.loads((D/'worktree-inventory.json').read_text());bundle=B/'history.bundle';archive=B/'worktree-and-cache.tar.gz'
# Refuse overwrite, to preserve first backup attempt/evidence.
assert not bundle.exists() and not archive.exists()
subprocess.run(['git','bundle','create',str(bundle),'--all'],cwd=R,check=True)
verify=subprocess.run(['git','bundle','verify',str(bundle)],cwd=R,capture_output=True,text=True,check=True)
with tarfile.open(archive,'w:gz',compresslevel=1) as t:
 for r in rows:
  p=R/r['path'];assert sha(p)==r['sha256'],r['path'];t.add(p,arcname=r['path'],recursive=False)
checks=[]
with tarfile.open(archive,'r:gz') as t:
 for m,r in zip(t,rows):
  assert m.name==r['path'];assert m.size==r['bytes'];b=t.extractfile(m).read();assert hashlib.sha256(b).hexdigest()==r['sha256'];checks.append(m.name)
assert len(checks)==len(rows)
# Check the actual pack payload in the bundle without rewriting any ref/history.
with bundle.open('rb') as f:
 while f.readline().strip():pass
 pack=B/'history.pack'
 with pack.open('xb') as out:
  for b in iter(lambda:f.read(1024*1024),b''):out.write(b)
p=subprocess.run(['git','index-pack','--strict',str(pack)],cwd=R,capture_output=True,text=True,check=True)
report={'location':'.cache/phase25-backup','durableOrOffsite':False,'encrypted':False,'uploaded':False,'filesVerified':len(checks),'tarPayloadSHA256AllMatch':True,'originalsUnmodified':all(sha(R/r['path'])==r['sha256'] for r in rows),'bundleVerify':verify.stdout+verify.stderr,'packStrictCheck':p.stdout.strip(),'archives':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in [bundle,archive]],'exclusions':['Git credentials/config/hooks/reflogs','node_modules','.venv','__pycache__','Phase25 outputs','remote Actions artifacts/logs, GitHub settings/issues/PR metadata beyond fetched refs'],'warning':'Cache is ephemeral and not captured in Arena snapshots. Not a sufficient backup for deletion or history rewriting.'}
(D/'backup-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='bundleVerify'},indent=2))
