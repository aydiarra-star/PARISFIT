import unittest,numpy as np
from core import angle,rigid_fit,dynamics,reconstruct
class Core(unittest.TestCase):
 def test_right_angle(self):self.assertAlmostEqual(float(angle(np.array([1,0,0]),np.zeros(3),np.array([0,1,0]))),90)
 def test_degenerate(self):self.assertRaises(ValueError,angle,np.zeros(3),np.zeros(3),np.ones(3))
 def test_rigid_fit(self):
  ref=np.array([[0.,0,0],[1,0,0],[0,1,0],[1,1,0]]);R=np.array([[0.,-1,0],[1,0,0],[0,0,1]]);q=ref@R+[2,3,1];r,t,e=rigid_fit(ref,q);np.testing.assert_allclose(ref@r+t,q,atol=1e-12);self.assertLess(e,1e-12);self.assertAlmostEqual(np.linalg.det(r),1)
 def test_collinear_rejected(self):self.assertRaises(ValueError,rigid_fit,np.array([[0,0,0],[1,0,0],[2,0,0]]),np.array([[0,0,0],[1,0,0],[2,0,0]]))
 def test_acceleration(self):
  t=np.arange(10)*.01;q=np.stack([t*t,0*t,0*t],axis=1);self.assertAlmostEqual(dynamics(q,.01)['maxAccelerationMS2'],2)
class Reconstruction(unittest.TestCase):
 def fixture(self):
  names=['Right_ASIC','Left_ASIC','Right_sacral_crest','Left_sacral_crest','Skull_vertex']+[s+'_'+n for s in ['Right','Left'] for n in ['greater_trochanter','lateral_epicondyle','lateral_malleolus','1st_metatarsal_head','acromioclavicular_joint','olecranon','ulna_head']]
  rng=np.random.default_rng(42);static=rng.normal(size=(len(names),3));p=static[None,:,:]+rng.normal(0,.01,size=(5,len(names),3));return p,static,names
 def test_static_lengths(self):
  p,static,names=self.fixture();models,meta=reconstruct(p,static,names)
  for mode in ['H1_static_lengths','H2_rigid_pelvis_static_lengths']:
   for side in ['Right','Left']:
    self.assertLess(np.ptp(np.linalg.norm(models[mode][side+'_hip']-models[mode][side+'_knee'],axis=1)),1e-12)
 def test_direction_preservation_is_not_validation(self):
  p,static,names=self.fixture();models,meta=reconstruct(p,static,names)
  angles=[]
  for mode in models:
   q=models[mode];angles.append(angle(q['Right_hip'],q['Right_knee'],q['Right_ankle']))
  np.testing.assert_allclose(angles[0],angles[1]);np.testing.assert_allclose(angles[0],angles[2])
 def test_no_input_mutation(self):
  p,static,names=self.fixture();original=p.copy();reconstruct(p,static,names);np.testing.assert_array_equal(original,p)
 def test_reflection_not_accepted_as_rotation(self):
  q=np.array([[0.,0,0],[1,0,0],[0,1,0],[0,0,1]]);r,t,e=rigid_fit(q,q*[-1,1,1]);self.assertAlmostEqual(np.linalg.det(r),1);self.assertGreater(e,.1)
if __name__=='__main__':unittest.main()
