"""Engine-independent format and numeric contracts. Standard library only."""
import json,math,re,struct
class Invalid(ValueError):pass
REQUIRED=['Hips','LowerBack','Spine','Spine1','Neck','Head']+[s+n for s in ['Left','Right'] for n in ['UpLeg','Leg','Foot','ToeBase','Shoulder','Arm','ForeArm','Hand']]
def bvh_contract(text,units='cmu-converted'):
 if units!='cmu-converted':raise Invalid('UNITS_UNVERIFIED: expected documented CMU conversion')
 try:hierarchy,motion=text.split('MOTION',1)
 except ValueError:raise Invalid('BVH_MOTION_MISSING')
 if hierarchy.count('{')!=hierarchy.count('}'):raise Invalid('BVH_HIERARCHY_TRUNCATED')
 names=re.findall(r'(?:ROOT|JOINT)\s+(\S+)',hierarchy)
 if len(names)!=len(set(names)):raise Invalid('BVH_DUPLICATE_JOINT')
 missing=set(REQUIRED)-set(names)
 if missing:raise Invalid('BVH_JOINTS_MISSING:'+','.join(sorted(missing)))
 offsets=re.findall(r'OFFSET\s+([^\n\r]+)',hierarchy)
 for row in offsets:
  try:v=list(map(float,row.split()))
  except ValueError:raise Invalid('BVH_BAD_OFFSET')
  if len(v)!=3 or not all(math.isfinite(x) and abs(x)<1000 for x in v):raise Invalid('BVH_OFFSET_LIMIT')
 channels=0
 for row in re.findall(r'CHANNELS\s+([^\n\r]+)',hierarchy):
  items=row.split()
  if not items or not items[0].isdigit():raise Invalid('BVH_BAD_CHANNELS')
  if int(items[0])!=len(items)-1 or any(c not in [a+b for a in 'XYZ' for b in ['position','rotation']] for c in items[1:]):raise Invalid('BVH_BAD_CHANNELS')
  channels+=int(items[0])
 try:
  m=re.fullmatch(r'\s*Frames:\s*(\d+)\s*Frame Time:\s*([\d.eE+-]+)\s*\n(.*)',motion,re.S);count=int(m[1]);dt=float(m[2]);rows=m[3].strip().splitlines()
 except (TypeError,ValueError):raise Invalid('BVH_HEADER_INVALID')
 if count<2 or len(rows)!=count:raise Invalid('BVH_FRAME_COUNT')
 if not math.isfinite(dt) or not 1/240<=dt<=1/24:raise Invalid('BVH_TIMING_LIMIT')
 for i,row in enumerate(rows):
  try:v=list(map(float,row.split()))
  except ValueError:raise Invalid('BVH_FRAME_INVALID:'+str(i))
  if len(v)!=channels or not all(math.isfinite(x) and abs(x)<100000 for x in v):raise Invalid('BVH_FRAME_VALUES:'+str(i))
 return {'joints':len(names),'mappedRequired':len(REQUIRED),'frames':count,'frameTime':dt,'channels':channels}
