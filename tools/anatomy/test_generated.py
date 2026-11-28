"""Numerical implementation contracts, not physiological approval."""
import json,math,unittest
from pathlib import Path
root=Path('.cache/phase11')
class Generated(unittest.TestCase):
 def test_three_equal_inputs(self):
  sources=[(root/m/'source-samples.json').read_bytes() for m in 'ABC'];self.assertEqual(sources[0],sources[1]);self.assertEqual(sources[1],sources[2])
 def test_fixed_human_rig_extent(self):
  for m in 'ABC':
   data=json.loads((root/m/'geometry.json').read_text())
   for f in data['frames']:
    self.assertEqual(len(f['joints']),80)
    pelvis=f['joints']['Bip01_Pelvis']['position']
    # Broad implementation bound for this fixed Rocketbox adult model.
    self.assertLess(max(math.dist(pelvis,j['position']) for j in f['joints'].values()),2)
 def test_baseline_hash(self):
  r=json.loads((root/'A/report.json').read_text());self.assertEqual(r['exportSHA256'],'fac4d26f57590f99951058c2532d6a96c4195cd8d39fbb797b35b19e3fcb7e7e')
 def test_solver_accuracy_not_admission(self):
  r=json.loads((root/'C/report.json').read_text());self.assertLess(r['IKSolverResidualMaxM'],.0001);self.assertEqual(r['status'],'REFUSÉ');self.assertFalse(r['runtimeEnabled'])
if __name__=='__main__':unittest.main()
