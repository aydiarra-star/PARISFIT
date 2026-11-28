"""Split/reassemble an already encrypted age file. No encryption, key handling, network or deletion.
Public manifest contains ciphertext hashes only. All outputs must be new.
"""
from pathlib import Path
import argparse,hashlib,json,re
CHUNK=1024*1024
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''):h.update(b)
 return h.hexdigest()
def split(src,dest,limit=20*1024*1024):
 with src.open('rb') as f:assert f.read(22).startswith(b'age-encryption.org/v1\n'),'Only binary age ciphertext accepted'
 assert 1<=limit<=20*1024*1024
 dest.mkdir(parents=True,exist_ok=False);rows=[]
 with src.open('rb') as f:
  while True:
   data=f.read(limit)
   if not data:break
   name=f'volume-{len(rows):06d}.agepart'
   with (dest/name).open('xb') as out:out.write(data)
   rows.append({'index':len(rows),'name':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 m={'schema':1,'format':'age-encryption.org/v1','ciphertextBytes':src.stat().st_size,'ciphertextSHA256':digest(src),'volumeLimit':limit,'parts':rows}
 (dest/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');return m
def join(folder,dest):
 m=json.loads((folder/'manifest.json').read_text());assert m['schema']==1 and m['format']=='age-encryption.org/v1';parts=m['parts'];assert parts
 assert [r['index'] for r in parts]==list(range(len(parts)))
 assert len({r['name'] for r in parts})==len(parts)
 for r in parts:
  assert re.fullmatch(r'volume-\d{6}\.agepart',r['name']);p=folder/r['name'];assert p.is_file() and not p.is_symlink();assert p.stat().st_size==r['bytes'] and digest(p)==r['sha256']
 assert sum(r['bytes'] for r in parts)==m['ciphertextBytes']
 with dest.open('xb') as out:
  for r in parts:
   with (folder/r['name']).open('rb') as src:
    for b in iter(lambda:src.read(CHUNK),b''):out.write(b)
 assert digest(dest)==m['ciphertextSHA256'],'Joined file must not be used: hash mismatch'
 return m
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('mode',choices=['split','join']);p.add_argument('source',type=Path);p.add_argument('destination',type=Path);a=p.parse_args();m=split(a.source,a.destination) if a.mode=='split' else join(a.source,a.destination);print(json.dumps({'bytes':m['ciphertextBytes'],'sha256':m['ciphertextSHA256'],'volumes':len(m['parts'])}))
