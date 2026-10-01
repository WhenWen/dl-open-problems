# Problem index

Generated from structured metadata. Edit cards and search records, then run `python3 scripts/catalog.py`.

Candidate means an incomplete literature audit, not a verified open problem.

[Batch discovery queue](discovery/README.md) contains additional leads awaiting deeper review and is not counted as canonical cards.

| ID | Question | Status | Topics | Last checked |
| --- | --- | --- | --- | --- |
| DLOP-0001 | [Predicting loss under unseen learning rate schedules](problems/DLOP-0001/README.md) | candidate | optimization | 2026-10-01 |
| DLOP-0002 | [Closing Adam norm and momentum dynamics with few states](problems/DLOP-0002/README.md) | candidate | optimization | 2026-10-01 |
| DLOP-0003 | [Predicting the limits of simultaneous scale transfer](problems/DLOP-0003/README.md) | candidate | scaling, precision | 2026-10-01 |

## Coverage

A tagged card is not proof that its topic was searched. Open the [ledger](coverage/searches.json) for methods and limitations.

| Topic | Cards | Recorded searches |
| --- | --- | --- |
| optimization | DLOP-0001, DLOP-0002 | SEARCH-0001, SEARCH-0003, SEARCH-B2-001 |
| scaling | DLOP-0003 | SEARCH-0002, SEARCH-0004, SEARCH-B2-002 |
| data | None | SEARCH-0005, SEARCH-B2-003 |
| representation-generalization | None | SEARCH-0006, SEARCH-B2-004 |
| in-context-learning | None | SEARCH-0007 |
| generative-models | None | SEARCH-0008, SEARCH-B2-005 |
| post-training | None | SEARCH-0009, SEARCH-B2-006 |
| precision | DLOP-0003 | SEARCH-0010 |

## Relationships

Edges are proposals with explicit rationales, not automated equivalence judgments.

- DLOP-0001 → related_to → DLOP-0002: Predictive state closure is one possible route, not a necessary component of every schedule law.
- DLOP-0002 → related_to → DLOP-0001: State prediction can support loss prediction but is a distinct test from fitting loss using observed states.
