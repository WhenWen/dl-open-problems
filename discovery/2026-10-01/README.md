# Discovery batch 2026 10 01

50 search queries in 17 query batches; 57 selected primary papers screened at abstract level; 26 leads across 8 topics.

**23 new candidate leads and 3 updates to existing cards. None is promoted to a literature-audited open problem.**

This is a discovery queue, not the canonical problem catalog. Paper summaries describe author-reported results; questions, boundaries and proposed tests are curator synthesis. Priority means order for deeper auditing, not confidence in novelty or scientific importance.

[Canonical catalog](../../INDEX.md) · [Structured leads](candidates.json) · [Exact queries](search-manifest.json) · [Triage log](triage.json)

## Method and limits

Searches combined foundational titles, recent-work queries, and targeted follow-ups for under-covered areas. Selected arXiv abstract pages were read directly, and citations record the retrieved version. Several search snippets used older titles or claims; current primary pages took precedence. No systematic backward/forward citation traversal, full-text theorem audit, independent experiment, or human scientific review was performed.

The selection is purposive, English-language, arXiv-heavy and biased toward language-model training. Eight coarse topics touched does not mean the field is covered. Search saturation was not measured. Vision beyond the selected theory examples, multimodal learning, graph learning, contrastive/self-supervised learning, causal/OOD robustness, non-language RL, architecture search and pruning deserve separate search passes. Within each topic, older and competing research communities may be missing.

No raw abstracts, private research logs, or unpublished experimental results are redistributed. AI-assisted discovery and synthesis were checked against primary abstracts by the assistant; human scholarly review remains pending.

## Coverage

| Topic | Leads |
| --- | --- |
| optimization | 4 |
| scaling | 3 |
| data | 3 |
| representation-generalization | 4 |
| in-context-learning | 3 |
| generative-models | 3 |
| post-training | 3 |
| precision | 3 |

## Lead index

