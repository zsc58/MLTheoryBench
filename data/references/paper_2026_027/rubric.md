# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Proves the empirical Gram convergence to the matrix formed from `E[u_1u_1^T]`, and correctly identifies `r` linearly growing eigenvalues and `d-r` exactly flat directions. Eventual active rank suffices; finite-sample full rank is not assumed.
- **3 points:** Handles the likelihood-flat directions and establishes the rank-`r` evidence penalty `-(r/2)log n`, including the absence of a `log log n` term and hence RLCT `r/2`. Accept either a justified quadratic-KL/local-integral route or a direct exact Gaussian calculation; a separate KL calculation is not required for the latter.
- **3 points:** Establishes the stochastic evidence expansion relative to `ell_n(beta_0)` under the stated Gaussian model, with every remaining random term controlled as `O_p(1)`. Determinant scaling alone does not establish control of the data-fit contribution.
- **2 points:** Shows that the maximized likelihood gain over the truth is `O_p(1)` and subtracts the expansions with the correct sign to obtain `Q_n-log Z_n=-(d-r)log n/2+O_p(1)` and the over-penalization interpretation.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat a sign reversal in the final discrepancy, failure to handle the flat directions, or replacing the RLCT calculation by merely naming a method as theorem-critical gaps.

Do not assume the inputs have zero mean: the population Gram matrix uses the uncentered second moment, not covariance alone. Do not require an arbitrary maximum-likelihood parameter representative to converge to `beta_0`; only its fitted likelihood is relevant. The full-rank endpoint `r=d` is included, and zero-dimensional flat-coordinate integration is interpreted as one. The general singular-learning expansion need not be invoked when the evidence expansion is proved directly.
