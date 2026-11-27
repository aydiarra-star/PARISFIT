"""Unqualified BVH→different-proportion test rig→GLB smoke.
Uses preserved CMU fixture, NOT a dedicated capture or Rocketbox premium result.
Run in prepared container with repository read-only and writable /out mount.
"""
import argparse,json,traceback
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--source',default='docs/coach/phase6/source-14_06.bvh');p.add_argument('--out',required=True);a=p.parse_args();out=Path(a.out).resolve()
repo=Path(__file__).resolve().parents[2]
if out==repo or repo in out.parents:raise SystemExit('Use an output directory outside the repository')
out.mkdir(parents=True,exist_ok=True)
r={'status':'NOT_RUN','fixture':'CMU14_06 existing capture, not dedicated PARISFIT','retarget':'uniformly 1.03-scaled test rig, not Rocketbox','runtimeEnabled':False,'professionalApproval':False}
try:
 import bpy
 from mathutils import Matrix
 bpy.ops.wm.read_factory_settings(use_empty=True)
 bpy.ops.preferences.addon_enable(module='io_anim_bvh')
 bpy.ops.import_anim.bvh(filepath=str(Path(a.source).resolve()),global_scale=.056444,axis_forward='-Z',axis_up='Y',use_fps_scale=False,update_scene_fps=True,update_scene_duration=True)
 source=bpy.context.object;target=source.copy();target.data=source.data.copy();bpy.context.collection.objects.link(target);target.animation_data_clear();target.name='RETARGET_SMOKE_NOT_COACH'
 bpy.context.view_layer.objects.active=target;source.select_set(False);target.select_set(True)
 bpy.ops.object.mode_set(mode='EDIT')
 for bone in target.data.edit_bones:bone.head*=1.03;bone.tail*=1.03
 bpy.ops.object.mode_set(mode='OBJECT')
 # Preserve rest-axis delta, retain changed target lengths. This is a smoke, not contact IK.
 start=round(8.6*bpy.context.scene.render.fps)+1;end=round(11*bpy.context.scene.render.fps)+1
 for frame in range(start,end+1):
  bpy.context.scene.frame_set(frame)
  for bone in target.pose.bones:
   src=source.pose.bones[bone.name];bone.rotation_mode='QUATERNION'
   bone.rotation_quaternion=src.rotation_quaternion.copy() if src.rotation_mode=='QUATERNION' else src.matrix_basis.to_quaternion()
   bone.location=src.location*1.03;bone.scale=(1,1,1)
   bone.keyframe_insert('rotation_quaternion',frame=frame-start);bone.keyframe_insert('location',frame=frame-start)
 bpy.data.objects.remove(source,do_unlink=True)
 bpy.context.scene.frame_start=0;bpy.context.scene.frame_end=end-start
 bpy.ops.export_scene.gltf(filepath=str(out/'smoke.glb'),export_format='GLB',export_animations=True,export_frame_range=True,export_force_sampling=True)
 r.update(status='EXPORTED_REQUIRES_THREEJS_CHECK',blenderVersion=bpy.app.version_string,frames=end-start+1,fps=bpy.context.scene.render.fps,bones=len(target.data.bones))
except Exception:r.update(status='FAILED',error=traceback.format_exc())
(out/'smoke-report.json').write_text(json.dumps(r,indent=2)+'\n')
if r['status']=='FAILED':raise SystemExit(2)
