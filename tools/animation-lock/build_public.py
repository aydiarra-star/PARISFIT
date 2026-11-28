"""Public allowlist + geometry-only derivative. Original GLB/animation bytes never changed."""
from pathlib import Path
import json,struct,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2]
def sha(b):return hashlib.sha256(b).hexdigest()
def static_model(raw):
 n=struct.unpack_from('<I',raw,12)[0];g=json.loads(raw[20:20+n]);binary=raw[28+n:]
 # Only geometry/skin accessors and texture views survive; animation data is not shipped.
 used=set()
 for m in g['meshes']:
  for p in m['primitives']:
   used.update(p['attributes'].values())
   if 'indices'in p:used.add(p['indices'])
   for target in p.get('targets',[]):used.update(target.values())
 for s in g['skins']:used.add(s['inverseBindMatrices'])
 amap={old:i for i,old in enumerate(sorted(used))};acc=[g['accessors'][old] for old in sorted(used)]
 views={a['bufferView'] for a in acc}|{i['bufferView'] for i in g['images']}
 assert all('sparse' not in a for a in acc)
 vmap={old:i for i,old in enumerate(sorted(views))};out=bytearray();newviews=[]
 for old in sorted(views):
  v=dict(g['bufferViews'][old]);start=v.get('byteOffset',0);data=binary[start:start+v['byteLength']];out.extend(b'\0'*((-len(out))%4));v['byteOffset']=len(out);out.extend(data);newviews.append(v)
 for a in acc:a['bufferView']=vmap[a['bufferView']]
 for i in g['images']:i['bufferView']=vmap[i['bufferView']]
 for m in g['meshes']:
  for p in m['primitives']:
   p['attributes']={k:amap[v] for k,v in p['attributes'].items()}
   if 'indices'in p:p['indices']=amap[p['indices']]
   for t in p.get('targets',[]):
    for k,v in t.items():t[k]=amap[v]
 for s in g['skins']:s['inverseBindMatrices']=amap[s['inverseBindMatrices']]
 g.pop('animations');g['accessors']=acc;g['bufferViews']=newviews;g['buffers']=[{'byteLength':len(out)}];g['asset']['extras']={'purpose':'geometry-only display; no animation samples published'}
 text=json.dumps(g,separators=(',',':')).encode();text+=b' '*((-len(text))%4);out.extend(b'\0'*((-len(out))%4))
 return struct.pack('<4sII',b'glTF',2,28+len(text)+len(out))+struct.pack('<I4s',len(text),b'JSON')+text+struct.pack('<I4s',len(out),b'BIN\0')+out

def build():
 public=ROOT/'.cache/public';shutil.rmtree(public,ignore_errors=True);public.mkdir(parents=True)
 files=['vendor/three/LICENSE.txt','app-state.js','index.html','styles.css','app.js','demo-data.js','coach-3d.js','coach-content.js','coach-transition-gate.js','animation-validation.js','animation-validation-registry.json','service-worker.js','manifest.webmanifest','assets/icon.svg','assets/coach-welcome.jpg','assets/workout.jpg','assets/coach/licenses/ROCKETBOX-MIT.txt','vendor/three/three.module.js','vendor/three/loaders/GLTFLoader.js','vendor/three/utils/BufferGeometryUtils.js','vendor/three/controls/OrbitControls.js']
 files += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'assets/coach/previews').glob('*.jpg'))]
 for name in files:
  p=public/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,p)
 original=(ROOT/'assets/coach/coach.glb').read_bytes();static=static_model(original);(public/'assets/coach/coach-static.glb').write_bytes(static)
 report={'sourceSHA256':sha(original),'staticSHA256':sha(static),'staticBytes':len(static),'publicFiles':sorted(str(p.relative_to(public)) for p in public.rglob('*') if p.is_file()),'excluded':['tools/','docs/','tests/','.git/','assets/coach/coach.glb','assets/coach/transitions/'],'sourceUnmodified':sha((ROOT/'assets/coach/coach.glb').read_bytes())==sha(original)}
 (ROOT/'.cache/phase24-build.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':build()
