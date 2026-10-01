# Focused reading queue: training and generalization

Updated 2026-10-01 following the maintainer's scope clarification. This is assistant-curated reading prioritization, not endorsement of individual questions, a completed literature audit, or a claim that the list is exhaustive. Original questions, source records and stable IDs are preserved.

The three lines organize one agenda: how neural models learn, what they learn, and why it generalizes. Each lead has one primary placement below for navigation; the placement does not assert that the scientific questions are disjoint. Relationships and possible duplicates require comparison of assumptions, observables and interventions.

## Training dynamics

| Lead | Existing question to review |
| --- | --- |
| [001](../discovery/2026-10-01/README.md#disc-20261001-001) | Frozen schedule prediction beyond solved random-feature settings |
| [002](../discovery/2026-10-01/README.md#disc-20261001-002) | A predictive stochastic extension of central flows |
| [003](../discovery/2026-10-01/README.md#disc-20261001-003) | Choosing a batch schedule from preconditioned noise measurements |
| [004](../discovery/2026-10-01/README.md#disc-20261001-004) | Identifiable closure for Adam alignment and momentum |
| [005](../discovery/2026-10-01/README.md#disc-20261001-005) | Finite-scale errors after architecture-specific parameterization |
| [006](../discovery/2026-10-01/README.md#disc-20261001-006) | When a measured loss exponent changes with training |
| [024](../discovery/2026-10-01/README.md#disc-20261001-024) | Which precision law matches the quantization mechanism |
| [025](../discovery/2026-10-01/README.md#disc-20261001-025) | Predicting low-learning-rate stagnation from update resolution |
| [053](../discovery/2026-10-01-expansion/README.md#disc-20261001-053) | Does initial dynamical isometry predict later feature-learning stability? |

## Representation formation

| Lead | Existing question to review |
| --- | --- |
| [009](../discovery/2026-10-01/README.md#disc-20261001-009) | When repetition helps and when duplication wastes compute |
| [010](../discovery/2026-10-01/README.md#disc-20261001-010) | Predicting curriculum effects from cross-difficulty transfer |
| [012](../discovery/2026-10-01/README.md#disc-20261001-012) | Representation collapse under contextual and imbalanced labels |
| [027](../discovery/2026-10-01-expansion/README.md#disc-20261001-027) | Predicting partial collapse in non-contrastive self-supervision |
| [028](../discovery/2026-10-01-expansion/README.md#disc-20261001-028) | When augmentation helps semantics and when it destroys them |
| [036](../discovery/2026-10-01-expansion/README.md#disc-20261001-036) | Forecasting loss of plasticity before performance stalls |
| [039](../discovery/2026-10-01-expansion/README.md#disc-20261001-039) | From sparse-network existence to inexpensive findability |

## Generalization mechanisms

| Lead | Existing question to review |
| --- | --- |
| [008](../discovery/2026-10-01/README.md#disc-20261001-008) | Predicting beneficial data transfer beyond aligned covariance models |
| [011](../discovery/2026-10-01/README.md#disc-20261001-011) | Distinguishing mechanisms of delayed generalization |
| [013](../discovery/2026-10-01/README.md#disc-20261001-013) | Predicting benign versus tempered overfitting under feature learning |
| [030](../discovery/2026-10-01-expansion/README.md#disc-20261001-030) | Predicting the robust–standard accuracy frontier |
| [050](../discovery/2026-10-01-expansion/README.md#disc-20261001-050) | Can invariant curvature predict generalization across training regimes? |
| [051](../discovery/2026-10-01-expansion/README.md#disc-20261001-051) | Finite-time implicit bias beyond separable small-step dynamics |
| [060](../discovery/2026-10-01-expansion/README.md#disc-20261001-060) | Predicting compositional generalization beyond designed splits |

## What happens to the other leads?

All existing canonical cards remain candidates. The three seed cards concern schedule-to-loss laws, Adam state closure, and scale transfer, and fit this focus.

The 23 discovery leads above form the active reading set. The other 42 non-excluded leads remain background or possible case studies; they are deferred from the active queue, not judged solved or uninteresting. Lead 066 remains explicitly excluded in its model-selection framing. These three sets account for all 66 historical records without deleting or renumbering them.

For example, diffusion memorization, multimodal competition, graph message passing or continual learning can be useful settings for a shared mechanism. They should enter when they resolve a specific question in the main agenda, rather than triggering a separate breadth campaign. Inference-budget policies, deployment allocation, generic coverage guarantees and application winner selection do not become core problems merely because a neural model is involved.

Historical batch audit priorities and per-area “next searches” are superseded by this queue. Their records remain intact as search provenance. No scientific maturity labels change through this editorial decision.

## Next review pass

Start with six leads: **001** (schedule-to-loss laws), **004** (Adam state closure), **027** (representation collapse), **036** (loss of plasticity), **013** (noise and feature-learning generalization), and **051** (finite-time implicit bias). These are a manageable first pass across the three lines, not six newly verified open problems.

For each, read the closest primary papers in full, map their assumptions and conclusions, search for subsequent answers and counterexamples, and compare adjacent leads before adding a canonical card. Keep a problem only when the target quantity, existing explanation, unresolved boundary and discriminating test are explicit. Measure progress by clarified questions and understanding, not by the number of topics or papers collected.
