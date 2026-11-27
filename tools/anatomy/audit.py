"""Rig conventions: imported display bone length is NOT anatomical segment length."""
def inventory(obj):
 rows=[]
 for b in obj.data.bones:
  world=obj.matrix_world@b.matrix_local
  rows.append({'name':b.name,'parent':b.parent.name if b.parent else None,'children':[c.name for c in b.children],'headWorldM':list(world.translation),'restMatrixLocal':[list(r) for r in b.matrix_local],'parentRelativeRest':[list(r) for r in (b.parent.matrix_local.inverted()@b.matrix_local if b.parent else b.matrix_local)],'worldAxes':[list(world.to_3x3().col[i].normalized()) for i in range(3)],'displayBoneLengthM':b.length,'parentPivotDistanceM':(world.translation-(obj.matrix_world@b.parent.matrix_local).translation).length if b.parent else None,'childPivotDistancesM':{c.name:((obj.matrix_world@c.matrix_local).translation-world.translation).length for c in b.children}})
 return {'units':'m','up':'Z','objectMatrix':[list(r) for r in obj.matrix_world],'objectScale':list(obj.scale),'bones':rows}
def correspondence(mapping,child,reference,tp,scale):
 rows=[]
 for k,v in mapping.items():
  sl=tl=None
  if k in child:
   a,b=child[k];sl=(reference[b]['p']-reference[v]['p']).length;tl=(tp('Bip01_'+a)-tp('Bip01_'+k)).length
  reason='Correspondence of joint labels only; anatomical axes unqualified'
  status='approximate'
  if sl is not None and sl<1e-6:status='impossible-direction';reason='Coincident source pivots: no anatomical segment direction or ratio may be inferred'
  elif k.endswith(('Thigh','Calf','UpperArm','Forearm')):status='direct-topology';reason='Matching chain topology, not matching anatomical coordinate systems or lengths'
  elif k in ['Neck','Spine','Spine1','Spine2','Pelvis']:reason='Different spine subdivision / branching; no one-to-one anatomical length'
  rows.append({'target':'Bip01_'+k,'source':v,'class':status,'reason':reason,'sourceSegmentM':sl,'targetSegmentM':tl,'normalizedSourceM':sl*scale if sl is not None else None,'ratio':tl/sl if sl is not None and sl>1e-6 else None})
 return rows
