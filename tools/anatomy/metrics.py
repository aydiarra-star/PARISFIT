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
 return {'sourceTrajectoryProxy':{'rmsM':(sum(e*e for e in errors)/len(errors))**.5,'maxM':max(errors),'perJoint':per,'meaning':'fixed normalized source pivots vs target pivots; includes morphology and non-equivalent spine pivots; NOT anatomical fidelity'},'torsion':'NON TESTÉ: anatomical axes unavailable','meshCollision':'NON TESTÉ: only inherited sparse sphere candidates','smoothing':False,'admission':'REFUSÉ'}
