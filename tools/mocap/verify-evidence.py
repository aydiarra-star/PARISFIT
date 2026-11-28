from pathlib import Path
import subprocess,json,hashlib,imageio_ffmpeg
root=Path('docs/coach/phase5');report={'status':'PASS','method':'Full FFmpeg decode of 16 comparison clips plus source and overlay; no visual-quality approval','videos':[],'artifacts':[]}
for p in sorted(root.glob('*.mp4'))+[root/'source.webm']:
 r=subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-v','error','-i',str(p),'-progress','pipe:1','-f','null','-'],capture_output=True,text=True,check=True);assert not r.stderr.strip(),r.stderr;fields=dict(s.split('=',1) for s in r.stdout.splitlines() if '=' in s);report['videos'].append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'frames':int(fields['frame']),'durationSeconds':int(fields['out_time_us'])/1e6})
assert len(report['videos'])==18
videos={v['file']:v for v in report['videos']}
for c in json.loads((root/'comparison-manifest.json').read_text())['cases']:
 for view in ['face','profil','trois-quarts','slow']:
  v=videos[c['id']+'-'+view+'.mp4'];assert v['frames']>=c['frames'];assert v['durationSeconds']>=c['duration']*(1.9 if view=='slow' else 1)
assert videos['source.webm']['frames']==videos['pose-overlay.mp4']['frames']==213
for name in ['video-prototype.glb','mocap-prototype.glb','pose-estimates.json','retarget-report.json','mocap-retarget-report.json']:
 p=root/name;report['artifacts'].append({'file':name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(root/'evidence-report.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS: 18 complete video decodes, source/GLB/landmark hashes')
