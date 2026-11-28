import unittest,math
from ik import solve
from metrics import extra_metrics
class Metrics(unittest.TestCase):
 def test_identical_fixed_axes(self):
  d={'frames':[{'joints':{'Bip01_Foot':{'position':[1,3,-2]}}}]};s=[{'sourcePositions':{'foot':[1,2,3]}}]
  self.assertEqual(extra_metrics({'frames':d['frames']*3},s*3,{'Foot':'foot'})['sourceTrajectoryProxy']['rmsM'],0)
 def test_not_best_fit(self):
  d={'frames':[{'joints':{'Bip01_Foot':{'position':[2,3,-2]}}}]};s=[{'sourcePositions':{'foot':[1,2,3]}}]
  r=extra_metrics({'frames':d['frames']*3},s*3,{'Foot':'foot'});self.assertEqual(r['sourceTrajectoryProxy']['rmsM'],1);self.assertEqual(r['admission'],'REFUSÉ')
class IK(unittest.TestCase):
 def test_lengths(self):
  k,a,r=solve([0,0,0],[0,0,1],[0,1,.5],.8,.7)
  self.assertAlmostEqual(math.dist(k,[0,0,0]),.8);self.assertAlmostEqual(math.dist(k,a),.7);self.assertAlmostEqual(r,0)
 def test_out_of_reach_is_reported(self):
  k,a,r=solve([0,0,0],[0,0,2],[0,1,0],.5,.5)
  self.assertGreater(r,1);self.assertAlmostEqual(math.dist(k,a),.5)
 def test_zero_direction_rejected(self):self.assertRaises(ValueError,solve,[0,0,0],[0,0,0],[0,1,0],.5,.5)
 def test_zero_length_rejected(self):self.assertRaises(ValueError,solve,[0,0,0],[0,0,1],[0,1,0],0,.5)
 def test_collinear_pole_rejected(self):self.assertRaises(ValueError,solve,[0,0,0],[0,0,1],[0,0,1],.5,.5)
if __name__=='__main__':unittest.main()
