"""Branches from unfiltered input; never passes a filtered stream into retargeting."""
from pathlib import Path
import json,hashlib,numpy as np
from bvh import parse,fk
SCALE=.056444;NORMAL=.9469891623878913
ROOT=Path('.cache/phase12');DOC=Path('docs/coach/phase12')
def metrics(p,dt,names,parents):
 v=np.diff(p,axis=0)/dt;a=np.diff(v,axis=0)/dt;sn=np.linalg.norm(v,axis=2);an=np.linalg.norm(a,axis=2);i,j=np.unravel_index(an.argmax(),an.shape)
 out={'frames':len(p),'sampleHz':1/dt,'maxSpeed':float(sn.max()),'maxAcceleration':float(an.max()),'peakAccelerationJoint':names[j],'peakAccelerationSample':int(i+1),'p95Acceleration':float(np.quantile(an,.95)),'maxStep':float(np.linalg.norm(np.diff(p,axis=0),axis=2).max()),'finite':bool(np.isfinite(p).all())}
 lengths=[np.linalg.norm(p[:,j]-p[:,par],axis=1) for j,par in enumerate(parents) if par is not None];out['maxSegmentLengthChange']=float(max(np.ptp(x) for x in lengths))
 def ix(n):return names.index(n)
 def angle(a,b,c):
  u=p[:,ix(a)]-p[:,ix(b)];v=p[:,ix(c)]-p[:,ix(b)];return np.rad2deg(np.arccos(np.clip(np.sum(u*v,axis=1)/(np.linalg.norm(u,axis=1)*np.linalg.norm(v,axis=1)),-1,1)))
 out['kneeFlexionDeg']={s:{'min':float((180-angle(s+'UpLeg',s+'Leg',s+'Foot')).min()),'max':float((180-angle(s+'UpLeg',s+'Leg',s+'Foot')).max())} for s in ['Left','Right']}
 trunk=p[:,ix('Neck')]-p[:,ix('Hips')];tilt=np.rad2deg(np.arccos(np.clip(trunk[:,1]/np.linalg.norm(trunk,axis=1),-1,1)));out['trunkTiltDeg']={'min':float(tilt.min()),'max':float(tilt.max())}
 out['pelvisAcceleration']=float(an[:,ix('Hips')].max());out['entryExitMaxJointDistance']=float(np.linalg.norm(p[-1]-p[0],axis=1).max());out['feet']={}
 for s in ['Left','Right']:
  j=ix(s+'Foot');toe=ix(s+'ToeBase');speed=np.linalg.norm(v[:,j],axis=1);candidate=speed<.08;drift=0.;anchor=None
  for k,c in enumerate(candidate):
   if c:
    if anchor is None:anchor=p[k,j]
    drift=max(drift,float(np.linalg.norm((p[k+1,j]-anchor)[[0,2]])))
   else:anchor=None
  out['feet'][s]={'pivotMinY':float(p[:,j,1].min()),'toeMinY':float(p[:,toe,1].min()),'horizontalRange':np.ptp(p[:,j,[0,2]],axis=0).tolist(),'candidateFrames':int(candidate.sum()),'candidateDrift':drift,'meaning':'low-speed pivot only; not sole contact or force; ground unknown'}
 return out
def interpolate(p,dt,times):
 x=times/dt;i=np.floor(x).astype(int);u=(x-i)[:,None,None];return p[i]*(1-u)+p[np.minimum(i+1,len(p)-1)]*u
def smooth(p):return (p[:-2]+2*p[1:-1]+p[2:])/4

