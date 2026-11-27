import unittest,numpy as np
from bvh import parse,fk,Invalid
from audit import smooth,interpolate
class Audit(unittest.TestCase):
 def test_rotation_order(self):
  nodes=[{'name':'r','parent':None,'offset':[0,0,0],'channels':[('Zrotation',0)]},{'name':'j','parent':0,'offset':[1,0,0],'channels':[]}];p=fk(nodes,np.array([[90.]]));np.testing.assert_allclose(p[0,1],[0,1,0],atol=1e-12)
 def test_linear_resampling(self):
  p=np.arange(5.)[:,None,None]*np.ones((1,1,3));np.testing.assert_allclose(interpolate(p,.5,np.array([.25,.75]))[:,0,0],[.5,1.5])
 def test_smooth_not_identity(self):
  p=np.array([0.,1.,0.])[:,None,None];self.assertEqual(smooth(p)[0,0,0],.5)
 def test_affine_derivative_scaling(self):
  x=np.array([0.,1.,4.,9.]);np.testing.assert_allclose(np.diff(x*.946989,n=2),np.diff(x,n=2)*.946989)
 def test_invalid(self):self.assertRaises(Invalid,parse,'garbage')
if __name__=='__main__':unittest.main()
