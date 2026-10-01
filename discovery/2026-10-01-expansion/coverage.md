# Subfield coverage and remaining work

All 24 rows are **abstract-screened entry points**, not completed field audits. Counts are selected leads, not coverage percentages. Exact executed queries are in [the manifest](search-manifest.json); a query may support more than one row. No row has full-text audit, systematic citation closure, independent replication, or measured saturation.

| Area | Leads | Next missing check |
| --- | --- | --- |
| self-supervised vision | [027](README.md#disc-20261001-027), [028](README.md#disc-20261001-028), [029](README.md#disc-20261001-029) | Compare objective-specific collapse theories with DINO/VICReg and dense prediction; trace MAE theory citations. |
| robustness and domain shift | [030](README.md#disc-20261001-030), [031](README.md#disc-20261001-031), [032](README.md#disc-20261001-032) | Add group DRO, causal representation learning, adversarial certificates and non-image shifts; inspect adaptation assumptions. |
| graph learning | [033](README.md#disc-20261001-033), [034](README.md#disc-20261001-034), [035](README.md#disc-20261001-035) | Check task-aware rewiring, graph-size transfer and graph transformer benchmarks against the selected theories. |
| non-language reinforcement learning | [036](README.md#disc-20261001-036), [037](README.md#disc-20261001-037), [038](README.md#disc-20261001-038) | Add exploration, off-policy instability, offline-to-online transfer and multi-agent control; audit neural uncertainty guarantees. |
| compression and adaptation | [039](README.md#disc-20261001-039), [040](README.md#disc-20261001-040), [041](README.md#disc-20261001-041) | Read recent pruning papers beyond the inaccessible landing page; add structured sparsity and matched-hardware compute. |
| multimodal learning | [042](README.md#disc-20261001-042), [043](README.md#disc-20261001-043) | Extend beyond dual encoders and late fusion to audio/video, generative fusion and missing modalities. |
| scientific machine learning | [044](README.md#disc-20261001-044), [045](README.md#disc-20261001-045) | Add chaotic long-time forecasting, inverse problems, irregular meshes and numerical-analysis literature. |
| synthetic-data feedback | [046](README.md#disc-20261001-046) | Audit filtering, finite retention, fresh-data bounds and rare-event metrics across modalities. |
| differentially private learning | [047](README.md#disc-20261001-047) | Search private scaling laws, clipping bias, lower bounds and subgroup utility beyond efficient implementation papers. |
| predictive uncertainty | [048](README.md#disc-20261001-048), [049](README.md#disc-20261001-049) | Audit calibration metric definitions, target-label budgets, dependent streams and conformal assumption violations. |
| generalization mechanisms | [050](README.md#disc-20261001-050), [051](README.md#disc-20261001-051) | Add PAC-Bayes, stability, information-theoretic bounds, double descent and feature-learning counterexamples. |
| architecture dynamics | [052](README.md#disc-20261001-052), [053](README.md#disc-20261001-053) | Add SSMs, attention sinks, recurrent memory, depth limits and architecture search; broaden beyond residual networks and MoE. |
| federated learning | [054](README.md#disc-20261001-054) | Add nonstationary participation, personalization, asynchronous updates and systems constraints. |
| mechanistic interpretability | [055](README.md#disc-20261001-055) | Add circuit faithfulness, feature splitting and cross-seed identification; audit SAE latent-model assumptions. |
| generative training dynamics | [056](README.md#disc-20261001-056), [057](README.md#disc-20261001-057) | Update GAN lineage and add flow matching, discrete generation, sampler bias and current consistency bounds. |
| data attribution | [058](README.md#disc-20261001-058) | Compare TRAK, TracIn, influence variants and data Shapley against actual retraining under a shared protocol. |
| machine unlearning | [059](README.md#disc-20261001-059) | Read certified unlearning guarantees and recent adaptive attacks; separate deletion from answer suppression. |
| compositional learning | [060](README.md#disc-20261001-060) | Audit entropy-based predictions and grammar-support assumptions; add non-language compositional tasks. |
| out-of-distribution detection | [061](README.md#disc-20261001-061) | Add semantic versus covariate OOD, near-OOD alternatives and sequential tests under dependent data. |
| model merging | [062](README.md#disc-20261001-062) | Add task arithmetic, nonlinear alignment, heterogeneous architectures and post-merge safety of unrelated tasks. |
| representation identifiability | [063](README.md#disc-20261001-063) | Compare auxiliary-variable, temporal and sparse-mixing identification; quantify approximate assumptions. |
| symmetry and geometric learning | [064](README.md#disc-20261001-064) | Add equivariant statistical learning theory and stochastic symmetry-breaking outputs. |
| long-tailed recognition | [065](README.md#disc-20261001-065) | Add label noise, unequal within-class diversity and changing deployment priors; inspect feature sufficiency claims. |
| tabular learning | [066](README.md#disc-20261001-066) | Compare recent tabular foundation models, meta-learning priors, unseen schema transfer and amortized compute. |

## Additional areas not yet given a dedicated pass

Speech and audio learning; robotics and embodied control; temporal forecasting; recurrent and state-space models; efficient attention and memory; retrieval-augmented systems; transfer and domain adaptation beyond selected shifts; meta-learning and few-shot adaptation; active learning; multi-task gradient interference; neural architecture search; recommender systems; multi-agent RL; distributed asynchronous optimization; Bayesian deep learning beyond calibration; structured prediction; neural combinatorial optimization; energy-based models; diffusion/flow matching beyond the selected losses; discrete generative models; 3D geometry; nonstationary evaluation; multilingual and cross-cultural data shifts. Some overlap current cards, but overlap has not been audited.

## How to reduce omissions without pretending completeness

Use a cross-product checklist: learning paradigm × modality/domain × phenomenon × assumption regime × available information × intervention. Start a separate search route from an original paper, a benchmark failure and a competing theorem; retain searches that produce no new lead. Trace references and later citations, including corrections and negative results. Record the marginal number of new distinct questions per route only after a fixed retrieval protocol exists. The current purposive sample cannot estimate a missing-problem fraction.

## Deduplication status

Stable IDs and explicit neighbor reasons distinguish nearby targets. Cross-batch exact-ID/question collisions and dangling links are validated automatically. Semantic equivalence is only a curator proposal until a reviewer compares setting, inputs, observable, intervention and success criterion. If two leads are equivalent, merge the questions and preserve aliases and evidence rather than erasing provenance.
