"""Validate and render discovery leads without promoting them to problem cards."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def read(p):
    return json.loads(p.read_text())

def require(ok, message):
    if not ok:
        raise ValueError(message)

def validate(root, batch):
    candidates = read(batch / 'candidates.json')
    bibliography = {p['id']: p for p in read(root / 'bibliography.json')}
    topics = read(root / 'taxonomy.json')['topics']
    all_batches = sorted((root / 'discovery').glob('*/candidates.json'))
    all_candidates = [p for file in all_batches for p in read(file)]
    all_ids = [p['id'] for p in all_candidates]
    require(len(all_ids) == len(set(all_ids)), 'duplicate discovery ID across batches')
    all_questions = [' '.join(p['question'].lower().split()) for p in all_candidates]
    require(len(all_questions) == len(set(all_questions)), 'duplicate discovery question across batches')
    locations = {p['id']: '../' + file.parent.name + '/README.md#' + p['id'].lower()
                 for file in all_batches for p in read(file)}
    ids = [p['id'] for p in candidates]
    require(len(ids) == len(set(ids)), 'duplicate discovery ID')
    signatures = [' '.join(p['question'].lower().split()) for p in candidates]
    require(len(signatures) == len(set(signatures)), 'duplicate discovery question')
    existing = {p.name for p in (root / 'problems').iterdir() if p.is_dir()}
    for p in candidates:
        require(re.fullmatch(r'DISC-\d{8}-\d{3}', p['id']), 'invalid discovery ID')
        require(p['topic'] in topics, 'unknown discovery topic')
        require(p['status'] == 'discovery_lead', 'discovery lead cannot be promoted in place')
        require(p['disposition'] in ['new_candidate', 'update_existing'], 'invalid disposition')
        require(p['sources'] and set(p['sources']) <= bibliography.keys(), 'unknown discovery source')
        require(set(p['existing_problems']) <= existing, 'unknown existing problem')
        require(bool(p['existing_problems']) == (p['disposition'] == 'update_existing'), 'existing-card update must map to a canonical ID')
        for key in ['title', 'known', 'question', 'boundary', 'decisive_test', 'priority_reason', 'audit_limitations']:
            require(isinstance(p[key], str) and p[key].strip(), f'missing discovery field {key}')
        for key in ['theory', 'empirical', 'prediction']:
            require(isinstance(p['evidence'][key], str) and p['evidence'][key].strip(), f'missing discovery evidence {key}')
        require(p['audit_priority'] in ['first', 'second'], 'unknown audit priority')
        if 'scope_review' in p:
            scope = p['scope_review']
            require(scope['decision'] == 'excluded_from_main', 'unknown scope decision')
            require(all(isinstance(scope.get(k), str) and scope[k].strip() for k in ['date', 'basis', 'reason', 'provenance']), 'incomplete scope decision')
        for edge in p['related_leads']:
            require(edge['target'] in all_ids and edge['target'] != p['id'], 'dangling discovery relation')
            require(edge['type'] == 'related_to' and edge['reason'].strip(), 'invalid discovery comparison')
    manifest = read(batch / 'search-manifest.json')
    require(len({x['id'] for x in manifest}) == len(manifest), 'duplicate query batch')
    for x in manifest:
        require(x['queries'] and all(isinstance(q, str) and q.strip() for q in x['queries']), 'empty search query')
    for record in read(root / 'coverage/searches.json'):
        # This batch validates only records that refer to its query manifest.
        if not record.get('query_batches') or not set(record['query_batches']) & {x['id'] for x in manifest}:
            continue
        require(set(record['query_batches']) <= {x['id'] for x in manifest}, 'unknown query batch')
        expected = set(q for x in manifest if x['id'] in record['query_batches'] for q in x['queries'])
        require(set(record['queries']) == expected, 'coverage queries disagree with manifest')
        require(set(record['discovery_leads']) <= set(ids), 'unknown coverage discovery lead')
        matching = [p for p in candidates if p['id'] in record['discovery_leads']]
        require(all(p['topic'] == record['topic'] for p in matching), 'coverage topic disagrees with lead')
        require(set(record['sources']) == {s for p in matching for s in p['sources']}, 'coverage sources disagree with leads')
    triage = read(batch / 'triage.json')
    require(len({x['id'] for x in triage}) == len(triage), 'duplicate triage ID')
    for x in triage:
        require(set(x['sources']) <= bibliography.keys() and set(x['leads']) <= set(ids), 'dangling triage reference')
        require(x['framing'].strip() and x['reason'].strip(), 'empty triage rationale')
    global_manifests = [entry for file in (root / 'discovery').glob('*/search-manifest.json') for entry in read(file)]
    query_ids = [entry['id'] for entry in global_manifests]
    require(len(query_ids) == len(set(query_ids)), 'duplicate query batch across batches')
    metadata = read(batch / 'batch.json') if (batch / 'batch.json').exists() else {}
    metadata['locations'] = {key: ('#'+key.lower() if key in ids else value) for key, value in locations.items()}
    if metadata.get('areas'):
        require(all(p.get('area') in metadata['areas'] for p in candidates), 'unknown discovery area')
        require(set(metadata['areas']) == {p['area'] for p in candidates}, 'area coverage disagrees with leads')
        coverage = read(batch / 'area-coverage.json')
        require(len(coverage) == len(metadata['areas']) and {x['area'] for x in coverage} == set(metadata['areas']), 'area ledger incomplete')
        for row in coverage:
            require(set(row['query_batches']) <= {x['id'] for x in manifest}, 'unknown area query batch')
            matching = [p for p in candidates if p['area'] == row['area']]
            require(set(row['leads']) == {p['id'] for p in matching}, 'area leads disagree')
            require(set(row['sources']) == {s for p in matching for s in p['sources']}, 'area sources disagree')
            require(row['stage'] == 'selected_primary_abstracts' and row['next_search'].strip(), 'invalid area stage or next search')
            require(all(row[key] is False for key in ['full_text_audit', 'citation_closure', 'saturation_measured']), 'discovery cannot certify area completeness')
    return candidates, bibliography, topics, manifest, triage, metadata

def render(candidates, bibliography, topics, manifest, triage, metadata=None):
    metadata = metadata or {}
    nqueries = sum(len(x['queries']) for x in manifest)
    source_ids = {s for c in candidates for s in c['sources']}
    counts = Counter(c['topic'] for c in candidates)
    new = sum(c['disposition'] == 'new_candidate' for c in candidates)
    excluded = [c for c in candidates if c.get('scope_review', {}).get('decision') == 'excluded_from_main']
    active = [c for c in candidates if c not in excluded]
    def refs(ids):
        return '; '.join(f"[{bibliography[s]['title']}]({bibliography[s]['url']})" for s in ids)
    rows = [metadata.get('title', '# Discovery batch 2026 10 01'), '',
            f'{nqueries} search queries in {len(manifest)} query batches; {len(source_ids)} selected primary papers screened at abstract level; {len(candidates)} leads across {len(counts)} topics.', '',
            f'**{new} new candidate leads and {len(candidates)-new} updates to existing cards. None is promoted to a literature-audited open problem.**', '',
            'This is a discovery queue, not the canonical problem catalog. Paper summaries describe author-reported results; questions, boundaries and proposed tests are curator synthesis. Priority means order for deeper auditing, not confidence in novelty or scientific importance.', '',
            '[Canonical catalog](../../INDEX.md) · [Structured leads](candidates.json) · [Exact queries](search-manifest.json) · [Triage log](triage.json)', '',
            '## Method and limits', '',
            'Searches combined foundational titles, recent-work queries, and targeted follow-ups for under-covered areas. Selected arXiv abstract pages were read directly, and citations record the retrieved version. Several search snippets used older titles or claims; current primary pages took precedence. No systematic backward/forward citation traversal, full-text theorem audit, independent experiment, or human scientific review was performed.', '',
            metadata.get('limitations', 'The selection is purposive, English-language, arXiv-heavy and biased toward language-model training. Eight coarse topics touched does not mean the field is covered. Search saturation was not measured. Vision beyond the selected theory examples, multimodal learning, graph learning, contrastive/self-supervised learning, causal/OOD robustness, non-language RL, architecture search and pruning deserve separate search passes. Within each topic, older and competing research communities may be missing.'), '',
            'No raw abstracts, private research logs, or unpublished experimental results are redistributed. AI-assisted discovery and synthesis were checked against primary abstracts by the assistant; human scholarly review remains pending.', '',
            '## Coverage', '', '| Topic | Leads |', '| --- | --- |']
    rows += [f'| {t} | {counts[t]} |' for t in topics]
    if metadata.get('areas'):
        rows += ['', '## Subfield coverage', '',
                 'Each row records selected leads, not completeness or search saturation. See [coverage and remaining gaps](coverage.md).', '',
                 '| Area | Leads |', '| --- | --- |']
        area_counts = Counter(c['area'] for c in candidates)
        rows += [f'| {area} | {area_counts[area]} |' for area in metadata['areas']]
    if excluded:
        rows += ['', f'**Scope update:** counts above describe historical discovery. {len(excluded)} lead is excluded from the main queue; the other {len(active)} remain proposals awaiting scope and scientific review. See [scientific scope](../../docs/SCOPE.md).', '']
    rows += ['', '## Lead index', '', '| Lead | Question family | Triage | Audit order |', '| --- | --- | --- | --- |']
    for c in active:
        rows.append(f"| [{c['id']}](#{c['id'].lower()}) | {c['title']} | {c['disposition']} | {c['audit_priority']} |")
    rows += ['', '## Audit next', '',
             metadata.get('audit_next', 'Start with a small set spanning different kinds of uncertainty: DISC-20261001-001 (known special cases), 009 (different experimental protocols), 012 (measurement definitions), 015 (mechanism identifiability), 022 (existing robustness guarantees), and 024 (theory-to-hardware mapping). This is a proposed reading order, not an authorized experimental queue.'), '',
             'For each, read full texts, trace subsequent citations, seek an existing answer, compare canonical and discovery neighbors, and write a bounded problem card only if the gap survives. Record resolved or narrowed proposals as useful outcomes.', '', '## Lead details', '']
    for c in active + excluded:
        if excluded and c is excluded[0]:
            rows += ['## Archived discoveries outside the main scope', '', 'IDs and evidence remain available for provenance; these are not part of the main candidate queue.', '']
        if c in excluded:
            rows += ['**Scope decision:** ' + c['scope_review']['reason'], '']
        rows += [f"### {c['id']}", '', f"**{c['title']}** · {c['topic']} · {c['disposition']}", '',
                 '**Author-reported starting points.** '+c['known']+' '+refs(c['sources']), '',
                 '**Proposed question.** '+c['question'], '',
                 '**Boundary to audit.** '+c['boundary'], '',
                 '**Proposed decisive test.** '+c['decisive_test'], '',
                 '**Current understanding, scoped to this question.**', '',
                 '- Theory: '+c['evidence']['theory'],
                 '- Empirical: '+c['evidence']['empirical'],
                 '- Prediction: '+c['evidence']['prediction'], '',
                 '**Audit priority.** '+c['audit_priority']+' — '+c['priority_reason'], '']
        if c['existing_problems']:
            rows += ['**Existing card.** '+', '.join(f'[{p}](../../problems/{p}/README.md)' for p in c['existing_problems'])+'. Update these IDs rather than creating duplicates.', '']
        for edge in c['related_leads']:
            rows += [f"**Identity check.** [{edge['target']}]({metadata.get('locations', {}).get(edge['target'], '#'+edge['target'].lower())}): {edge['reason']}", '']
    rows += ['## Rejected or narrowed framings', '']
    for t in triage:
        rows += [f"- **{t['id']} — {t['decision']}:** {t['framing']} {t['reason']}" + (' '+refs(t['sources']) if t['sources'] else '')]
    return '\n'.join(rows)+'\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        for batch in sorted((ROOT/'discovery').iterdir()):
            if not batch.is_dir():
                continue
            output = render(*validate(ROOT, batch))
            path = batch/'README.md'
            if args.check:
                require(path.exists() and path.read_text() == output, f'{path.relative_to(ROOT)} is stale')
            else:
                path.write_text(output)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        parser.exit(1, f'Discovery validation failed: {exc}\n')
    print('Discovery queue validated; reports '+('verified.' if args.check else 'generated.'))

if __name__ == '__main__':
    main()
