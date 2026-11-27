import unittest
from metrics import extra_metrics
class Metrics(unittest.TestCase):
 def test_identical_fixed_axes(self):
  d={'frames':[{'joints':{'Bip01_Foot':{'position':[1,3,-2]}}}]};s=[{'sourcePositions':{'foot':[1,2,3]}}]
  self.assertEqual(extra_metrics(d,s,{'Foot':'foot'})['sourceTrajectoryProxy']['rmsM'],0)
 def test_not_best_fit(self):
  d={'frames':[{'joints':{'Bip01_Foot':{'position':[2,3,-2]}}}]};s=[{'sourcePositions':{'foot':[1,2,3]}}]
  r=extra_metrics(d,s,{'Foot':'foot'});self.assertEqual(r['sourceTrajectoryProxy']['rmsM'],1);self.assertEqual(r['admission'],'REFUSÉ')
if __name__=='__main__':unittest.main()
