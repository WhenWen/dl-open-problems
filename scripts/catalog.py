"""Validate the catalog and generate its offline Markdown index (Python 3.10+)."""
import argparse
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = ['Question', 'Setting and available information', 'Established results',
            'Remaining uncertainty', 'Competing explanations', 'Decisive test',
            'Success criteria and cost', 'Literature audit', 'Related problems']


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    return json.loads(path.read_text())


def text(value):
    return isinstance(value, str) and bool(value.strip())


def strings(value):
    return isinstance(value, list) and bool(value) and all(text(x) for x in value)


def dated(value):
    require(isinstance(value, str), 'date must be an ISO string')
    require(date.fromisoformat(value).isoformat() == value, f'invalid date: {value}')


def url(value):
    return isinstance(value, str) and urlparse(value).scheme == 'https' and bool(urlparse(value).netloc)


def unique(items, field, label):
    keys = [x[field] for x in items]
    require(len(keys) == len(set(keys)), f'duplicate {label}')
    return {x[field]: x for x in items}


def validate(root):
    tax = read(root / 'taxonomy.json')
    papers = read(root / 'bibliography.json')
    sources = unique(papers, 'id', 'source ID')
    require(len({p['url'] for p in papers}) == len(papers), 'duplicate source URL')
    for p in papers:
        require(text(p['title']) and url(p['url']), 'source title or URL invalid')
        require(p['reading_depth'] in ['abstract', 'full_text'], 'invalid reading depth')
        dated(p['checked_on'])
    cards = []
    for folder in sorted((root / 'problems').iterdir()):
        require(folder.is_dir() and not folder.is_symlink(), f'unexpected problem entry: {folder.name}')
        p = read(folder / 'metadata.json')
        ident = p['id']
        require(re.fullmatch(r'DLOP-\d{4}', ident) and ident == folder.name, 'invalid or mismatched problem ID')
        for field in ['title', 'setting', 'inputs', 'target', 'intervention']:
            require(text(p[field]), f'{ident}: empty {field}')
        for field in ['topics', 'phenomena', 'gaps']:
            require(strings(p[field]) and len(p[field]) == len(set(p[field])) and set(p[field]) <= set(tax[field]), f'{ident}: invalid {field}')
        require(p['status'] in tax['statuses'], f'{ident}: invalid status')
        require(strings(p['contributors']), f'{ident}: missing contributors')
        require(strings(p['sources']) and set(p['sources']) <= sources.keys(), f'{ident}: missing source')
        for field in ['created', 'last_reviewed']:
            dated(p[field])
        require(p['last_reviewed'] >= p['created'], f'{ident}: review precedes creation')
        for field in ['theory', 'empirical', 'prediction']:
            require(text(p['evidence'][field]), f'{ident}: missing evidence axis {field}')
        require(isinstance(p['relations'], list), f'{ident}: invalid relations')
        unique(p['relations'], 'target', f'{ident} relation target')
        for edge in p['relations']:
            require(edge['type'] in tax['relations'] and text(edge['reason']), f'{ident}: invalid relation')
        body = (folder / 'README.md').read_text()
        for heading in HEADINGS:
            require(f'## {heading}\n' in body, f'{ident}: missing section {heading}')
        cards.append(p)
    require(cards, 'no problem cards')
    by_id = unique(cards, 'id', 'problem ID')
    titles = [' '.join(p['title'].casefold().split()) for p in cards]
    require(len(set(titles)) == len(titles), 'duplicate normalized title; review identity')
    for p in cards:
        for edge in p['relations']:
            require(edge['target'] in by_id and edge['target'] != p['id'], f"{p['id']}: dangling or self relation")
        if p['status'] == 'merged':
            target = p['canonical_id']
            require(target in by_id and target != p['id'] and by_id[target]['status'] != 'merged', 'invalid merge target')
        else:
            require(p['canonical_id'] is None, 'only merged cards have canonical IDs')
    decisions = read(root / 'reviews/decisions.json')
    unique(decisions, 'id', 'decision ID')
    for d in decisions:
        dated(d['date'])
        require(d['problem'] in by_id and d['status'] in tax['statuses'], 'invalid decision target')
        require(strings(d['reviewers']) and isinstance(d['self_review'], bool) and text(d['rationale']), 'incomplete review')
        require(strings(d['evidence']) and all(url(x) for x in d['evidence']), 'review requires public evidence URLs')
    for p in cards:
        if p['status'] != 'candidate':
            history = [d for d in decisions if d['problem'] == p['id']]
            require(history and history[-1]['status'] == p['status'], f"{p['id']}: status lacks matching latest review")
        if p['status'] in ['literature_audited', 'empirical_gap', 'resolved']:
            require(any(sources[s]['reading_depth'] == 'full_text' for s in p['sources']), f"{p['id']}: promotion requires full-text evidence")
    searches = read(root / 'coverage/searches.json')
    unique(searches, 'id', 'search ID')
    for s in searches:
        dated(s['date'])
        require(s['topic'] in tax['topics'], 'invalid coverage topic')
        for field in ['method', 'limitations', 'next_steps']:
            require(text(s[field]), f'incomplete search {field}')
        require(strings(s['queries']), 'search needs actual queries or traversal descriptions')
        require(isinstance(s['sources'], list) and set(s['sources']) <= sources.keys(), 'unknown search source')
        require(isinstance(s['problems'], list) and set(s['problems']) <= by_id.keys(), 'unknown search problem')
        require(isinstance(s['excluded'], list) and all(text(x) for x in s['excluded']), 'invalid exclusions')
    # Paths only: remote link availability and anchors require separate review.
    for md in root.rglob('*.md'):
        if '.git' in md.parts:
            continue
        for target in re.findall(r'\]\(([^\s)]+)\)', md.read_text()):
            if urlparse(target).scheme or target.startswith('#'):
                continue
            target = unquote(target.split('#')[0])
            require((md.parent / target).exists(), f'broken local link in {md.relative_to(root)}: {target}')
    return tax, cards, searches


