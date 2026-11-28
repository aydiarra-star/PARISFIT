"""All retained mesh/skin accessors and embedded texture bytes are byte-identical."""
import sys,json,struct
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from build_public import static_model,ROOT
raw=(ROOT/'assets/coach/coach.glb').read_bytes();derived=static_model(raw)
def parse(b):
 n=struct.unpack_from('<I',b,12)[0];return json.loads(b[20:20+n]),b[28+n:]
a,ab=parse(raw);b,bb=parse(derived)
def view(g,bin,i):
 v=g['bufferViews'][i];o=v.get('byteOffset',0);return bin[o:o+v['byteLength']]
def accessor(i,j):
 aa=dict(a['accessors'][i]);ba=dict(b['accessors'][j]);av=aa.pop('bufferView');bv=ba.pop('bufferView');assert aa==ba;assert view(a,ab,av)==view(b,bb,bv)
assert a['nodes']==b['nodes'];assert a['materials']==b['materials'];assert a['textures']==b['textures'];assert len(a['meshes'])==len(b['meshes']);assert len(a['images'])==len(b['images'])
for am,bm in zip(a['meshes'],b['meshes']):
 for ap,bp in zip(am['primitives'],bm['primitives']):
  assert ap['material']==bp['material'];assert ap['attributes'].keys()==bp['attributes'].keys()
  for k in ap['attributes']:accessor(ap['attributes'][k],bp['attributes'][k])
  accessor(ap['indices'],bp['indices'])
for aa,ba in zip(a['skins'],b['skins']):
 assert aa['joints']==ba['joints'];accessor(aa['inverseBindMatrices'],ba['inverseBindMatrices'])
for ai,bi in zip(a['images'],b['images']):assert view(a,ab,ai['bufferView'])==view(b,bb,bi['bufferView'])
assert 'animations' not in b
print('PASS: geometry, skeleton rest transforms, skin weights, indices, materials, four embedded textures byte-identical; no animation data references')
