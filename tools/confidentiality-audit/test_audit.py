"""Checks the bounded Phase25 evidence and preservation without network or runtime changes."""
import unittest,json,hashlib,subprocess,struct
from pathlib import Path
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase25'
def read(p):return json.loads((D/p).read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class Audit(unittest.TestCase):
 def test_worktree_preserved(self):
  for x in read('worktree-inventory.json'):self.assertEqual(digest(R/x['path']),x['sha256'],x['path'])
 def test_history(self):
  data=read('history-inventory.json');self.assertEqual(len(data),read('inventory-summary.json')['pathBlobVersions'])
  self.assertEqual(len({r['gitBlob'] for r in data}),read('inventory-summary.json')['uniqueGitBlobs'])
  self.assertEqual(subprocess.check_output(['git','rev-parse','--is-shallow-repository'],cwd=R).strip(),b'false')
  self.assertEqual(subprocess.check_output(['git','branch','--show-current'],cwd=R).strip(),b'arena/a03f64da-parisfit')
 def test_publication(self):
  report=read('publication-verification.json');self.assertEqual(report['allowedCount'],28);self.assertEqual(report['deniedCount'],866)
  for t in report['httpTests']:self.assertEqual(t['status'],t['expected'])
  for x in report['files']:self.assertEqual(digest(R/'.cache/public'/x['path']),x['sha256'])
  self.assertEqual(report['staticGLB']['animations'],0);self.assertTrue(report['staticGLB']['exactReproducibleDerivative'])
 def test_backup(self):
  b=read('backup-verification.json');self.assertFalse(b['durableOrOffsite']);self.assertFalse(b['uploaded']);self.assertEqual(b['filesVerified'],len(read('worktree-inventory.json')))
  for x in b['archives']:self.assertEqual(digest(R/x['path']),x['sha256'])
 def test_artifacts(self):
  a=read('action-artifacts.json');self.assertEqual(a['total_count'],a['listed_count']);self.assertEqual(len(a['artifacts']),a['listed_count']);self.assertEqual(len({x['id'] for x in a['artifacts']}),a['listed_count'])
 def test_reports(self):
  for p in ['resource-inventory','git-history-exposure','publication-audit','solution-comparison','backup-integrity-report','decision-report']:self.assertGreater((D/(p+'.md')).stat().st_size,1000)
if __name__=='__main__':unittest.main(verbosity=2)
