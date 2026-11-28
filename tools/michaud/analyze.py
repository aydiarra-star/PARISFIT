from pathlib import Path
import numpy as np,json,gzip,io,csv,hashlib
from core import angle,dynamics,reconstruct
ROOT=Path('.cache/phase13')
def read(name):return np.genfromtxt(io.StringIO(gzip.decompress((ROOT/name).read_bytes()).decode()),delimiter=',',names=True)
def region(n):
 if any(k in n for k in ['ASIC','sacral']):return 'pelvis'
 if any(k in n for k in ['temporal','Skull']):return 'head'
 if any(k in n for k in ['acromio','deltoid','olecranon','forearm','ulna','metacarpal']):return 'upper-limb/trunk-landmark'
 return 'lower-limb/foot'
def main():
 data=read('P001_markers.csv.gz');force=read('P001_force_plates.csv.gz');stat=read('static_markers.csv.gz');names=[n[:-2] for n in data.dtype.names if n.endswith('_x')]
 assert len(names)==37 and set(data.dtype.names)==set(stat.dtype.names),'MARKER_SCHEMA'
 def positions(d):return np.stack([np.stack([d[n+'_'+a] for a in 'xyz'],axis=1) for n in names],axis=1)
 allp=positions(data);staticp=positions(stat);assert np.isfinite(allp).all() and np.isfinite(staticp).all(),'NONFINITE_MARKERS'
 assert len(data)==len(force) and np.max(np.abs(data['time']-force['time']))<1e-6,'SYNC_FILE_TIMESTAMPS'
 for d in [data,force,stat]:assert np.all(np.diff(d['time'])>0),'NONMONOTONIC_TIME'
 dt=float(np.median(np.diff(data['time'])));assert abs(dt-.01)<1e-7
 rep=next(r for r in csv.DictReader((ROOT/'squat_repetitions.csv').read_text().splitlines()) if r['trial']=='P001' and r['rep']=='1');start,bottom,end=[float(rep[k]) for k in ['t_start','t_bottom','t_end']];mask=(data['time']>=start-1e-8)&(data['time']<=end+1e-8);p=allp[mask];f=force[mask];times=data['time'][mask];static=np.median(staticp,axis=0)
 inventory=[]
 for j,n in enumerate(names):
  q=allp[:,j];v=np.diff(q,axis=0)/dt;acc=np.diff(q,n=2,axis=0)/dt**2
  inventory.append({'name':n,'kind':'skin marker, not joint centre','region':region(n),'initialPositionM':q[0].tolist(),'minPositionM':q.min(axis=0).tolist(),'maxPositionM':q.max(axis=0).tolist(),'staticMedianM':static[j].tolist(),'staticSDM':np.std(staticp[:,j],axis=0).tolist(),'missingSamples':int((~np.isfinite(q)).sum()),'zeroTripletSamples':int(np.all(q==0,axis=1).sum()),'maxStepM':float(np.linalg.norm(np.diff(q,axis=0),axis=1).max()),'jumpFlagsOver50mm':[int(i+1) for i in np.where(np.linalg.norm(np.diff(q,axis=0),axis=1)>.05)[0]],'repeatedConsecutiveTriplets':int(np.all(np.diff(q,axis=0)==0,axis=1).sum()),**dynamics(q,dt)})
 marker_report={'status':'EN ATTENTE DE VALIDATION HUMAINE','scope':'full P0013350samples; rep1 separately reconstructed','frames':len(data),'markers':inventory,'sampleHz':1/dt,'maxTimestampDeviationFrom10ms':float(np.max(abs(np.diff(data['time'])-.01))),'occlusions':'NON TESTÉ: no visibility/confidence/gap-filling log in CSV; finite coordinates do not prove no occlusions','noise':'static SD includes postural sway and soft tissue; second difference mixes movement/noise; no sensor noise estimate','units':'m per README, lab axes with Z-up hypothesis'}
 models,fit=reconstruct(p,static,names);get=lambda n:p[:,names.index(n)]
 force_rows=[]
 for plate in [1,2]:
  cols=['PLATE_'+str(plate)+'_'+c for c in ['Fx','Fy','Fz','Mx','My','Mz']];assert all(c in f.dtype.names for c in cols)
  for c in cols:assert np.isfinite(force[c]).all(),'NONFINITE_FORCE'
  Fz=f[cols[2]];row={'plate':plate,'components':{c:{'min':float(f[c].min()),'max':float(f[c].max()),'secondDifferenceRMS':float(np.sqrt(np.mean(np.diff(f[c],n=2)**2)))} for c in cols},'forceUnits':'N','momentUnits':'N m','thresholdSensitivity':{str(th):{'loadedFrames':int((Fz>th).sum()),'fraction':float((Fz>th).mean())} for th in [10,20,50,100]},'calibration':'NON TESTÉ: no matrix, zero trial or uncertainty certificate','momentsReference':'NON TESTÉ: sensor-origin height, rotation and sign not established; COP not computed'};force_rows.append(row)
 total=f['PLATE_1_Fz']+f['PLATE_2_Fz'];share=f['PLATE_1_Fz']/total
 pelvis=models['H0_skin_landmarks']['pelvis'];accel=np.diff(pelvis[:,2],n=2)/dt**2
 lag=[]
 for k in range(-10,11):
  aa=accel[max(0,k):len(accel)+min(0,k)];ff=total[1:-1][max(0,-k):len(accel)-max(0,k)];corr=float(np.corrcoef(aa,ff)[0,1]);lag.append({'lagSamples':k,'correlation':corr})
 nearest={}
 for side in ['Right','Left']:
  heel=get(side+'_calcaneal_tuberosity');toe=get(side+'_1st_metatarsal_head');center=(heel+toe)/2;dist=np.stack([np.linalg.norm(center[:,:2]-c,axis=1) for c in [np.array([-.698,0]),np.array([0,0])]],axis=1)
  nearest[side]={'nearestPlateFrames':{'1':int((dist.argmin(axis=1)==0).sum()),'2':int((dist.argmin(axis=1)==1).sum())},'heelDisplacementMaxM':float(np.linalg.norm(heel[:,:2]-heel[0,:2],axis=1).max()),'heelZRangeM':[float(heel[:,2].min()),float(heel[:,2].max())],'meaning':'nearest known plate centre, not proof of sole area or foot assignment; marker motion is not sliding'}
 forces={'status':'EN ATTENTE DE VALIDATION HUMAINE','frames':len(times),'maxFileTimestampDifferenceS':float(np.max(abs(data['time']-force['time']))),'hardwareSync':'NON TESTÉ: identical timestamps are not a trigger validation','plates':force_rows,'plate1FractionOfTotalFz':{'min':float(share.min()),'max':float(share.max()),'mean':float(share.mean())},'forceDoesNotIdentifyDescent':'both plates remain loaded; phases require markers and depositor annotation','feet':nearest,'lagDiagnostic':{'values':lag,'best':max(lag,key=lambda x:x['correlation']),'meaning':'proxy pelvis acceleration vs Fz, not COM; do not shift data or infer hardware delay'},'COP':{'status':'NON TESTÉ','reason':'moment origin/surface elevation/sign/plate frame unqualified'},'forceUsedToCorrectGeometry':False}
 summaries={};series={}
 for mode,pts in models.items():
  rows={};residuals=[]
  for side in ['Right','Left']:
   H,K,A=[pts[side+'_'+n] for n in ['hip','knee','ankle']];knee=180-angle(H,K,A);hip=180-angle(pts['trunk'],H,K)
   l1=np.linalg.norm(K-H,axis=1);l2=np.linalg.norm(A-K,axis=1)
   rows[side]={'kneeProxyDeg':{'min':float(knee.min()),'max':float(knee.max()),'maxAngularSpeedDegS':float(np.abs(np.diff(knee)/dt).max()),'maxAngularAccelerationDegS2':float(np.abs(np.diff(knee,n=2)/dt**2).max())},'hipTrunkProxyDeg':{'min':float(hip.min()),'max':float(hip.max())},'thighProxyLengthM':{'min':float(l1.min()),'max':float(l1.max())},'shankProxyLengthM':{'min':float(l2.min()),'max':float(l2.max())}}
   for key,marker in [('hip','greater_trochanter'),('knee','lateral_epicondyle'),('ankle','lateral_malleolus')]:residuals.append(np.linalg.norm(pts[side+'_'+key]-get(side+'_'+marker),axis=1))
  qs=np.stack(list(pts.values()),axis=1);trunk=pts['trunk']-pts['pelvis'];tilt=np.degrees(np.arccos(np.clip(trunk[:,2]/np.linalg.norm(trunk,axis=1),-1,1)));left=180-angle(pts['Left_hip'],pts['Left_knee'],pts['Left_ankle']);right=180-angle(pts['Right_hip'],pts['Right_knee'],pts['Right_ankle'])
  summaries[mode]={'status':'REFUSÉ','reason':'diagnostic surface-landmark chain, not validated anatomical centres','sides':rows,'pointDynamics':{k:dynamics(v,dt) for k,v in pts.items()},'markerEndpointRMSM':float(np.sqrt(np.mean(np.array(residuals)**2))),'markerEndpointMaxM':float(np.max(residuals)),'kneeProxyMaxAsymmetryDeg':float(abs(left-right).max()),'trunkTiltDeg':{'min':float(tilt.min()),'max':float(tilt.max())},**dynamics(qs,dt)};series[mode]={'points':{k:v.tolist() for k,v in pts.items()},'trunkTiltDeg':tilt.tolist(),'leftKneeDeg':left.tolist(),'rightKneeDeg':right.tolist()}
 # Sensitivity is NOT a confidence interval: unknown fixed centre offsets ±10/20mm.
 sensitivity={}
 for mm in [10,20]:
  scenarios=[]
  for axis in range(3):
   for joint in ['hip','knee','ankle']:
    for sign in [-1,1]:
     H,K,A=[models['H0_skin_landmarks']['Right_'+n].copy() for n in ['hip','knee','ankle']];[H,K,A][['hip','knee','ankle'].index(joint)][:,axis]+=sign*mm/1000;val=180-angle(H,K,A);scenarios.append(val)
  base=np.array(series['H0_skin_landmarks']['rightKneeDeg']);sensitivity[str(mm)]={'maxDeviationDeg':float(np.max(abs(np.array(scenarios)-base))),'scenarios':18,'meaning':'fixed endpoint offsets, not random measurement SD or95%CI'}
 velocity=np.diff(pelvis[:,2])/dt;mid=int(np.argmin(abs(times-bottom)));minimum=int(np.argmin(pelvis[:,2]));phases={'status':'EN ATTENTE DE VALIDATION HUMAINE','sourceAnnotations':{'start':start,'bottom':bottom,'end':end},'initial':'NON TESTÉ: cropped set begins at repetition start, no preceding hold','descent':{'start':start,'end':bottom,'fractionNegativePelvisProxyVelocity':float((velocity[:mid]<0).mean())},'bottom':{'annotatedS':bottom,'pelvisProxyMinimumS':float(times[minimum]),'differenceS':float(times[minimum]-bottom),'plateau':'NON TESTÉ: no assumed dwell'},'ascent':{'start':bottom,'end':end,'fractionPositivePelvisProxyVelocity':float((velocity[mid:]>0).mean())},'finalStabilization':'NON TESTÉ: next repetition starts at11.94s, no recorded hold certified','pelvisInitialVelocityMS':float(velocity[0]),'pelvisFinalVelocityMS':float(velocity[-1])}
 report={'status':'REFUSÉ','runtimeEnabled':False,'frames':len(p),'fit':fit,'models':summaries,'sensitivityFixedEndpointOffsetsMM':sensitivity,'filtering':{'applied':False,'reason':'no smoothing to make rigid or force metrics pass'},'jointCentres':{'status':'NON TESTÉ','reason':'lateral epicondyle/malleolus only; no functional joint-centre calibration; sacral crests not certified PSIS; rigid marker fit not anatomical registration'},'OpenSim':{'status':'NON TESTÉ','reason':'recognized LaiUhlrich2022 template metadata inspected; no subject-specific ScaleTool/IK or marker registration executed'},'Rocketbox':{'status':'NON TESTÉ','reason':'gated before retarget: no qualified centres/axes; no GLB created'},'questions':{'sourceReliability':'EN ATTENTE DE VALIDATION HUMAINE','anatomicalSkeleton':'EN ATTENTE DE VALIDATION HUMAINE','transferToRocketbox':'NON TESTÉ'}}
 (ROOT/'markers-report.json').write_text(json.dumps(marker_report,ensure_ascii=False,indent=2)+'\n');(ROOT/'forces-report.json').write_text(json.dumps(forces,ensure_ascii=False,indent=2)+'\n');(ROOT/'reconstruction-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');(ROOT/'phases-report.json').write_text(json.dumps(phases,ensure_ascii=False,indent=2)+'\n')
 # Small reproducible review data transported as text, avoids artifact download dependence.
 review={'status':'REFUSÉ','meaning':'measured surface markers + diagnostic segment chains, NOT validated skeleton','times':times.tolist(),'names':names,'markers':np.round(p,6).tolist(),'staticMedian':np.round(static,6).tolist(),'forces':{n:f[n].tolist() for n in f.dtype.names if n!='time'},'bottom':bottom}
 (ROOT/'trajectories.json').write_text(json.dumps(series)+'\n')
 (ROOT/'review-data.json').write_text(json.dumps(review,separators=(',',':'))+'\n')
if __name__=='__main__':main()
