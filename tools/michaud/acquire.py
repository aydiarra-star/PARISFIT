"""Only the pinned, public dataset subset; no private participant files."""
from pathlib import Path
import urllib.request,hashlib,zipfile,json,xml.etree.ElementTree as ET
ROOT=Path('.cache/phase13');ROOT.mkdir(parents=True,exist_ok=True)
URL='https://zenodo.org/records/23979972/files/Fatigue_Squat_2026_dataset.zip?download=1'
ARCHIVE='901112330ed234ad97ce24cb866bd5e7e33bef766861d21264953b3ac1875782'
EXPECTED={'P001_markers.csv.gz':'b3099afbb56ecf024807129969fb202b441968d14959b0e9598189c1c2aa339e','P001_force_plates.csv.gz':'a08c957955a49c5e578c2ac9b047a392ce12b6f0e97e95eb4997947898179d40','static_markers.csv.gz':'09511dabccd98c94ffe714bb926f052ae4ecd8f6c071fb3fbe33021823d0f784','squat_repetitions.csv':'11e8c7fbcc55622850ce89154510d049a53e894060c286dd7db152891b734b2a','README.md':'cb65ee390ccde63cf876c6d27ce5583ea42bb0a8ed5b832dc921dc99acf0813f'}
def acquire():
 z=ROOT/'archive.zip'
 try:
  with urllib.request.urlopen(urllib.request.Request(URL,headers={'User-Agent':'PARISFIT-source-audit/1.0'}),timeout=90) as r,z.open('wb') as f:
   total=0
   while True:
    b=r.read(1024*1024)
    if not b:break
    total+=len(b)
    if total>150000000:raise ValueError('SIZE_LIMIT')
    f.write(b)
  assert hashlib.sha256(z.read_bytes()).hexdigest()==ARCHIVE,'ARCHIVE_HASH'
  files={};model=None
  with zipfile.ZipFile(z) as archive:
   for name in archive.namelist():
    base=Path(name).name
    if (base=='README.md' or '/S01/' in name) and base in EXPECTED:
     raw=archive.read(name);assert hashlib.sha256(raw).hexdigest()==EXPECTED[base],base;(ROOT/base).write_bytes(raw);files[base]={'sha256':EXPECTED[base],'archivePath':name,'bytes':len(raw)}
    if name.endswith('/model/LaiUhlrich2022_symmetric.osim'):
     raw=archive.read(name);x=ET.fromstring(raw)
     private=Path('.cache/phase13-model');private.mkdir(parents=True,exist_ok=True);(private/'template.osim').write_bytes(raw)
     model={'status':'NON TESTÉ','scope':'XML metadata inspection only; no OpenSim solver, scaling or inverse kinematics executed; model not redistributed','archivePath':name,'sha256':hashlib.sha256(raw).hexdigest(),'credits':x.findtext('.//credits'),'publications':x.findtext('.//publications'),'bodies':[b.attrib['name'] for b in x.findall('.//BodySet/objects/Body')],'joints':[{'name':b.attrib.get('name'),'type':b.tag,'coordinates':[c.attrib.get('name') for c in b.findall('.//Coordinate')]} for b in x.findall('.//JointSet/objects/*')],'markers':[{'name':m.attrib.get('name'),'frame':m.findtext('socket_parent_frame'),'location':m.findtext('location')} for m in x.findall('.//MarkerSet/objects/Marker')]}
  assert set(files)==set(EXPECTED),'MISSING_PINNED_SUBSET'
  assert model is not None,'MODEL_METADATA_MISSING'
  (ROOT/'provenance.json').write_text(json.dumps({'status':'VALIDÉ','scope':'integrity/public subset only','url':URL,'version':'v1 / record23979972','archiveSHA256':ARCHIVE,'files':files,'personalFilesExtracted':False,'licenseBasis':'dataset README + Zenodo record CC BY4.0, not article license alone'},indent=2)+'\n')
  (ROOT/'model-inspection.json').write_text(json.dumps(model,indent=2)+'\n')
  (ROOT/'NOTICE.txt').write_text('Florian Michaud (2026), Motion capture, ground reaction forces and knee extension strength during repeated dumbbell squats to fatigue: dataset and symmetric OpenSim model, v1, https://zenodo.org/records/23979972 . Associated article: Michaud, Katwal, Porzio and Cuadrado, Toward Real-Time Estimation of Muscle Force and Fatigue During Resistance Training Using a Neural Network Surrogate of OpenSim Musculotendon Kinematics. CC BY4.0 https://creativecommons.org/licenses/by/4.0/ . PARISFIT phase13: public S01/P001 subset and static calibration; diagnostic reconstructions/metrics/renders are modifications, no endorsement. No private signatures or participant demographics extracted. Original model inspected as XML and optionally loaded in a separate OpenSim probe; not redistributed, no subject scaling or IK.\n')
 finally:
  if z.exists():z.unlink()
if __name__=='__main__':acquire()
