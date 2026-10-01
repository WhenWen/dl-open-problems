# Predicting the limits of simultaneous scale transfer

**Status: candidate. Literature audit incomplete.**

## Question

Can we predict when a hyperparameter transfer prescription fails as several scale axes change together?

## Setting and available information

Choose and document one parametrization, architecture family, optimizer and compute accounting rule. Distinguish width from depth, horizon and precision.

## Established results

Yang et al. report stable optimal hyperparameters under maximal update parametrization and demonstrate transfer in Transformers and ResNets. See the [paper abstract](https://arxiv.org/abs/2203.03466v2). This is not a claim about arbitrary joint scaling changes.

## Remaining uncertainty

Candidate question: what predicts transfer error outside a documented validation envelope? Existing extensions may already answer particular cases; the literature audit must identify those before promotion.

## Competing explanations

Finite-size effects, implementation mismatch, and a genuine change in training regime can all look like transfer failure. Controls must distinguish them.

## Decisive test

Reproduce one published width-transfer result. Check coordinate and update scaling, then change other axes individually before a small joint factorial comparison. Use direct tuning in selected target settings as a reference and account for its cost.

## Success criteria and cost

Measure excess loss and tuning regret with repeated runs, and preregister the tolerance for successful transfer. Decide whether the goal is a practical predictor or an asymptotic bound. No experimental budget has been estimated yet.

## Literature audit

Only the seed abstract was checked on 2026-10-01. Later work on depth, unit scaling, optimizer interactions and precision remains to be searched; this is not a comprehensive assessment.

## Related problems

No relation to another seed card has been established. Shared use of the word scaling is not sufficient to assert equivalence.

## Discovery update on 2026 10 01

The batch found architecture-specific MoE and GQA prescriptions, alongside deep-linear and unit-scaled analyses. A broad claim that joint scale transfer lacks theory would be misleading; finite-scale error prediction needs a narrower audit. See the [batch discovery report](../../discovery/2026-10-01/README.md) and its versioned references. Status remains candidate; full-text review is incomplete.
