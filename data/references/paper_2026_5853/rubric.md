# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **3 points:** Derives the transformed-residual representation and conditional cross-covariance. Uses nonconstant variance ratios to force both covariance coefficients to vanish, and uses the stable bounds to recover gamma_0 uniquely. The argument must not divide by either true interaction coefficient or exclude boundary true coefficients.
2. **3 points:** Establishes the unrestricted global profile comparison and its equality case; derives the stated second-order matrix with a valid justification for taking expectations; and proves strict positive definiteness from nonconstant rho_0. Bounded-ratio control of standardized quantities is sufficient; additional unconditional moments of the variances are not required.
3. **3 points:** Transfers the unrestricted expansion to the neural supremum using the stated likelihood approximation and local slice domain, with the same baseline and each fixed sufficiently small positive delta. Derives the Schur-complement curvature, treating the nuisance kernel correctly. A valid argument may use a justified local optimizer, completion of the quadratic form and the compatibility path, or another equivalent method. Merely naming the Schur complement without establishing that it equals the profiled curvature is insufficient.
4. **1 point:** States global stable-region uniqueness, strict local maximization of the neural profile, and local identification of the interaction coordinate on the quotient slice. Does not claim unique neural weights or identification outside the stated local slice without further hypotheses.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Theorem-critical omissions of the covariance diagonalization argument, expectation-valid curvature expansion, positive-definiteness argument, or quotient-slice curvature transfer are major gaps.

The approximation hypothesis concerns population quasi-likelihood along a C^2 path anchored at zero. It is not an unspecified pointwise or function-norm approximation. The unrestricted upper bound and inclusion of the path in each fixed local ball justify transferring it to the supremum. Additive constants must be aligned when comparing Q with Q^*; comparisons of differences are equivalent.

Do not require Gaussian shocks, independent observations, causal invariance, finite-sample consistency, or analysis of penalized or stabilized training. None is part of the frozen population-identification target. Do not demand uniformity as delta tends to zero. A zero-dimensional slice is covered by the direct profile and zero-pseudoinverse conventions; omission of an otherwise immediate explanation of this convention is at most a minor issue.

The reference proof explicitly closes all theorem-critical obligations. No unavailable appendix or specialized external theorem is an accepted substitute for a missing core argument.
