"""Documentary invariants only: no historical pipelines or trajectories."""
from pathlib import Path
import csv,json,hashlib,subprocess,re
D=Path('docs/coach/phase19');ref='71bae7d1ed34227b2fc2c1c4e79aa7fdf1be22f1'
required=['dependency-version-inventory.md','ab01-original-logs-inventory.md','marker-placement-evidence.md','capture-synchronization-evidence.md','missing-evidence-register.csv','independent-review-readiness.md','decision-report.md']
for n in required:assert (D/n).stat().st_size>100
rows=list(csv.DictReader((D/required[4]).open()));assert len(rows)==18
assert all(r['statut'] in ['vérifié','partiel','absent','contradictoire'] for r in rows)
for p in D.glob('*.md'):
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not link.startswith('https://'):assert (p.parent/link).exists(),(p,link)
j=json.loads((D/'archive-probe.json').read_text());assert not j.get('error') and j['totalRangeBytes']<=24000000
assert all(not f.get('error') for f in j['files'])
logs=[x for f in j['files'] for x in f.get('acquired',[]) if x['path'].endswith('.log')];assert len(logs)==2 and all(x['sha256'] for x in logs)
assert any('AB01\\Squat\\1\\' in t['text'] for l in logs for t in l.get('targetMentions',[]))
allowed=['.github/workflows/validate.yml']
files=subprocess.check_output(['git','ls-tree','-r','--name-only',ref]).decode().splitlines();changed=[]
for p in files:
 b=subprocess.check_output(['git','show',f'{ref}:{p}']);current=Path(p)
 if not current.exists() or current.read_bytes()!=b:changed.append(p)
assert changed==allowed,changed
report={'referenceCommit':ref,'trackedReferenceFiles':len(files),'unchangedCount':len(files)-len(changed),'changedExistingFiles':changed,'justification':'CI authoring disabled unless explicit workflow_dispatch legacy_authoring=true; no runtime changes','rocketboxSHA256':hashlib.sha256(Path('assets/coach/coach.glb').read_bytes()).hexdigest(),'sourceC3D':{}}
m=json.loads(Path('docs/coach/phase17/source-manifest.json').read_text())
for x in m['files']:
 if x['path'].endswith('.c3d'):
  actual=hashlib.sha256((Path('.cache/phase17/source')/x['path']).read_bytes()).hexdigest();assert actual==x['sha256'];report['sourceC3D'][x['path']]=actual
(D/'preservation-check.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS: 7 deliverables,18 questions,links,2 original logs,reference preservation,C3D hashes')
