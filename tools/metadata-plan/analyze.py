"""Surface-point observability, not anatomical IK, scaling or registration."""
from pathlib import Path
import json,hashlib
import numpy as np
D=Path('docs/coach/phase15');P=Path('docs/coach/phase13');Q=Path('docs/coach/phase14')
def save(n,d):(D/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def pose_rank(p):
 # Translation(m) and infinitesimal rotation(rad); rank geometric, singular values not dimensionless condition numbers.
 J=[]
 for x,y,z in p-p.mean(axis=0):J.append(np.hstack((np.eye(3),-np.array([[0,-z,y],[z,0,-x],[-y,x,0]]))))
 return int(np.linalg.matrix_rank(np.vstack(J),tol=1e-10))
def main():
 d=json.loads((P/'review-data.json').read_text());names=d['names'];s=np.array(d['staticMedian']);p=np.array(d['markers']);groups={'pelvis':['Right_ASIC','Left_ASIC','Right_sacral_crest','Left_sacral_crest'],'head':['Right_temporal_bone','Left_temporal_bone','Skull_vertex'],'shoulder_line':['Right_acromioclavicular_joint','Left_acromioclavicular_joint']}
 for side in ['Right','Left']:
  for region,suffix in {'thigh':['greater_trochanter','lateral_epicondyle'],'shank':['tibial_tuberosity','lateral_malleolus'],'forearm':['olecranon','forearm_centre','ulna_head'],'hand':['5th_metacarpal_head','2nd_metacarpal_head'],'foot':['calcaneal_tuberosity','1st_metatarsal_head','5th_metatarsal_head'],'upper_arm':['deltoid_tuberosity']}.items():groups[side+'_'+region]=[side+'_'+n for n in suffix]
 rows=[]
 for group,labels in groups.items():
  ids=[names.index(n) for n in labels];v=s[ids];lengths=[]
  for i in range(len(ids)):
   for j in range(i+1,len(ids)):
    l=np.linalg.norm(p[:,ids[i]]-p[:,ids[j]],axis=1);lengths.append({'pair':[labels[i],labels[j]],'minM':float(l.min()),'maxM':float(l.max()),'rangeM':float(np.ptp(l))})
  rows.append({'group':group,'labels':labels,'status':'VALIDÉ','scope':'technical geometry only; segment membership inferred from labels and NOT certified placement','rigidPoseRankOf6':pose_rank(v),'unobservableRigidDimensions':6-pose_rank(v),'pairDistancesRep1':lengths,'anatomicalDOFStatus':'NON TESTÉ','anatomicalCentresIdentified':False})
 save('observability.json',{'status':'VALIDÉ','scope':'numerical rigid-point observability on six-decimal display data, not anatomical accuracy','sourceSHA256':hashlib.sha256((P/'review-data.json').read_bytes()).hexdigest(),'frames':150,'groups':rows,'IKExecuted':False})
 a=json.loads((Q/'anthropometry.json').read_text());rows=[]
 for n in ['P1','P2','P3','Fem','Tib','Foot']:
  rows.append({'name':n,'S01':a['documentedS01'][n],'unit':'dimensionless','documentedRole':'pelvis axis (axis order unspecified)' if n.startswith('P') else {'Fem':'femur','Tib':'tibia','Foot':'foot'}[n],'valueStatus':'VALIDÉ','applicationStatus':'EN ATTENTE DE DOCUMENTATION','application':None,'missing':['body/component identifiers','axis assignment and isotropy','reference geometry/version','scaling order and marker registration','mass/inertia treatment and other segment factors'],'source':'../phase14/dataset-README.md + participants.csv SHA256 '+a['sourceSHA256'],'certainty':'value and broad role documented, execution recipe unknown','applied':False})
 save('scaling-audit.json',{'status':'EN ATTENTE DE DOCUMENTATION','sufficientForIndividualization':False,'rows':rows})
 save('decision.json',{'status':'EN ATTENTE DE DOCUMENTATION','scenario':'B','reason':'documented data and factors available, required anatomical metadata still missing; no author response requested or received through this session','authorRequestSent':False,'professionalApproval':False,'IK':'NON TESTÉ','COP':'NON TESTÉ','retarget':'NON TESTÉ','runtimeEnabled':False,'newSourceAdmitted':False})
if __name__=='__main__':main()
