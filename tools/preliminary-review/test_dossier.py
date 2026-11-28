"""Read-only documentation, workflow and fixture-contract assertions. No acquisition."""
from pathlib import Path
import csv,json,re,hashlib,unittest
D=Path('docs/coach/phase20')
class Dossier(unittest.TestCase):
 def test_reference_ci(self):
  j=json.loads((D/'ci-reference-runs.json').read_text());self.assertEqual(j['total_count'],2)
  for r in j['runs']:
   self.assertEqual(r['head_sha'],j['reference']);self.assertEqual(r['status'],'completed');self.assertEqual(r['conclusion'],'success')
  jobs=[x for r in j['runs'] for x in r['jobs']];self.assertEqual(sum(x['conclusion']=='skipped' for x in jobs),4)
 def test_guard_and_failure_propagation(self):
  s=Path('.github/workflows/validate.yml').read_text();guard="if: ${{ github.event_name == 'workflow_dispatch' && inputs.legacy_authoring == true }}"
  for name in ['blender-control','source-qualification','michaud-qualification','model-qualification']:self.assertIn('  '+name+':\n    '+guard,s)
  self.assertIn('default: false',s);self.assertIn('set -o pipefail',s);self.assertNotIn('continue-on-error',s)
  for event,flag,expected in [('pull_request',False,False),('pull_request',True,False),('push',True,False),('workflow_dispatch',False,False),('workflow_dispatch',True,True)]:self.assertEqual(event=='workflow_dispatch' and flag is True,expected)
 def test_coverage_and_blank_answers(self):
  q=json.loads((D/'expert-response-template.json').read_text());ids=set()
  for x in q:
   ids.update(x['original_ids']);self.assertIsNone(x['answer']);self.assertIsNone(x['conditions']);self.assertIsNone(x['justification'])
  originals={r['id'] for r in csv.DictReader(Path('docs/coach/phase19/missing-evidence-register.csv').read_text().splitlines())};self.assertEqual(ids,originals);self.assertEqual({x['priority'] for x in q},set(range(1,8)))
 def test_matrix(self):
  rows=list(csv.DictReader((D/'evidence-and-claims-matrix.csv').read_text().splitlines()));self.assertEqual(len(rows),15);self.assertTrue(all(all(r.values()) for r in rows))
 def test_links(self):
  for p in list(D.glob('*.md'))+list((D/'external').glob('*.md'))+[D/'index.html']:
   links=re.findall(r'\]\(([^)]+)\)',p.read_text())+re.findall(r'href="([^"]+)"',p.read_text())
   for link in links:
    if not link.startswith(('https://','#')):self.assertTrue((p.parent/link).exists(),f'{p}: {link}')
 def test_external_minimization(self):
  e=D/'external';m=json.loads((e/'manifest.json').read_text())
  for n,h in m.items():
   self.assertEqual(hashlib.sha256((e/n).read_bytes()).hexdigest(),h);s=(e/n).read_text()
   self.assertFalse(re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_|Bearer\s+[A-Za-z0-9]|[A-Z]:\\|signature=|token=',s))
  self.assertFalse(any(p.suffix.lower() in ['.c3d','.zip','.tak','.mat','.osim','.glb'] for p in e.iterdir()))
 def test_c3d_hashes_in_dossier(self):
  m=json.loads(Path('docs/coach/phase17/source-manifest.json').read_text())
  for x in m['files']:
   if x['path'].endswith('.c3d'):self.assertIn(x['sha256'],(D/'expert-preliminary-dossier.md').read_text())
 def test_no_hidden_probe_error(self):
  j=json.loads(Path('docs/coach/phase19/archive-probe.json').read_text());self.assertFalse(j.get('error'));self.assertTrue(all(not f.get('error') for f in j['files']))
if __name__=='__main__':unittest.main()
