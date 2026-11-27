"""Independent BVH parser/FK, NumPy only. Honors declared channel order."""
import re,numpy as np
class Invalid(ValueError):pass
def parse(text):
 try:header,motion=text.split('MOTION',1)
 except ValueError:raise Invalid('MISSING_MOTION')
 tokens=re.findall(r'\{|\}|[^\s{}]+',header);index=0;nodes=[];count=0
 def take():
  nonlocal index
  if index>=len(tokens):raise Invalid('TRUNCATED_HIERARCHY')
  t=tokens[index];index+=1;return t
 if take()!='HIERARCHY':raise Invalid('HIERARCHY')
 def node(parent,kind=None):
  nonlocal count
  kind=kind or take()
  if kind not in ['ROOT','JOINT','End']:raise Invalid('NODE')
  name=take()
  if kind=='End':name=nodes[parent]['name']+'__End'
  if take()!='{':raise Invalid('OPEN_BRACE')
  idx=len(nodes);n={'name':name,'parent':parent,'offset':None,'channels':[]};nodes.append(n)
  while True:
   t=take()
   if t=='}':break
   if t=='OFFSET':n['offset']=[float(take()) for _ in range(3)]
   elif t=='CHANNELS':
    num=int(take());n['channels']=[(take(),count+j) for j in range(num)];count+=num
   elif t in ['JOINT','End']:node(idx,t)
   else:raise Invalid('UNKNOWN_TOKEN:'+t)
  if n['offset'] is None:raise Invalid('OFFSET')
 node(None)
 if index!=len(tokens):raise Invalid('TRAILING_HIERARCHY')
 lines=motion.strip().splitlines();frames=int(lines[0].split(':')[1]);dt=float(lines[1].split(':')[1]);data=np.array([[float(v) for v in line.split()] for line in lines[2:] if line.strip()])
 if data.shape!=(frames,count) or not np.isfinite(data).all() or dt<=0:raise Invalid('MOTION_SHAPE_OR_VALUES')
 return nodes,data,dt
def fk(nodes,data):
 n=len(data);R=np.zeros((n,len(nodes),3,3));P=np.zeros((n,len(nodes),3));eye=np.broadcast_to(np.eye(3),(n,3,3))
 for j,b in enumerate(nodes):
  rot=eye.copy();pos=np.broadcast_to(b['offset'],(n,3)).copy()
  for channel,k in b['channels']:
   axis='XYZ'.index(channel[0])
   if channel.endswith('position'):pos[:,axis]+=data[:,k]
   elif channel.endswith('rotation'):
    angle=np.deg2rad(data[:,k]);c=np.cos(angle);s=np.sin(angle);r=eye.copy();a=(axis+1)%3;z=(axis+2)%3;r[:,a,a]=c;r[:,z,z]=c;r[:,a,z]=-s;r[:,z,a]=s;rot=rot@r
   else:raise Invalid('CHANNEL')
  parent=b['parent']
  if parent is None:R[:,j]=rot;P[:,j]=pos
  else:R[:,j]=R[:,parent]@rot;P[:,j]=P[:,parent]+np.einsum('nij,nj->ni',R[:,parent],pos)
 return P
