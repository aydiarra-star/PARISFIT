import unittest,numpy as np
from core import angle,rigid_fit,dynamics
class Core(unittest.TestCase):
 def test_right_angle(self):self.assertAlmostEqual(float(angle(np.array([1,0,0]),np.zeros(3),np.array([0,1,0]))),90)
 def test_degenerate(self):self.assertRaises(ValueError,angle,np.zeros(3),np.zeros(3),np.ones(3))
 def test_rigid_fit(self):
  ref=np.array([[0.,0,0],[1,0,0],[0,1,0],[1,1,0]]);R=np.array([[0.,-1,0],[1,0,0],[0,0,1]]);q=ref@R+[2,3,1];r,t,e=rigid_fit(ref,q);np.testing.assert_allclose(ref@r+t,q,atol=1e-12);self.assertLess(e,1e-12);self.assertAlmostEqual(np.linalg.det(r),1)
 def test_collinear_rejected(self):self.assertRaises(ValueError,rigid_fit,np.array([[0,0,0],[1,0,0],[2,0,0]]),np.array([[0,0,0],[1,0,0],[2,0,0]]))
 def test_acceleration(self):
  t=np.arange(10)*.01;q=np.stack([t*t,0*t,0*t],axis=1);self.assertAlmostEqual(dynamics(q,.01)['maxAccelerationMS2'],2)
if __name__=='__main__':unittest.main()
