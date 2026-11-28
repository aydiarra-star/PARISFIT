"""Record actual subprocess failures; background does not bypass dynamic linking."""
import json,subprocess,sys,importlib.util,platform,shutil
from pathlib import Path
p=Path('docs/coach/phase8');p.mkdir(parents=True,exist_ok=True)
spec=importlib.util.find_spec('bpy');binary=spec.origin if spec else None
ldd=subprocess.run(['ldd',binary],capture_output=True,text=True) if binary else None
probe=subprocess.run([sys.executable,'-c','import bpy; print(bpy.app.version_string)'],capture_output=True,text=True)
r={'python':platform.python_version(),'platform':platform.platform(),'bpyBinary':binary,'missingLibraries':[s.strip().split(' =>')[0] for s in ldd.stdout.splitlines() if 'not found' in s] if ldd else [],'importExitCode':probe.returncode,'stdout':probe.stdout,'stderr':probe.stderr,'executables':{k:shutil.which(k) for k in ['blender','docker','podman']},'status':'IMPORT_OK_NOT_PIPELINE_VALIDATED' if probe.returncode==0 else 'BLOCKED_ENVIRONMENT','retargetExecuted':False,'productionAssetCreated':False}
(p/'environment-report.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
