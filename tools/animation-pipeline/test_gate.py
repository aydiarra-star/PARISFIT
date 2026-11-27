import unittest,json,copy
from pathlib import Path
from gate import evaluate
C=json.loads(Path('tools/animation-pipeline/pushup.json').read_text());R=json.loads(Path(C['output'],'measurements.json').read_text())
class GateTests(unittest.TestCase):
 def test_control_cannot_admit(self):
  d=evaluate(C,R);self.assertEqual(d['status'],'BLOCKED');self.assertFalse(d['runtimeEnabled'])
 def test_numbers_do_not_approve(self):
  c=copy.deepcopy(C);r=copy.deepcopy(R);c['sourceType']=r['sourceType']='verified-optical-mocap';c['reviews']={k:True for k in c['reviews']};self.assertIn('signed-asset-bound-review-not-implemented',evaluate(c,r)['blockingReasons'])
 def test_rights(self):
  c=copy.deepcopy(C);c['license']['commercialUseVerified']=False;self.assertIn('rightsUnverified',evaluate(c,R)['blockingReasons'])
 def test_nan_and_bad_ground(self):
  for value in [-.1,float('nan')]:
   r=copy.deepcopy(R);r['stages'][-1]['maxJointSpeedMS']=value if value!=value else 100
   self.assertFalse(evaluate(C,r)['numericChecks']['speed']['pass'])
 def test_hash(self):
  r=copy.deepcopy(R);r['runtimeSHA256']='wrong';self.assertIn('sourceHashMismatch',evaluate(C,r)['blockingReasons'])
 def test_missing(self):
  r=copy.deepcopy(R);del r['stages'];self.assertRaises(KeyError,evaluate,C,r)
if __name__=='__main__':unittest.main()
