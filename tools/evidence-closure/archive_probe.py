"""Public ZIP directory/member range reads only. Never execute acquired material."""
import urllib.request,json,struct,zlib,hashlib,re,base64
from pathlib import Path
OUT=Path('.cache/phase19');OUT.mkdir(parents=True,exist_ok=True)
BUDGET=24_000_000
class Remote:
 def __init__(self,file):self.file=file;self.used=0
 def get(self,a,b):
  global BUDGET
  assert 0<=a<=b<self.file['size'] and b-a+1<=6_000_000 and b-a+1<=BUDGET
  req=urllib.request.Request(self.file['download_url'],headers={'Range':f'bytes={a}-{b}','User-Agent':'PARISFIT-passive-evidence-review'})
  with urllib.request.urlopen(req,timeout=60) as r:
   assert r.status==206 and r.headers.get('Content-Range','').startswith(f'bytes {a}-{b}/'),'RANGE_NOT_HONORED: whole archive download refused'
   data=r.read(b-a+2);assert len(data)==b-a+1
  self.used+=len(data);BUDGET-=len(data);return data
 def directory(self):
  size=self.file['size'];tail=self.get(max(0,size-66000),size-1);i=tail.rfind(b'PK\x05\x06');assert i>=0
  e=struct.unpack_from('<4s4H2IH',tail,i);n,sz,off=e[4],e[5],e[6];assert n<65535 and off+sz<=size and sz<=6_000_000,'ZIP64_OR_OVERSIZE_NOT_SUPPORTED'
  raw=self.get(off,off+sz-1);items=[];p=0
  while p<len(raw):
   a=struct.unpack_from('<4s6H3I5H2I',raw,p);assert a[0]==b'PK\x01\x02';name=raw[p+46:p+46+a[10]].decode('utf-8' if a[3]&2048 else 'cp437');items.append({'path':name,'flags':a[3],'method':a[4],'crc32':a[7],'compressed':a[8],'bytes':a[9],'offset':a[16]});p+=46+a[10]+a[11]+a[12]
  assert len(items)==n;return items,hashlib.sha256(raw).hexdigest()
 def member(self,x):
  assert not(x['flags']&1) and x['bytes']<=1_000_000 and x['compressed']<=1_000_000
  h=self.get(x['offset'],x['offset']+29);a=struct.unpack('<4s5H3I2H',h);assert a[0]==b'PK\x03\x04';start=x['offset']+30+a[9]+a[10]
  raw=self.get(start,start+x['compressed']-1);data=zlib.decompress(raw,-15) if x['method']==8 else raw if x['method']==0 else None
  assert data is not None and len(data)==x['bytes'] and zlib.crc32(data)==x['crc32'];return data

def main():
 report={'mode':'read-only public metadata/ranges; no author code executed','requests':[],'files':[]}
 try:
  with urllib.request.urlopen('https://api.figshare.com/v2/articles/28689221',timeout=60) as r:meta=json.load(r)
  report['dataset']={k:meta.get(k) for k in ['id','doi','version','modified_date','license']}
  for name in ['MATLAB tools.zip','AB01.zip']:
   f=next(x for x in meta['files'] if x['name']==name);rr=Remote(f);entry={'name':name,'id':f['id'],'archiveBytes':f['size'],'publishedMD5':f['computed_md5']}
   report['files'].append(entry)
   try:
    items,h=rr.directory();entry['centralDirectorySHA256']=h;entry['entryCount']=len(items)
    targets=[x for x in items if not x['path'].endswith('/') and (name=='AB01.zip' and any(t in x['path'].lower() for t in ['squat/1/','static/1/','log','calib','quality','sync']) or name=='MATLAB tools.zip' and x['path'].split('/')[-1].lower() in ['scale.m','ik.m','osimc3d.m','trial_class.m','version.txt','license','license.txt','readme.md','one_leg_squat_shoe_lace_samples.mat'])]
    entry['targetInventory']=targets
    for x in targets:
     leaf=x['path'].split('/')[-1].lower()
     allowed=leaf in ['scale.m','ik.m','osimc3d.m','trial_class.m','version.txt','license','license.txt','readme.md'] or name=='AB01.zip' and leaf.endswith(('.log','.txt','.xml'))
     if not allowed or x['bytes']>250000 or x['compressed']==0:continue
     data=rr.member(x);record={'path':x['path'],'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
     # Only publicly released code/config text; redact local profile paths if present.
     text=data.decode('utf-8',errors='replace');text=re.sub(r'(?i)([A-Z]:[\\/]Users[\\/])[^\\/\s<]+',r'\1[REDACTED]',text)
     lines=text.splitlines();keep=set()
     for i,line in enumerate(lines):
      if re.search(r'(?i)version|scaleTool|set\w+|marker|model_file|time_range|butter|filt|sync|latency|error|rms|mass|calib|copyright|license',line):keep.update(range(max(0,i-1),min(len(lines),i+2)))
     record['excerpts']=[{'line':i+1,'text':lines[i]} for i in sorted(keep)[:110]];entry.setdefault('acquired',[]).append(record)
   except Exception as e:entry['error']=str(e)
   entry['downloadedBytes']=rr.used
 except Exception as e:report['error']=str(e)
 report['totalRangeBytes']=24_000_000-BUDGET
 (OUT/'archive-probe.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 packed=base64.b64encode(zlib.compress(json.dumps(report,ensure_ascii=False,separators=(',',':')).encode(),9)).decode()
 if len(packed)>35000:
  for f in report['files']:
   for x in f.get('acquired',[]):x['excerpts']=x['excerpts'][:30]
  packed=base64.b64encode(zlib.compress(json.dumps(report,ensure_ascii=False,separators=(',',':')).encode(),9)).decode()
 assert len(packed)<=35000,'TRANSPORT_LIMIT'
 for i in range(0,len(packed),3500):print('::warning title=phase19-archive-'+str(i//3500)+'::'+packed[i:i+3500])
 print('Range bytes:',report['totalRangeBytes'])
if __name__=='__main__':main()
