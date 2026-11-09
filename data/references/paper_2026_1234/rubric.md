# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly defines the generalized conditional quantiles and uses the quantile-sandwich inequalities for each retained model to establish central-interval mass at least `1-alpha_0`.
- **3 points:** Derives posterior mass at least `1-gamma` for the endpoint-trimmed set by the two endpoint quantile bounds and a union bound, then integrates over retained parameters to prove posterior-predictive envelope mass at least `(1-gamma)(1-alpha_0)`.
- **3 points:** Establishes conditional exchangeability of calibration and test distance scores after fitting the envelope on the independent training split, and applies the correct split-conformal order-statistic argument to obtain probability at least `1-alpha`.
- **2 points:** Correctly identifies the score sublevel set with `[L(X)-hat t,U(X)+hat t]` and states both integrated target conclusions under the given assumptions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award the conformal points only for an actual exchangeability/order-statistic derivation, not merely naming conformal prediction. Do not propagate an error in the predictive-mixture calculation to the independent conformal step when that step is otherwise valid.