def render(tax, cards, searches):
    def cell(s):
        return s.replace('|', '\\|').replace('\n', ' ')
    rows = ['# Problem index', '', 'Generated from structured metadata. Edit cards and search records, then run `python3 scripts/catalog.py`.', '',
            'Candidate means an incomplete literature audit, not a verified open problem.', '', '[Batch discovery queue](discovery/README.md) contains additional leads awaiting deeper review and is not counted as canonical cards.', '',
            '| ID | Question | Status | Topics | Last checked |', '| --- | --- | --- | --- | --- |']
    for p in cards:
        rows.append(f"| {p['id']} | [{cell(p['title'])}](problems/{p['id']}/README.md) | {p['status']} | {', '.join(p['topics'])} | {p['last_reviewed']} |")
    rows += ['', '## Coverage', '', 'A tagged card is not proof that its topic was searched. Open the [ledger](coverage/searches.json) for methods and limitations.', '', '| Topic | Cards | Recorded searches |', '| --- | --- | --- |']
    for topic in tax['topics']:
        matching = ', '.join(p['id'] for p in cards if topic in p['topics']) or 'None'
        entries = ', '.join(s['id'] for s in searches if s['topic'] == topic) or '**Not searched**'
        rows.append(f'| {topic} | {matching} | {entries} |')
    rows += ['', '## Relationships', '', 'Edges are proposals with explicit rationales, not automated equivalence judgments.', '']
    for p in cards:
        for edge in p['relations']:
            rows.append(f"- {p['id']} → {edge['type']} → {edge['target']}: {edge['reason']}")
    return '\n'.join(rows) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the generated index is stale')
    args = parser.parse_args()
    try:
        index = ROOT / 'INDEX.md'
        if not index.exists() and not args.check:
            index.write_text('# Problem index\n')
        output = render(*validate(ROOT))
        if args.check:
            require(index.exists() and index.read_text() == output, 'INDEX.md is stale; run python3 scripts/catalog.py')
        else:
            index.write_text(output)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f'Validation failed: {exc}\n')
    print('Catalog validated; index ' + ('verified.' if args.check else 'generated.'))


if __name__ == '__main__':
    main()
