# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Isolation of the insertion transition (3 points).** Derives recovery of each fresh batch mean from the cumulative releases, establishes the relevant batch independence, and justifies cancellation of all conditional-density ratios except the insertion transition. An equivalent invertible-change-of-variables argument is acceptable. Handles tau=1 using the first-release density or an explicit harmless deterministic initial-state convention. Shows that the observed likelihood ratio depends only on the insertion batch mean. Merely asserting isolation earns at most 1 point.
2. **Correct Gaussian likelihood ratio and optimality (3 points).** Derives the null covariance Sigma/n, alternative covariance (n-1)Sigma/n^2, and shifted mean. Expands the full multivariate quadratic log likelihood ratio with coefficient -n/[2(n-1)], including determinant, linear, and constant terms. Correctly applies Neyman-Pearson to the fully specified observation laws, with optimality understood at a fixed Type-I level.
3. **Exact sequential error formulas (2 points).** In the scalar case solves the threshold inequality and integrates under both hypotheses. Uses a signed interval center or explicitly reflects the standardized variable before using a=sqrt(n*m*); does not assume z*-mu is nonnegative. Derives both displayed normal-CDF formulas, handles the maximum and above-maximum thresholds, and covers m*=0. Establishes independence from tau and T for fixed gamma.
4. **Final-only comparison (2 points).** Derives the scalar final-snapshot Gaussian laws for the same replacement experiment and obtains the formulas with q=nT. If roots in W=hat(mu)_T-mu are used, their center is z*-mu and their half-width is sigma*sqrt((q-1)/q)*sqrt(m*+log c_T-2gamma). Handles the threshold boundary and explains dilution through the target's weight, mean displacement, or relative variance reduction. The formulas must remain valid at T=1, when the experiments coincide.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a separate discussion of every boundary if the derivation demonstrably covers it. Strict and non-strict rejection conventions give the same errors because the equality boundaries have probability zero. A symmetry argument permits replacing a signed target displacement by its absolute value in the error formulas, but not silently in the unreflected rejection interval. Do not require or accept the scalar normal-CDF formulas as general-dimensional formulas. Deduct for changing assumptions, omitting a target clause, or treating a paper-specific cancellation or Gaussian calculation as an unsupported assertion.

The source's incorrect final-only roots are not an acceptable alternative to the correct roots. Its main-text final-only error formulas are correct after the local proof repair. No unresolved reference-proof obligation is delegated to scoring.
