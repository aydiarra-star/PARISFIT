"""Prepared Blender 4.2 roundtrip adapter. NOT a validated retarget solver.
Run with Blender: blender --background --python tools/animation-pipeline/blender-stage.py
or a working bpy 4.2 Python environment. Never writes runtime assets.
"""
from pathlib import Path
import json,traceback
out=Path('docs/coach/phase7');out.mkdir(parents=True,exist_ok=True)
try:
 import bpy
 bpy.ops.wm.read_factory_settings(use_empty=True)
 bpy.ops.import_scene.gltf(filepath=str(Path(out,'prototype.glb').resolve()))
 bpy.context.scene.render.fps=60
 bpy.context.scene.frame_start=0;bpy.context.scene.frame_end=300
 # Resampling is an export operation, not foot cleanup. No auto IK / smoothing.
 bpy.ops.export_scene.gltf(filepath=str(Path(out,'blender-roundtrip.glb').resolve()),export_format='GLB',export_animations=True,export_frame_range=True,export_force_sampling=True)
 report={'status':'EXPORTED_NOT_VALIDATED','version':bpy.app.version_string,'retargetingExecuted':False,'contactCorrectionExecuted':False,'requiresRoundtripComparison':True}
except Exception:
 report={'status':'BLOCKED_ENVIRONMENT','error':traceback.format_exc(),'retargetingExecuted':False,'contactCorrectionExecuted':False}
(out/'blender-report.json').write_text(json.dumps(report,indent=2)+'\n')
if report['status']=='BLOCKED_ENVIRONMENT':raise SystemExit(2)
