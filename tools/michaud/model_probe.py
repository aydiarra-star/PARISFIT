"""Headless load and semantic compatibility gate, NOT inverse kinematics."""
from pathlib import Path
import json,hashlib,traceback,sys
ROOT=Path('.cache/phase13');result={'status':'NON TESTÉ','subjectReconstruction':'NON TESTÉ','retarget':'NON TESTÉ','forcesUsedForGeometry':False,'scope':'model library loading and schema check only; no scaling or IK','wheelSHA256':'6bb4983097323e60326f6f102ee9f385e470deba6cb3a666219bf27aacbefb6d'}
try:
 import opensim as osim
 path=Path('.cache/phase13-model/template.osim');assert hashlib.sha256(path.read_bytes()).hexdigest()=='42eca458626f42aa1e49d5925e14ec3c16fe81324293bacece643e11319ddbd9'
 model=osim.Model(str(path));state=model.initSystem();markers=model.getMarkerSet();names=[markers.get(i).getName() for i in range(markers.getSize())];data=json.loads((ROOT/'review-data.json').read_text());source=data['names'];g=model.getGravity()
 result.update(status='VALIDÉ',engine=osim.GetVersionAndDate(),python=sys.version,modelSHA256=hashlib.sha256(path.read_bytes()).hexdigest(),modelName=model.getName(),gravity=[g.get(i) for i in range(3)],bodies=model.getBodySet().getSize(),coordinates=model.getCoordinateSet().getSize(),constraints=model.getConstraintSet().getSize(),modelMarkers=len(names),dataMarkers=len(source),exactNameMatches=sorted(set(source)&set(names)),registrationGate='REFUSÉ: no validated37-marker attachment/alias map or individualized model; do not silently match virtual joint-centre markers to skin markers',modelMarkerNames=names)
except Exception:result['error']=traceback.format_exc()
(ROOT/'model-probe.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
if 'error' in result:raise SystemExit(1)
