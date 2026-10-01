# Closing Adam norm and momentum dynamics with few states

**Status: candidate. Literature audit incomplete.**

## Question

Can a small, identifiable set of statistics predict AdamW norm evolution under unseen schedules?

## Setting and available information

Specify weight decay, bias correction, moment coefficients, epsilon, clipping and numerical precision. Define every norm and angle before comparing trajectories.

## Established results

Malladi et al. derive SDE approximations for Adam and RMSprop, with theoretical guarantees and batch-scaling experiments. The [abstract](https://arxiv.org/abs/2205.10287v3) does not establish the particular low-dimensional module closure proposed here.

## Remaining uncertainty

Candidate question: which correlations can be omitted without losing predictive accuracy during feature learning? Exact norm identities alone do not establish a closed predictive model.

## Competing explanations

Module averages may concentrate sufficiently; alternatively, update alignment and coordinate correlations may require additional states. Neither is asserted to hold in general.

## Decisive test

Start with a controlled model whose distribution is known. Derive the statistics retained and the neglected terms explicitly. Freeze the closure before held-out schedules, then test a specified neural network with an equal calibration budget. Compare against a constant-injection norm recurrence.

## Success criteria and cost

Assess signed norm errors, forecast stability, and calibration sensitivity before asking whether the state improves loss prediction. Record moment and update definitions. The experiment and resource estimate have not yet been supplied.

## Literature audit

Seed abstract screening only, 2026-10-01. Full-text assumptions, related normalized-network dynamics and subsequent adaptive-optimizer work require review.

## Related problems

DLOP-0001 asks for loss prediction. This card asks whether a proposed state representation can forecast itself; it does not assume norms are uniquely causal.

## Discovery update on 2026 10 01

The batch identified preconditioning and momentum results that delimit relevant special cases. Their optimizer definitions and small-step assumptions require full-text checking before importing them into EMA AdamW. See the [batch discovery report](../../discovery/2026-10-01/README.md) and its versioned references. Status remains candidate; full-text review is incomplete.
