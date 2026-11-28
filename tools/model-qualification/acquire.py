"""Inspect pinned archive, not all participants; no IK or model redistribution."""
from pathlib import Path
import urllib.request,zipfile,hashlib,json,csv,io,gzip,xml.etree.ElementTree as ET,subprocess,base64
import numpy as np
OUT=Path('.cache/phase14');OUT.mkdir(parents=True,exist_ok=True)
SHA='901112330ed234ad97ce24cb866bd5e7e33bef766861d21264953b3ac1875782'
URL='https://zenodo.org/records/23979972/files/Fatigue_Squat_2026_dataset.zip?download=1'
def digest(b):return hashlib.sha256(b).hexdigest()
def markers(x):return {m.attrib['name']:{'frame':m.findtext('socket_parent_frame'),'location':m.findtext('location')} for m in x.findall('.//MarkerSet/objects/Marker')}
def leaves(e,path=''):
 path+= '/'+e.tag+('[@name='+e.attrib['name']+']' if 'name' in e.attrib and e.tag!='Model' else '')
 if len(e)==0:return {path:(e.text or '').strip()}
 r={}
 for ch in e:r.update(leaves(ch,path))
 return r
def main():
 archive=OUT/'archive.zip'
 try:
  with urllib.request.urlopen(URL,timeout=90) as r,archive.open('wb') as f:
   size=0
   while True:
    b=r.read(1048576)
    if not b:break
    size+=len(b);assert size<=150000000;f.write(b)
  assert digest(archive.read_bytes())==SHA
  with zipfile.ZipFile(archive) as z:
   prefix='Fatigue_Squat_2026_dataset/'
   inventory=[{'path':n,'bytes':z.getinfo(n).file_size} for n in z.namelist() if not n.endswith('/')]
   rb=z.read(prefix+'README.md');assert digest(rb)=='cb65ee390ccde63cf876c6d27ce5583ea42bb0a8ed5b832dc921dc99acf0813f'
   pb=z.read(prefix+'participants.csv');reader=csv.DictReader(io.StringIO(pb.decode('utf-8-sig')));fields=reader.fieldnames;rows=[r for r in reader if 'S01' in r.values()];assert len(rows)==1
   model=z.read(prefix+'model/LaiUhlrich2022_symmetric.osim');assert digest(model)=='42eca458626f42aa1e49d5925e14ec3c16fe81324293bacece643e11319ddbd9';x=ET.fromstring(model)
   report={'status':'VALIDÉ','scope':'archive inspection, not anatomical compatibility','archiveSHA256':SHA,'archiveURL':URL,'inventory':inventory,'README':rb.decode(),'participantsFileSHA256':digest(pb),'participantsColumns':fields,'S01':rows[0],'noOtherParticipantRowsPublished':True,'model':{'sha256':digest(model),'name':x.find('.//Model').attrib['name'],'lengthUnits':x.findtext('.//length_units'),'forceUnits':x.findtext('.//force_units'),'gravity':x.findtext('.//gravity'),'credits':x.findtext('.//credits'),'markers':markers(x),'genericBodyParameters':[{'name':b.attrib['name'],'mass':b.findtext('mass'),'massCenter':b.findtext('mass_center'),'inertia':b.findtext('inertia')} for b in x.findall('.//BodySet/objects/Body')]}}
   # An independently pinned upstream comparison is not a claim of exact direct ancestry.
   ref='5244f7d32abb2399d065a741479bbe4323586b45';repo='stanfordnmbl/PassiveMuscleForceCalibration';u=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/contents/LaiUhlrich2022.osim?ref={ref}']));ub=base64.b64decode(u['content']);assert digest(ub)=='f61d844fb20c25ee0db76cd1ed7c916e53683f31926caebfeb40d62bd4dbfd37';ux=ET.fromstring(ub);a,c=leaves(ux),leaves(x)
   diffs=[{'path':k,'upstream':a.get(k),'dataset':c.get(k)} for k in sorted(set(a)|set(c)) if a.get(k)!=c.get(k)]
   report['upstreamComparison']={'repo':repo,'commit':ref,'sha256':digest(ub),'modelName':ux.find('.//Model').attrib['name'],'markers':markers(ux),'markerDefinitionsEqual':markers(ux)==markers(x),'leafDifferences':diffs,'limitation':'canonical leaf text comparison; excludes XML comments/attribute-only changes, not direct lineage proof'}
   outforces={}
   def read(name):return np.genfromtxt(io.StringIO(gzip.decompress(z.read(prefix+'participants/S01/'+name)).decode()),delimiter=',',names=True)
   f=read('P001_force_plates.csv.gz');m=read('P001_markers.csv.gz');assert len(f)==3350 and np.array_equal(f['time'],m['time']);assert all(np.isfinite(f[c]).all() for c in f.dtype.names)
   repetitions=list(csv.DictReader(io.StringIO(z.read(prefix+'participants/S01/squat_repetitions.csv').decode())))
   masks={'fullP001':np.ones(len(f),dtype=bool)}
   for rep in repetitions:
    if rep['trial']=='P001':masks['rep'+rep['rep']]=(f['time']>=float(rep['t_start'])-1e-8)&(f['time']<=float(rep['t_end'])+1e-8)
   for scope,mask in masks.items():
    v=f[mask];item={'frames':len(v),'start':float(v['time'][0]),'end':float(v['time'][-1]),'components':{},'plates':{}}
    for col in f.dtype.names[1:]:item['components'][col]={'min':float(v[col].min()),'max':float(v[col].max()),'mean':float(v[col].mean())}
    for plate in [1,2]:
     fx,fy,fz=[v[f'PLATE_{plate}_F{axis}'] for axis in 'xyz'];horizontal=np.hypot(fx,fy)
     item['plates'][str(plate)]={'maxHorizontalN':float(horizontal.max()),'minFzN':float(fz.min()),'maxFzN':float(fz.max()),'thresholds':{str(th):{'belowOrEqualFrames':int((fz<=th).sum()),'transitions':int(np.count_nonzero(np.diff((fz>th).astype(int))))} for th in [10,20,50,100]}}
    total=v['PLATE_1_Fz']+v['PLATE_2_Fz'];valid=total>200;share=v['PLATE_1_Fz'][valid]/total[valid];item['plate1ShareWhereTotalAbove200N']={'frames':int(valid.sum()),'min':float(share.min()),'max':float(share.max()),'mean':float(share.mean())};outforces[scope]=item
   report['forces']={'status':'VALIDÉ','scope':'numerical component audit only; lab common frame and physical contact NOT validated','sourceSHA256':digest(z.read(prefix+'participants/S01/P001_force_plates.csv.gz')),'equalFileTimestamps':True,'sampleHz':float(1/np.median(np.diff(f['time']))),'windows':outforces,'COP':'NON TESTÉ','footAssignment':'EN ATTENTE DE VALIDATION HUMAINE','IK':'NON TESTÉ'}
  (OUT/'original-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 finally:
  if archive.exists():archive.unlink()
if __name__=='__main__':main()
