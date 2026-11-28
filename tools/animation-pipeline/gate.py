"""Admission is independent of successful export. Unknown/missing evidence blocks."""
import json,math,hashlib
from pathlib import Path

def evaluate(config, report):
 reasons=[];checks={};s=report['stages'][-1];t=config['thresholds']
 for key in ['minSurfaceY','maxSupportGapM','maxSupportPointDriftM','maxSegmentErrorM','maxRotationStepRad','maxJointSpeedMS','maxJointAccelerationMS2','loopMaxPositionM']:
  if not math.isfinite(s[key]):reasons.append('nonfinite:'+key)
 for name,value,limit in [('penetration',max(0,-s['minSurfaceY']),t['penetrationM']),('supportGap',s['maxSupportGapM'],t['supportGapM']),('supportDrift',s['maxSupportPointDriftM'],t['supportDriftM']),('segments',s['maxSegmentErrorM'],t['segmentErrorM']),('rotationStep',s['maxRotationStepRad'],t['rotationStepRad']),('speed',s['maxJointSpeedMS'],t['jointSpeedMS']),('acceleration',s['maxJointAccelerationMS2'],t['jointAccelerationMS2']),('loopPosition',s['loopMaxPositionM'],t['loopPositionM'])]:
  checks[name]={'value':value,'limit':limit,'pass':math.isfinite(value) and value<=limit}
  if not checks[name]['pass']:reasons.append(name)
 if report['sourceType']!=config['sourceType']:reasons.append('sourceTypeMismatch')
 if config['sourceType']!='verified-optical-mocap':reasons.append('not-qualified-production-capture')
 if report['runtimeSHA256']!=config['sourceSHA256']:reasons.append('sourceHashMismatch')
 if not all(config['license'].get(k) is True for k in ['commercialUseVerified','redistributionVerified']):reasons.append('rightsUnverified')
 # Review booleans alone cannot approve: require separate signed, asset-bound review evidence.
 for k,v in config['reviews'].items():
  if v is not True:reasons.append('review:'+k)
 reasons.append('signed-asset-bound-review-not-implemented')
 return {'status':'BLOCKED','runtimeEnabled':False,'numericChecks':checks,'blockingReasons':reasons,'scope':'Engineering triage, not medical/biomechanical approval'}
if __name__=='__main__':
 c=json.loads(Path('tools/animation-pipeline/pushup.json').read_text());r=json.loads(Path(c['output'],'measurements.json').read_text());d=evaluate(c,r);Path(c['output'],'decision.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
