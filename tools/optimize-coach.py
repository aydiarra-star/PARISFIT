"""Repack colour textures as JPEG and preserve lossless PNG normals; keep the rig and clips untouched."""
from pathlib import Path
import struct,json,io
from PIL import Image
p=Path('assets/coach/coach.glb');raw=p.read_bytes();n=struct.unpack_from('<I',raw,12)[0];doc=json.loads(raw[20:20+n]);binary=raw[28+n:];replacements={}
normalSources={doc['textures'][m['normalTexture']['index']]['source'] for m in doc['materials'] if 'normalTexture' in m}
headSources={doc['textures'][m['pbrMetallicRoughness']['baseColorTexture']['index']]['source'] for m in doc['materials'] if m.get('name')=='Rocketbox head'}
for index,image in enumerate(doc.get('images',[])):
 view=doc['bufferViews'][image['bufferView']];data=binary[view.get('byteOffset',0):view.get('byteOffset',0)+view['byteLength']]
 im=Image.open(io.BytesIO(data)).convert('RGB');size=2048 if index in headSources and index not in normalSources else 1024;im.thumbnail((size,size));out=io.BytesIO();im.save(out,format='PNG' if index in normalSources else 'JPEG',quality=94,optimize=True)
 replacements[image['bufferView']]=out.getvalue();image['mimeType']='image/png' if index in normalSources else 'image/jpeg'
result=bytearray()
for i,view in enumerate(doc['bufferViews']):
 data=replacements.get(i,binary[view.get('byteOffset',0):view.get('byteOffset',0)+view['byteLength']]);result.extend(b'\0'*((-len(result))%4));view['byteOffset']=len(result);view['byteLength']=len(data);result.extend(data)
result.extend(b'\0'*((-len(result))%4));doc['buffers'][0]['byteLength']=len(result)
js=json.dumps(doc,separators=(',',':')).encode();js+=b' '*((-len(js))%4)
p.write_bytes(struct.pack('<III',0x46546c67,2,28+len(js)+len(result))+struct.pack('<II',len(js),0x4e4f534a)+js+struct.pack('<II',len(result),0x004e4942)+result)
print(f'GLB {len(raw):,} → {p.stat().st_size:,} bytes')
