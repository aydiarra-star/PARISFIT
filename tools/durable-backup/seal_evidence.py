"""Seal final Phase26 reports/tools separately, with external non-self-referential receipt."""
from pathlib import Path,PurePosixPath
import json,hashlib,tarfile,datetime,ast,re
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase26';B=R/'.cache/phase26-work/backups';T=R/'.cache/phase26-work/evidence-restored'
def sha(b):return hashlib.sha256(b).hexdigest()
assert not T.exists();T.mkdir();archive=B/'phase26-evidence.tar.gz';assert not archive.exists()
paths=sorted([p for p in D.rglob('*') if p.is_file() and p.name not in ['evidence-seal.json','manifest.json']]+[p for p in (R/'tools/durable-backup').glob('*.py')]);rows=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in paths]
# Apply the same six redacted secret patterns to newly generated evidence/tool files.
parsed=ast.parse((R/'tools/durable-backup/security_scan.py').read_text());rules=next(ast.literal_eval(n.value) for n in parsed.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='patterns' for t in n.targets) and isinstance(n.value,ast.Dict));findings=[]
for p in paths:
 for kind,pattern in rules.items():
  if re.search(pattern,p.read_bytes()):findings.append({'path':str(p.relative_to(R)),'kind':kind})
assert not findings,'Review required; no values displayed'
created=datetime.datetime.now(datetime.timezone.utc).isoformat()
with tarfile.open(archive,'x:gz',compresslevel=1) as t:
 for p in paths:t.add(p,arcname=str(p.relative_to(R)),recursive=False)
with tarfile.open(archive,'r:gz') as t:
 members=t.getmembers();assert len(members)==len(rows)
 for m in members:
  rel=PurePosixPath(m.name);assert m.isfile() and not rel.is_absolute() and '..' not in rel.parts
  dest=T/m.name;dest.parent.mkdir(parents=True,exist_ok=True)
  with dest.open('xb') as f:f.write(t.extractfile(m).read())
assert all(sha((T/r['path']).read_bytes())==r['sha256'] for r in rows)
receipt={'path':str(archive.relative_to(R)),'bytes':archive.stat().st_size,'fileCount':len(rows),'sha256':sha(archive.read_bytes()),'createdAtObservedUTC':created,'restore':'PASS','restoredFiles':len(rows),'secretPatternMatches':findings,'certifiesNoSecret':False,'durable':False,'uploaded':False,'files':rows,'receiptExcludedFromArchive':True};(D/'evidence-seal.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k!='files'},indent=2))
