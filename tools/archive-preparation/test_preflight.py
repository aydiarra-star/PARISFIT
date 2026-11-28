"""Validate an honestly blocked Phase28; success is NOT an encryption/restore success."""
from pathlib import Path
import unittest,json,csv,hashlib,subprocess
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase28'
class Preparation(unittest.TestCase):
 def test_gate_closed(self):
  r=json.loads((D/'preflight-result.json').read_text());self.assertEqual(r['status'],'BLOCKED_OWNER_KEY_MISSING')
  for k in ['productionRecipientConfirmed','keySearchedOrRead','encryptionPerformed','phase28PostEncryptionRestorePerformed']:self.assertFalse(r[k])
  self.assertEqual(r['ciphertextVolumesCreated'],0);self.assertEqual(r['missingActionsArtifacts'],216)
 def test_precise_scope(self):
  for name,n,key in [('input-files.csv',1783,'path'),('input-git-objects.csv',1779,'gitObject')]:
   with (D/name).open() as f:rows=list(csv.DictReader(f))
   self.assertEqual(len(rows),n);self.assertEqual(len({r[key] for r in rows}),n);self.assertTrue(all(len(r['sha256'])==64 for r in rows))
 def test_no_fake_checksums(self):
  s=(D/'volume-checksums.txt').read_text();self.assertIn('BLOCKED_OWNER_KEY_MISSING',s);self.assertTrue(all(not l.strip() or l.startswith('#') for l in s.splitlines()))
 def test_prior_evidence(self):
  for phase in [26,27]:
   folder=R/f'docs/coach/phase{phase}';m=json.loads((folder/'manifest.json').read_text())['files']
   for p,h in m.items():self.assertEqual(hashlib.sha256((folder/p).read_bytes()).hexdigest(),h,str(folder/p))
 def test_branch(self):self.assertEqual(subprocess.check_output(['git','branch','--show-current'],cwd=R).strip(),b'arena/a03f64da-parisfit')
 def test_deliverables(self):
  for n in ['archive-manifest','encryption-report','restore-verification','publication-exclusion-audit','recovery-instructions','decision-report']:self.assertGreater((D/(n+'.md')).stat().st_size,1000)
if __name__=='__main__':unittest.main(verbosity=2)
