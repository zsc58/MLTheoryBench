# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Essentially complete, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Lower bounds (3 points).** Derive the local soft-thresholded noise penalty from interpolation at sample points and the design-density lower bound. Also establish both unrestricted contributions: the ordinary nonparametric estimation rate and an attack-variation lower bound of order r^(2(1∧β)). A bare citation to a paper-specific prior minimax theorem does not close either missing derivation.
2. **Valid interpolator (2 points).** Give a jointly measurable sample-dependent correction supported in the stated neighborhoods; verify the residual bound at every training point almost surely, including the empty-neighborhood and zero-radius cases.
3. **Upper risk and matching mechanism (3 points).** Control the base-estimator and target-variation terms and the clipped residuals. For a nonzero-neighborhood construction, prove rather than assert the comparison A_δ(r+τ)≲A_δ(r)+nτ^d; a binomial-mark concavity calculation or an equally rigorous argument suffices.
4. **Rate and conclusion (2 points).** Use the two restrictions on τ_n to absorb τ_n^(2(1∧β)) and nτ_n^d, then combine upper and lower bounds with the stated infimum–supremum order and uniform constants.

# Evaluator Notes

Accept a complete valid alternative proof. In particular, a correction confined to the sample points is supported inside every positive τ_n-neighborhood and can prove the measurable constructive claim directly; do not demand an unnecessary radius-enlargement calculation from that alternative. Do not require continuity or smoothness of the full estimator. Apply the strict-predecessor smoothness index k=⌈β⌉−1, including at integer β, and respect the fresh-test-input, joint-measurability, Gaussian-independence, and conditional base-estimator assumptions.
