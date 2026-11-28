import json,hashlib,subprocess,imageio_ffmpeg
from pathlib import Path
root=Path('docs/coach/phase6');result={'status':'PASS','scope':'Decode/integrity, NOT motion approval','videos':[],'assets':[]}
for c in json.loads((root/'comparison-manifest.json').read_text())['cases']:
 for view in ['face','profil','trois-quarts','slow']:
  p=root/(c['id']+'-'+view+'.mp4');r=subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-v','error','-i',str(p),'-progress','pipe:1','-f','null','-'],capture_output=True,text=True,check=True);assert not r.stderr.strip();fields=dict(x.split('=',1) for x in r.stdout.splitlines() if '=' in x);frames=int(fields['frame']);duration=int(fields['out_time_us'])/1e6;assert frames>=c['frames'];assert duration>=2.4*(1.9 if view=='slow' else 1);result['videos'].append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'frames':frames,'durationSeconds':duration})
for file in ['source-14_06.bvh','source-22_14.bvh','retargeted.glb','corrected.glb','source-samples.json','retarget-frames.json']:
 p=root/file;result['assets'].append({'file':file,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
(root/'evidence-report.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS: 12 complete videos + original BVHs and GLBs integrity')