def run():
 ROOT.mkdir(parents=True,exist_ok=True);reports=[]
 fixtures=[('14_06',Path('docs/coach/phase6/source-14_06.bvh'))]+[(n,ROOT/(n+'.bvh')) for n in ['14_14','13_30','86_08']]
 for name,path in fixtures:
  raw=path.read_bytes();nodes,ch,dt=parse(raw.decode());pos=fk(nodes,ch);keep=[i for i,b in enumerate(nodes) if not b['name'].endswith('__End')];names=[nodes[i]['name'] for i in keep];parents=[keep.index(nodes[i]['parent']) if nodes[i]['parent'] is not None else None for i in keep];p=pos[:,keep]
  # No raw marker claims: this is the unmodified converted BVH fixture.
  base=p[1:];m=base*SCALE
  report={'id':name,'status':'EN ATTENTE DE VALIDATION HUMAINE','selectedReference':False,'inputSHA256':hashlib.sha256(raw).hexdigest(),'format':'converted BVH, NOT original marker capture','declaredHz':1/dt,'timing':'single declared Frame Time, no per-frame capture timestamps','frames':len(p),'durationS':(len(p)-1)*dt,'artificialFrame0TransitionMaxRawUnits':float(np.linalg.norm(p[1]-p[0],axis=1).max()),'axes':'BVH Y-up, X/Z ground plane; no heading rotation for invariant speed norms','names':names,'parents':parents,'zeroParentOffsets':[nodes[i]['name'] for i in keep if nodes[i]['parent'] is not None and np.linalg.norm(nodes[i]['offset'])<1e-6],'rawUnitsFullExcludingArtificialFrame0':metrics(base,dt,names,parents),'meterFullExcludingArtificialFrame0':metrics(m,dt,names,parents),'missingMeasurement':['capture timestamps','forces','sole patches','original marker residuals'],'branches':{}}
  if name=='14_06':
   # Native window and 60Hz window share exact bounds only to nearest native sample.
   start,end=8.6,11.;lo=int(np.ceil(start/dt));hi=int(np.floor(end/dt));native=p[lo:hi+1]*SCALE;ts=np.arange(145)/60+start
   branches={'native_m':(native,dt,{'input':'unfiltered BVH FK','startS':lo*dt,'endS':hi*dt}), 'filtered_only_m':(smooth(native),dt,{'input':'native_m','kernel':[.25,.5,.25],'edge':'drop1sample per side','warning':'diagnostic Cartesian filter distorts bone lengths; never retargeted'}),'resampled_position60_m':(interpolate(p*SCALE,dt,ts),1/60,{'input':'unfiltered BVH FK','method':'linear joint-position interpolation','startS':start,'endS':end}),'normalized_only_m':(native*NORMAL,dt,{'input':'native_m','uniformScale':NORMAL})}
   # Same channel interpolation as Blender: unwrap Euler before evaluating its FK.
   channels=ch.copy()
   for bone in nodes:
    for channel,k in bone['channels']:
     if channel.endswith('rotation'):channels[:,k]=np.rad2deg(np.unwrap(np.deg2rad(channels[:,k])))
   res=np.array([np.interp(ts,np.arange(len(ch))*dt,channels[:,k]) for k in range(ch.shape[1])]).T
   euler=fk(nodes,res)[:,keep]*SCALE;branches['resampled_channels60_m']=(euler,1/60,{'input':'unfiltered BVH channels','method':'unwrapped Euler linear interpolation then FK'})
   branches['historical_normalized60_m']=(euler*NORMAL,1/60,{'input':'resampled_channels60_m','uniformScale':NORMAL,'purpose':'reproduce historical combination, not independent ablation'})
   for label,(points,step,params) in branches.items():
    dest=ROOT/(label+'.npz');np.savez_compressed(dest,positions=points,dt=step,names=names,parents=np.array([-1 if p is None else p for p in parents]));report['branches'][label]={'parameters':params,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'metrics':metrics(points,step,names,parents)}
   center=(native[:-2]+native[2:])/2;report['highFrequencyResidualProxyRMSM']=float(np.sqrt(np.mean((native[1:-1]-center)**2)));report['noiseInterpretation']='second-difference residual mixes genuine acceleration and noise; NOT measured sensor noise'
   # Derivative estimator check: central second difference == diff(diff(x))/dt².
   report['secondDifferenceAgreement']=float(np.max(np.abs((native[2:]-2*native[1:-1]+native[:-2])/dt**2-np.diff(np.diff(native,axis=0),axis=0)/dt**2)))
   expected=report['branches']['native_m']['metrics']['maxAcceleration']*NORMAL;actual=report['branches']['normalized_only_m']['metrics']['maxAcceleration'];report['normalizationLinearScalingResidual']=abs(expected-actual)
   # Small auditable diagnostic samples; no ground projection, no morphology retarget.
   viewer={'names':names,'parents':parents,'times':(ts-start).tolist(),'positions':euler.tolist(),'status':'REFUSÉ','meaning':'source joint geometry, not filmed person; ground uncalibrated'};(ROOT/'viewer.json').write_text(json.dumps(viewer,separators=(',',':'))+'\n')
  np.savez_compressed(ROOT/(name+'-native.npz'),positions=p,channels=ch,dt=dt,names=names)
  (ROOT/(name+'-report.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');reports.append(report)
 result={'status':'REFUSÉ','qualifiedSecondReference':None,'reason':'No candidate has established contacts, complete annotated squat cycle and visual/professional review; whole-clip screening is NOT matched-cycle benchmarking','sources':reports,'retargeting':{m:json.loads(Path('docs/coach/phase11',m+'_report.json').read_text()) for m in 'ABC'}}
 (ROOT/'benchmark.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':run()
