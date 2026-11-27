"""Blender-specific sampler, intentionally separate from independent validation."""
def sample_geometry(bpy,target,bones):
 from mathutils import Vector
 import numpy as np
 meshes=[o for o in bpy.context.scene.objects if o.type=='MESH'];parts={s:[] for s in ['L_Foot','R_Foot','L_Hand','R_Hand']};markers={}
 for mi,m in enumerate(meshes):
  for v in m.data.vertices:
   if not v.groups:continue
   g=max(v.groups,key=lambda g:g.weight);name=m.vertex_groups[g.group].name
   for side in ['L','R']:
    if name.startswith('Bip01_'+side+'_Foot') or name.startswith('Bip01_'+side+'_Toe'):parts[side+'_Foot'].append((mi,v.index))
    if name.startswith('Bip01_'+side+'_Hand') or name.startswith('Bip01_'+side+'_Finger'):parts[side+'_Hand'].append((mi,v.index))
 if not all(parts.values()):raise ValueError('SUPPORT_VERTEX_GROUP_MISSING')
 def xyz(v):return [v[0],v[2],-v[1]]
 frames=[]
 for i in range(145):
  bpy.context.scene.frame_set(i);bpy.context.view_layer.update();deps=bpy.context.evaluated_depsgraph_get();coords=[]
  for m in meshes:
   ev=m.evaluated_get(deps);mesh=ev.to_mesh();arr=np.empty(len(mesh.vertices)*3,dtype=np.float64);mesh.vertices.foreach_get('co',arr);arr=arr.reshape(-1,3);matrix=np.array(ev.matrix_world);world=arr@matrix[:3,:3].T+matrix[:3,3];coords.append(world);ev.to_mesh_clear()
  supports={}
  for name,indices in parts.items():
   if i==0:
    chosen=[]
    for marker in sorted(indices,key=lambda ind:coords[ind[0]][ind[1]][2]):
     point=coords[marker[0]][marker[1]]
     if all(np.linalg.norm(point-coords[a][b])>.025 for a,b in chosen):chosen.append(marker)
     if len(chosen)==3:break
    if len(chosen)!=3:raise ValueError('INSUFFICIENT_SUPPORT_PATCH')
    markers[name]=chosen
   supports[name]={'minY':min(float(coords[a][b][2]) for a,b in indices),'points':[xyz(coords[a][b].tolist()) for a,b in markers[name]]}
  joints={}
  for b in bones:
   world=target.matrix_world@b.matrix;q=world.to_quaternion();joints[b.name]={'position':xyz(world.translation),'rotation':[q.x,q.z,-q.y,q.w]}
  frames.append({'time':i/60,'joints':joints,'supports':supports,'surfaceMinY':min(float(c[:,2].min()) for c in coords)})
 return {'schemaVersion':1,'sourceType':'CMU14_06 licensed control NOT PARISFIT capture','units':'m','up':'Y','sampleHz':60,'parents':{b.name:b.parent.name if b.parent else None for b in bones},'supportMarkers':markers,'supportMeaning':'three low skin vertices selected once, not anatomically reviewed sole/palm patches','frames':frames}
