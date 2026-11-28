"""Read-only pinned metadata inspection. No IK or processing scripts executed."""
import json,subprocess,base64,hashlib,xml.etree.ElementTree as E
from pathlib import Path
D=Path('docs/coach/phase16');REF='a26fe4852a78f30c5e8a437b158847031cb8dc3c';REPO='WeRoLab/healthy-whole-body-noncyclic-dataset'
def api(p):return json.loads(subprocess.check_output(['gh','api','repos/'+REPO+'/'+p]))
def main():
 tree=api('git/trees/'+REF+'?recursive=1');assert not tree['truncated'];items={x['path']:x for x in tree['tree']};paths=['AB01/Squat/1/Setup/Setup_IK.xml','AB01/Static/1/Setup/Setup_Scale_GUI.xml','AB01/Squat/1/Setup/Setup_External_Forces.xml','AB01/Squat/1/Processing/process_force_data.m','Model/marker_set.xml'];rows=[]
 for p in paths:
  x=items[p];assert x['size']<100000
  raw=base64.b64decode(api('git/blobs/'+x['sha'])['content']);assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==x['sha']
  row={'path':p,'gitBlob':x['sha'],'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
  if p.endswith('.xml'):
   root=E.fromstring(raw);row['fileReferences']={tag:[n.text for n in root.findall('.//'+tag)] for tag in ['model_file','marker_file','time_range','datafile']};row['markerNames']=[n.attrib['name'] for n in root.findall('.//Marker')];row['IKMarkerTaskNames']=[n.attrib['name'] for n in root.findall('.//IKMarkerTask')]
  rows.append(row)
 counts={}
 for p in items:
  if '/Squat/' in p and p.endswith('.c3d'):counts[p.split('/')[0]]=counts.get(p.split('/')[0],0)+1
 report={'status':'VALIDÉ','scope':'pinned repository metadata only; no C3D downloaded, IK or author script executed','repo':REPO,'commit':REF,'files':rows,'squatC3DCountsInTree':counts,'exampleMotion':{k:items['AB01/Squat/1/Data/squat_1.c3d'][k] for k in ['path','sha','size']},'exampleStatic':{k:items['AB01/Static/1/Data/static.c3d'][k] for k in ['path','sha','size']},'qualification':'EN ATTENTE DE VALIDATION HUMAINE','IKExecuted':False,'retargetExecuted':False}
 (D/'candidate-inspection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
