"""Independent geometric/kinematic triage. NO bpy, Three.js, numpy or corrections.
Input is measured model geometry from a sampler, not physical measurements.
"""
import math,json,argparse
from pathlib import Path
from contracts import Invalid
P='Bip01_'
NEEDED=['Pelvis','Spine','Spine1','Spine2','Neck','Head']+[s+'_'+n for s in ['L','R'] for n in ['Thigh','Calf','Foot','Toe0','UpperArm','Forearm','Hand']]
def vec(a,b):return [x-y for x,y in zip(a,b)]
def norm(a):return math.sqrt(sum(x*x for x in a))
def angle(a,b,c):
 u=vec(a,b);v=vec(c,b);den=norm(u)*norm(v)
 if den<1e-10:raise Invalid('DEGENERATE_JOINT_ANGLE')
 return math.degrees(math.acos(max(-1,min(1,sum(x*y for x,y in zip(u,v))/den))))
def percentile(v,p):return sorted(v)[round((len(v)-1)*p)] if v else None
def in_support_hull(points,p):
 pts=sorted(set((v[0],v[2]) for v in points))
 def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
 if len(pts)<3:return None
 lower=[];upper=[]
 for seq,half in [(pts,lower),(list(reversed(pts)),upper)]:
  for q in seq:
   while len(half)>=2 and cross(half[-2],half[-1],q)<=0:half.pop()
   half.append(q)
 hull=lower[:-1]+upper[:-1]
 if len(hull)<3:return None
 return all(cross(hull[i],hull[(i+1)%len(hull)],(p[0],p[2]))>=-1e-8 for i in range(len(hull)))
