"""Small accessible diagnostic PNGs + MP4; skeletal diagnostics, not avatar assets."""
from pathlib import Path
import json,numpy as np,subprocess,hashlib
from PIL import Image,ImageDraw
ROOT=Path('.cache/phase12');files=[]
def render(p,names,parents,origin,label,vel=None,other=None):
 im=Image.new('RGB',(960,380),'#edf5ef');d=ImageDraw.Draw(im);d.text((12,8),label,fill='#164b39');p=p-origin
 for view in range(3):
  if view==0:x=p[:,0]
  elif view==1:x=p[:,2]
  else:x=(p[:,0]+p[:,2])/2**.5
  y=p[:,1];pts=[(int(view*320+160+v*130),int(340-h*130)) for v,h in zip(x,y)]
  d.text((view*320+10,30),['Front','Side','Three-quarter'][view]+' | floor uncalibrated',fill='#164b39')
  for j,par in enumerate(parents):
   if par>=0:d.line([pts[j],pts[par]],fill='#164b39',width=3)
  if other is not None:
   q=other-origin;ox=q[:,0] if view==0 else q[:,2] if view==1 else (q[:,0]+q[:,2])/2**.5;op=[(int(view*320+160+v*130),int(340-h*130)) for v,h in zip(ox,q[:,1])]
   for j,par in enumerate(parents):
    if par>=0:d.line([op[j],op[par]],fill='#c54d3b',width=1)
  for side in ['Left','Right']:

   j=names.index(side+'Foot');xx,yy=pts[j];candidate=vel is not None and vel[j]<.08;d.ellipse((xx-5,yy-5,xx+5,yy+5),fill='#c54d3b' if candidate else '#6699bb')
 d.text((12,363),'Red = low speed hypothesis, NOT measured contact | public CMU, NOT PARISFIT capture',fill='#84301f')
 return im
for label in ['native_m','filtered_only_m','resampled_channels60_m','historical_normalized60_m']:
 a=np.load(ROOT/(label+'.npz'));p=a['positions'];names=a['names'].tolist();parents=a['parents'].tolist();dt=float(a['dt']);origin=p[0,names.index('Hips')].copy();origin[1]=0
 # Render actual samples at declared rate, no resampling to improve measured metrics.
 dest=ROOT/(label+'.mp4');proc=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','960x380','-r',str(1/dt),'-i','pipe:0','-an','-c:v','libx264','-crf','23','-pix_fmt','yuv420p','-movflags','+faststart',str(dest)],stdin=subprocess.PIPE)
 for i,pose in enumerate(p):
  v=np.linalg.norm((pose-p[max(0,i-1)])/dt,axis=1);im=render(pose,names,parents,origin,label+' t='+str(round(i*dt,3))+'s',v if i else None);proc.stdin.write(im.tobytes())
  if i in [0,len(p)//2,len(p)-1]:im.save(ROOT/(label+'-'+str(i)+'.png'))
 proc.stdin.close();assert proc.wait()==0
 dec=subprocess.run(['ffmpeg','-v','error','-i',str(dest),'-progress','pipe:1','-f','null','-'],capture_output=True,text=True,check=True);assert not dec.stderr.strip();fields=dict(x.split('=',1) for x in dec.stdout.splitlines() if '=' in x);assert int(fields['frame'])==len(p)
 files.append({'file':dest.name,'frames':len(p),'seconds':int(fields['out_time_us'])/1e6,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
a=np.load(ROOT/'native_m.npz');p=a['positions'][1:-1];filtered=np.load(ROOT/'filtered_only_m.npz')['positions'];names=a['names'].tolist();parents=a['parents'].tolist();origin=p[0,names.index('Hips')].copy();origin[1]=0
render(p[len(p)//2],names,parents,origin,'Overlay: native green / filtered coral | same sample time',other=filtered[len(p)//2]).save(ROOT/'overlay.png')
(ROOT/'visual-report.json').write_text(json.dumps({'status':'VALIDÉ','scope':'render and complete decode only, NOT visual/professional approval','videos':files},indent=2)+'\n')
