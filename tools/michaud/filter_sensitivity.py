"""Display-data sensitivity only, never input to retarget or admission."""
from pathlib import Path
import numpy as np,json
from core import angle,dynamics
R=Path('docs/coach/phase13');d=json.loads((R/'review-data.json').read_text());p=np.array(d['markers']);names=d['names'];idx=[names.index('Right_'+n) for n in ['greater_trochanter','lateral_epicondyle','lateral_malleolus']]
def knee(q):return 180-angle(*[q[:,j] for j in idx])
rows=[]
for window in [1,5,9]:
 h=window//2;q=p.copy()
 if h:
  pad=np.pad(p,((h,h),(0,0),(0,0)),mode='reflect');q=sum(pad[i:i+len(p)] for i in range(window))/window
 # Common interior excludes boundary padding and derivative edge effects.
 sl=slice(5,-5);rows.append({'windowSamples':window,'windowMs':window*10,'commonInteriorFrames':140,'maxPositionChangeM':float(np.linalg.norm((q-p)[sl],axis=2).max()),'maxKneeProxyChangeDeg':float(abs(knee(q)[sl]-knee(p)[sl]).max()),'interiorDynamics':dynamics(q[sl],.01)})
(R/'filter-sensitivity.json').write_text(json.dumps({'status':'VALIDÉ','scope':'numerical sensitivity on six-decimal review samples, not anatomical validation','method':'centred boxcar windows1/5/9, reflected boundaries, common interior frames5..144 only; no selected optimal filter','usedInReconstruction':False,'usedInRetarget':False,'rows':rows},indent=2)+'\n')
