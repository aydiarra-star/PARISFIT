"""Bounded primary-source retrieval in CI; failures remain explicit, never substituted."""
from pathlib import Path
import urllib.request,json,hashlib,zipfile,gzip,csv,io
ROOT=Path('.cache/phase12/originals');ROOT.mkdir(parents=True,exist_ok=True)
def fetch(url,path,limit):
 req=urllib.request.Request(url,headers={'User-Agent':'PARISFIT-source-audit/1.0'})
 with urllib.request.urlopen(req,timeout=60) as r,open(path,'wb') as out:
  n=0
  while True:
   chunk=r.read(1024*1024)
   if not chunk:break
   n+=len(chunk)
   if n>limit:raise ValueError('DOWNLOAD_SIZE_LIMIT')
   out.write(chunk)
 return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
 reports=[]
 for name in ['14.asf','14_06.amc','14_06.c3d']:
  p=ROOT/name;url='https://mocap.cs.cmu.edu/subjects/14/'+name;r={'file':name,'url':url,'status':'NON TESTÉ'}
  try:
   r['sha256']=fetch(url,p,30000000);r['bytes']=p.stat().st_size;r['status']='VALIDÉ';r['scope']='retrieval only, not quality'
   if name.endswith('.amc'):
    lines=p.read_text().splitlines();frames=[int(x) for x in lines if x.strip().isdigit()];r['frameCount']=len(frames);r['consecutiveFrameNumbers']=all(b==a+1 for a,b in zip(frames,frames[1:]));r['header']=lines[:8]
   elif name.endswith('.asf'):r['header']=p.read_text().split(':bonedata')[0]
  except Exception as e:r['status']='NON TESTÉ';r['error']=str(e)
  reports.append(r)
 z=ROOT/'zenodo.zip';r={'id':'Zenodo23979972/S01/P001','url':'https://zenodo.org/records/23979972/files/Fatigue_Squat_2026_dataset.zip?download=1','status':'NON TESTÉ','rights':'CC BY4.0, Florian Michaud2026; dataset only, OpenSim model not extracted'}
 try:
  r['archiveSHA256']=fetch(r['url'],z,150000000);assert r['archiveSHA256']=='901112330ed234ad97ce24cb866bd5e7e33bef766861d21264953b3ac1875782','ZENODO_SHA256_MISMATCH';assert hashlib.md5(z.read_bytes()).hexdigest()=='ae51793940720bcd0877bdad8c155e82','ZENODO_MD5_MISMATCH'
  r['files']=[]
  with zipfile.ZipFile(z) as archive:
   for name in archive.namelist():
    if name.endswith('README.md') or ('/S01/' in '/'+name and name.endswith(('P001_markers.csv.gz','P001_force_plates.csv.gz','squat_repetitions.csv','static_markers.csv.gz'))):
     raw=archive.read(name);out=ROOT/('zenodo-'+Path(name).name);out.write_bytes(raw);text=gzip.decompress(raw).decode() if name.endswith('.gz') else raw.decode();r['files'].append({'name':name,'sha256':hashlib.sha256(raw).hexdigest(),'header':text.splitlines()[:5],'rows':len(text.splitlines())-1})
     if name.endswith('README.md'):r['readme']=text
  assert any('P001_markers' in f['name'] for f in r['files']),'EXPECTED_TRIAL_MISSING'
  r['status']='EN ATTENTE DE VALIDATION HUMAINE';r['meaning']='downloaded subset; markers/forces not interchangeable with BVH joint pivots; no qualified reference selected'
 except Exception as e:r['error']=str(e)
 finally:
  if z.exists():z.unlink()
 reports.append(r);(ROOT.parent/'original-retrieval.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'NOTICE.txt').write_text('CMU: The data used in this project was obtained from mocap.cs.cmu.edu. The database was created with funding from NSF EIA-0196217. No standalone data resale.\nZenodo: Florian Michaud (2026), Motion capture, ground reaction forces and knee extension strength during repeated dumbbell squats to fatigue: dataset and symmetric OpenSim model, v1, https://zenodo.org/records/23979972 . Article: Michaud, Katwal, Porzio and Cuadrado, Toward Real-Time Estimation of Muscle Force and Fatigue During Resistance Training Using a Neural Network Surrogate of OpenSim Musculotendon Kinematics. CC BY4.0 https://creativecommons.org/licenses/by/4.0/ . Only S01/P001, static calibration, repetition annotations and README extracted; model not redistributed, no endorsement.\n')
if __name__=='__main__':main()
