"""Regression tests for contribution failures CI must reject."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('catalog', ROOT / 'scripts/catalog.py')
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        self.addCleanup(self.temp.cleanup)

    def edit(self, path, fn):
        path = self.root / path
        data = json.loads(path.read_text())
        fn(data)
        path.write_text(json.dumps(data))

    def card(self, fn):
        self.edit('problems/DLOP-0001/metadata.json', fn)

    def reject(self, pattern):
        with self.assertRaisesRegex(ValueError, pattern):
            catalog.validate(self.root)

    def test_seed_catalog_and_deterministic_index(self):
        self.assertEqual(catalog.render(*catalog.validate(self.root)), (self.root / 'INDEX.md').read_text())

    def test_unknown_topic(self):
        self.card(lambda p: p.update(topics=['unregistered']))
        self.reject('invalid topics')

    def test_unknown_source(self):
        self.card(lambda p: p.update(sources=['missing']))
        self.reject('missing source')

    def test_dangling_relation(self):
        self.card(lambda p: p['relations'][0].update(target='DLOP-9999'))
        self.reject('dangling or self relation')

    def test_duplicate_title(self):
        other = json.loads((self.root / 'problems/DLOP-0002/metadata.json').read_text())
        self.card(lambda p: p.update(title=other['title'].upper()))
        self.reject('duplicate normalized title')

    def test_promotion_without_review(self):
        self.card(lambda p: p.update(status='literature_audited'))
        self.reject('status lacks matching latest review')

    def test_abstract_only_promotion(self):
        self.card(lambda p: p.update(status='literature_audited'))
        self.edit('reviews/decisions.json', lambda d: d.append(dict(id='R1', date='2026-10-01', problem='DLOP-0001', status='literature_audited', reviewers=['reviewer'], self_review=False, rationale='Example review', evidence=['https://example.org/review'])))
        self.reject('promotion requires full-text evidence')

    def test_missing_section(self):
        p = self.root / 'problems/DLOP-0001/README.md'
        p.write_text(p.read_text().replace('## Decisive test', '## Experiment'))
        self.reject('missing section Decisive test')

    def test_broken_local_link(self):
        p = self.root / 'README.md'
        p.write_text(p.read_text() + '\n[Broken](missing.md)\n')
        self.reject('broken local link')

    def test_coverage_reference(self):
        self.edit('coverage/searches.json', lambda x: x[0].update(problems=['DLOP-9999']))
        self.reject('unknown search problem')

    def test_index_changes_when_metadata_changes(self):
        self.card(lambda p: p.update(title='A corrected scientific question'))
        self.assertNotEqual(catalog.render(*catalog.validate(self.root)), (self.root / 'INDEX.md').read_text())


if __name__ == '__main__':
    unittest.main()
