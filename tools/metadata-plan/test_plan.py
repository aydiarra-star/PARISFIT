import unittest,json
from pathlib import Path
import numpy as np
from analyze import pose_rank
class Plan(unittest.TestCase):
 def test_point(self):self.assertEqual(pose_rank(np.array([[1.,2,3]])),3)
 def test_line(self):self.assertEqual(pose_rank(np.array([[0.,0,0],[1,0,0],[2,0,0]])),5)
 def test_triangle(self):self.assertEqual(pose_rank(np.array([[0.,0,0],[1,0,0],[0,1,0]])),6)
 def test_translation_invariance(self):
  p=np.array([[0.,0,0],[1,0,0],[0,1,0]]);self.assertEqual(pose_rank(p),pose_rank(p+22))
 def test_no_admission(self):
  d=json.loads(Path('docs/coach/phase15/decision.json').read_text());self.assertEqual(d['scenario'],'B');self.assertFalse(d['authorRequestSent']);self.assertFalse(d['runtimeEnabled']);self.assertFalse(d['newSourceAdmitted']);self.assertEqual(d['IK'],'NON TESTÉ')
if __name__=='__main__':unittest.main()
