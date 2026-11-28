"""Repeat read-only verification while the local archives/restoration still exist."""
import json,hashlib,unittest,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase26';T=R/'.cache/phase26-work/restored/files'
def read(n):return json.loads((D/n).read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
class Backup(unittest.TestCase):
 def test_archive_hashes(self):
  for a in read('archive-register.json')['archives']:self.assertEqual(sha(R/a['archive']),a['sha256'])
 def test_file_restore_and_sources(self):
  for r in read('backup-file-manifest.json'):
   self.assertEqual(sha(T/r['path']),r['sha256'],r['path']);self.assertEqual(sha(R/r['path']),r['sha256'],r['path'])
 def test_refs_and_integrity(self):
  self.assertEqual(read('restored-git-fsck.json')['exitCode'],0)
  self.assertTrue(all(x['matches'] for x in read('remote-coverage.json')))
  self.assertTrue(read('archive-register.json')['sourceRefsUnchanged'])
  self.assertEqual(subprocess.check_output(['git','branch','--show-current'],cwd=R).strip(),b'arena/a03f64da-parisfit')
 def test_no_overclaim(self):
  self.assertFalse(read('archive-register.json')['durable']);self.assertFalse(read('archive-register.json')['uploaded'])
  self.assertFalse(read('destination-evidence.json')['durableDestinationVerified']);self.assertFalse(read('security-scan.json')['certifiesNoSecret'])
  self.assertEqual(len(read('artifact-retrieval.json')['metadataOnlyIds']),216)
 def test_reports(self):
  for n in ['destination-assessment','backup-scope','backup-procedure','integrity-report','restore-test','security-review','public-repository-plan','decision-report']:self.assertGreater((D/(n+'.md')).stat().st_size,1000)
if __name__=='__main__':unittest.main(verbosity=2)