def validate(data,c):
 if data.get('schemaVersion')!=1:raise Invalid('SCHEMA_VERSION')
 if data.get('units')!='m' or data.get('up')!='Y':raise Invalid('UNITS_OR_AXES')
 frames=data.get('frames',[])
 if len(frames)<3:raise Invalid('EMPTY_OR_TOO_SHORT')
 names=set(frames[0]['joints'])
 if len(names)!=80 or not {P+n for n in NEEDED}<=names:raise Invalid('INCOMPATIBLE_JOINT_SET')
 for i,f in enumerate(frames):
  if set(f['joints'])!=names:raise Invalid('MISSING_JOINT_AT_FRAME:'+str(i))
  if not math.isfinite(f['time']) or abs(f['time']-i/c['sampleHz'])>1e-6:raise Invalid('NONUNIFORM_OR_DISCONTINUOUS_TIME')
  values=[f['surfaceMinY']]
  for j in f['joints'].values():
   if len(j['position'])!=3 or len(j['rotation'])!=4:raise Invalid('JOINT_SHAPE')
   values+=j['position']+j['rotation']
   if abs(norm(j['rotation'])-1)>.001:raise Invalid('QUATERNION_NOT_UNIT')
  for s in ['L_Foot','R_Foot','L_Hand','R_Hand']:
   support=f['supports'][s]
   if len(support['points'])!=3 or any(len(p)!=3 for p in support['points']):raise Invalid('SUPPORT_SHAPE')
   values+=[support['minY']]+sum(support['points'],[])
  if not all(math.isfinite(x) and abs(x)<100 for x in values):raise Invalid('NONFINITE_OR_OUT_OF_BOUNDS:'+str(i))
 parents=data['parents']
 if set(parents)!=names:raise Invalid('PARENT_SET')
 for name in names:
  seen=set();current=name
  while current is not None:
   if current in seen or current not in names:raise Invalid('PARENT_CYCLE_OR_MISSING')
   seen.add(current);current=parents[current]
 lengths={};speed=[];acc=[];rot=[];steps=[];lastvel={};length_error=0;rows=[];collisions=[];foot_drift={'L':0,'R':0};anchors={};knee={'L':[],'R':[]};pelvis_speed=[];pelvis_acc=[];stance_counts={'L':0,'R':0};normals=[];amplitudes={s+'_'+joint:[] for s in ['L','R'] for joint in ['hipProxy','elbow','ankleProxy']};trunk=[]
 for i,f in enumerate(frames):
  js=f['joints'];position=lambda n:js[P+n]['position'];previous=frames[max(0,i-1)]['joints']
  for n,j in js.items():
   if parents.get(n):
    if parents[n] not in names:raise Invalid('PARENT_MISSING')
    length=math.dist(j['position'],js[parents[n]]['position']);lengths.setdefault(n,length);length_error=max(length_error,abs(length-lengths[n]))
   if i:
    v=[x*c['sampleHz'] for x in vec(j['position'],previous[n]['position'])];speed.append(norm(v));steps.append(norm(v)/c['sampleHz'])
    if n==P+'Pelvis':pelvis_speed.append(norm(v))
    if n in lastvel:
     acceleration=norm(vec(v,lastvel[n]))*c['sampleHz'];acc.append(acceleration)
     if n==P+'Pelvis':pelvis_acc.append(acceleration)
    lastvel[n]=v
    dot=abs(sum(x*y for x,y in zip(j['rotation'],previous[n]['rotation'])));rot.append(math.degrees(2*math.acos(min(1,dot))))
  for side in ['L','R']:
   k=180-angle(position(side+'_Thigh'),position(side+'_Calf'),position(side+'_Foot'));knee[side].append(k)
   amplitudes[side+'_hipProxy'].append(180-angle(position('Spine'),position(side+'_Thigh'),position(side+'_Calf')))
   amplitudes[side+'_elbow'].append(180-angle(position(side+'_UpperArm'),position(side+'_Forearm'),position(side+'_Hand')))
   amplitudes[side+'_ankleProxy'].append(angle(position(side+'_Calf'),position(side+'_Foot'),position(side+'_Toe0')))
   points=f['supports'][side+'_Foot']['points'];a=frames[max(0,i-1)]['supports'][side+'_Foot']['points'];b=frames[min(len(frames)-1,i+1)]['supports'][side+'_Foot']['points'];dt=(min(len(frames)-1,i+1)-max(0,i-1))/c['sampleHz']
   velocity=max(math.hypot(q[0]-p[0],q[2]-p[2])/dt for p,q in zip(a,b));h=f['supports'][side+'_Foot']['minY'];candidate=-c['maxPenetrationM']<=h<=c['stanceCandidateHeightM'] and velocity<=c['stanceCandidateSpeedMS']
   if candidate:
    stance_counts[side]+=1;anchors.setdefault(side,points)
    foot_drift[side]=max(foot_drift[side],max(math.hypot(p[0]-q[0],p[2]-q[2]) for p,q in zip(points,anchors[side])))
   else:anchors.pop(side,None)
  trunk_vector=vec(position('Neck'),position('Pelvis'));trunk.append(math.degrees(math.acos(max(-1,min(1,trunk_vector[1]/norm(trunk_vector))))))
  # Explicitly heuristic mass proxy. No individualized anthropometry or forces.
  segments=[('Pelvis','Neck',.50),('Neck','Head',.08),('L_Thigh','L_Calf',.10),('R_Thigh','R_Calf',.10),('L_Calf','L_Foot',.05),('R_Calf','R_Foot',.05),('L_UpperArm','L_Hand',.06),('R_UpperArm','R_Hand',.06)]
  com=[sum((position(a)[k]+position(b)[k])*.5*w for a,b,w in segments) for k in range(3)]
  support_points=f['supports']['L_Foot']['points']+f['supports']['R_Foot']['points'];bounds=[min(p[0] for p in support_points),max(p[0] for p in support_points),min(p[2] for p in support_points),max(p[2] for p in support_points)]
  inside=bounds[0]<=com[0]<=bounds[1] and bounds[2]<=com[2]<=bounds[3]
  # Broad-phase sphere overlaps only. Not mesh collision detection or anatomical diagnosis.
  candidates=[]
  for a,b,radius in [('L_Hand','R_Hand',.08),('L_Calf','R_Calf',.10),('L_Hand','R_Thigh',.12),('R_Hand','L_Thigh',.12)]:
   if math.dist(position(a),position(b))<radius:candidates.append([a,b])
  if candidates:collisions.append({'frame':i,'pairs':candidates})
  rows.append({'time':f['time'],'estimatedCOM':com,'COMInsideFootAABB':inside,'COMInsideAssumedFootHull':in_support_hull(support_points,com),'kneeFlexionDeg':{s:knee[s][-1] for s in knee},'collisionCandidates':candidates})
 penetration=max(0,-min(f['surfaceMinY'] for f in frames));gap=max(f['supports'][s+'_Foot']['minY'] for f in frames for s in ['L','R']);drift=max(foot_drift.values());sym=max(abs(a-b) for a,b in zip(knee['L'],knee['R']));rotation=max(rot)
 observed={'maxSurfacePenetrationM':penetration,'maxFootGapM':gap,'maxCandidateStanceDriftM':drift,'candidateFrames':stance_counts,'maxSegmentErrorM':length_error,'maxJointSpeedMS':max(speed),'p95JointSpeedMS':percentile(speed,.95),'maxJointAccelerationMS2':max(acc),'maxRotationStepDeg':rotation,'maxAngularSpeedDegS':rotation*c['sampleHz'],'maxJointStepM':max(steps),'maxPelvisSpeedMS':max(pelvis_speed),'maxPelvisAccelerationMS2':max(pelvis_acc),'kneeFlexionDeg':{s:{'min':min(v),'max':max(v)} for s,v in knee.items()},'geometricAngleRangesDeg':{k:{'min':min(v),'max':max(v)} for k,v in amplitudes.items()},'trunkTiltFromVerticalDeg':{'min':min(trunk),'max':max(trunk)},'maxKneeAsymmetryDeg':sym,'entryExitMaxJointGapM':max(math.dist(frames[0]['joints'][n]['position'],frames[-1]['joints'][n]['position']) for n in names)}
 checks={}
 for name,value,limit in [('floor',penetration,c['maxPenetrationM']),('segments',length_error,c['maxSegmentErrorM']),('speed',max(speed),c['maxJointSpeedMS']),('acceleration',max(acc),c['maxJointAccelerationMS2']),('rotationContinuity',rotation,c['maxRotationStepDeg']),('positionContinuity',max(steps),c['maxJointStepM'])]:checks[name]={'status':'VALIDÉ' if value<=limit else 'REFUSÉ','value':value,'limit':limit,'scope':'geometric screening only'}
 checks['kneeROM']={'status':'VALIDÉ' if all(c['kneeFlexionRangeDeg'][0]<=k<=c['kneeFlexionRangeDeg'][1] for v in knee.values() for k in v) else 'REFUSÉ','scope':'unsigned flexion only; hyperextension/axial rotation not established'}
 checks['support']={'status':'EN ATTENTE DE VALIDATION HUMAINE','reason':'candidate windows and selected skin points are not reviewed contacts','gapM':gap,'candidateDriftM':drift}
 checks['balance']={'status':'EN ATTENTE DE VALIDATION HUMAINE','reason':'COM is heuristic; foot convex hull assumes both contacts unverified, AABB also reported; no forces or balance certification'}
 checks['collisions']={'status':'EN ATTENTE DE VALIDATION HUMAINE','candidateFrames':len(collisions),'reason':'spheres only; exhaustive surface self-collision NON TESTÉ'}
 checks['axialTorsion']={'status':'NON TESTÉ','reason':'anatomical joint frames unqualified; quaternion speed is not anatomical twist'}
 checks['symmetry']={'status':('VALIDÉ' if sym<=c['maxSymmetryDifferenceDeg'] else 'REFUSÉ') if c['symmetryExpected'] else 'NON TESTÉ','reason':'do not impose symmetry absent source annotation','differenceDeg':sym}
 for name in ['transitionRecovery','visual','professional','sourceFidelity']:checks[name]={'status':'EN ATTENTE DE VALIDATION HUMAINE'}
 return {'criteria':c,'sampledMeshes':data.get('sampledMeshes',[]),'excludedMeshes':data.get('excludedMeshes',[]),'status':'REFUSÉ','runtimeEnabled':False,'samples':len(frames),'sourceType':data['sourceType'],'observedModelGeometry':observed,'estimates':{'COMMethod':'unvalidated fixed segment-midpoint weights .50/.08/.10/.10/.05/.05/.06/.06','COMOutsideAssumedFootHullFrames':sum(r['COMInsideAssumedFootHull'] is False for r in rows),'COMOutsideFootAABBFrames':sum(not r['COMInsideFootAABB'] for r in rows),'collisionCandidateFrames':len(collisions),'contactTruth':'unknown'},'checks':checks,'reviewRequired':True,'rows':rows,'limits':['not medical or professional validation','input geometry sampled by Blender; independent algorithm is not independent physical evidence','floor reference and contact patches unqualified','no automatic corrections']}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--criteria',default='tools/biomechanics/criteria.json');a=p.parse_args()
 try:
  r=validate(json.loads(Path(a.input).read_text()),json.loads(Path(a.criteria).read_text()));Path(a.output).write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n');print(r['status'])
 except (Invalid,KeyError,ValueError,TypeError) as e:print('BLOCKING_INPUT_ERROR:',str(e));raise SystemExit(2)
