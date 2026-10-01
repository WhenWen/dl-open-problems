# Discovery queue

Batch searches generate leads before full problem-card review. An entry here is a proposed research question, not a claim that the literature has no answer.

**Scope:** model training and generalization, organized around training dynamics, representation formation and generalization mechanisms. Start with the [focused reading queue](../docs/TRAINING_GENERALIZATION.md) and [admission criteria](../docs/SCOPE.md). Historical search breadth is background, not the active agenda.

| Batch | Queries | Primary abstracts screened | New leads | Existing-card updates |
| --- | --- | --- | --- | --- |
| [2026 10 01](2026-10-01/README.md) | 50 | 57 | 23 | 3 |
| [2026 10 01 breadth expansion](2026-10-01-expansion/README.md) · [中文](2026-10-01-expansion/README.zh-CN.md) | 61 | 94 | 40 | 0 |
| Total | 111 | 151 unique papers | 63 | 3 |

See each batch for exact queries, source versions, current understanding, proposed tests, identity comparisons and excluded framings. Review selected leads in full before adding canonical cards. Edit JSON records and run `python3 scripts/discovery.py` to regenerate detailed reports.

The expansion has a [24-subfield coverage ledger](2026-10-01-expansion/coverage.md), including explicit next searches and areas still without dedicated passes. Counts are not completeness estimates. The bibliography also retains three original seed references, for 154 total source records.
