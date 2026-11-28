import unittest,json,hashlib,sys,tempfile,re
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent));import volumes
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase27';B=R/'.cache/phase27';P=B/'poc'
class Proof(unittest.TestCase):
 def test_recorded_crypto(self):
  r=json.loads((D/'poc-results.json').read_text());self.assertEqual(r['status'],'PASS');self.assertFalse(r['keySerialized']);self.assertFalse(r['originalsReadByTest']);self.assertTrue(all(x=='rejected' for x in r['negativeTests'].values()))
  self.assertEqual(hashlib.sha256((P/'fictitious-example.txt').read_bytes()).hexdigest(),r['restoredPlaintextSHA256']);self.assertEqual((P/'restored/fictitious-example.txt').read_bytes(),(P/'fictitious-example.txt').read_bytes())
 def test_multi_volume_tool(self):
  root=Path(tempfile.mkdtemp(prefix='volumes-',dir=B));m=volumes.split(P/'fiction.tar.age',root/'parts',4096);self.assertEqual(len(m['parts']),3);volumes.join(root/'parts',root/'joined.age');self.assertEqual(volumes.digest(root/'joined.age'),m['ciphertextSHA256'])
  with self.assertRaises(FileExistsError):volumes.join(root/'parts',root/'joined.age')
  manifest=root/'parts/manifest.json';m['parts'].reverse();manifest.write_text(json.dumps(m))
  with self.assertRaises(AssertionError):volumes.join(root/'parts',root/'reordered.age')
  m['parts'].reverse();m['parts'][0]['name']='../untrusted.agepart';manifest.write_text(json.dumps(m))
  with self.assertRaises(AssertionError):volumes.join(root/'parts',root/'unsafe.age')
  with self.assertRaises(AssertionError):volumes.split(P/'fictitious-example.txt',root/'plaintext-refused')
 def test_no_private_key_in_deliverables(self):
  paths=list(D.glob('*'))+list((R/'tools/encrypted-backup').glob('*.py'))
  for p in paths:
   if p.is_file():self.assertIsNone(re.search(rb'AGE-SECRET-KEY-1[0-9A-Z]{50,}',p.read_bytes()),str(p))
 def test_preservation(self):
  for r in json.loads((R/'docs/coach/phase26/backup-file-manifest.json').read_text()):self.assertEqual(hashlib.sha256((R/r['path']).read_bytes()).hexdigest(),r['sha256'],r['path'])
 def test_history_scope(self):
  a=json.loads((D/'history-versions.json').read_text());self.assertEqual(len(a),1158);self.assertEqual(sum(x['historicalOnlyVersion'] for x in a),204)
  self.assertEqual((D/'remote-refs.txt').read_text(),(R/'docs/coach/phase26/remote-refs.txt').read_text())
 def test_deliverables(self):
  for n in ['architecture-proposal','encryption-comparison','git-history-exposure','github-storage-limits','proof-of-concept-report','recovery-procedure','decision-report']:self.assertGreater((D/(n+'.md')).stat().st_size,1000)
if __name__=='__main__':unittest.main(verbosity=2)
