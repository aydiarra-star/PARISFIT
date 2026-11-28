import unittest,json,csv
from pathlib import Path
import numpy as np
from metrics import project_to_plate,frame_inventory
D=Path('docs/coach/phase17')
class Passive(unittest.TestCase):
 def test_projection_not_contact(self):
  uv,d=project_to_plate([[.5,.5,3]],[[0,0,0],[1,0,0],[1,1,0],[0,1,0]])
  np.testing.assert_allclose(uv,[[.5,.5]]);np.testing.assert_allclose(d,[3]) # inside footprint does not imply contact
 def test_projection_translation(self):
  c=np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]]);p=np.array([[.2,.4,.8]])
  a=project_to_plate(p,c);b=project_to_plate(p+7,c+7)
  for x,y in zip(a,b):np.testing.assert_allclose(x,y)
 def test_degenerate_rejected(self):
  with self.assertRaises(ValueError):project_to_plate([[1,2,3]],[[0,0,0]]*4)
 def test_header_discrepancy_preserved(self):
  j=frame_inventory(4439424,12,1504,2948,0,2948);self.assertTrue(j['matchesPointFrames']);self.assertFalse(j['matchesInclusiveHeader']);self.assertEqual(j['completeFramesByBytes'],2948)
 def test_mapping_not_centres(self):
  rows=list(csv.DictReader((D/'marker-anatomical-mapping.csv').read_text().splitlines()));self.assertEqual(len(rows),57)
  self.assertEqual(sum(r['anatomical_status']=='Confirmé' for r in rows),44)
  self.assertTrue(all(r['rocketbox_status']=='Inconnu' for r in rows));self.assertTrue(all(r['joint_centre_equivalence'].startswith('Inconnu') for r in rows))
 def test_readable_not_raw_quality(self):
  j=json.loads((D/'c3d-inspection.json').read_text())
  for d in j.values():
   self.assertTrue(d['independentFloatBlockCheck']['pointXYZExact']);self.assertTrue(d['independentFloatBlockCheck']['analogExact']);self.assertEqual(d['analogSamples'],5*d['pointFrames']);self.assertTrue(any('EOF' in w for w in d['warnings']))
 def test_closed_gates(self):
  j=json.loads((D/'mapping-status.json').read_text());self.assertEqual(j['decision'],'B')
  for k in ['expertReviewed','IKExecuted','retargetExecuted','trajectoryCorrected','runtimeChanged','MichaudFactorsTransferred']:self.assertFalse(j[k])
if __name__=='__main__':unittest.main()
