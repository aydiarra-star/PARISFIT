"""Fictional data ONLY. Disposable age identity stays in memory; never serialized/logged.
Run with pyrage 1.4.0 installed. No network or real PARISFIT resource access.
"""
from pathlib import Path
import io,tarfile,json,hashlib,datetime,platform
import pyrage
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase27';B=R/'.cache/phase27/poc';B.mkdir(parents=True,exist_ok=False)
def sha(b):return hashlib.sha256(b).hexdigest()
plain=('PARISFIT_PHASE27_FICTITIOUS_ONLY_8c4d1e\nAucune donnee humaine, aucun modele et aucun secret reel.\nTest local de chiffrement et restauration.\n').encode();name='fictitious-example.txt';(B/name).write_bytes(plain)
stream=io.BytesIO()
with tarfile.open(fileobj=stream,mode='w') as t:
 info=tarfile.TarInfo(name);info.size=len(plain);info.mtime=0;info.mode=0o600;t.addfile(info,io.BytesIO(plain))
archive=stream.getvalue();(B/'fiction.tar').write_bytes(archive)
identity=pyrage.x25519.Identity.generate();recipient=identity.to_public()
encrypted=pyrage.encrypt(archive,[recipient]);assert encrypted.startswith(b'age-encryption.org/v1\n');assert plain not in encrypted and b'PARISFIT_PHASE27_FICTITIOUS_ONLY_8c4d1e' not in encrypted and name.encode() not in encrypted
assert pyrage.encrypt(archive,[recipient])!=encrypted
(B/'fiction.tar.age').write_bytes(encrypted);parts=[]
for i,start in enumerate(range(0,len(encrypted),4096)):
 b=encrypted[start:start+4096];p=B/f'volume-{i:04d}.agepart';p.write_bytes(b);parts.append({'name':p.name,'index':i,'bytes':len(b),'sha256':sha(b)})
def assemble(records):
 assert [x['index'] for x in records]==list(range(len(parts))), 'missing/reordered volumes'
 assert len(records)==len(parts)
 blocks=[]
 for r in records:
  b=(B/r['name']).read_bytes();assert len(b)==r['bytes'] and sha(b)==r['sha256'];blocks.append(b)
 out=b''.join(blocks);assert sha(out)==sha(encrypted);return out
assembled=assemble(parts);decrypted=pyrage.decrypt(assembled,[identity]);assert sha(decrypted)==sha(archive)
with tarfile.open(fileobj=io.BytesIO(decrypted)) as t:
 members=t.getmembers();assert len(members)==1 and members[0].name==name and members[0].isfile();restored=t.extractfile(members[0]).read()
(B/'restored').mkdir();(B/'restored'/name).write_bytes(restored);assert restored==plain
negative={}
for label,data,key in [('wrong-key',encrypted,pyrage.x25519.Identity.generate()),('tampered',encrypted[:-1]+bytes([encrypted[-1]^1]),identity),('truncated',encrypted[:-20],identity)]:
 try:pyrage.decrypt(data,[key])
 except pyrage.DecryptError:negative[label]='rejected'
 else:raise AssertionError(label)
for label,records in [('missing-volume',parts[:-1]),('reordered-volumes',list(reversed(parts)))]:
 try:assemble(records)
 except AssertionError:negative[label]='rejected'
 else:raise AssertionError(label)
report={'status':'PASS','data':'one fictional text file only','implementation':'pyrage 1.4.0 / age format / X25519','python':platform.python_version(),'createdAtObservedUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'keyGeneratedInMemoryOnly':True,'keySerialized':False,'productionKeyCreated':False,'networkUsedByTest':False,'originalsReadByTest':False,'plaintext':{'bytes':len(plain),'sha256':sha(plain)},'tar':{'bytes':len(archive),'sha256':sha(archive)},'ciphertext':{'bytes':len(encrypted),'sha256':sha(encrypted),'headerReadable':'age-encryption.org/v1','knownPlaintextAndFilenameAbsent':True},'parts':parts,'restoredPlaintextSHA256':sha(restored),'restoredTarSHA256':sha(decrypted),'negativeTests':negative,'randomizedEncryption':True,'cliInteroperabilityTested':False,'limitations':['Only a small file, not a large-archive benchmark.','Identity is not saved: this run cannot be decrypted again after process exit; rerun creates a fresh independent fixture.','Absence of known readable strings is not a cryptographic proof.']}
(D/'poc-results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
