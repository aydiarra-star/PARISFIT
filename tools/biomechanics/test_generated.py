"""Mutation tests on real control output, not synthetic human evidence."""
import json,copy,unittest
from pathlib import Path
from contracts import Invalid
from validate import validate
D=json.loads(Path('.cache/phase10/before-geometry.json').read_text());C=json.loads(Path('tools/biomechanics/criteria.json').read_text())
class Generated(unittest.TestCase):
 def test_rejection_is_reproducible(self):self.assertEqual(validate(D,C),validate(copy.deepcopy(D),C))
 def test_order_does_not_change(self):
  d=copy.deepcopy(D)
  for f in d['frames']:f['joints']=dict(reversed(list(f['joints'].items())))
  self.assertEqual(validate(D,C)['observedModelGeometry'],validate(d,C)['observedModelGeometry'])
 def test_missing(self):
  d=copy.deepcopy(D);del d['frames'][1]['joints']['Bip01_L_Foot'];self.assertRaises(Invalid,validate,d,C)
 def test_nonfinite(self):
  d=copy.deepcopy(D);d['frames'][1]['joints']['Bip01_Pelvis']['position'][0]=float('nan');self.assertRaises(Invalid,validate,d,C)
 def test_time(self):
  d=copy.deepcopy(D);d['frames'][1]['time']=0;self.assertRaises(Invalid,validate,d,C)
 def test_bad_rotation(self):
  d=copy.deepcopy(D);d['frames'][1]['joints']['Bip01_Pelvis']['rotation']=[0,0,0,0];self.assertRaises(Invalid,validate,d,C)
 def test_no_professional_approval_from_numbers(self):
  r=validate(D,C);self.assertEqual(r['status'],'REFUSÉ');self.assertFalse(r['runtimeEnabled']);self.assertEqual(r['checks']['professional']['status'],'EN ATTENTE DE VALIDATION HUMAINE')
if __name__=='__main__':unittest.main()
