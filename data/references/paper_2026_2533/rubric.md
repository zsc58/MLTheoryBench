# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines a training-conditional fitted-PIT discrepancy and proves that conditional-CDF sup-norm consistency and true continuity make it tend to zero in probability for almost every covariate. A correct coupling to the true uniform PIT, or an equivalent direct argument, suffices.
- **3 points:** Validly relates coverage of the reported generalized-inverse response interval to the expected calibrated cutoff gap. The reference route uses left-limit endpoint probabilities and bounds each discrepancy by the conditional PIT error. Handles possible flat portions or jumps of the estimated CDF and calibrated levels zero or one without imposing additional estimator regularity.
- **3 points:** Establishes the marginal calibration PIT deviation bound and closes the order-statistic gap argument under the iid calibration law conditional on training. Derives or correctly states and verifies the relevant ordinary quantile/order-statistic result, and checks the index-rounding error. The resulting control must apply to all admissible training/test-covariate-dependent indices and permit PIT atoms.
- **2 points:** Combines the estimates and justifies integrated-error convergence in training probability, then the joint training/calibration limit for almost every covariate. Pointwise convergence in probability alone must not be silently treated as pointwise almost-sure convergence.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its exact constants, or use of a PIT discrepancy rather than the original CDF error. A direct inverse-quantile argument giving a vanishing response-coverage error is acceptable.

The inclusive PIT event is not generally equivalent to membership in the closed generalized-inverse interval. Do not award the inverse-conversion step merely for asserting that equivalence. A proof can repair it with left limits and true nonatomicity, or with a valid bound on the discrepancy between the two events. It may not assume continuity or strict increase of the estimated CDF without deriving or eliminating that extra assumption.

Ordinary order-statistic facts may be used when their relevant statements and applicability are clear; no specialized paper-specific citation is necessary. Treat an unclosed coverage conversion, missing order-statistic gap control, or unjustified final convergence as a theorem-critical gap. Grade the logical gap and the rest of the proof, not whether the presentation matches the reference.
