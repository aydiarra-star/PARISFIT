import math
def extra_metrics(data,source,mapping):
 # Fixed source-root placement and scale; no per-frame best-fit alignment.
 errors=[];per={};speeds=[]
 for key,name in mapping.items():
  es=[]
  for f,s in zip(data['frames'],source):
   p=s['sourcePositions'][name];p=[p[0],p[2],-p[1]]
   es.append(math.dist(f['joints']['Bip01_'+key]['position'],p))
  per[key]={'rmsM':(sum(e*e for e in es)/len(es))**.5,'maxM':max(es)};errors+=es
 source_speed=[];source_acc=[];root_acc=[];per_acc={}
 for name in mapping.values():
  velocities=[[60*(b-a) for a,b in zip(prev['sourcePositions'][name],curr['sourcePositions'][name])] for prev,curr in zip(source,source[1:])]
  accelerations=[60*math.dist(a,b) for a,b in zip(velocities,velocities[1:])]
  source_speed.extend(math.sqrt(sum(x*x for x in v)) for v in velocities);source_acc+=accelerations;per_acc[name]=max(accelerations)
  if name=='Hips':root_acc=accelerations
 return {'sourceDiscreteDynamics':{'maxSpeedMS':max(source_speed),'maxAccelerationMS2':max(source_acc),'maxRootAccelerationMS2':max(root_acc) if root_acc else None,'perJointMaxAccelerationMS2':per_acc,'meaning':'same normalized source positions at 60Hz, without target FK or smoothing'},'sourceTrajectoryProxy':{'rmsM':(sum(e*e for e in errors)/len(errors))**.5,'maxM':max(errors),'perJoint':per,'meaning':'fixed normalized source pivots vs target pivots; includes morphology and non-equivalent spine pivots; NOT anatomical fidelity'},'torsion':'NON TESTÉ: anatomical axes unavailable','meshCollision':'NON TESTÉ: only inherited sparse sphere candidates','smoothing':False,'admission':'REFUSÉ'}
