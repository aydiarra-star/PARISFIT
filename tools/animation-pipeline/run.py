"""Isolated deterministic control pipeline; requires a local HTTP server and Chromium.
No downloads, purchases, runtime writes or automatic admission. Blender is separate.
"""
import subprocess,json,hashlib,sys
from pathlib import Path
c=json.loads(Path('tools/animation-pipeline/pushup.json').read_text());source=Path(c['source']);before=hashlib.sha256(source.read_bytes()).hexdigest()
assert before==c['sourceSHA256'],'Source changed; re-review provenance'
assert c['start']==0 and c['end']==5 and c['sampleHz']==60,'This fixture is qualified only for the documented full 5s control'
assert c['output']=='docs/coach/phase7','Refuse runtime or historical output'
for cmd in [['node','tools/animation-pipeline/export.cjs'],[sys.executable,'tools/optimize-coach.py',c['output']+'/prototype.glb'],['node','tools/animation-pipeline/measure.cjs'],[sys.executable,'tools/animation-pipeline/gate.py']]:subprocess.run(cmd,check=True)
assert hashlib.sha256(source.read_bytes()).hexdigest()==before
print('Control pipeline executed. Admission BLOCKED; no production-ready animation asserted.')
