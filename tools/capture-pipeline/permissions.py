"""Explicit operation-scoped permission checks; no transmission implementation.
Operator attestations are not legal verification of consent documents.
"""
import re
REQUIRED={
 'record':['recording'],
 'local-analysis':['recording','localPoseProcessing','operatorCopyright'],
 'commercial-animation':['recording','localPoseProcessing','operatorCopyright','commercialAvatarAnimation'],
 'publish-source':['recording','operatorCopyright','sourceVideoPublication'],
 'publish-motion':['recording','localPoseProcessing','operatorCopyright','publicMotionRedistribution'],
 'external-upload':['recording','operatorCopyright','externalServiceUpload'],
}
def authorize(manifest,operation,service=None):
 if operation not in REQUIRED:return False,['unknown-operation']
 r=manifest.get('rights',{});errors=[]
 for k in ['verifiedByOperator','participantAdult']+REQUIRED[operation]:
  if r.get(k) is not True:errors.append('permission:'+k)
 if not re.fullmatch('[0-9a-f]{64}',str(r.get('privateRecordSHA256',''))):errors.append('missing-private-rights-record')
 if operation=='external-upload':
  scope=manifest.get('externalServiceAuthorization',{})
  if not service or scope.get('service')!=service or scope.get('purpose')!='pose-processing' or scope.get('verified') is not True:errors.append('service-scope-not-authorized')
 return not errors,errors
