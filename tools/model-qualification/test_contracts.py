import unittest,json,csv
from pathlib import Path
import numpy as np
from contracts import transform,ik_gate
D=Path('docs/coach/phase14')
class Frames(unittest.TestCase):
 def test_unproven_blocked(self):
  with self.assertRaisesRegex(ValueError,'PROVENANCE'):transform([1,2,3],[1,2,3],[0,0,0],np.eye(3),np.zeros(3))
 def test_roundtrip(self):
  p=np.array([[1.,2,3],[4,5,6]]);f=p*2;m=p*.3;R=np.array([[0.,-1,0],[1,0,0],[0,0,1]]);t=np.array([2.,3,4]);q,g,n=transform(p,f,m,R,t,True);a,b,c=transform(q,g,n,R.T,-R.T@t,True)
  for old,new in [(p,a),(f,b),(m,c)]:np.testing.assert_allclose(old,new,atol=1e-12)
  self.assertAlmostEqual(np.linalg.norm(p[1]-p[0]),np.linalg.norm(q[1]-q[0]))
 def test_moment_translation(self):
  _,_,m=transform([0,0,0],[0,1,0],[0,0,0],np.eye(3),[2,0,0],True);np.testing.assert_allclose(m,[0,0,2])
 def test_reflection_rejected(self):
  with self.assertRaises(ValueError):transform([0,0,0],[0,1,0],[0,0,0],np.diag([-1,1,1]),[0,0,0],True)
 def test_scale_rejected(self):
  with self.assertRaises(ValueError):transform([0,0,0],[0,1,0],[0,0,0],np.eye(3)*1000,[0,0,0],True)
 def test_ik_closed(self):
  rows=json.loads((D/'correspondences.json').read_text())['rows'];self.assertFalse(ik_gate(rows,True,True));self.assertFalse(ik_gate([],True,True));self.assertFalse(ik_gate([{'status':'CONFIRMÉE PAR DOCUMENTATION'}],True,True))
 def test_dimensions_and_sources(self):
  rows=json.loads((D/'correspondences.json').read_text())['rows'];grid=list(csv.reader((D/'matrix-37x66.csv').read_text().splitlines()));self.assertEqual(len(rows),37);self.assertEqual(len(grid),38);self.assertTrue(all(len(r)==67 for r in grid));self.assertTrue(all(r['source'] and not r['usableForIK'] for r in rows));self.assertEqual(len(set(r['csv'] for r in rows)),37)
 def test_decision(self):
  d=json.loads((D/'decision.json').read_text());self.assertEqual(d['scenario'],'C');self.assertFalse(d['allowIK']);self.assertEqual(d['IK'],'NON TESTÉ')
if __name__=='__main__':unittest.main()
