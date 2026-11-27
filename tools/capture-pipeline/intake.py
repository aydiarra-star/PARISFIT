"""Local private intake. No upload, inference, editing, or admission.
Consent fields are operator attestations, not cryptographic/legal verification.
"""
import argparse,json,hashlib,math
from permissions import authorize
from pathlib import Path
REQUIRED_RIGHTS=['verifiedByOperator','participantAdult','recording','localPoseProcessing','commercialAvatarAnimation','operatorCopyright','professionalReview']
def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
def sha(v):return isinstance(v,str) and len(v)==64 and all(c in '0123456789abcdef' for c in v)
def validate(m):
 problems=[]
 if m.get('schemaVersion')!=1:problems.append('schemaVersion')
 if m.get('sourceType')!='dedicated-consented-human-video':problems.append('sourceType')
 r=m.get('rights',{})
 for k in REQUIRED_RIGHTS:
  if r.get(k) is not True:problems.append('rights:'+k)
 if not sha(r.get('privateRecordSHA256')):problems.append('rights:privateRecordSHA256')
 streams=m.get('streams',[])
 if len(streams)!=2 or {s.get('view') for s in streams}!={'front','profile'}:problems.append('streams:front-and-profile-required')
 for s in streams:
  if not sha(s.get('sha256')):problems.append('streamHash:'+str(s.get('view')))
  for k in ['syncStartFrame','syncEndFrame']:
   if type(s.get(k)) is not int or s[k]<0:problems.append('sync:'+str(s.get('view'))+':'+k)
  if type(s.get('syncEndFrame')) is int and type(s.get('syncStartFrame')) is int and s['syncEndFrame']<=s['syncStartFrame']:problems.append('sync:order')
 for k in ['sameTake','fullBodyAndFeetVisible','oneAdultOnly','completeSquatAndReturn','noPainReported']:
  if m.get('operatorReview',{}).get(k) is not True:problems.append('operatorReview:'+k)
 for k in ['reviewed','metricScaleMeasured','camerasUnmoved']:
  if m.get('calibration',{}).get(k) is not True:problems.append('calibration:'+k)
 if not sha(m.get('calibration',{}).get('sha256')):problems.append('calibration:sha256')
 return problems

def private_file(root,name):
 p=(root/name).resolve()
 if root not in p.parents or not p.is_file():raise ValueError('File must exist within private session root; symlink escapes refused')
 return p

def run(m,root):
 issues=validate(m);allowed,permission_errors=authorize(m,'local-analysis')
 if not allowed:issues.extend(permission_errors)
 result={'status':'BLOCKED','runtimeEnabled':False,'inferenceExecuted':False,'captureVerifiedByAssistant':False,'issues':issues,'streams':[],'professionalReviewObtained':False}
 if issues:return result # Do not read or decode any footage without rights attestation.
 cal=private_file(root,m['calibration']['file'])
 if digest(cal)!=m['calibration']['sha256']:result['issues'].append('calibrationHashMismatch');return result
 import cv2
 intervals=[]
 for s in m['streams']:
  p=private_file(root,s['file']);actual=digest(p)
  if actual!=s['sha256']:result['issues'].append('sourceHashMismatch:'+s['view']);continue
  cap=cv2.VideoCapture(str(p));fps=cap.get(cv2.CAP_PROP_FPS);width=cap.get(cv2.CAP_PROP_FRAME_WIDTH);height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT);frames=0
  while True:
   ok,_=cap.read()
   if not ok:break
   frames+=1
  expected=cap.get(cv2.CAP_PROP_FRAME_COUNT);cap.release()
  if not math.isfinite(fps) or not 29<=fps<=121:result['issues'].append('fps:'+s['view']);continue
  if frames==0 or abs(frames-expected)>1:result['issues'].append('decodeCount:'+s['view'])
  if min(width,height)<1080:result['issues'].append('resolution:'+s['view'])
  if s['syncEndFrame']>=frames:result['issues'].append('syncFrameOutsideVideo:'+s['view'])
  intervals.append((s['syncEndFrame']-s['syncStartFrame'])/fps)
  result['streams'].append({'view':s['view'],'sha256':actual,'framesDecoded':frames,'fpsReported':fps,'width':width,'height':height})
 if len(intervals)==2 and abs(intervals[0]-intervals[1])>1/60:result['issues'].append('syncDriftOverOne60HzFrame')
 result['issues'].append('frame-timestamps-calibration-and-visual-review-required')
 # Nominal FPS and visible sync events do not establish temporal calibration.
 result['status']='PREFLIGHT_ONLY_NOT_RECONSTRUCTION_READY' if len(result['issues'])==1 else 'BLOCKED'
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--manifest',required=True);p.add_argument('--private-root',required=True);p.add_argument('--report',required=True);a=p.parse_args()
 root=Path(a.private_root).resolve();repo=Path(__file__).resolve().parents[2]
 if root==repo or repo in root.parents:raise SystemExit('Private footage must be outside the Git repository')
 m=json.loads(Path(a.manifest).read_text());r=run(m,root);Path(a.report).write_text(json.dumps(r,indent=2)+'\n');print(r['status']);raise SystemExit(2 if r['status']=='BLOCKED' else 0)
