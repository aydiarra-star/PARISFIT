"""Decode every evidence video entirely; write checksums and decoded frame counts."""
from pathlib import Path
import subprocess,os,json,hashlib
root=Path('docs/coach/phase2');report={'method':'Full FFmpeg decode, all frames; offline WebGL renders, not device benchmarks','files':[]}
for stage in ['before','after']:
 manifest=json.loads((root/stage/'capture-manifest.json').read_text())
 if stage=='before' and 'modelSHA256' not in manifest:
  manifest['modelSHA256']=hashlib.sha256(Path('.cache/phase2/before.glb').read_bytes()).hexdigest();(root/stage/'capture-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 for clip in manifest['clips']:
  for view in ['face','profil','trois-quarts','slow']:
   p=root/stage/(clip['name']+'-'+view+'.mp4')
   result=subprocess.run([os.environ['FFMPEG_PATH'],'-v','error','-i',str(p),'-progress','pipe:1','-f','null','-'],capture_output=True,text=True,check=True)
   assert not result.stderr.strip(),result.stderr
   frames=[int(x.split('=')[1]) for x in result.stdout.splitlines() if x.startswith('frame=')][-1]
   duration=[int(x.split('=')[1])/1e6 for x in result.stdout.splitlines() if x.startswith('out_time_us=')][-1]
   assert frames>=clip['frames']
   assert duration>=clip['duration']*(1.9 if view=='slow' else 1)
   report['files'].append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'decodedFrames':frames,'durationSeconds':duration,'status':'PASS'})
assert len(report['files'])==64
report['status']='PASS';(root/'video-report.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS: 64 videos fully decoded')