def glb_contract(raw,expected='phase9-cmu-control'):
 if len(raw)<28:raise Invalid('GLB_TRUNCATED')
 magic,version,size=struct.unpack_from('<III',raw)
 if magic!=0x46546c67 or version!=2 or size!=len(raw):raise Invalid('GLB_HEADER')
 pos=12;chunks=[]
 while pos<len(raw):
  if pos+8>len(raw):raise Invalid('GLB_CHUNK_HEADER')
  n,t=struct.unpack_from('<II',raw,pos);pos+=8
  if n%4 or pos+n>len(raw):raise Invalid('GLB_CHUNK_BOUNDS')
  chunks.append((t,raw[pos:pos+n]));pos+=n
 if not chunks or chunks[0][0]!=0x4e4f534a:raise Invalid('GLB_JSON_MISSING')
 try:d=json.loads(chunks[0][1])
 except (ValueError,UnicodeError):raise Invalid('GLB_JSON_INVALID')
 animations=d.get('animations',[])
 if len(animations)!=1 or animations[0].get('name')!=expected:raise Invalid('GLB_ACTION_SET')
 if not animations[0].get('channels') or not animations[0].get('samplers'):raise Invalid('GLB_EMPTY_ANIMATION')
 if not d.get('skins') or len(d['skins'][0].get('joints',[]))!=80:raise Invalid('GLB_RIG_INCOMPATIBLE')
 binary=next((b for t,b in chunks if t==0x004e4942),None)
 if binary is None:raise Invalid('GLB_BINARY_MISSING')
 for v in d.get('bufferViews',[]):
  if v.get('byteOffset',0)<0 or v['byteLength']<0 or v.get('byteOffset',0)+v['byteLength']>len(binary):raise Invalid('GLB_BUFFER_BOUNDS')
 accessors=d.get('accessors',[]);views=d.get('bufferViews',[]);nodes=d.get('nodes',[])
 def read_accessor(index):
  if type(index) is not int or not 0<=index<len(accessors):raise Invalid('GLB_ACCESSOR_INDEX')
  a=accessors[index]
  if a.get('componentType')!=5126 or a.get('type') not in ['SCALAR','VEC3','VEC4'] or a.get('count',0)<1 or 'sparse' in a:raise Invalid('GLB_ANIMATION_ACCESSOR')
  vi=a.get('bufferView')
  if type(vi) is not int or not 0<=vi<len(views):raise Invalid('GLB_ACCESSOR_VIEW')
  v=views[vi];width={'SCALAR':1,'VEC3':3,'VEC4':4}[a['type']];stride=v.get('byteStride',4*width);offset=a.get('byteOffset',0)
  if stride<4*width or offset<0 or offset+(a['count']-1)*stride+4*width>v['byteLength']:raise Invalid('GLB_ACCESSOR_BOUNDS')
  rows=[struct.unpack_from('<'+'f'*width,binary,v.get('byteOffset',0)+offset+i*stride) for i in range(a['count'])]
  if not all(math.isfinite(x) for row in rows for x in row):raise Invalid('GLB_ANIMATION_NONFINITE')
  return rows
 durations=[]
 for sampler in animations[0]['samplers']:
  times=read_accessor(sampler.get('input'));values=read_accessor(sampler.get('output'))
  if any(len(t)!=1 for t in times) or len(times)<2 or any(b[0]<=a[0] for a,b in zip(times,times[1:])):raise Invalid('GLB_TIME_ORDER')
  mult=3 if sampler.get('interpolation')=='CUBICSPLINE' else 1
  if len(values)!=len(times)*mult:raise Invalid('GLB_SAMPLE_COUNT')
  if abs(times[0][0])>.0001 or abs(times[-1][0]-2.4)>.0001:raise Invalid('GLB_DURATION')
  durations.append(times[-1][0])
 for channel in animations[0]['channels']:
  target=channel.get('target',{});sampler=channel.get('sampler')
  if type(sampler) is not int or not 0<=sampler<len(animations[0]['samplers']) or type(target.get('node')) is not int or not 0<=target['node']<len(nodes) or target.get('path') not in ['rotation','translation','scale']:raise Invalid('GLB_CHANNEL_TARGET')
 return {'animation':expected,'bones':80,'bytes':len(raw),'duration':max(durations)}
def compare_positions(a,b,tolerance=.0002):
 if len(a)!=len(b):raise Invalid('ROUNDTRIP_FRAME_COUNT')
 maximum=0
 for x,y in zip(a,b):
  if set(x)!=set(y):raise Invalid('ROUNDTRIP_JOINT_SET')
  for n in x:
   if not all(math.isfinite(v) for v in x[n]+y[n]):raise Invalid('ROUNDTRIP_NONFINITE')
   maximum=max(maximum,math.dist(x[n],y[n]))
 if maximum>tolerance:raise Invalid('ROUNDTRIP_POSITION_LIMIT')
 return maximum
