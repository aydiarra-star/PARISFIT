import unittest,json,csv,tempfile,struct
from pathlib import Path
from audit import differences,binary
D=Path('docs/coach/phase18')
class Review(unittest.TestCase):
 def test_difference_is_exhaustive(self):
  self.assertEqual(differences({'a':[1,2]},{'a':[1,3]})[0]['path'],'/a/1')
  self.assertEqual(differences({'a':1},{'a':1}),[])
 def fixture(self,last=1):
  def rec(name,gid,payload):
   n=name.encode();return struct.pack('bb',len(n),gid)+n+struct.pack('<h',2+len(payload))+payload
  h=bytearray(512);h[0]=2;h[1]=80;struct.pack_into('<HHHH',h,2,1,5,0,last);struct.pack_into('<fHHf',h,12,-1.,3,5,200.)
  params=bytes([0,0,1,84])+rec('POINT',-1,b'\0')+rec('FRAMES',1,bytes([2,0])+struct.pack('<H',2)+b'\0')+bytes(2)
  return bytes(h)+params.ljust(512,b'\0')+bytes(72)
 def test_independent_fixture_zero_based(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'fixture.c3d';p.write_bytes(self.fixture());x=binary(p)
   self.assertEqual(x['completeFrames'],2);self.assertEqual(x['inclusiveHeaderFrames'],2);self.assertTrue(x['recordCountAgreement']);self.assertEqual(x['header']['lastFrame'],1)
 def test_actual_header_mismatch_detectable(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'fixture.c3d';p.write_bytes(self.fixture(2));x=binary(p)
   self.assertNotEqual(x['inclusiveHeaderFrames'],x['completeFrames']);self.assertEqual(x['parameters']['POINT:FRAMES']['values'],[2])
 def test_preserved_labels_and_confidence(self):
  old={r['original_name']:r for r in csv.DictReader(Path('docs/coach/phase17/marker-anatomical-mapping.csv').read_text().splitlines())};new=json.loads((D/'marker-review-register.json').read_text())
  self.assertEqual(len(new),57);self.assertEqual(set(old),{r['marker'] for r in new})
  for r in new:self.assertEqual(r['phase17_status'],old[r['marker']]['anatomical_status']);self.assertIsNone(r['expert_answer']);self.assertTrue(r['expert_question']);self.assertEqual(r['joint_centre_status'],'Inconnu')
 def test_no_expert_approval(self):
  d=json.loads((D/'expert-feedback-template.json').read_text());self.assertFalse(d['sent']);self.assertFalse(d['automaticAdmission']);self.assertIsNone(d['reviewer']);self.assertTrue(all(q['answer'] is None for q in d['questions']));self.assertEqual(len(d['allowedAnswers']),4)
 def test_header_vs_property(self):
  d=json.loads((D/'c3d-independent-byte-audit.json').read_text())
  for x in d['files'].values():
   self.assertEqual(x['header']['lastFrame']+1,x['completeFrames']);self.assertEqual(x['inclusiveHeaderFrames'],x['completeFrames']);self.assertEqual(x['pythonC3DComparison']['computedLastFrameProperty'],x['completeFrames']);self.assertEqual(x['pythonC3DComparison']['rawHeaderLastFrame'],x['completeFrames']-1);self.assertEqual(x['trailingBytes'],0);self.assertFalse(x['repaired'])
 def test_historical_context_not_motion_improvement(self):
  d=json.loads((D/'historical-diff.json').read_text());self.assertEqual(len(d['mobile']['differences']),6);self.assertEqual(len(d['transition']['differences']),6);self.assertTrue(d['oldSecondClipDuplicatesFirstExceptName']);self.assertTrue(all(x['path'].startswith('/clips/1/') for x in d['transition']['differences']))
 def test_cache_key_evidence(self):
  d=json.loads((D/'cache-identity.json').read_text());self.assertEqual(len(set(d['oldCacheKeys'])),1);self.assertEqual(len(set(d['currentLabCacheKeys'])),2);self.assertFalse(d['animationExecuted'])
if __name__=='__main__':unittest.main()
