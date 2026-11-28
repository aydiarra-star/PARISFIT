"""Diagnostic surface-landmark chains, not a human avatar replacement."""
from pathlib import Path
import json,numpy as np,hashlib,subprocess,sys
from PIL import Image,ImageDraw
from core import reconstruct
ROOT=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.cache/phase13');d=json.loads((ROOT/'review-data.json').read_text());p=np.array(d['markers']);names=d['names'];times=np.array(d['times']);models,_=reconstruct(p,np.array(d['staticMedian']),names);F1=np.array(d['forces']['PLATE_1_Fz']);F2=np.array(d['forces']['PLATE_2_Fz']);origin=models['H0_skin_landmarks']['pelvis'][0].copy();origin[2]=0;outputs=[]
pairs=[('pelvis','trunk'),('trunk','head')]
for side in ['Right','Left']:
 pairs += [('pelvis',side+'_hip'),(side+'_hip',side+'_knee'),(side+'_knee',side+'_ankle'),(side+'_ankle',side+'_toe'),('trunk',side+'_shoulder'),(side+'_shoulder',side+'_elbow'),(side+'_elbow',side+'_wrist')]
def frame(i,mode):
 im=Image.new('RGB',(960,500),'#edf5ef');draw=ImageDraw.Draw(im);draw.text((12,8),'Michaud2026 CC BY4.0 | S01 P001 rep1 | '+mode+' | t='+str(round(times[i],2)),fill='#164b39')
 pts=models[mode];q=p[i]-origin
 for view in range(3):
  def project(v):
   x=v[0] if view==0 else v[1] if view==1 else (v[0]+v[1])/2**.5
   return int(view*320+160+x*155),int(340-v[2]*155)
  draw.text((view*320+10,30),['Front-like','Side-like','Oblique'][view]+' / lab axes',fill='#164b39')
  for v in q:
   x,y=project(v);draw.ellipse((x-2,y-2,x+2,y+2),fill='#596b61')
  for a,b in pairs:draw.line([project(pts[a][i]-origin),project(pts[b][i]-origin)],fill='#c54d3b',width=2)
  draw.text((view*320+8,353),'Coral = hypothesis, NOT joint centres',fill='#84301f')
 # Force traces stay independent of reconstruction; no COP or force arrows at guessed contact points.
 x0,y0,w,h=25,395,610,76
 for F,color in [(F1,'#164b39'),(F2,'#c54d3b')]:
  poly=[(x0+k/(len(times)-1)*w,y0+h-v/650*h) for k,v in enumerate(F)];draw.line(poly,fill=color,width=2)
 cursor=x0+i/(len(times)-1)*w;draw.line([(cursor,y0-h*.1),(cursor,y0+h)],fill='#333333');draw.text((660,399),'Plate1 Fz '+str(round(F1[i],1))+' N',fill='#164b39');draw.text((660,422),'Plate2 Fz '+str(round(F2[i],1))+' N',fill='#c54d3b');draw.text((12,480),'Grey = measured skin markers | geometry not anatomically qualified | no Rocketbox retarget',fill='#164b39');return im
for mode in models:
 dest=ROOT/(mode+'.mp4');proc=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','960x500','-r','100','-i','pipe:0','-an','-c:v','libx264','-crf','25','-pix_fmt','yuv420p','-movflags','+faststart',str(dest)],stdin=subprocess.PIPE)
 for i in range(len(times)):proc.stdin.write(frame(i,mode).tobytes())
 proc.stdin.close();assert proc.wait()==0
 dec=subprocess.run(['ffmpeg','-v','error','-i',str(dest),'-progress','pipe:1','-f','null','-'],capture_output=True,text=True,check=True);assert not dec.stderr.strip();fields=dict(x.split('=',1) for x in dec.stdout.splitlines() if '=' in x);assert int(fields['frame'])==150
 frame(int(np.argmin(abs(times-d['bottom']))),mode).save(ROOT/(mode+'.png'))
 outputs.append({'file':dest.name,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'frames':150,'seconds':int(fields['out_time_us'])/1e6})
(ROOT/'render-report.json').write_text(json.dumps({'status':'VALIDÉ','scope':'render + full decode, NOT visual or professional approval','videos':outputs},indent=2)+'\n')
page='<!doctype html><html lang="fr"><meta charset="utf-8"><title>Phase13 diagnostics</title><style>body{font:16px system-ui;max-width:1050px;margin:auto;background:#edf5ef;color:#164b39}video,img{width:100%}</style><h1>Michaud2026 — reconstruction non qualifiée</h1><p>CC BY4.0. Marqueurs cutanés et hypothèses, pas centres articulaires mesurés. Aucun retarget Rocketbox.</p>'
for o in outputs:page+='<h2>'+o['file']+'</h2><video controls playsinline preload="none" src="'+o['file']+'"></video>'
page+='<p><a href="NOTICE.txt">Attribution</a> · <a href="reconstruction-report.json">Rapport</a> · <a href="markers-report.json">Marqueurs</a> · <a href="forces-report.json">Forces</a></p>'; (ROOT/'index.html').write_text(page)
