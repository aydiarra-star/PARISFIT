"""Bounded acquisition, pinned public blobs only. No author code is executed."""
import base64, hashlib, json, subprocess
from pathlib import Path
REF='a26fe4852a78f30c5e8a437b158847031cb8dc3c'
REPO='WeRoLab/healthy-whole-body-noncyclic-dataset'
CACHE=Path('.cache/phase17/source'); OUT=Path('docs/coach/phase17')
def api(path):return json.loads(subprocess.check_output(['gh','api',f'repos/{REPO}/{path}']))
def main():
 tree=api(f'git/trees/{REF}?recursive=1');assert not tree['truncated'];items={x['path']:x for x in tree['tree']}
 paths=['AB01/Squat/1/Data/squat_1.c3d','AB01/Static/1/Data/static.c3d','Model/marker_set.xml','Model/Biomech57.osim','MATLAB tools/trial_class.m','Readme.pdf']
 paths += [p for p in items if p.startswith(('AB01/Squat/1/Setup/','AB01/Static/1/Setup/','AB01/Squat/1/Processing/','AB01/Static/1/Processing/','All subjects processing/')) and p.endswith(('.xml','.m','.mat'))]
 assert sum(items[p]['size'] for p in paths)<15000000
 rows=[]
 for p in paths:
  x=items[p];dest=CACHE/p;dest.parent.mkdir(parents=True,exist_ok=True)
  b=dest.read_bytes() if dest.exists() else base64.b64decode(api('git/blobs/'+x['sha'])['content'])
  assert len(b)==x['size'];assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['sha']
  dest.write_bytes(b);rows.append({'path':p,'bytes':len(b),'gitBlob':x['sha'],'sha256':hashlib.sha256(b).hexdigest(),'md5':hashlib.md5(b).hexdigest()})
 for p,h in {'Readme.pdf':'cd440a4a2365bc9f3a5da8385201df94','Model/marker_set.xml':'b6f4f1cd418353e7af5fd0007e936e2e','Model/Biomech57.osim':'dddb2c1c25da0b3266261bad0e27cc68'}.items():assert hashlib.md5((CACHE/p).read_bytes()).hexdigest()==h
 inventory=[{'path':p,'bytes':x['size'],'gitBlob':x['sha']} for p,x in items.items() if p.endswith('.c3d') and ('/Squat/' in p or '/Static/' in p)]
 OUT.mkdir(parents=True,exist_ok=True);(OUT/'source-manifest.json').write_text(json.dumps({'repository':REPO,'commit':REF,'files':rows,'downloadedBytes':sum(r['bytes'] for r in rows),'inventoryNotAllDownloaded':inventory,'authorCodeExecuted':False,'treeTruncated':False,'missingDependencySearch':{n:[p for p in items if p.split('/')[-1].lower()==n.lower()] for n in ['Scale.m','IK.m','osimC3D.m','one_leg_squat_shoe_lace_samples.mat']},'publishedMD5Matched':{'Readme.pdf':'cd440a4a2365bc9f3a5da8385201df94','Model/marker_set.xml':'b6f4f1cd418353e7af5fd0007e936e2e','Model/Biomech57.osim':'dddb2c1c25da0b3266261bad0e27cc68'}},indent=2)+'\n')
 print('Acquired',len(rows),'files;',sum(r['bytes'] for r in rows),'bytes')
if __name__=='__main__':main()