| Lead | Question family | Triage | Audit order |
| --- | --- | --- | --- |
| [DISC-20261001-001](#disc-20261001-001) | Frozen schedule prediction beyond solved random-feature settings | update_existing | first |
| [DISC-20261001-002](#disc-20261001-002) | A predictive stochastic extension of central flows | new_candidate | first |
| [DISC-20261001-003](#disc-20261001-003) | Choosing a batch schedule from preconditioned noise measurements | new_candidate | second |
| [DISC-20261001-004](#disc-20261001-004) | Identifiable closure for Adam alignment and momentum | update_existing | first |
| [DISC-20261001-005](#disc-20261001-005) | Finite-scale errors after architecture-specific parameterization | update_existing | first |
| [DISC-20261001-006](#disc-20261001-006) | When a measured loss exponent changes with training | new_candidate | first |
| [DISC-20261001-007](#disc-20261001-007) | Compute allocation when the deployment workload changes | new_candidate | second |
| [DISC-20261001-008](#disc-20261001-008) | Predicting beneficial data transfer beyond aligned covariance models | new_candidate | first |
| [DISC-20261001-009](#disc-20261001-009) | When repetition helps and when duplication wastes compute | new_candidate | first |
| [DISC-20261001-010](#disc-20261001-010) | Predicting curriculum effects from cross-difficulty transfer | new_candidate | first |
| [DISC-20261001-011](#disc-20261001-011) | Distinguishing mechanisms of delayed generalization | new_candidate | first |
| [DISC-20261001-012](#disc-20261001-012) | Representation collapse under contextual and imbalanced labels | new_candidate | first |
| [DISC-20261001-013](#disc-20261001-013) | Predicting benign versus tempered overfitting under feature learning | new_candidate | second |
| [DISC-20261001-014](#disc-20261001-014) | Forecasting forgetting from evolving task geometry | new_candidate | second |
| [DISC-20261001-015](#disc-20261001-015) | Identifying the algorithm behind in-context predictions | new_candidate | first |
| [DISC-20261001-016](#disc-20261001-016) | Task diversity and the boundary of in-context generalization | new_candidate | first |
| [DISC-20261001-017](#disc-20261001-017) | Predicting failures to combine dispersed context evidence | new_candidate | second |
| [DISC-20261001-018](#disc-20261001-018) | Guidance schedules with finite-dimensional score error | new_candidate | second |
| [DISC-20261001-019](#disc-20261001-019) | A quantitative boundary between diffusion generalization and memorization | new_candidate | first |
| [DISC-20261001-020](#disc-20261001-020) | Making diffusion error decompositions operational | new_candidate | first |
| [DISC-20261001-021](#disc-20261001-021) | Distinguishing reasoning acquisition from probability reweighting | new_candidate | first |
| [DISC-20261001-022](#disc-20261001-022) | Observable warning signals for preference overoptimization | new_candidate | first |
| [DISC-20261001-023](#disc-20261001-023) | Adaptive inference budgets with imperfect verifiers | new_candidate | second |
| [DISC-20261001-024](#disc-20261001-024) | Which precision law matches the quantization mechanism | new_candidate | first |
| [DISC-20261001-025](#disc-20261001-025) | Predicting low-learning-rate stagnation from update resolution | new_candidate | first |
| [DISC-20261001-026](#disc-20261001-026) | Precision allocation after scale-stable initialization | new_candidate | second |

## Audit next

Start with a small set spanning different kinds of uncertainty: DISC-20261001-001 (known special cases), 009 (different experimental protocols), 012 (measurement definitions), 015 (mechanism identifiability), 022 (existing robustness guarantees), and 024 (theory-to-hardware mapping). This is a proposed reading order, not an authorized experimental queue.

For each, read full texts, trace subsequent citations, seek an existing answer, compare canonical and discovery neighbors, and write a bounded problem card only if the gap survives. Record resolved or narrowed proposals as useful outcomes.

## Lead details

### DISC-20261001-001

**Frozen schedule prediction beyond solved random-feature settings** · optimization · update_existing

**Author-reported starting points.** Functional-scaling and random-feature analyses already derive optimal schedules with task-dependent regimes. A September 2026 preprint also studies joint learning-rate and batch-size effects using spectral response components. [Optimal Learning Rate Schedules under Functional Scaling Laws: Power Decay and Warmup-Stable-Decay](https://arxiv.org/abs/2602.06797v3); [Theory of Optimal Learning Rate Schedules and Scaling Laws for a Random Feature Model](https://arxiv.org/abs/2602.04774v2); [From Spectra to Joint Schedules in LLM Pre-training: 3+3(+2) Scaling-Law Regimes](https://arxiv.org/abs/2609.40148v1)

**Proposed question.** Can a law calibrated on a few AdamW language-model runs predict complete held-out schedule curves and identify the regime in which its prediction is valid?

**Boundary to audit.** The existence of optimal schedules in controlled SGD models is already addressed. The candidate gap is identifiable, quantitative transfer to adaptive optimization and feature learning, not the absence of any schedule theory.

**Proposed decisive test.** Reproduce a published special case, then hold out schedules and horizons in a fixed neural architecture. Freeze parameter fitting before the target run and report systematic residuals against seed variation.

**Current understanding, scoped to this question.**

- Theory: Analytical solutions and phase regimes are reported for specified surrogate models.
- Empirical: The papers report numerical tests; one includes controlled nanoGPT experiments.
- Prediction: Cross-schedule transfer is already studied; its precise AdamW and feature-learning envelope needs auditing.

**Audit priority.** first — Recent work could substantially narrow the existing card.

**Existing card.** [DLOP-0001](../../problems/DLOP-0001/README.md). Update these IDs rather than creating duplicates.

**Identity check.** [DISC-20261001-006](#disc-20261001-006): Schedule transfer and exponent identification have different targets.

### DISC-20261001-002

**A predictive stochastic extension of central flows** · optimization · new_candidate

**Author-reported starting points.** Central flows model time-averaged optimization trajectories in deterministic neural-network training, including adaptive-optimizer behavior. [Understanding Optimization in Deep Learning with Central Flows](https://arxiv.org/abs/2410.24206v2)

**Proposed question.** Which stochastic corrections let a coarse-grained flow forecast averaged loss and stability boundaries for a specified minibatch AdamW training setup?

**Boundary to audit.** Deterministic trajectory prediction is an existing result. Minibatch noise, momentum and preconditioner evolution must be introduced explicitly rather than assumed covered.

**Proposed decisive test.** Compare full-batch and matched minibatch runs on the same problem. Fit any correction on one batch size and predict another, measuring both averaged loss and oscillation envelopes.

**Current understanding, scoped to this question.**

- Theory: Deterministic coarse-grained dynamics are developed in the cited work.
- Empirical: Numerical trajectory agreement is reported in the tested networks.
- Prediction: The minibatch AdamW target in this proposal has not been audited.

**Audit priority.** first — One tractable change of setting with observable trajectories.

**Identity check.** [DISC-20261001-004](#disc-20261001-004): A coarse-grained trajectory is not the same object as a module-statistic closure.

### DISC-20261001-003

**Choosing a batch schedule from preconditioned noise measurements** · optimization · new_candidate

**Author-reported starting points.** Gradient noise scale predicts useful batch size empirically; newer surrogate analyses study joint batch and learning-rate schedules. [An Empirical Model of Large-Batch Training](https://arxiv.org/abs/1812.06162v1); [Theory of Optimal Learning Rate Schedules and Scaling Laws for a Random Feature Model](https://arxiv.org/abs/2602.04774v2); [From Spectra to Joint Schedules in LLM Pre-training: 3+3(+2) Scaling-Law Regimes](https://arxiv.org/abs/2609.40148v1)

**Proposed question.** Can early measurements of preconditioned signal and noise select a compute-efficient batch schedule for AdamW without tuning every target schedule?

**Boundary to audit.** Useful parallelism, token efficiency and wall-clock efficiency are different objectives. A result for SGD noise is not automatically a rule for adaptive updates.

**Proposed decisive test.** Hold tokens and compute accounting fixed, measure throughput separately, and predict the useful-batch transition on held-out learning rates. Compare scalar noise scale with preconditioned diagnostics.

**Current understanding, scoped to this question.**

- Theory: Noise-based models and solvable schedule analyses exist.
- Empirical: Large-batch behavior has been measured across multiple domains.
- Prediction: A universal unpreconditioned noise rule is not assumed; calibration and transfer need review.

**Audit priority.** second — Potentially valuable, but needs careful hardware and optimizer controls.

**Identity check.** [DISC-20261001-001](#disc-20261001-001): Joint batch control adds an intervention beyond schedule-only prediction.

### DISC-20261001-004

**Identifiable closure for Adam alignment and momentum** · optimization · update_existing

**Author-reported starting points.** Adam-style and Gauss-Newton preconditioning behave differently with basis choice and minibatch noise in controlled objectives. Small-learning-rate SGD studies also delimit when momentum provides little benefit. [Adam or Gauss-Newton? A Comparative Study In Terms of Basis Alignment and SGD Noise](https://arxiv.org/abs/2510.13680v2); [The Marginal Value of Momentum for Small Learning Rate SGD](https://arxiv.org/abs/2307.15196v2)

**Proposed question.** Which few module statistics are enough to forecast norms and update alignment for actual EMA AdamW under a changed schedule?

**Boundary to audit.** An Adam-style theoretical preconditioner must not be silently identified with every implementation of EMA AdamW. Momentum conclusions for small-step SGD are not universal statements about Adam.

**Proposed decisive test.** First compare a controlled regression model with exact observable dynamics, then add EMA preconditioning and feature learning one at a time. Forecast held-out norm trajectories rather than feed in their future values.

**Current understanding, scoped to this question.**

- Theory: Controlled-objective results distinguish noise and geometry; precise optimizer definitions require full-text review.
- Empirical: The papers include experiments, not a validated general module-level closure.
- Prediction: No closed, identifiable module predictor is established by this abstract screening.

**Audit priority.** first — Directly sharpens what the existing norm-state question must demonstrate.

**Existing card.** [DLOP-0002](../../problems/DLOP-0002/README.md). Update these IDs rather than creating duplicates.

### DISC-20261001-005

**Finite-scale errors after architecture-specific parameterization** · scaling · update_existing

**Author-reported starting points.** Deep-linear dynamics, unit-scaled parametrization, MoE scale-stable parametrization and GQA scaling prescriptions already address several extensions beyond basic width transfer. [Deep Linear Network Training Dynamics from Random Initialization: Data, Width, Depth, and Hyperparameter Transfer](https://arxiv.org/abs/2502.02531v3); [u-$\mu$P: The Unit-Scaled Maximal Update Parametrization](https://arxiv.org/abs/2407.17465v3); [How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization](https://arxiv.org/abs/2605.14200v1); [GQA-{\mu}P: The maximal parameterization update for grouped query attention](https://arxiv.org/abs/2605.15290v1)

**Proposed question.** After implementing the appropriate prescription, can small runs predict finite-scale tuning regret when depth, routing structure or precision also changes?

**Boundary to audit.** Do not list the derivation of any MoE or GQA transfer rule as wholly unsolved. Separate implementation errors, asymptotic prescriptions and quantitative finite-scale residuals.

**Proposed decisive test.** Reproduce the matching architecture-specific baseline and its scaling diagnostics before varying two axes jointly. Estimate tuning regret with direct target tuning on a small validation subset.

**Current understanding, scoped to this question.**

- Theory: Architecture-specific limiting analyses and scaling prescriptions are reported.
- Empirical: Transfer experiments exist in the cited architecture families.
- Prediction: A finite-scale error predictor for a declared joint intervention remains a candidate to audit.

**Audit priority.** first — The initial card is too broad without these newer answers.

**Existing card.** [DLOP-0003](../../problems/DLOP-0003/README.md). Update these IDs rather than creating duplicates.

**Identity check.** [DISC-20261001-026](#disc-20261001-026): Scale transfer changes model size; module precision allocation changes numerical policy.

### DISC-20261001-006

**When a measured loss exponent changes with training** · scaling · new_candidate

**Author-reported starting points.** Empirical language-model power laws coexist with surrogate theories in which spectral structure, schedules and feature-learning regimes change learning curves. [From Spectra to Joint Schedules in LLM Pre-training: 3+3(+2) Scaling-Law Regimes](https://arxiv.org/abs/2609.40148v1); [Deep Linear Network Training Dynamics from Random Initialization: Data, Width, Depth, and Hyperparameter Transfer](https://arxiv.org/abs/2502.02531v3); [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361v1)

**Proposed question.** Can early observable statistics distinguish a genuinely changing asymptotic exponent from finite-horizon mixtures of learning and noise components?

**Boundary to audit.** A fitted exponent is not necessarily an intrinsic constant of a dataset. Statistical identifiability of competing curve forms must be addressed before assigning a mechanism.

**Proposed decisive test.** Fit several theoretically motivated forms on identical early windows, freeze long-horizon predictions, and test sensitivity to additive floors, schedules and window length on synthetic and neural models.

**Current understanding, scoped to this question.**

- Theory: Controlled spectral and deep-linear models provide alternative mechanisms.
- Empirical: Power-law behavior is empirically established in specific ranges.
- Prediction: Separating mechanisms from finite-window fit ambiguity is not completed here.

**Audit priority.** first — A clear prediction-versus-identification problem connecting several literatures.

### DISC-20261001-007

**Compute allocation when the deployment workload changes** · scaling · new_candidate

**Author-reported starting points.** Pretraining scaling studies allocate model size and tokens under training budgets. Test-time compute work finds allocation depends on prompt difficulty and inference strategy. [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361v1); [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556v1); [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314v1)

**Proposed question.** Given a specified deployment-query distribution and expected query volume, can a small calibration portfolio choose model size, training tokens and inference budget jointly?

**Boundary to audit.** Training-only compute optimality and total lifecycle optimality have different objectives. This search does not claim that joint-allocation literature is absent.

**Proposed decisive test.** Compare training-only and workload-aware allocation on held-out query mixtures using the same total compute convention. Include verifier and failed-sample costs.

**Current understanding, scoped to this question.**

- Theory: Empirical scaling and inference-allocation frameworks exist; complete related-work review is pending.
- Empirical: Separate components have experimental support.
- Prediction: A portable lifecycle decision rule is a candidate; prioritize searching existing answers before experiments.

**Audit priority.** second — Broad literature likely contains partial or complete answers under additional terminology.

**Identity check.** [DISC-20261001-023](#disc-20261001-023): Lifecycle allocation chooses training investment; inference stopping conditions on a fixed model.

### DISC-20261001-008

**Predicting beneficial data transfer beyond aligned covariance models** · data · new_candidate

**Author-reported starting points.** Data Mixing Laws predicts performance across empirical mixtures. Recent high-dimensional regression theory specifies when auxiliary data can improve scaling rates under covariance and target assumptions. [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://arxiv.org/abs/2403.16952v2); [When do data mixtures improve scaling laws? Insights from high-dimensional regression](https://arxiv.org/abs/2609.38011v1)

**Proposed question.** Can measurable source-target statistics predict whether adding a new domain improves target learning when representations change and the domains do not share a regression function?

**Boundary to audit.** The regression result already answers meaningful special cases. Qualitative agreement of LM experiments does not by itself identify the quantities needed for numerical prediction.

**Proposed decisive test.** Begin with the theory-supported case, then independently perturb covariance alignment and target agreement. Freeze a predictor before neural-domain mixture tests.

**Current understanding, scoped to this question.**

- Theory: Minimax and ridge-regression analyses are reported under explicit structures.
- Empirical: Empirical mixing laws and qualitative LM comparisons exist.
- Prediction: Transfer outside shared-target or aligned settings needs precise audit.

**Audit priority.** first — A concrete theory-to-practice assumption boundary with a new primary paper.

**Identity check.** [DISC-20261001-009](#disc-20261001-009): Changing domain composition and changing duplicate concentration are different interventions.

### DISC-20261001-009

**When repetition helps and when duplication wastes compute** · data · new_candidate

**Author-reported starting points.** Data-limited pretraining, domain repetition, internal duplicate injection and long-CoT SFT report different effects of repeated examples under different budgets and objectives. [Scaling Data-Constrained Language Models](https://arxiv.org/abs/2305.16264v5); [Scaling Domain Data Repetition in LLM Pretraining](https://arxiv.org/abs/2608.14071v1); [Internal Data Repetition Destroys Language Models](https://arxiv.org/abs/2606.24998v1); [Data Repetition Beats Data Scaling in Long-CoT Supervised Fine-Tuning](https://arxiv.org/abs/2602.11149v2)

**Proposed question.** Can a model of exposure structure, task alignment and optimization progress predict the sign and size of repetition effects in a specified training regime?

**Boundary to audit.** These findings are not automatically contradictory: whole-corpus epochs, repeated subsets, domain dilution and SFT are distinct interventions. Equal updates need not mean equal tokens or compute.

**Proposed decisive test.** Use one fixed model and objective to vary duplicate concentration and epoch count with matched tokens and compute; only then test transfer to SFT. Separate exact duplicates from semantically related samples.

**Current understanding, scoped to this question.**

- Theory: A misspecified-regression account of a duplication peak is reported; other lines are primarily empirical.
- Empirical: Several distinct repetition protocols have measured effects.
- Prediction: A joint predictor is a proposed synthesis, not a demonstrated unsolved theorem.

**Audit priority.** first — Apparent disagreement can be narrowed into controlled, useful questions.

**Identity check.** [DISC-20261001-010](#disc-20261001-010): Exposure multiplicity differs from ordering a fixed multiset.

### DISC-20261001-010

**Predicting curriculum effects from cross-difficulty transfer** · data · new_candidate

**Author-reported starting points.** Curriculum studies report scale-dependent optimization effects and no universally best ordering; recent work proposes relative-transfer measurements to guide sampling. [Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics](https://arxiv.org/abs/2601.21698v2); [What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning](https://arxiv.org/abs/2510.19099v2); [Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics](https://arxiv.org/abs/2608.17268v1)

**Proposed question.** Can transfer measurements taken before or early in training forecast which ordering helps, holding sample selection and exposure counts fixed?

**Boundary to audit.** Adaptive resampling changes exposure as well as order. A useful dynamic sampler does not automatically provide an early predictive law for a fixed multiset.

**Proposed decisive test.** Permute the same multiset, match learning-rate schedules and token budgets, and compare frozen early transfer estimates with an online oracle. Track when the transfer matrix changes.

**Current understanding, scoped to this question.**

- Theory: Optimization-dynamics explanations and a transfer-based sampling rule are reported; a quantitative theory audit remains pending.
- Empirical: Pretraining and reasoning post-training studies exist.
- Prediction: The target is early prediction rather than retrospective characterization or unrestricted adaptive resampling.

**Audit priority.** first — A clean intervention can separate common confounds.

### DISC-20261001-011

**Distinguishing mechanisms of delayed generalization** · representation-generalization · new_candidate

**Author-reported starting points.** Lazy-to-rich feature learning and numerical/logit-scaling effects each explain delayed generalization in studied grokking settings. [Grokking as the Transition from Lazy to Rich Training Dynamics](https://arxiv.org/abs/2310.06110v3); [Grokking at the Edge of Numerical Stability](https://arxiv.org/abs/2501.04697v2)

**Proposed question.** Can early diagnostics predict which mechanism controls generalization timing in a new controlled task and initialization regime?

**Boundary to audit.** These mechanisms can coexist and the papers need not disagree. Delayed test generalization is not interchangeable with an arbitrary bend in training loss.

**Proposed decisive test.** Cross precision changes with feature-learning controls while preserving the task. Predict timing before running long trajectories and quantify seed uncertainty.

**Current understanding, scoped to this question.**

- Theory: A controlled regression mechanism and numerical-stability account are available.
- Empirical: Interventions and task experiments support aspects of both accounts.
- Prediction: Cross-setting onset prediction and mechanism identification remain to be audited.

**Audit priority.** first — Competing explanations can be distinguished with modest interventions.

**Identity check.** [DISC-20261001-012](#disc-20261001-012): Delayed generalization timing and terminal representation geometry are distinct outcomes.

### DISC-20261001-012

**Representation collapse under contextual and imbalanced labels** · representation-generalization · new_candidate

**Author-reported starting points.** Layer-peeled models analyze minority collapse. LM studies investigate collapse-like geometry, while a recent preprint emphasizes retained context information and variance floors. [Exploring Deep Neural Networks via Layer-Peeled Model: Minority Collapse in Imbalanced Training](https://arxiv.org/abs/2101.12699v3); [Linguistic Collapse: Neural Collapse in (Large) Language Models](https://arxiv.org/abs/2405.17767v3); [Neural Collapse Is Forbidden: Information Floors in Language Models](https://arxiv.org/abs/2607.09487v1)

**Proposed question.** For a specified token or semantic partition, what representation geometry is predicted when class imbalance, contextual label uncertainty and dimension all matter?

**Boundary to audit.** Class means, token identities and semantic categories are different partitions. An information floor and partial collapse metrics may be compatible, not a direct contradiction.

**Proposed decisive test.** Use identical partitions and centering conventions to reproduce the metrics, then vary imbalance and conditional ambiguity separately in a controllable next-token task.

**Current understanding, scoped to this question.**

- Theory: Analytical surrogate results and information-floor claims exist; the newer claims require full-text scrutiny.
- Empirical: Empirical LM geometry has been studied using differing definitions.
- Prediction: A shared measurable prediction requires reconciling definitions first.

**Audit priority.** first — A measurement and assumption audit should precede new experiments.

### DISC-20261001-013

**Predicting benign versus tempered overfitting under feature learning** · representation-generalization · new_candidate

**Author-reported starting points.** Lazy-training theory establishes benign-overfitting results under specified data conditions. A taxonomy separates benign, tempered and catastrophic regimes; robustness work identifies a distinct cost of label noise. [Benign Overfitting in Deep Neural Networks under Lazy Training](https://arxiv.org/abs/2305.19377v1); [Benign, Tempered, or Catastrophic: A Taxonomy of Overfitting](https://arxiv.org/abs/2207.06569v3); [How benign is benign overfitting?](https://arxiv.org/abs/2007.04028v1)

**Proposed question.** Can spectral, margin and representation diagnostics predict noise-induced excess risk when a network leaves the lazy regime?

**Boundary to audit.** Low natural test error does not imply vanishing excess risk or adversarial robustness. Classification and regression statements require separate accounting.

**Proposed decisive test.** Vary label noise and feature-learning strength with a known Bayes reference. Measure excess risk, margins and robustness separately and compare early stopping with interpolation.

**Current understanding, scoped to this question.**

- Theory: Precise results exist under restricted distributional and training assumptions.
- Empirical: Neural experiments motivate distinctions between risk regimes.
- Prediction: The proposed feature-learning risk predictor has not been checked against all existing theories.

**Audit priority.** second — Broad and mature literature needs a deeper novelty search.

**Identity check.** [DISC-20261001-014](#disc-20261001-014): Noise-induced risk under one task differs from interference across sequential tasks.

### DISC-20261001-014

**Forecasting forgetting from evolving task geometry** · representation-generalization · new_candidate

**Author-reported starting points.** EWC slows updates to parameters important for previous tasks. Teacher-student theory distinguishes input-feature and readout similarity; a current parameter-gradient method uses conflicting versus collaborative contributions. [Overcoming catastrophic forgetting in neural networks](https://arxiv.org/abs/1612.00796v2); [Disentangling and Mitigating the Impact of Task Similarity for Continual Learning](https://arxiv.org/abs/2405.20236v1); [Collaborative Parameter Learning: Mitigating Forgetting via Parameter-Level Gradient Analysis](https://arxiv.org/abs/2601.21577v2)

**Proposed question.** Can a bounded calibration set of old-task gradients predict a future retention-learning tradeoff under finite-step AdamW and changing representations?

**Boundary to audit.** A local gradient relation is not a full future trajectory model. Limited access to old tasks changes the information available to the predictor.

**Proposed decisive test.** Control feature and readout overlap separately, then test finite learning rates and partial old-task coverage. Freeze predicted forgetting curves before the second task.

**Current understanding, scoped to this question.**

- Theory: Latent linear teacher-student analysis gives conditional relationships.
- Empirical: Continual-learning methods and current LM knowledge-injection experiments provide evidence.
- Prediction: Current theory does not automatically establish the specific finite-horizon forecast proposed here.

**Audit priority.** second — Requires current-version and access-assumption checks before prioritizing compute.

### DISC-20261001-015

**Identifying the algorithm behind in-context predictions** · in-context-learning · new_candidate

**Author-reported starting points.** Bayesian and optimization accounts explain ICL in controlled settings. A later regression study reports prompt-shift failures inconsistent with exact OLS behavior in its trained models. [An Explanation of In-context Learning as Implicit Bayesian Inference](https://arxiv.org/abs/2111.02080v6); [Transformers learn in-context by gradient descent](https://arxiv.org/abs/2212.07677v2); [What learning algorithm is in-context learning? Investigations with linear models](https://arxiv.org/abs/2211.15661v3); [Transformers Don't In-Context Learn Least Squares Regression](https://arxiv.org/abs/2507.09440v1)

**Proposed question.** Which interventions distinguish approximate algorithm implementation from a predictor that agrees with that algorithm only on the training distribution?

**Boundary to audit.** Bayesian inference and gradient methods are not always mutually exclusive descriptions. Existence constructions do not imply every trained transformer implements the construction.

**Proposed decisive test.** Match in-distribution accuracy, then apply covariance, scale and prompt perturbations on which candidate algorithms predict different outputs. Include internal-state predictions where available.

**Current understanding, scoped to this question.**

- Theory: Constructive and distribution-specific results already exist.
- Empirical: In-distribution agreement and selected OOD failures are documented.
- Prediction: The target is identifiable mechanism within a declared model family, not one universal ICL algorithm.

**Audit priority.** first — Explicitly addresses the difference between observational agreement and mechanism.

**Identity check.** [DISC-20261001-016](#disc-20261001-016): Mechanism identifiability differs from predicting task-distribution transfer.

### DISC-20261001-016

**Task diversity and the boundary of in-context generalization** · in-context-learning · new_candidate

**Author-reported starting points.** Subspace analyses and task-diversity experiments explain some ICL OOD behavior. Uncertainty-prediction tasks help distinguish prior-dependent estimators. [Out-of-Distribution Generalization of In-Context Learning: A Low-Dimensional Subspace Perspective](https://arxiv.org/abs/2505.14808v2); [When can in-context learning generalize out of task distribution?](https://arxiv.org/abs/2506.05574v2); [Towards Better Understanding of In-Context Learning Ability from In-Context Uncertainty Quantification](https://arxiv.org/abs/2405.15115v1)

**Proposed question.** Can a measurable description of pretraining task diversity predict generalization and uncertainty outside the observed task span in nonlinear tasks?

**Boundary to audit.** Within-span novelty is not arbitrary out-of-support transfer. Predictive uncertainty and point accuracy are distinct outcomes.

**Proposed decisive test.** Vary span coverage independently of task count, then test nonlinear features and novel subspaces. Freeze both mean-risk and uncertainty predictions.

**Current understanding, scoped to this question.**

- Theory: Linear/subspace and Bayes-related results support restricted cases.
- Empirical: Synthetic task transitions and selected transformer experiments exist.
- Prediction: General nonlinear out-of-span prediction is only a candidate boundary, not a certified open theorem.

**Audit priority.** first — Existing results sharply define a useful special-case boundary.

**Identity check.** [DISC-20261001-017](#disc-20261001-017): Task-span shift differs from relocating the same evidence in a prompt.

### DISC-20261001-017

**Predicting failures to combine dispersed context evidence** · in-context-learning · new_candidate

**Author-reported starting points.** Long-context studies measure position sensitivity; multi-hop work also reports effects of the separation between necessary pieces of information. [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172v3); [Lost in the Middle, and In-Between: Enhancing Language Models' Ability to Reason Over Long Contexts in Multi-Hop QA](https://arxiv.org/abs/2412.10079v1)

**Proposed question.** Can a model of retrieval and composition predict accuracy from evidence placement, distractor density and hop count for a specified long-context model?

**Boundary to audit.** Single-fact retrieval and multi-hop composition are different tasks. Positional performance curves alone do not identify a causal attention mechanism.

**Proposed decisive test.** Hold facts and question semantics fixed while permuting positions and distances. Use retrieval probes to separate missing evidence from failed composition and validate predictions on held-out layouts.

**Current understanding, scoped to this question.**

- Theory: This seed line is primarily empirical; a theory audit is still required.
- Empirical: Controlled position and multi-hop experiments exist.
- Prediction: Quantitative transfer to held-out layouts is the proposed target.

**Audit priority.** second — Need to search more recent positional and attention-mechanism theories.

### DISC-20261001-018

**Guidance schedules with finite-dimensional score error** · generative-models · new_candidate

**Author-reported starting points.** High-dimensional CFG analysis characterizes finite-dimensional overshoot and variance effects and motivates nonlinear guidance forms. [Classifier-Free Guidance: From High-Dimensional Analysis to Generalized Guidance Forms](https://arxiv.org/abs/2502.07849v2)

**Proposed question.** Can measurable score error and conditioning strength select a guidance schedule that predicts a quality-diversity tradeoff on a held-out conditional distribution?

**Boundary to audit.** Exact or idealized high-dimensional scores and finite learned scores need different error accounting. A guidance method improving benchmarks is not yet a transferable selection law.

**Proposed decisive test.** First reproduce Gaussian-mixture predictions, then introduce controlled score errors and finite dimension. Freeze schedule selection before a specified image experiment.

**Current understanding, scoped to this question.**

- Theory: High-dimensional and finite-dimensional analysis exists in a controlled framework.
- Empirical: Gaussian and image-generation experiments are reported.
- Prediction: Practical schedule selection with known error budgets remains to be reviewed.

**Audit priority.** second — Only one primary line was screened; expand citations before declaring a gap.

**Identity check.** [DISC-20261001-020](#disc-20261001-020): Guidance bias and numerical sampling error can interact but require different controls.

### DISC-20261001-019

**A quantitative boundary between diffusion generalization and memorization** · generative-models · new_candidate

**Author-reported starting points.** A synthetic/natural-image-like laboratory predicts a memorization crossover by model capacity. Manifold analysis describes direction-dependent geometric memorization. [On the Edge of Memorization in Diffusion Models](https://arxiv.org/abs/2508.17689v1); [Losing dimensions: Geometric memorization in generative diffusion](https://arxiv.org/abs/2410.08727v2)

**Proposed question.** Can local data geometry and model capacity predict partial memorization before exact training-example reproduction occurs in a specified learned diffusion model?

**Boundary to audit.** Exact duplication, nearest-neighbor resemblance and lost tangent directions measure different phenomena. Their thresholds should not be treated as identical.

**Proposed decisive test.** Use manifolds with controlled directional variance, train across capacities and sample counts, and freeze predictions for geometry loss and exact-copy rates separately.

**Current understanding, scoped to this question.**

- Theory: Tractable crossover and geometric analyses already provide predictions.
- Empirical: Controlled simulations and image-like experiments support those analyses.
- Prediction: Generalization to a learned-score setting beyond tested assumptions needs audit.

**Audit priority.** first — A precise measurement bridge between two explanatory lines.

**Identity check.** [DISC-20261001-020](#disc-20261001-020): Training-data memorization is distinct from approximation error to a specified target.

### DISC-20261001-020

**Making diffusion error decompositions operational** · generative-models · new_candidate

**Author-reported starting points.** Sampling bounds relate score error to convergence; later work analyzes deterministic and stochastic samplers, and an end-to-end framework includes learning and discretization errors. [Sampling is as easy as learning the score: theory for diffusion models with minimal data assumptions](https://arxiv.org/abs/2209.11215v3); [Convergence of Deterministic and Stochastic Diffusion-Model Samplers: A Simple Analysis in Wasserstein Distance](https://arxiv.org/abs/2508.03210v2); [From Score Learning to Discretized Sampling: An End-to-End Generalization Analysis of Diffusion Models](https://arxiv.org/abs/2607.23226v1)

**Proposed question.** Can quantities estimated from finite validation data guide how to allocate training effort and sampler evaluations for a fixed target distribution?

**Boundary to audit.** End-to-end error decompositions already exist. The candidate concerns estimability and useful finite-budget decisions, not the absence of convergence theory.

**Proposed decisive test.** Compare bound-derived choices with an empirical budget sweep on a tractable target, then a declared image dataset. Measure whether estimated components rank the best allocation correctly.

**Current understanding, scoped to this question.**

- Theory: Score-conditional and end-to-end convergence frameworks are reported.
- Empirical: Practical tightness and decision utility were not established by this screening.
- Prediction: Observable allocation rules need further validation and novelty checking.

**Audit priority.** first — Avoids proposing a theorem class that recent work already addresses.

### DISC-20261001-021

**Distinguishing reasoning acquisition from probability reweighting** · post-training · new_candidate

**Author-reported starting points.** One RLVR study uses large-k evaluation to argue for reweighting in its settings; ProRL reports broader reasoning performance after prolonged training under a different protocol. [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837v5); [ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models](https://arxiv.org/abs/2505.24864v1)

**Proposed question.** Which finite-sample tests can distinguish reusable new task-solving behavior from improved sampling of rare base-model behavior under matched budgets?

**Boundary to audit.** Finite sampling cannot prove a base policy assigns zero probability. Training duration, task mixtures, decoding and reference-policy changes differ across studies.

**Proposed decisive test.** Reproduce both protocols on a shared base model and tasks. Match sample and training budgets, report uncertainty for rare success events, and test held-out compositional transfer.

**Current understanding, scoped to this question.**

- Theory: This dispute needs an operational definition of capability before a theorem or causal claim.
- Empirical: Competing empirical interpretations are reported under different protocols.
- Prediction: Neither abstract establishes a universal yes/no answer; a common test is proposed.

**Audit priority.** first — High scientific value but measurement definitions must lead the investigation.

**Identity check.** [DISC-20261001-023](#disc-20261001-023): Changing the policy through RL differs from allocating sampling to a fixed policy.

### DISC-20261001-022

**Observable warning signals for preference overoptimization** · post-training · new_candidate

**Author-reported starting points.** Empirical reward-overoptimization laws extend from proxy-reward optimization to direct alignment. Chi-squared preference optimization provides a theoretical alternative with robustness guarantees. [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760v1); [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://arxiv.org/abs/2406.02900v2); [Correcting the Mythos of KL-Regularization: Direct Alignment without Overoptimization via Chi-Squared Preference Optimization](https://arxiv.org/abs/2407.13399v3)

**Proposed question.** Without access to a gold reward oracle, can observable coverage and uncertainty diagnostics forecast harmful overoptimization for a declared preference-learning setup?

**Boundary to audit.** The existence of a robust preference algorithm is already addressed under assumptions. Synthetic gold-model reward is not identical to human preferences, and KL alone may not identify optimization pressure.

**Proposed decisive test.** Use hidden gold reward only for evaluation, calibrate on limited held-out preferences, and freeze warning thresholds. Compare DPO and chi-squared regularization under controlled coverage shifts.

**Current understanding, scoped to this question.**

- Theory: Robustness guarantees already exist; their coverage assumptions require full-text audit.
- Empirical: Overoptimization trajectories have been measured for several methods.
- Prediction: An oracle-free warning rule is a separate candidate from designing a robust algorithm.

**Audit priority.** first — Existing positive theory should narrow rather than erase the practical question.

### DISC-20261001-023

**Adaptive inference budgets with imperfect verifiers** · post-training · new_candidate

**Author-reported starting points.** Test-time compute studies find prompt-dependent allocation benefits, while reward-model work shows selection can overoptimize an imperfect proxy. [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314v1); [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760v1)

**Proposed question.** Can a small calibration set predict when another sample or reasoning step helps more than it increases verifier selection error on a shifted task distribution?

**Boundary to audit.** An oracle difficulty estimate and a learned verifier supply different information. Best-of-N success and judged quality must be separated.

**Proposed decisive test.** Hold the proposal model fixed, perturb verifier calibration and task difficulty, and predict stopping decisions. Include all rejected samples and verifier calls in compute.

**Current understanding, scoped to this question.**

- Theory: Empirical allocation and overoptimization models provide ingredients.
- Empirical: Both sampling-based selection and inference strategies have measured tradeoffs.
- Prediction: A transferable stopping criterion is a proposed synthesis awaiting audit.

**Audit priority.** second — Related to lifecycle compute allocation but operates after the model is fixed.

### DISC-20261001-024

**Which precision law matches the quantization mechanism** · precision · new_candidate

**Author-reported starting points.** Empirical precision-aware scaling laws use effective capacity; sketched-regression theory distinguishes additive and multiplicative quantization effects. [Scaling Laws for Precision](https://arxiv.org/abs/2411.04330v2); [Scaling Laws for Precision in High-Dimensional Linear Regression](https://arxiv.org/abs/2602.19241v2)

**Proposed question.** Can measured error structure identify the correct precision-loss model before fitting a separate scaling law for each format and tensor group?

**Boundary to audit.** Additive and multiplicative noise models are assumptions, not interchangeable descriptions of every hardware quantizer. Training and post-training quantization must be separated.

**Proposed decisive test.** Check error conditional on tensor magnitude, then predict loss under held-out bit budgets and group assignments with a fixed calibration budget.

**Current understanding, scoped to this question.**

- Theory: A controlled high-dimensional analysis explains distinct scaling forms.
- Empirical: Precision-aware LM scaling fits have empirical support.
- Prediction: Mapping real tensor errors to the right theoretical regime is the proposed validation target.

**Audit priority.** first — A concrete bridge from mechanism to predictive functional form.

**Identity check.** [DISC-20261001-025](#disc-20261001-025): Global precision-loss scaling and tail update stagnation are different prediction targets.

### DISC-20261001-025

**Predicting low-learning-rate stagnation from update resolution** · precision · new_candidate

**Author-reported starting points.** M+Adam identifies update stagnation with low-precision master weights and proposes additive-multiplicative updates; precision scaling work studies loss effects more broadly. [M+Adam: Low-Precision Training via Additive-Multiplicative Optimization](https://arxiv.org/abs/2607.10611v2); [Scaling Laws for Precision](https://arxiv.org/abs/2411.04330v2)

**Proposed question.** Given rounding mode, master-weight precision and update-to-weight ratios, can we predict when a decaying schedule stops producing useful parameter changes?

**Boundary to audit.** BF16 forward computation with FP32 master weights is not the low-precision-master setting. Loss quantization, parameter rounding and statistical plateaus require separate diagnostics.

**Proposed decisive test.** Branch identical checkpoints into controlled master-weight and rounding configurations with matched data order. Forecast zero-update fractions and loss differences before running tails.

**Current understanding, scoped to this question.**

- Theory: A proposed optimizer has a smooth-objective descent analysis; exact assumptions still need review.
- Empirical: Low-precision-master LM experiments are reported.
- Prediction: Tail-specific quantitative thresholds across precision configurations remain a candidate.

**Audit priority.** first — A cheap decisive test with an important implementation distinction.

**Identity check.** [DISC-20261001-026](#disc-20261001-026): Late update resolution and early module precision allocation have different inputs.

### DISC-20261001-026

**Precision allocation after scale-stable initialization** · precision · new_candidate

**Author-reported starting points.** Unit-scaled maximal-update parametrization supports low-precision training, while precision-aware laws quantify quality-cost effects of tensor precisions. [u-$\mu$P: The Unit-Scaled Maximal Update Parametrization](https://arxiv.org/abs/2407.17465v3); [Scaling Laws for Precision](https://arxiv.org/abs/2411.04330v2)

**Proposed question.** Can initial scaling plus early tensor statistics predict which modules need higher precision later in training, without per-module ablation sweeps?

**Boundary to audit.** Unit-scale initialization does not imply stationary distributions throughout training. Format range, rounding and accumulated optimizer state must be specified.

**Proposed decisive test.** Freeze a module precision allocation from early diagnostics, then test later distributions and quality on held-out sizes and schedules against uniform and tuned allocations.

**Current understanding, scoped to this question.**

- Theory: Parametrization principles and empirical precision laws provide starting points.
- Empirical: Low-precision training and mixed-component fits have been reported.
- Prediction: An early-data precision allocator is the proposed target, not an established gap.

**Audit priority.** second — Needs a fuller audit of mixed-precision allocation methods.

## Rejected or narrowed framings

- **TRIAGE-01 — narrow:** There is no theory of optimal learning rate schedules. Controlled-model schedule results already exist; focus on identifiable transfer to a declared AdamW feature-learning setting. [Optimal Learning Rate Schedules under Functional Scaling Laws: Power Decay and Warmup-Stable-Decay](https://arxiv.org/abs/2602.06797v3); [Theory of Optimal Learning Rate Schedules and Scaling Laws for a Random Feature Model](https://arxiv.org/abs/2602.04774v2)
- **TRIAGE-02 — narrow:** No scale-transfer prescriptions exist for MoE or GQA. Recent papers provide architecture-specific prescriptions; audit residual finite-scale errors rather than restating solved special cases. [How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization](https://arxiv.org/abs/2605.14200v1); [GQA-{\mu}P: The maximal parameterization update for grouped query attention](https://arxiv.org/abs/2605.15290v1)
- **TRIAGE-03 — separate_protocols:** Benefits and harms of repeated data directly contradict each other. Epochs, concentrated duplicate injection, domain dilution and SFT differ in objectives and budgets. They motivate controlled comparison, not an established contradiction. [Scaling Data-Constrained Language Models](https://arxiv.org/abs/2305.16264v5); [Internal Data Repetition Destroys Language Models](https://arxiv.org/abs/2606.24998v1); [Data Repetition Beats Data Scaling in Long-CoT Supervised Fine-Tuning](https://arxiv.org/abs/2602.11149v2)
- **TRIAGE-04 — narrow:** No direct preference algorithm has robustness guarantees. Chi-squared preference optimization supplies a relevant positive result. Audit assumptions and practical warning signals instead. [Correcting the Mythos of KL-Regularization: Direct Alignment without Overoptimization via Chi-Squared Preference Optimization](https://arxiv.org/abs/2407.13399v3)
- **TRIAGE-05 — narrow:** No end-to-end diffusion error decomposition exists. A 2026 paper reports an end-to-end framework. Focus on observable estimates and finite-budget decision utility. [From Score Learning to Discretized Sampling: An End-to-End Generalization Analysis of Diffusion Models](https://arxiv.org/abs/2607.23226v1)
- **TRIAGE-06 — reject_inference:** A BF16 experiment necessarily has low-precision master weights. Forward/backward dtype and master-weight storage are different implementation choices; inspect both before applying low-resolution update arguments. [M+Adam: Low-Precision Training via Additive-Multiplicative Optimization](https://arxiv.org/abs/2607.10611v2)
- **TRIAGE-07 — reject_inference:** Finite pass at k proves the base model has zero support for a solution. Finite samples do not prove zero probability; use uncertainty bounds and controlled transfer measurements. [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837v5); [ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models](https://arxiv.org/abs/2505.24864v1)
- **TRIAGE-08 — out_of_scope:** Scaling laws for precision in quantum interferometry. A keyword collision returned arXiv:1006.1645. It is outside the deep-learning scope and was not added to the bibliography.
- **TRIAGE-09 — version_correction:** Reuse the search snippet of the first version of arXiv:2601.21577 as a current claim. The retrieved primary v2 page has a different title and revised abstract. This batch summarizes v2 and does not carry over the old snippet guarantee. [Collaborative Parameter Learning: Mitigating Forgetting via Parameter-Level Gradient Analysis](https://arxiv.org/abs/2601.21577v2)
- **TRIAGE-10 — narrow:** Treat Bayesian ICL and gradient-descent ICL as universally incompatible. Algorithmic and statistical descriptions can coincide on particular tasks. Propose interventions where their specified predictions actually differ. [An Explanation of In-context Learning as Implicit Bayesian Inference](https://arxiv.org/abs/2111.02080v6); [Transformers learn in-context by gradient descent](https://arxiv.org/abs/2212.07677v2); [What learning algorithm is in-context learning? Investigations with linear models](https://arxiv.org/abs/2211.15661v3)
