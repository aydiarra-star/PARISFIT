from pathlib import Path
import subprocess,json,hashlib,os
root=Path('docs/coach/phase3');report={'status':'PASS','method':'Full FFmpeg decode; source-retarget before versus floor-corrected after','files':[]}
for stage in ['before','after']:
 manifest=json.loads((root/stage/'capture-manifest.json').read_text())
 for clip in manifest['clips']:
  for view in ['face','profil','trois-quarts','slow']:
   p=root/stage/(clip['name']+'-'+view+'.mp4');r=subprocess.run([os.environ['FFMPEG_PATH'],'-v','error','-i',str(p),'-progress','pipe:1','-f','null','-'],capture_output=True,text=True,check=True);assert not r.stderr.strip()
   fields=dict(line.split('=',1) for line in r.stdout.splitlines() if '=' in line);frames=int(fields['frame']);duration=int(fields['out_time_us'])/1e6
   assert frames>=clip['frames'];assert duration>=clip['duration']*(1.9 if view=='slow' else 1)
   report['files'].append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'frames':frames,'durationSeconds':duration})
assert len(report['files'])==16
(root/'video-report.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS: 16 transition videos fully decoded')
