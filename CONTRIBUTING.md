# Contributing

Contribute problems, answers, corrections, replications, and coverage audits. Discovering that a proposed problem is already solved is a valuable contribution.

## Issues first or a direct pull request

1. Check the [scientific scope](docs/SCOPE.md): explain the training or generalization mechanism and scientific payoff, beyond selecting a best method. Use the [focused queue](docs/TRAINING_GENERALIZATION.md) before opening a new domain track. Search the index, existing cards, issues, and closed issues using synonyms.
2. Use an issue form for a candidate or evidence update. You do not need a complete literature review to propose a candidate.
3. For a new card, copy `templates/problem` into `problems/DLOP-NNNN`. Use the next unused number provisionally; the maintainer resolves simultaneous ID collisions before merge. Published IDs are never reused.
4. Fill both files. Add primary references to `bibliography.json`, reusing existing source IDs. Record the exact reading depth. Do not mark a source full-text reviewed after reading only its abstract.
5. Compare nearby cards and add justified relations. Add a coverage record for any search actually performed. Unperformed work is an explicit next step, never a completed audit.
6. Run the README commands and include generated `INDEX.md` changes in the PR.

## Evidence and attribution

Cite specific sections, equations, figures, or theorem assumptions for substantive claims. Separate authors' results, your interpretation, and proposed hypotheses. Do not claim universal applicability from a successful special case. Record source versions and an as-of date; a lack of search results is not proof of novelty.

Summarize papers in your own words and link to primary sources. Only contribute text, code and artifacts you have permission to share; do not upload paper PDFs, private logs, credentials or unpublished third-party material. Link large experimental artifacts instead of committing them.

AI-assisted contributions are welcome. Disclose assistance and the verification performed in the PR. Contributors are responsible for checking every citation and claim. Large unaudited generated lists should remain proposals rather than being merged as reviewed problems.

By contributing, you agree to license your original contribution under the repository MIT license. Add your public name or handle to the card contributors when making substantive changes; Git history also preserves attribution. Do not add others as endorsers without their agreement.

## Updating or resolving a problem

An evidence PR must name the exact setting it addresses. A toy-model answer may resolve a subproblem without resolving the practical question. For state changes, merges and exclusions, add a dated entry to `reviews/decisions.json` and follow the review checklist. For a merge, keep the old card with `status: merged` and a `canonical_id`; update inbound relations. Never delete an ID to make the catalog look cleaner.

## Batch discovery

Large searches belong in `discovery/YYYY-MM-DD/` as leads with explicit reading depth. They do not create canonical problem IDs automatically. Keep exact queries, versioned primary references, identity comparisons and rejected framings. Use the current batch as a schema example, and run `python3 scripts/discovery.py` followed by `python3 scripts/discovery.py --check`. Extend this script when introducing new batch conventions; do not silently drop provenance validation. Follow-up searches should use globally unique query-batch IDs.

A lead can map to an existing card or propose a new one. Promotion requires a separate scoped review; moving a lead into `problems/` does not establish novelty. AI assistance and the absence or presence of human review must be stated.
