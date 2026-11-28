"""Read preserved evidence, installed metadata and immutable Git history; no biomechanical computation."""
from pathlib import Path
import json,hashlib,subprocess,sys,platform,importlib.metadata as md,warnings
D=Path('docs/coach/phase19');D.mkdir(parents=True,exist_ok=True)
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
 packages={}
 for n in ['numpy','c3d','scipy','Pillow','imageio-ffmpeg','opensim']:
  try:packages[n]=md.version(n)
  except md.PackageNotFoundError:packages[n]='inconnue / non installé dans cet interpréteur'
 import c3d
 metadata={}
 manifest=json.loads(Path('docs/coach/phase17/source-manifest.json').read_text())
 for x in manifest['files']:
  if x['path'].endswith('.c3d'):
   p=Path('.cache/phase17/source')/x['path'];assert sha(p.read_bytes())==x['sha256']
   with p.open('rb') as f,warnings.catch_warnings():
    warnings.simplefilter('ignore');r=c3d.Reader(f);groups=[k for k,g in r.group_items()]
    metadata[x['path']]={'sha256':x['sha256'],'groups':groups,'manufacturer':{n:v.string_array.tolist() for n,v in r.get('MANUFACTURER').param_items()},'subjectNames':r.get('SUBJECTS:NAMES').string_array.tolist(),'eventGroupPresent':'EVENT' in groups,'trialGroupPresent':'TRIAL' in groups,'analogLabels':[s.strip() for s in r.analog_labels],'pointRate':float(r.point_rate),'analogRate':float(r.analog_rate)}
 j=json.loads(Path('.cache/phase16/tree.json').read_text());assert not j['truncated'];paths=[x['path'] for x in j['tree'] if x['type']=='blob']
 scope=[p for p in paths if p.startswith(('AB01/Squat/1/','AB01/Static/1/'))];matches=[p for p in paths if p.startswith('AB01/') and any(s in p.lower() for s in ['log','calib','quality','sync'])]
 out={'referenceCommit':'71bae7d1ed34227b2fc2c1c4e79aa7fdf1be22f1','scope':'current local interpreter metadata, not claimed historical run environment','localPython':sys.version,'localPlatform':platform.platform(),'pythonPackages':packages,'node':subprocess.check_output(['node','--version']).decode().strip(),'npmLockSHA256':sha(Path('package-lock.json').read_bytes()),'playwrightInstalled':json.loads(Path('node_modules/@playwright/test/package.json').read_text())['version'],'threeInstalled':json.loads(Path('node_modules/three/package.json').read_text())['version'],'c3dMetadataOnly':metadata,'pinnedRepoCommit':'a26fe4852a78f30c5e8a437b158847031cb8dc3c','pinnedTreeEntryCount':len(j['tree']),'selectedTrialFiles':scope,'AB01LogCalibrationQualitySyncNameMatches':matches,'authorCodeExecuted':False}
 for p in ['docs/coach/phase9/blender-report.json','docs/coach/phase13/model-probe.json']:
  if Path(p).exists():out.setdefault('preservedReports',{})[p]={'sha256':sha(Path(p).read_bytes()),'report':json.loads(Path(p).read_text())}
 (D/'local-and-preserved-inventory.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
