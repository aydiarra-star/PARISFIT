import unittest,json,copy,tempfile
from pathlib import Path
from intake import validate,run,private_file
T=json.loads(Path('tools/capture-pipeline/session-template.json').read_text())
class IntakeTests(unittest.TestCase):
 def test_unsigned_blocks_before_read(self):
  r=run(T,Path('/no-footage-present'));self.assertEqual(r['status'],'BLOCKED');self.assertEqual(r['streams'],[]);self.assertFalse(r['inferenceExecuted'])
 def test_no_old_source(self):
  m=copy.deepcopy(T);m['sourceType']='CMU';self.assertIn('sourceType',validate(m))
 def test_views(self):
  m=copy.deepcopy(T);m['streams'][1]['view']='front';self.assertIn('streams:front-and-profile-required',validate(m))
 def test_bool_is_not_frame(self):
  m=copy.deepcopy(T);m['streams'][0]['syncStartFrame']=True;self.assertIn('sync:front:syncStartFrame',validate(m))
 def test_hash_format(self):
  m=copy.deepcopy(T);m['rights']['privateRecordSHA256']='signed';self.assertIn('rights:privateRecordSHA256',validate(m))
 def test_private_path(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);self.assertRaises(ValueError,private_file,root,'../outside')
 def test_truthy_does_not_consent(self):
  m=copy.deepcopy(T);m['rights']['recording']='yes';self.assertIn('rights:recording',validate(m))
if __name__=='__main__':unittest.main()
