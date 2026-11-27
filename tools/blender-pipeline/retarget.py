"""CMU control BVH → calibrated FK Rocketbox → baked GLB, offline only.
No source data cleanup, IK, smoothing, or production admission.
"""
import argparse,json,hashlib,platform,traceback,time,sys,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--out',default='.cache/phase9');a=p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else ([] if 'blender' in Path(sys.argv[0]).name else None));out=Path(a.out).resolve();repo=Path(__file__).resolve().parents[2]
if out!=repo/'.cache/phase9':raise SystemExit('Only isolated .cache/phase9 output is allowed')
out.mkdir(parents=True,exist_ok=True)
source=repo/'docs/coach/phase6/source-14_06.bvh';model=repo/'assets/coach/coach.glb'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'status':'STARTING','dataKind':'CMU licensed optical control, NOT dedicated PARISFIT capture','sourceSHA256':sha(source),'modelSHA256':sha(model),'runtimeEnabled':False,'professionalApproval':False,'platform':platform.platform(),'python':platform.python_version(),'steps':[],'corrections':{'IK':False,'smoothing':False,'manual':[]}}
started=time.time()
def step(n,**kw):r['steps'].append({'step':n,'seconds':round(time.time()-started,3),**kw});print('STEP',n,json.dumps(kw),flush=True)
try:
 assert r['sourceSHA256']=='e75bcdec4d6fdeac91571020d0b75d45cd4b2532113e699f465b5b297373ac05'
 assert r['modelSHA256']=='1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb'
 # Ubuntu's Blender embeds Python but may omit Debian's dist-packages path.
 if Path('/usr/lib/python3/dist-packages').is_dir():sys.path.append('/usr/lib/python3/dist-packages')
 import bpy
 import numpy
 r['numpyVersion']=numpy.__version__
 from mathutils import Vector,Quaternion
 r['blenderVersion']=bpy.app.version_string;step('startup',version=bpy.app.version_string)
 bpy.ops.wm.read_factory_settings(use_empty=True)
 bpy.ops.import_scene.gltf(filepath=str(model))
 targets=[o for o in bpy.context.scene.objects if o.type=='ARMATURE'];assert len(targets)==1,[(o.name,o.type) for o in targets]
 target=targets[0];step('rocketbox-import',armature=target.name,bones=len(target.data.bones))
 for o in list(bpy.context.scene.objects):o.animation_data_clear()
 for action in list(bpy.data.actions):bpy.data.actions.remove(action)
 for pb in target.pose.bones:pb.matrix_basis.identity();pb.rotation_mode='QUATERNION'
 bpy.context.view_layer.update()
 rest={b.name:b.matrix_local.copy() for b in target.data.bones}
 bpy.ops.preferences.addon_enable(module='io_anim_bvh')
 bpy.ops.import_anim.bvh(filepath=str(source),global_scale=.056444,axis_forward='-Z',axis_up='Y',use_fps_scale=False,update_scene_fps=True,update_scene_duration=True)
 src=bpy.context.object;fps=1/float(source.read_text().split('Frame Time:')[1].splitlines()[0].strip());step('bvh-import',bones=len(src.data.bones),nativeHz=fps)
 def frame(t):
  n=1+t*fps;bpy.context.scene.frame_set(int(n),subframe=n-int(n));bpy.context.view_layer.update()
 def sp(n):return (src.matrix_world@src.pose.bones[n].matrix).translation.copy()
 def sq(n):return (src.matrix_world@src.pose.bones[n].matrix).to_quaternion()
 def tp(n):return (target.matrix_world@rest[n]).translation.copy()
 frame(0);reference={b.name:{'q':sq(b.name),'p':sp(b.name)} for b in src.pose.bones}
 mapping={'Pelvis':'Hips','Spine':'LowerBack','Spine1':'Spine','Spine2':'Spine1','Neck':'Neck','Head':'Head'}
 child={'Pelvis':('Spine','LowerBack'),'Spine':('Spine1','Spine'),'Spine1':('Spine2','Spine1'),'Spine2':('Neck','Neck'),'Neck':('Head','Head')}
 for side,long in [('L','Left'),('R','Right')]:
  for a,b in [('Thigh','UpLeg'),('Calf','Leg'),('Foot','Foot'),('Toe0','ToeBase'),('Clavicle','Shoulder'),('UpperArm','Arm'),('Forearm','ForeArm'),('Hand','Hand')]:mapping[side+'_'+a]=long+b
  for a,b,sa,sb in [('Thigh','Calf','UpLeg','Leg'),('Calf','Foot','Leg','Foot'),('Foot','Toe0','Foot','ToeBase'),('Clavicle','UpperArm','Shoulder','Arm'),('UpperArm','Forearm','Arm','ForeArm'),('Forearm','Hand','ForeArm','Hand')]:child[side+'_'+a]=(side+'_'+b,long+sb)
 for k,v in mapping.items():assert 'Bip01_'+k in rest and v in reference,(k,v)
 offset={}
 for k,v in mapping.items():
  offset[k]=Quaternion()
  if k in child:
   a,b=child[k];u=tp('Bip01_'+a)-tp('Bip01_'+k);w=reference[b]['p']-reference[v]['p'];offset[k]=u.normalized().rotation_difference(w.normalized())
 scale=((tp('Bip01_L_Thigh')-tp('Bip01_L_Calf')).length+(tp('Bip01_L_Calf')-tp('Bip01_L_Foot')).length)/((reference['LeftUpLeg']['p']-reference['LeftLeg']['p']).length+(reference['LeftLeg']['p']-reference['LeftFoot']['p']).length)
 start=8.6;duration=2.4;frame(start);origin=sp('Hips');lateral=sp('LeftUpLeg')-sp('RightUpLeg');lateral.z=0
 # Blender world is Z up. Align the source lateral axis to target left/right axis.
 targetLateral=tp('Bip01_L_Thigh')-tp('Bip01_R_Thigh');targetLateral.z=0;heading=lateral.normalized().rotation_difference(targetLateral.normalized())
 bones=list(target.pose.bones)
 def depth(b):return 0 if b.parent is None else 1+depth(b.parent)
 bones.sort(key=depth);root=target.pose.bones.get('Bip01');assert root and root.parent is None,[(b.name,b.parent.name if b.parent else None) for b in bones[:3]]
 armq=target.matrix_world.to_quaternion();localRest={b.name:(rest[b.parent.name].inverted()@rest[b.name] if b.parent else rest[b.name]).to_quaternion() for b in bones}
 previous={};records=[]
 for i in range(145):
  frame(start+i/60);world={}
  for b in bones:
   key=b.name.removeprefix('Bip01_');parentq=world[b.parent.name] if b.parent else Quaternion()
   b.location=(0,0,0);b.scale=(1,1,1)
   if key in mapping:
    name=mapping[key];desired=heading@sq(name)@reference[name]['q'].inverted()@offset[key]@(target.matrix_world@rest[b.name]).to_quaternion()
    poseq=armq.inverted()@desired;basis=localRest[b.name].inverted()@parentq.inverted()@poseq
   else:basis=Quaternion();poseq=parentq@localRest[b.name]
   basis.normalize()
   if b.name in previous and previous[b.name].dot(basis)<0:basis.negate()
   previous[b.name]=basis.copy();b.rotation_quaternion=basis;world[b.name]=poseq
  displacement=heading@(sp('Hips')-origin)*scale
  root.location=rest[root.name].to_3x3().inverted()@(target.matrix_world.to_3x3().inverted()@displacement)
  bpy.context.view_layer.update()
  for b in bones:
   b.keyframe_insert(data_path='rotation_quaternion',frame=i,group=b.name)
   if b==root:b.keyframe_insert(data_path='location',frame=i,group=b.name)
  records.append({'time':i/60,'sourceTime':start+i/60})
 step('calibration-and-retarget',mappedBones=len(mapping),scale=scale,frames=len(records))
 bpy.data.objects.remove(src,do_unlink=True)
 target.animation_data.action.name='phase9-cmu-control'
 for fc in target.animation_data.action.fcurves:
  for k in fc.keyframe_points:k.interpolation='LINEAR'
 bpy.context.scene.render.fps=60;bpy.context.scene.render.fps_base=1;bpy.context.scene.frame_start=0;bpy.context.scene.frame_end=144;bpy.context.scene.frame_set(0)
 target['source']='CMU14_06 8.6-11s, licensed control only';target['admission']='BLOCKED';target['runtimeEnabled']=False
 bpy.ops.export_scene.gltf(filepath=str(out/'rocketbox-control.glb'),export_format='GLB',export_animations=True,export_frame_range=True,export_force_sampling=True,export_nla_strips=False,export_extras=True)
 step('glb-export',bytes=(out/'rocketbox-control.glb').stat().st_size)
 r.update(status='EXPORTED_PENDING_THREEJS',duration=duration,samples=len(records),mapping=mapping,scale=scale,outputSHA256=sha(out/'rocketbox-control.glb'),groundCorrection='none; floor/contact must be measured, not silently projected')
 assert sha(model)==r['modelSHA256'];assert sha(source)==r['sourceSHA256']
except Exception:
 r.update(status='FAILED',error=traceback.format_exc());print(r['error'],flush=True)
finally:
 r['elapsedSeconds']=round(time.time()-started,3);(out/'blender-report.json').write_text(json.dumps(r,indent=2)+'\n');print('BLENDER_REPORT_JSON='+json.dumps(r),flush=True)
if r['status']=='FAILED':raise SystemExit(1)
