# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly proves that componentwise \(b\ge\widehat b\) makes the true primal-dual pair feasible for the predicted LP, including unchanged dual feasibility.
2. **2 points:** Correctly proves that overprediction on any tight true primal constraint violates predicted primal feasibility.
3. **3 points:** Proves necessity of equality \(b_j=\widehat b_j\) on every positive-dual index using complementary slackness, predicted feasibility, strong duality, and the sign argument for the weighted sum.
4. **3 points:** Proves sufficiency: equality on the positive dual support together with predicted feasibility yields equal predicted primal and dual objectives and hence predicted optimal-pair membership.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation or ordering. Treat omission of the sign/support argument or of either direction of the zero-gap characterization as a theorem-critical gap.
