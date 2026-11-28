"""Local tests of candidate traceability and preserved repository, no network or contact."""
from pathlib import Path
import json,csv,re,hashlib,subprocess,unittest
D=Path('docs/coach/phase22');REF='7a301e0f61b1328b70192b3514fdae26eaaad183'
class Candidates(unittest.TestCase):
 def test_deliverables(self):
  for n in ['expert-candidates.md','laboratories.md','expertise-criteria.md','candidate-comparison.csv','contact-readiness.md','decision-report.md']:self.assertGreater((D/n).stat().st_size,200)
 def test_sources_contacts(self):
  s={x['id']:x for x in json.loads((D/'sources.json').read_text())};p=json.loads((D/'candidates.json').read_text());self.assertEqual(len(p),4)
  for x in p:
   self.assertTrue(all(i in s for i in x['sources']));self.assertIn(x['contact'],s[x['contact_source']]['observed']);self.assertEqual(x['consulted'],'2026-11-27')
 def test_rank_limits(self):
  p=json.loads((D/'candidates.json').read_text());self.assertEqual(sorted(x['rank'] for x in p if x['rank']),[1,2,3]);self.assertEqual({x['priority'] for x in p},{'1','2','3'})
  for x in p:self.assertTrue(x['limits']);self.assertTrue(x['independence']);self.assertFalse(x['contacted']);self.assertFalse(x['documents_sent']);self.assertFalse(x['quote_requested']);self.assertEqual(x['public_cost'],'devis nécessaire')
 def test_csv(self):
  r=list(csv.DictReader((D/'candidate-comparison.csv').read_text().splitlines()));self.assertEqual(len(r),9);self.assertEqual(sum(x['type']=='personne' for x in r),4);self.assertEqual(sum(bool(x['rang_finaliste']) for x in r),3)
  for x in r:self.assertEqual(x['contact_effectue'],'non');self.assertEqual(x['cout_public'],'devis nécessaire');self.assertTrue(x['source_contact'].startswith('https://'))
 def test_no_secret_or_binary(self):
  for p in D.iterdir():
   self.assertIn(p.suffix,['.md','.csv','.json','.html']);self.assertNotRegex(p.read_text(),r'github_pat_|gh[pousr]_[A-Za-z0-9]{20,}|[?&](?:token|Signature|signature)=|-----BEGIN .*PRIVATE KEY')
 def test_links(self):
  for p in D.glob('*.md'):
   for u in re.findall(r'\]\(([^)]+)\)',p.read_text()):
    if not u.startswith('https://'):self.assertTrue((p.parent/u).exists(),f'{p}: {u}')
 def test_reference_ci(self):
  j=json.loads((D/'ci-reference-runs.json').read_text());self.assertEqual(j['total_count'],3)
  for r in j['runs']:self.assertEqual(r['head_sha'],REF);self.assertEqual(r['status'],'completed');self.assertEqual(r['conclusion'],'success')
  self.assertEqual(sum(x['conclusion']=='skipped' for r in j['runs'] for x in r['jobs']),4)
 def test_preservation(self):
  paths=subprocess.check_output(['git','ls-tree','-r','--name-only',REF]).decode().splitlines()
  for p in paths:self.assertEqual(Path(p).read_bytes(),subprocess.check_output(['git','show',REF+':'+p]),p)
if __name__=='__main__':unittest.main()
