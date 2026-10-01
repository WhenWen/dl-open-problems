"""Protect the distinction between discovery leads and reviewed catalog entries."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('discovery', ROOT / 'scripts/discovery.py')
discovery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(discovery)

class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)/'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git','__pycache__'))
        self.batch = self.root/'discovery/2026-10-01'
        self.addCleanup(self.temp.cleanup)

    def edit(self, relative, fn):
        p=self.root/relative
        x=json.loads(p.read_text());fn(x);p.write_text(json.dumps(x))

    def lead(self, fn):
        self.edit('discovery/2026-10-01/candidates.json', lambda x:fn(x[0]))

    def reject(self, pattern):
        with self.assertRaisesRegex(ValueError,pattern):
            discovery.validate(self.root,self.batch)

    def test_snapshot_matches_records(self):
        self.assertEqual(discovery.render(*discovery.validate(self.root,self.batch)),(self.batch/'README.md').read_text())

    def test_no_silent_promotion(self):
        self.lead(lambda x:x.update(status='literature_audited'))
        self.reject('cannot be promoted')

    def test_missing_primary_reference(self):
        self.lead(lambda x:x.update(sources=['missing']))
        self.reject('unknown discovery source')

    def test_update_without_canonical_id(self):
        self.lead(lambda x:x.update(existing_problems=[]))
        self.reject('must map to a canonical ID')

    def test_unknown_comparison_target(self):
        self.lead(lambda x:x['related_leads'][0].update(target='DISC-20990101-999'))
        self.reject('dangling discovery relation')

    def test_query_provenance_mismatch(self):
        self.edit('coverage/searches.json',lambda x:x[2]['queries'].append('Unperformed query'))
        self.reject('queries disagree with manifest')

    def test_unknown_triage_evidence(self):
        self.edit('discovery/2026-10-01/triage.json',lambda x:x[0].update(sources=['missing']))
        self.reject('dangling triage reference')

    def test_duplicate_question(self):
        self.edit('discovery/2026-10-01/candidates.json',lambda x:x[1].update(question=x[0]['question']))
        self.reject('duplicate discovery question')

    def test_cross_batch_duplicate_id(self):
        original = json.loads((self.batch/'candidates.json').read_text())[0]
        self.edit('discovery/2026-10-01-expansion/candidates.json', lambda x:x[0].update(id=original['id']))
        self.reject('duplicate discovery ID across batches')

    def test_cross_batch_duplicate_question(self):
        original = json.loads((self.batch/'candidates.json').read_text())[0]
        self.edit('discovery/2026-10-01-expansion/candidates.json', lambda x:x[0].update(question=original['question']))
        self.reject('duplicate discovery question across batches')

    def test_expansion_snapshot_and_cross_batch_link(self):
        batch = self.root/'discovery/2026-10-01-expansion'
        output = discovery.render(*discovery.validate(self.root,batch))
        self.assertEqual(output,(batch/'README.md').read_text())
        self.assertIn('../2026-10-01/README.md#disc-20261001-012',output)

    def test_area_cannot_silently_claim_completion(self):
        self.batch = self.root/'discovery/2026-10-01-expansion'
        self.edit('discovery/2026-10-01-expansion/area-coverage.json',lambda x:x[0].update(full_text_audit=True))
        self.reject('cannot certify area completeness')

    def test_area_source_provenance(self):
        self.batch = self.root/'discovery/2026-10-01-expansion'
        self.edit('discovery/2026-10-01-expansion/area-coverage.json',lambda x:x[0].update(sources=[]))
        self.reject('area sources disagree')

    def test_query_ids_unique_across_batches(self):
        old = json.loads((self.batch/'search-manifest.json').read_text())[0]['id']
        self.edit('discovery/2026-10-01-expansion/search-manifest.json',lambda x:x[0].update(id=old))
        self.reject('duplicate query batch across batches')

if __name__=='__main__':
    unittest.main()
