"""Read-only current release audit: preservation, public resources, secret patterns, deployment gate."""
from pathlib import Path
import subprocess,json,hashlib,re,tarfile
R=Path(__file__).resolve().parents[2];D=R/'docs/audits/pr11-final';P=R/'.cache/public'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((D/'start-baseline.json').read_text())['files']
authorized={'.gitignore','tools/animation-lock/__pycache__/build_public.cpython-311.pyc','.github/workflows/deploy-pages.yml','.github/workflows/validate.yml','app.js','index.html','package.json','service-worker.js','styles.css','tests/phase24-preservation.cjs','tests/coach-animation-lock-browser.cjs','tests/coach-animation-lock-migration.cjs','tools/animation-lock/build_public.py'}
missing=[p for p in base if not (R/p).is_file()];changed=[p for p,h in base.items() if (R/p).is_file() and sha(R/p)!=h];assert not missing;assert set(changed)<=authorized,(set(changed)-authorized)
files=sorted(set(subprocess.check_output(['git','ls-files','-co','--exclude-standard'],cwd=R).decode().splitlines()));new=[p for p in files if p not in base];prohibited=[p for p in new if Path(p).suffix.lower() in ['.age','.agepart','.zip','.gz','.tar','.bundle','.key','.pem','.c3d','.bvh','.glb']];assert not prohibited,prohibited
patterns={'private-key':rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----[\r\n]+[A-Za-z0-9+/=\r\n]{64,}-----END ','age-key':rb'AGE-SECRET-KEY-1[0-9A-Z]{50,}','github-token':rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b','aws-key':rb'\bAKIA[0-9A-Z]{16}\b'};findings=[]
for p in files:
 b=(R/p).read_bytes()
 for kind,pat in patterns.items():
  if re.search(pat,b):findings.append({'path':p,'kind':kind})
assert not findings,findings
public=sorted(str(p.relative_to(P)) for p in P.rglob('*') if p.is_file());expected=json.loads((D/'public-build.json').read_text())['publicFiles'];assert public==expected;assert len(public)==30
assert not any(p.startswith(('docs/','tools/','tests/','.git/','archives-encrypted/')) or Path(p).suffix in ['.mp4','.bvh','.c3d','.age','.agepart','.gz','.zip','.bundle'] for p in public)
workflow=(R/'.github/workflows/deploy-pages.yml').read_text();assert not re.search(r'^  push:',workflow,re.M);assert 'workflow_dispatch:' in workflow and "inputs.confirm_deployment == true" in workflow and "github.ref == 'refs/heads/main'" in workflow;assert 'path: .cache/public' in workflow
assert sha(R/'assets/coach/coach.glb')=='1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb'
archives=json.loads((R/'docs/coach/phase26/archive-register.json').read_text())['archives'];seal=json.loads((R/'docs/coach/phase26/evidence-seal.json').read_text());archives+=[{'archive':seal['path'],'sha256':seal['sha256']}]
for a in archives:assert sha(R/a['archive'])==a['sha256']
report={'baselineFiles':len(base),'unchanged':len(base)-len(changed),'authorizedChanges':changed,'deleted':missing,'historicalReportsUnchanged':not any(p.startswith('docs/coach/') for p in changed),'originalGLBUnchanged':True,'fourPhase26ArchivesUnchanged':True,'newPlaintextArchivesOrKeys':prohibited,'secretPatternFindings':findings,'secretScanLimit':'Known patterns only; not proof of absence of every secret or personal datum. Existing public scientific history remains exposed.','publicFiles':public,'automaticDeploymentOnMerge':False,'ownerConfirmedDispatchRequired':True}
(D/'release-audit.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
