"""Read-only submission contracts: no messages, source acquisition or biomechanics."""
from pathlib import Path
import unittest,json,re
D=Path('docs/coach/phase21')
class Submission(unittest.TestCase):
 def test_deliverables(self):
  for n in ['external-dossier-audit','expert-profile','professional-evaluation-grid','expert-outreach-fr','expert-outreach-en','collaboration-and-confidentiality','post-review-decision-tree','decision-report']:self.assertGreater((D/(n+'.md')).stat().st_size,400)
 def test_blank_grid(self):
  rows=json.loads((D/'professional-evaluation-template.json').read_text());self.assertEqual(len(rows),9);self.assertEqual(len({r['id'] for r in rows}),9)
  for r in rows:
   for k in ['conclusion','justification','evidence_examined','confidence','additional_information_needed','conditions']:self.assertIsNone(r[k])
 def test_audit(self):
  j=json.loads((D/'audit-results.json').read_text());self.assertEqual(len(j['equivalence']),4);self.assertEqual(len(j['manifest']),6);self.assertFalse(j['preservation']['changed']);self.assertFalse(any(j['sensitivePatternCounts'].values()))
 def test_reference_ci(self):
  j=json.loads((D/'ci-reference-runs.json').read_text());self.assertEqual(j['total_count'],3)
  for r in j['runs']:self.assertEqual(r['head_sha'],j['reference']);self.assertEqual(r['status'],'completed');self.assertEqual(r['conclusion'],'success')
  self.assertEqual(sum(x['conclusion']=='skipped' for r in j['runs'] for x in r['jobs']),4)
 def test_links(self):
  for p in D.glob('*.md'):
   for s in re.findall(r'\]\(([^)]+)\)',p.read_text()):
    if not s.startswith('https://'):self.assertTrue((p.parent/s).exists(),f'{p}: {s}')
 def test_licenses(self):
  x=json.loads((D/'scientific-reference-check.json').read_text());self.assertNotEqual(x['article']['licenseDisplayed'],x['dataset']['licenseDisplayed']);self.assertIn('CC BY-NC-ND4.0',(D/'submission-addendum.md').read_text())
 def test_outreach_boundaries(self):
  fr=(D/'expert-outreach-fr.md').read_text();en=(D/'expert-outreach-en.md').read_text();self.assertIn('NE PAS ENVOYER',fr);self.assertIn('DO NOT SEND',en)
  for text in [fr,en]:self.assertNotRegex(text,r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}');self.assertIn('4',text);self.assertIn('8',text)
if __name__=='__main__':unittest.main()
