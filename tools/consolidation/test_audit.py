"""Read-only consolidation contracts; no pipelines or source motion generation."""
import unittest,json,hashlib,re
from pathlib import Path
D=Path('docs/coach/phase23')
class Consolidation(unittest.TestCase):
 def test_reports_and_links(self):
  for n in ['git-audit','interface-audit','cache-audit','coach-3d-audit','expertise-audit','ci-audit','decision-report']:
   p=D/(n+'.md');self.assertGreater(p.stat().st_size,300)
   for u in re.findall(r'\]\(([^)]+)\)',p.read_text()):
    if not u.startswith('https://'):self.assertTrue((p.parent/u).exists(),u)
 def test_preservation(self):
  j=json.loads((D/'git-evidence.json').read_text())
  for p,h in j['baseline'].items():self.assertEqual(hashlib.sha256(Path(p).read_bytes()).hexdigest(),h,p)
 def test_ci(self):
  j=json.loads((D/'ci-evidence.json').read_text());self.assertEqual(j['total_count'],3)
  for r in j['runs']:self.assertEqual(r['head_sha'],j['reference']);self.assertEqual(r['status'],'completed');self.assertEqual(r['conclusion'],'success')
  self.assertEqual(sum(x['conclusion']=='skipped' for r in j['runs'] for x in r['jobs']),4)
 def test_cache_and_home(self):
  j=json.loads((D/'browser-audit.json').read_text());self.assertEqual(j['status'],'PASS');self.assertEqual(len(j['home']['widths']),8);self.assertTrue(j['home']['realOverridesIllustration']);self.assertTrue(j['cache']['warmCoachOffline']);self.assertTrue(j['cache']['successfulUpdate']['oldShellRemoved']);self.assertEqual(j['cache']['failedUpdate']['workerState'],'redundant')
 def test_motion_scope(self):
  j=json.loads((D/'trajectory-regression.json').read_text());self.assertEqual(len(j['clips']),8);self.assertEqual(j['failures'],[]);self.assertEqual(j['status'],'PASS');self.assertIn('Non prêt',(D/'decision-report.md').read_text());self.assertIn('restent jouables',(D/'coach-3d-audit.md').read_text())
if __name__=='__main__':unittest.main()
