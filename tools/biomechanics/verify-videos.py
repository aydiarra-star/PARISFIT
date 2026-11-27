import subprocess,json,hashlib
from pathlib import Path
root=Path('.cache/phase10');rows=[]
for stage in ['before','after']:
 for view in ['face','profil','trois-quarts','slow']:
  p=root/(stage+'-'+view+'.mp4');r=subprocess.run(['ffmpeg','-v','error','-i',str(p),'-progress','pipe:1','-f','null','-'],capture_output=True,text=True,check=True);assert not r.stderr.strip();fields=dict(x.split('=',1) for x in r.stdout.splitlines() if '=' in x);frames=int(fields['frame']);duration=int(fields['out_time_us'])/1e6;assert frames>=59 and duration>=(4.7 if view=='slow' else 2.4);rows.append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'frames':frames,'seconds':duration})
(root/'video-report.json').write_text(json.dumps({'status':'VALIDÉ','scope':'complete decode, not visual approval','videos':rows},indent=2)+'\n')
