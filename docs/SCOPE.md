# Scientific scope

The main collection seeks mechanisms and predictive laws of deep learning. An entry should explain what solving it would teach us about learned representations, optimization dynamics, architectural composition, parameterization, overparameterization, or their interaction with data. Having prior papers, a benchmark gap and a possible theorem is not enough.

## Admission criteria

A proposed problem should identify all of the following:

1. A specific phenomenon in neural learning, with an observable and a controlled intervention.
2. The neural mechanism or structural property whose role is unresolved. Examples include feature learning, coupled parameter and optimizer states, compositional depth, representation geometry, learned routing, or finite-width departures from a tractable limit.
3. A scientific payoff beyond selecting a winning method: an explanation, identifiable dynamics, a necessity/sufficiency boundary, or a quantitative prediction across controlled regimes.
4. Prior explanations and the assumptions that may fail in the target regime, together with a test that distinguishes them.

A useful diagnostic is to replace the neural network with an arbitrary black-box predictor. If the question and its intended answer barely change, it probably belongs to general statistics, decision theory or application methodology rather than this collection's main scope. This is a diagnostic, not a ban on phenomena shared with simpler models: linear, kernel and logistic models can be essential controlled limits for understanding what changes during neural feature learning.

Naming gradients, norms or a neural architecture does not itself establish a mechanistic contribution. A mechanism should have observable consequences that can fail a test. A theorem in a toy setting is valuable when the bridge to the neural phenomenon is explicit.

## Examples

| Broad framing | Scope judgment | A possible mechanistic direction, subject to its own review |
| --- | --- | --- |
| Which dataset favors trees, ordinary NNs or a tabular foundation model? | Model-family selection; outside the main scope as currently framed. | How does learned feature geometry interact with target-function structure to produce a specific optimization or generalization transition? This is a different question, not a cosmetic rename. |
| Which LR schedule gives the lowest loss? | A tuning objective by itself. | What dynamical state makes the response to a schedule predictable, and can a law recover constant and decay cases without refitting each run? |
| Which pruning method wins? | Method ranking by itself. | Why does early dense training make a sparse subnetwork trainable, and which dynamics distinguish existence from learnability? |
| Which architecture performs best on graphs? | Model selection by itself. | How do message passing, nonlinear feature learning and topology jointly preserve or destroy task-relevant information? |

These are editorial examples, not claims that the proposed mechanisms are correct or open in every setting. Domain specificity is not a reason for rejection. Graphs, vision, scientific computing, multimodal learning and RL can expose fundamental neural mechanisms.

## Reassessment of the discovery queue

On 2026-10-01 the maintainer clarified that breadth should stay within problems intrinsic to deep learning and identified DISC-20261001-066 as uninteresting in its model-selection form. That lead is excluded from the main queue. Its ID, sources, search history and original question remain available as an archived discovery record. The field of tabular learning is not excluded.

The following are an assistant-authored watchlist, not additional maintainer rejection decisions or completed scientific reviews:

| Lead | Why its current framing needs scrutiny | Mechanistic requirement before main-scope endorsement |
| --- | --- | --- |
| [007](../discovery/2026-10-01/README.md#disc-20261001-007) | Deployment workload and compute allocation can be operations research. | Identify the neural training/inference dynamics that create the resource frontier. |
| [023](../discovery/2026-10-01/README.md#disc-20261001-023) | Inference stopping can remain a generic sequential decision problem. | Isolate a property of learned reasoning or verifier representations that explains the frontier. |
| [047](../discovery/2026-10-01-expansion/README.md#disc-20261001-047) | Privacy accounting and budget selection are not by themselves neural mechanisms. | Explain how clipping and injected noise change feature learning or optimization, beyond utility tuning. |
| [049](../discovery/2026-10-01-expansion/README.md#disc-20261001-049) | Conditional coverage can apply to any black-box predictor. | Establish a necessary role for learned representation geometry; otherwise keep it as adjacent statistical background. |
| [054](../discovery/2026-10-01-expansion/README.md#disc-20261001-054) | Communication scheduling can be a generic distributed optimization problem. | Connect the effect to neural feature drift or representation alignment across clients. |
| [059](../discovery/2026-10-01-expansion/README.md#disc-20261001-059) | Designing a deletion test is an evaluation task by itself. | Explain neural memory organization and how an intervention actually changes it. |
| [061](../discovery/2026-10-01-expansion/README.md#disc-20261001-061) | Statistical detection power can be independent of deep learning. | Identify how neural density or representation learning produces the semantic/statistical mismatch. |

The rest of the queue is not automatically endorsed by omission from this watchlist. Research scope, literature novelty, evidence maturity and audit priority are separate judgments. Broader search results can remain useful background without increasing the main problem count.
