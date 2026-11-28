import unittest
from permissions import authorize
class Permissions(unittest.TestCase):
 def test_unknown(self):self.assertFalse(authorize({},'anything')[0])
 def test_none(self):self.assertFalse(authorize({},'local-analysis')[0])
 def test_local_not_cloud(self):
  m={'rights':dict(verifiedByOperator=True,participantAdult=True,recording=True,localPoseProcessing=True,operatorCopyright=True,privateRecordSHA256='a'*64)}
  self.assertTrue(authorize(m,'local-analysis')[0]);self.assertFalse(authorize(m,'external-upload',service='Arena')[0]);self.assertFalse(authorize(m,'publish-source')[0]);self.assertFalse(authorize(m,'commercial-animation')[0])
 def test_separate_publications(self):
  m={'rights':dict(verifiedByOperator=True,participantAdult=True,recording=True,operatorCopyright=True,sourceVideoPublication=True,privateRecordSHA256='a'*64)}
  self.assertTrue(authorize(m,'publish-source')[0]);self.assertFalse(authorize(m,'publish-motion')[0])
 def test_cloud_scope(self):
  m={'rights':dict(verifiedByOperator=True,participantAdult=True,recording=True,operatorCopyright=True,externalServiceUpload=True,privateRecordSHA256='a'*64),'externalServiceAuthorization':{'service':'named-test-service','purpose':'pose-processing','verified':True}}
  self.assertTrue(authorize(m,'external-upload','named-test-service')[0]);self.assertFalse(authorize(m,'external-upload','other')[0])
if __name__=='__main__':unittest.main()
