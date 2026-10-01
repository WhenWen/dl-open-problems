# Predicting loss under unseen learning rate schedules

**Status: candidate. Literature audit incomplete.**

## Question

Can a small calibration set support frozen loss predictions for unseen schedules, including long horizons?

## Setting and available information

Fix architecture, tokenization, data distribution, optimizer, batch size, warmup and evaluation protocol. Declare schedule families and calibration runs before examining held-out results.

## Established results

Tissue et al. report an empirical learning-rate annealing law and cross-schedule loss prediction after fitting a small number of curves. This seed summary is based on the [abstract](https://arxiv.org/abs/2408.11029v2); exact validation boundaries require full-text review.

## Remaining uncertainty

Candidate question: which calibration and state assumptions permit reliable transfer beyond the tested conditions? No failure of the cited law is claimed by this card.

## Competing explanations

Schedule integrals may suffice in a limited regime; evolving optimizer or parameter states may be needed elsewhere. These are alternatives to test, not established explanations.

## Decisive test

Reproduce a published law first. Freeze model choice and calibration on selected runs, then predict new schedules and horizons. Compare against simple schedule-only baselines. If a state model is used, separately evaluate an observed-state diagnostic and a fully forecast-state prediction.

## Success criteria and cost

Predeclare a practically meaningful absolute loss tolerance and compare with seed variation and evaluation noise. Report trajectory RMSE, signed residuals and endpoint bias. Hardware and run budget remain to be specified; no experiment has been performed for this card.

## Literature audit

Only the linked abstract was screened on 2026-10-01. Backward and forward citations, full-text assumptions, and recent competing laws remain to be audited. This is not a verified novelty claim.

## Related problems

DLOP-0002 concerns forecasting internal states. This card concerns loss predictions; either can make progress without resolving the other.

## Discovery update on 2026 10 01

The batch identified optimal-schedule and joint-schedule results in controlled models. The question must focus on the precise transfer and identifiability boundary, rather than claim there is no schedule theory. See the [batch discovery report](../../discovery/2026-10-01/README.md) and its versioned references. Status remains candidate; full-text review is incomplete.
