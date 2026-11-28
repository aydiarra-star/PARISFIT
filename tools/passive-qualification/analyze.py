"""Passive C3D/XML inspection only. No OpenSim import, solver, filtering or trajectory editing."""
from pathlib import Path
import json,csv,hashlib,xml.etree.ElementTree as E,collections,warnings
import c3d,numpy as np
from metrics import project_to_plate,frame_inventory
ROOT=Path('.cache/phase17/source');OUT=Path('docs/coach/phase17')
def write(n,x): (OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False,default=lambda v:v.item() if isinstance(v,np.generic) else str(v))+'\n')
def summary(v):return {'min':float(np.min(v)),'max':float(np.max(v)),'mean':float(np.mean(v))}
def inspect_c3d(path):
 with open(ROOT/path,'rb') as f,warnings.catch_warnings(record=True) as ww:
  warnings.simplefilter('always');r=c3d.Reader(f);labels=[s.strip() for s in r.point_labels];al=[s.strip() for s in r.analog_labels];frames=[];points=[];analogs=[]
  for i,p,a in r.read_frames(check_nan=False):frames.append(i);points.append(p.copy());analogs.append(a.copy())
  p=np.stack(points);a=np.concatenate(analogs,axis=1);valid=(p[:,:,3]>=0)&np.isfinite(p[:,:,:3]).all(axis=2)
  out={'headerFirstFrame':int(r.first_frame),'headerLastFrame':int(r.last_frame),'pointParameterFrames':int(r.get('POINT:FRAMES').uint16_value),'dataStartBlock':int(r._header.data_block),'bytesPerFrame':int((4*r.point_used+r.analog_used*r.analog_per_frame)*4),'fileBytes':(ROOT/path).stat().st_size,'path':path,'reader':'python-c3d '+c3d.__version__,'warnings':sorted(set(str(w.message) for w in ww)),'pointRateHz':r.point_rate,'analogRateHz':r.analog_rate,'firstFrame':int(frames[0]),'lastFrame':int(frames[-1]),'pointFrames':len(frames),'analogSamples':a.shape[1],'frameSequenceContiguous':bool(np.all(np.diff(frames)==1)),'markerLabels':labels,'markerUnits':r.get('POINT:UNITS').string_value.strip(),'analogLabels':al,'analogUnits':[s.strip() for s in r.get('ANALOG:UNITS').string_array],'relativePointSeconds':[0,(len(frames)-1)/r.point_rate],'relativeAnalogSeconds':[0,(a.shape[1]-1)/r.analog_rate],'relativeClockOnly':True,'markerMissingCounts':dict(zip(labels,((~valid).sum(axis=0)).tolist())),'analogNonfinite':int((~np.isfinite(a)).sum()),'pointResidualRange':summary(p[:,:,3]),'forcePlatformType':r.get('FORCE_PLATFORM:TYPE').int16_array.tolist(),'forcePlatformOrigin':r.get('FORCE_PLATFORM:ORIGIN').float_array.tolist(),'forcePlatformCorners':r.get('FORCE_PLATFORM:CORNERS').float_array.tolist(),'forcePlatformChannels':r.get('FORCE_PLATFORM:CHANNEL').int16_array.tolist(),'analogGeneralScale':float(r.get('ANALOG:GEN_SCALE').float_value),'analogScale':r.get('ANALOG:SCALE').float_array.tolist(),'analogOffset':r.get('ANALOG:OFFSET').int16_array.tolist()}
  out['byteInventory']=frame_inventory(out['fileBytes'],out['dataStartBlock'],out['bytesPerFrame'],out['pointParameterFrames'],out['headerFirstFrame'],out['headerLastFrame'])
  assert r.point_scale<0 and r._dtypes.float32==np.dtype('<f4')
  raw=np.frombuffer((ROOT/path).read_bytes(),dtype='<f4',offset=(out['dataStartBlock']-1)*512,count=len(frames)*out['bytesPerFrame']//4).reshape(len(frames),-1)
  raw_points=raw[:,:r.point_used*4].reshape(len(frames),r.point_used,4)
  raw_analog=raw[:,r.point_used*4:].reshape(len(frames)*r.analog_per_frame,r.analog_used).T
  scale,offset=r.get_analog_transform();decoded=(raw_analog-offset[:,:1])*scale[:,:1]
  out['independentFloatBlockCheck']={'pointXYZExact':bool(np.array_equal(raw_points[:,:,:3],p[:,:,:3])),'analogExact':bool(np.array_equal(decoded,a)),'scope':'independent float block extraction, metadata still read by python-c3d; not a second general C3D reader'}
  if 'Squat' in path:
   out['forcePlateLocalChannels']=[{'plate':k,'Fz':summary(a[al.index('Fz'+str(k))]),'absoluteFzAbove20N':int(np.count_nonzero(np.abs(a[al.index('Fz'+str(k))])>20)),'samples':a.shape[1]} for k in range(1,7)]
   out['footMarkerProjectionChecks']=[]
   for side,k in [('R',0),('L',1)]:
    co=np.array(out['forcePlatformCorners'][k])
    for name in [side+s for s in ['FCC','FM1','FM5','DP1']]:
     xyz=p[:,labels.index(name),:3];uv,dist=project_to_plate(xyz,co)
     out['footMarkerProjectionChecks'].append({'marker':name,'plate':k+1,'u':summary(uv[:,0]),'v':summary(uv[:,1]),'insideRectangleFrames':int(np.sum((uv>=0).all(axis=1)&(uv<=1).all(axis=1))),'planeDistanceM':summary(dist),'scope':'marker projection only, not sole contact; original C3D coordinates'})
   # Decimated original samples, solely a diagnostic plot input, not exported motion.
   out['diagnosticSeries']=[{'t':i/r.point_rate,'RIAS_original_z_m':float(p[i,labels.index('RIAS'),2]),'Fz1_local_N':float(a[al.index('Fz1'),i*5]),'Fz2_local_N':float(a[al.index('Fz2'),i*5])} for i in range(0,len(frames),10)]
  return out

def line(path,text):return next(i for i,l in enumerate((ROOT/path).read_text().splitlines(),1) if text in l)
def xml_audit(path):
 root=E.parse(ROOT/path);out={'path':path}
 def tasks(tag):return [{'name':n.attrib['name'],'line':line(path,'<'+tag+' name="'+n.attrib['name']+'"'),'apply':n.findtext('apply'),'weight':n.findtext('weight'),'value':n.findtext('value')} for n in root.findall('.//'+tag)]
 out['markerTasks']=tasks('IKMarkerTask');out['coordinateTasks']=tasks('IKCoordinateTask')
 counts=collections.Counter();leaves=[];lines=(ROOT/path).read_text().splitlines()
 for n in root.iter():
  if len(n)==0 and n.tag in ['mass','height','age','model_file','marker_set_file','scaling_order','marker_file','time_range','preserve_mass_distribution','constraint_weight','accuracy','max_marker_movement']:
   positions=[i for i,l in enumerate(lines,1) if '<'+n.tag+'>' in l];ix=counts[n.tag];counts[n.tag]+=1
   leaves.append({'tag':n.tag,'value':n.text.strip() if n.text else '', 'line':positions[ix] if ix<len(positions) else None})
 out['scalarLeaves']=leaves
 out['measurements']=[{'name':m.attrib['name'],'line':line(path,'<Measurement name="'+m.attrib['name']+'"'),'apply':m.findtext('apply'),'pairs':[n.text.strip().split() for n in m.findall('.//markers')],'bodyAxes':[{'body':n.attrib['name'],'axes':n.findtext('axes').strip()} for n in m.findall('.//BodyScale')]} for m in root.findall('.//Measurement')]
 return out

def main():
 manifest=json.loads((OUT/'source-manifest.json').read_text())
 for x in manifest['files']:assert hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256']
 dynamic=inspect_c3d('AB01/Squat/1/Data/squat_1.c3d');static=inspect_c3d('AB01/Static/1/Data/static.c3d');write('c3d-inspection.json',{'dynamic':dynamic,'static':static})
 configs=[xml_audit(p) for p in ['AB01/Static/1/Setup/Setup_Scale.xml','AB01/Static/1/Setup/Setup_Scale_GUI.xml','AB01/Squat/1/Setup/Setup_IK.xml']]
 model=E.parse(ROOT/'Model/Biomech57.osim');marker=E.parse(ROOT/'Model/marker_set.xml');markers=[]
 for m in marker.findall('.//Marker'):
  n=m.attrib['name'];parent=m.findtext('socket_parent_frame');markers.append({'name':n,'parent':parent,'location':[float(t) for t in m.findtext('location').split()],'fixed':m.findtext('fixed'),'line':line('Model/marker_set.xml','<Marker name="'+n+'"'),'staticPresent':n in static['markerLabels'],'dynamicPresent':n in dynamic['markerLabels']})
 write('configuration-inspection.json',{'configs':configs,'markers':markers,'embeddedMarkerSetMatches':all(E.tostring(m)==E.tostring(marker.find('.//Marker[@name="'+m.attrib['name']+'"]')) for m in model.findall('.//Marker')),'modelCoordinates':[{'name':n.attrib['name'],'locked':n.findtext('locked'),'range':n.findtext('range'),'default':n.findtext('default_value')} for n in model.findall('.//Coordinate')],'constraints':[{'name':n.attrib['name'],'xml':E.tostring(n,encoding='unicode')} for n in model.findall('.//ConstraintSet/objects/*')],'modelBodies':[n.attrib['name'] for n in model.findall('.//BodySet/objects/Body')],'modelJoints':[{'name':n.attrib['name'],'type':n.tag,'xml':E.tostring(n,encoding='unicode')} for n in model.findall('.//JointSet/objects/*')]})
 print('Dynamic',dynamic['pointFrames'],dynamic['analogSamples'],'missing',sum(dynamic['markerMissingCounts'].values()))
 print('Static',static['pointFrames'],static['analogSamples'],'missing',sum(static['markerMissingCounts'].values()))
 print('Removed calibration', sorted(set(static['markerLabels'])-set(dynamic['markerLabels'])))
 print(json.dumps(dynamic['forcePlateLocalChannels'],indent=2));print(json.dumps(dynamic['footMarkerProjectionChecks'],indent=2))
if __name__=='__main__':main()
