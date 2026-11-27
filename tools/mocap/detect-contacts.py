"""Conservative source-joint contact hypotheses, not force-plate truth."""
from pathlib import Path
import json,math,statistics
root=Path('docs/coach/phase6');samples=json.loads((root/'source-samples.json').read_text());report={'sampleHz':60,'thresholds':{'stanceHeightM':.015,'stanceSpeedMS':.08,'airCandidateHeightM':.04,'minWindowSeconds':.15},'method':'Toe-joint proxy height and horizontal speed, median ground from first 0.2 s; feet not video-verified; no correction for uncertain/moving/air-candidate samples','frames':[],'windows':[]}
for side,long in [('L','Left'),('R','Right')]:
 toe=[s['joints'][long+'ToeBase'] for s in samples];ground=statistics.median(p[1] for p in toe[:13]);flags=[]
 for i,s in enumerate(samples):
  a=toe[max(0,i-1)];b=toe[min(len(toe)-1,i+1)];dt=(min(len(toe)-1,i+1)-max(0,i-1))/60;speed=math.hypot(b[0]-a[0],b[2]-a[2])/dt;height=toe[i][1]-ground
  state='stance_candidate' if height<=.015 and speed<=.08 else 'air_candidate' if height>.04 else 'moving_or_uncertain';flags.append(state=='stance_candidate');report['frames'].append({'time':s['time'],'side':side,'state':state,'toeHeightM':height,'horizontalSpeedMS':speed})
 start=None
 for i,flag in enumerate(flags+[False]):
  if flag and start is None:start=i
  if not flag and start is not None:
   end=i-1
   if (end-start)/60>=.15:report['windows'].append({'side':side,'start':start/60,'end':end/60,'ramp':min(.08,(end-start)/240),'status':'estimated-not-professionally-reviewed'})
   start=None
(root/'contact-classification.json').write_text(json.dumps(report,indent=2)+'\n');print(report['windows'])
