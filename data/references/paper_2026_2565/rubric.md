# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly expands the bias-corrected first moment and derives its stale-gradient and martingale decomposition, including the lag-weighted stale bound.
2. **2 points:** Proves simultaneous concentration with justified predictable variance and bounded-increment estimates, including the stated constants and failure-probability accounting.
3. **2 points:** Controls the discrepancy between the bias-corrected second moment and the uncorrected predictable proxy, obtaining the stated preconditioner-perturbation bound.
4. **2 points:** Derives the one-step Euclidean-projection contraction with the displayed coefficients and unrolls it to the simultaneous finite-time assertion.
5. **2 points:** Establishes the stated uniform constant-step floor without dropping the finite-time second-moment transient; proves burn-in, the restarted endpoint bounds, confidence allocation, floor comparability, and total-time scaling.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. In particular, the floor need not be justified by the reference proof's coarse pathwise argument, but a solution cannot simply replace a finite-time second-moment transient by its limit. Do not award credit for merely naming a concentration result without checking its hypotheses. A restarted-epoch argument must use the predictable preconditioner calculated from that epoch's reset moment state and verify that the stated monotonicity and along-iterate noise assumptions apply to it; monotonicity for an uninterrupted run cannot be transferred by assertion. Account for resets and failure probabilities without requiring independence between epochs. The stated positive-floor and attained-minimum conditions govern the burn-in formulas; do not require a claim about an optimizer when those conditions are absent.
