"""Read-only C3D metadata via stdlib, plus historical JSON/Git provenance. No motion processing."""
from pathlib import Path
import struct,json,hashlib,subprocess,inspect,sys
D=Path('docs/coach/phase18');P=Path('docs/coach/phase17');BASE='f4d4146a372d08acca620b1a9facf54368c1fcda'
def sha(b):return hashlib.sha256(b).hexdigest()
def display_diff(s):return '# Git excerpt; trailing whitespace removed for presentation only. Original blobs identified by commit and SHA256.\n'+'\n'.join(line.rstrip() for line in s.splitlines())+'\n'
def save(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def parameters(b,block):
 start=(block-1)*512;assert b[start+3]==84,'Intel format only';pos=start+4;groups={};values=[]
 while pos+2<len(b):
  ln,gid=struct.unpack_from('bb',b,pos)
  if ln==0:break
  name=b[pos+2:pos+2+abs(ln)].decode('ascii');q=pos+2+abs(ln);nxt=struct.unpack_from('<h',b,q)[0];v=q+2
  if gid<0:groups[-gid]=name
  else:
   typ,ndim=struct.unpack_from('bB',b,v);dims=list(b[v+2:v+2+ndim]);count=1
   for dim in dims:count*=dim
   raw=b[v+2+ndim:v+2+ndim+abs(typ)*count];values.append((gid,name,typ,dims,raw))
  if nxt==0:break
  assert nxt>0;pos=q+nxt
 out={}
 for gid,name,typ,dims,raw in values:
  key=groups[gid]+':'+name
  if key in ['POINT:FRAMES','POINT:RATE','POINT:USED','POINT:DATA_START','POINT:SCALE','ANALOG:RATE','ANALOG:USED','TRIAL:ACTUAL_START_FIELD','TRIAL:ACTUAL_END_FIELD','POINT:LONG_FRAMES']:
   fmt={2:'H',4:'f',1:'B'}[typ];out[key]={'type':typ,'dimensions':dims,'values':list(struct.unpack('<'+fmt*(len(raw)//abs(typ)),raw))}
 return out

def binary(path):
 b=path.read_bytes();assert b[1]==80
 h={'firstParameterBlock':b[0],'pointCount':struct.unpack_from('<H',b,2)[0],'analogValuesPerPointFrame':struct.unpack_from('<H',b,4)[0],'firstFrame':struct.unpack_from('<H',b,6)[0],'lastFrame':struct.unpack_from('<H',b,8)[0],'pointScale':struct.unpack_from('<f',b,12)[0],'dataStartBlock':struct.unpack_from('<H',b,16)[0],'analogSubsamples':struct.unpack_from('<H',b,18)[0],'pointRateHz':struct.unpack_from('<f',b,20)[0]};params=parameters(b,b[0]);assert h['pointScale']<0
 size=(h['pointCount']*4+h['analogValuesPerPointFrame'])*4;data=len(b)-(h['dataStartBlock']-1)*512;n,tail=divmod(data,size)
 return {'sha256':sha(b),'header':h,'parameters':params,'fileBytes':len(b),'frameBytes':size,'completeFrames':n,'trailingBytes':tail,'trailingAllZero':not any(b[len(b)-tail:]) if tail else True,'inclusiveHeaderFrames':h['lastFrame']-h['firstFrame']+1,'recordCountAgreement':n==params['POINT:FRAMES']['values'][0],'clockOriginProven':False,'repaired':False}

def differences(a,b,path=''):
 if type(a)!=type(b):return [{'path':path,'old':a,'new':b}]
 if isinstance(a,dict):return [x for k in sorted(a.keys()|b.keys()) for x in differences(a.get(k),b.get(k),path+'/'+k)]
 if isinstance(a,list):return [x for i in range(max(len(a),len(b))) for x in differences(a[i] if i<len(a) else None,b[i] if i<len(b) else None,path+'/'+str(i))]
 return [] if a==b else [{'path':path,'old':a,'new':b,'delta':b-a if isinstance(a,(int,float)) and not isinstance(a,bool) else None}]
def gitbytes(ref,path):return subprocess.check_output(['git','show',ref+':'+path])
def main():
 sm=json.loads((P/'source-manifest.json').read_text());rows={}
 for rec in sm['files']:
  if rec['path'].endswith('.c3d'):
   p=Path('.cache/phase17/source')/rec['path'];v=binary(p);assert v['sha256']==rec['sha256'];rows[rec['path']]=v
 save('c3d-independent-byte-audit.json',{'method':'stdlib struct reader, header and parameter records independently decoded; no trajectory loading or write','files':rows})
 pairs=[('mobile','docs/coach/phase2/mobile-report.json','docs/coach/phase17/legacy-mobile-rerun.json'),('transition','docs/coach/phase3/transition-report.json','docs/coach/phase17/legacy-transition-rerun.json')];out={}
 for key,a,b in pairs:
  aa=Path(a).read_bytes();bb=Path(b).read_bytes();out[key]={'old':a,'new':b,'oldSHA256':sha(aa),'newSHA256':sha(bb),'differences':differences(json.loads(aa),json.loads(bb))}
 paths=['tools/coach-lab.html','tests/coach-transitions.cjs','tests/coach-mobile.cjs','vendor/three/three.module.js','assets/coach/transitions/candidates.json','assets/coach/coach.glb','coach-3d.js','package.json','package-lock.json'];out['gitFiles']={}
 for ref in ['697523f7f11661eb385c9b8ada821b1edbf1aa3b','c391ab8e7cd0a26c4a6a02b8b05fe39068407be8','52d903122a0e8179f5ecee6a7038565adac0a563',BASE]:
  out['gitFiles'][ref]={}
  for p in paths:
   result=subprocess.run(['git','show',ref+':'+p],capture_output=True)
   out['gitFiles'][ref][p]=sha(result.stdout) if result.returncode==0 else None
 old=json.loads(Path(pairs[1][1]).read_text())['clips'];out['oldSecondClipDuplicatesFirstExceptName']= {k:v for k,v in old[0].items() if k!='name'}=={k:v for k,v in old[1].items() if k!='name'}
 out['localEnvironment']={'node':subprocess.check_output(['node','--version']).decode().strip(),'python':sys.version.split()[0],'platform':sys.platform,'playwright':json.loads(Path('node_modules/@playwright/test/package.json').read_text())['version'],'threePackage':json.loads(Path('node_modules/three/package.json').read_text())['version'],'historicalBrowserBinaryVersion':'not recorded in the two original JSON reports'};save('historical-diff.json',out)
 excerpt=subprocess.check_output(['git','show','52d903122a0e8179f5ecee6a7038565adac0a563','--','tools/coach-lab.html','tests/coach-transitions.cjs']).decode();(D/'historical-code-evidence.txt').write_text(display_diff(excerpt))
 (D/'historical-mobile-code-evidence.txt').write_text(display_diff(subprocess.check_output(['git','diff','697523f7f11661eb385c9b8ada821b1edbf1aa3b',BASE,'--','tests/coach-mobile.cjs','coach-3d.js']).decode()))
 import c3d
 for name,v in rows.items():
  with (Path('.cache/phase17/source')/name).open('rb') as f:
   import warnings
   with warnings.catch_warnings():
    warnings.simplefilter('ignore');reader=c3d.Reader(f)
   v['pythonC3DComparison']={'rawHeaderLastFrame':int(reader.header.last_frame),'computedLastFrameProperty':int(reader.last_frame),'firstFrameProperty':int(reader.first_frame),'version':c3d.__version__}
 save('c3d-independent-byte-audit.json',{'method':'stdlib struct reader, header and parameter records independently decoded; source unchanged; no trajectories exported','files':rows})
 lines=[]
 for name,fn in [('first_frame',c3d.Reader.first_frame.fget),('last_frame',c3d.Reader.last_frame.fget)]:
  src,ln=inspect.getsourcelines(fn);lines+=['\n# '+name]+[f'{ln+i}: {s.rstrip()}' for i,s in enumerate(src)]
 src,ln=inspect.getsourcelines(c3d.Reader.read_frames)
 for i,s in enumerate(src):
  if 'for frame_no in range' in s or 'reached end of file' in s:lines.append(f'{ln+i}: {s.rstrip()}')
 (D/'python-c3d-reader-evidence.txt').write_text('python-c3d '+c3d.__version__+'\nSource SHA256 '+sha(Path(inspect.getfile(c3d.Reader)).read_bytes())+'\n'+'\n'.join(lines)+'\n')
 print('Independent counts:',[(k,v['completeFrames'],v['trailingBytes']) for k,v in rows.items()]);print('Historical deltas:',len(out['mobile']['differences']),len(out['transition']['differences']),'duplicated old clip:',out['oldSecondClipDuplicatesFirstExceptName'])
if __name__=='__main__':main()
