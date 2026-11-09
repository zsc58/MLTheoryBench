# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes local empirical reward-quantile concentration from the density lower bound and correctly controls calibration drift. Uses the source timing: the level at local time m+1 is localized with sqrt(log(m)/m). Justifies the population correction bound throughout the calibration interval, for example by subdividing the level interval into locally controlled increments.
- **3 points:** Derives uniform control of the recomputed score correction: compares recomputed scores with oracle-score empirical quantiles, applies DKW to the i.i.d. oracle scores, proves or correctly explains the order-statistic perturbation transfer, and explains why uniformity permits evaluation at the adaptive level. Handles strict versus non-strict events correctly, including the endpoint of the permitted radius, by strict premises and limits or another valid argument.
- **3 points:** Combines the anchor, correction, and drift terms into valid endpoint concentration at every fixed local count needed by the policy. Checks localization within the density radii, obtains summable failure probabilities with the stated exploration constant, and does not incorrectly condition an i.i.d. concentration bound on an adaptively selected count.
- **2 points:** Performs a tie-safe index comparison and pull-count argument, excludes the gap alternative at the stated threshold, handles initialization using rho>=Delta_j/8, and derives both the per-arm and regret bounds with constants independent of n. Covers vacuous or boundary cases when relevant.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or exact numerical remainder. Merely citing a recomputed-score concentration result without deriving its oracle comparison and perturbation transfer does not earn the central-bottleneck credit.

The arbitrary-CDF inverse-quantile implication with a non-strict CDF-error premise is not valid in full generality at the boundary of the density neighborhood. A valid proof may instead use a strict premise, probability limits, or suitable slack. Similarly, strict endpoint bad events alone do not justify the reference index-event inclusion when index ties are possible; non-strict bad events or another explicit tie treatment suffice. These are local technical issues, not reasons to change the target or impose additional distributional assumptions.

The recurrence need not be analyzed beyond its projection property. No convergence claim for the adaptive update, independent calibration sample, cross-arm independence assumption, or finite reward moment is required. All theorem-critical obligations in the replacement reference proof are closed; there is no unresolved specialized dependency.
