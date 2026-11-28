"""Geometry hypotheses, never anatomical truth or force-driven correction."""
import numpy as np
def angle(a,b,c):
 u=a-b;v=c-b;den=np.linalg.norm(u,axis=-1)*np.linalg.norm(v,axis=-1)
 if np.any(den<1e-10):raise ValueError('DEGENERATE_ANGLE')
 return np.degrees(np.arccos(np.clip(np.sum(u*v,axis=-1)/den,-1,1)))
def rigid_fit(reference,points):
 """Least-squares rigid Procrustes/Kabsch. Row vectors: reference @ R + t."""
 x=reference-reference.mean(axis=0);y=points-points.mean(axis=0)
 if np.linalg.matrix_rank(x)<2:raise ValueError('DEGENERATE_CLUSTER')
 u,s,vt=np.linalg.svd(x.T@y);D=np.eye(3);D[-1,-1]=np.linalg.det(u@vt);R=u@D@vt;t=points.mean(axis=0)-reference.mean(axis=0)@R
 return R,t,float(np.sqrt(np.mean(np.sum((reference@R+t-points)**2,axis=1))))
def dynamics(p,dt):
 v=np.diff(p,axis=0)/dt;a=np.diff(p,n=2,axis=0)/dt**2
 return {'maxSpeedMS':float(np.linalg.norm(v,axis=-1).max()),'maxAccelerationMS2':float(np.linalg.norm(a,axis=-1).max()),'highFrequencySecondDifferenceRMSM':float(np.sqrt(np.mean((p[2:]-2*p[1:-1]+p[:-2])**2)))}
def reconstruct(p,static,names):
 get=lambda name:p[:,names.index(name)];sg=lambda name:static[names.index(name)]
 pelvis_names=['Right_ASIC','Left_ASIC','Right_sacral_crest','Left_sacral_crest'];ids=[names.index(n) for n in pelvis_names]
 reference=static[ids];fits=[rigid_fit(reference,q[ids]) for q in p]
 models={};anchors={};lengths={}
 for mode in ['H0_skin_landmarks','H1_static_lengths','H2_rigid_pelvis_static_lengths']:
  points={'pelvis':p[:,ids].mean(axis=1),'trunk':(get('Right_acromioclavicular_joint')+get('Left_acromioclavicular_joint'))/2,'head':get('Skull_vertex')}
  for side in ['Right','Left']:
   names3=[side+'_greater_trochanter',side+'_lateral_epicondyle',side+'_lateral_malleolus'];H,K,A=[get(n) for n in names3];l1=np.linalg.norm(sg(names3[1])-sg(names3[0]));l2=np.linalg.norm(sg(names3[2])-sg(names3[1]));lengths[side]={'staticThighProxyM':float(l1),'staticShankProxyM':float(l2),'notAnatomicalBoneLength':True}
   if mode=='H2_rigid_pelvis_static_lengths':H=np.array([sg(names3[0])@R+t for R,t,_ in fits])
   if mode!='H0_skin_landmarks':
    u=get(names3[1])-get(names3[0]);v=get(names3[2])-get(names3[1]);K=H+u/np.linalg.norm(u,axis=1)[:,None]*l1;A=K+v/np.linalg.norm(v,axis=1)[:,None]*l2
   for key,arr in [('hip',H),('knee',K),('ankle',A),('toe',get(side+'_1st_metatarsal_head')),('shoulder',get(side+'_acromioclavicular_joint')),('elbow',get(side+'_olecranon')),('wrist',get(side+'_ulna_head'))]:points[side+'_'+key]=arr
  models[mode]=points
 return models,{'pelvisClusterRMSM':float(np.sqrt(np.mean([e*e for _,_,e in fits]))),'pelvisClusterMaxFrameRMSM':max(e for _,_,e in fits),'staticLengths':lengths,'meaning':'cluster rigidity and virtual surface landmarks only; no hip/knee/ankle centre identified'}
