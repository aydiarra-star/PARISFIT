"""Re-fetch pinned alternate template/MarkerSets, compare metadata only."""
import json,base64,hashlib,subprocess,xml.etree.ElementTree as E
from pathlib import Path
D=Path('docs/coach/phase14');ref='e5d29f12e725a2e14e6e4e85617834685f738753'
expected={'LaiUhlrich2022.osim':'7499645500d4bca9269f27fd669bd3ed3abbeccd549d87f86cd01119a1a24366','LaiUhlrich2022_markers_mocap.xml':'16a0aa5028b19c0576bc2058b8f425fffc810150b714aa4b7aa75c4163a20c90','LaiUhlrich2022_markers_mocap_shoulder.xml':'e8796ed02bcad145038b27178e174603cbcdef5bcc6b02daa02ae556f236087d','LICENSE':'c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4'}
d=json.loads(Path('docs/coach/phase13/model-inspection.json').read_text());target={m['name']:(m['frame'],[float(v) for v in m['location'].split()]) for m in d['markers']};out={'status':'VALIDÉ','scope':'upstream marker metadata comparison, not proof of Michaud direct ancestry or CSV registration','repo':'opencap-org/opencap-core','commit':ref,'files':[]}
for name,h in expected.items():
 path=name if name=='LICENSE' else 'opensimPipeline/Models/'+name
 r=json.loads(subprocess.check_output(['gh','api',f'repos/opencap-org/opencap-core/contents/{path}?ref={ref}']));b=base64.b64decode(r['content']);assert hashlib.sha256(b).hexdigest()==h;row={'path':path,'sha256':h,'bytes':len(b)}
 if name!='LICENSE':
  x=E.fromstring(b);mm={m.attrib['name']:(m.findtext('socket_parent_frame'),[float(v) for v in m.findtext('location').split()]) for m in x.findall('.//Marker')};row.update(markerCount=len(mm),sharedNames=sorted(set(mm)&set(target)),identicalDefinitions=sorted(k for k in set(mm)&set(target) if mm[k]==target[k]),datasetOnlyNames=sorted(set(target)-set(mm)),upstreamOnlyNames=sorted(set(mm)-set(target)))
 else:row['license']='Apache-2.0; LICENSE hash identical to upstream D5'
 out['files'].append(row)
(D/'opencap-comparison.json').write_text(json.dumps(out,indent=2)+'\n')
