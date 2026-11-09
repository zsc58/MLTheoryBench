# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Formulates each finite-input output vector as a bias plus a sum of iid hidden-unit contribution vectors, with the stated independence, centering, and 1/H scaling.
- **3 points:** Expands the covariance and derives cancellation of all cross-activation and cross-hidden-unit terms, obtaining sigma_b^2 + sigma_v^2 sum_m w_m K_m.
- **3 points:** Verifies finite second moments and applies a valid multivariate CLT or Cramer-Wold argument to establish convergence for every finite input set to the claimed centered Gaussian law.
- **2 points:** Establishes that each component kernel, and hence the nonnegative weighted sum plus the bias term, is positive semidefinite and a valid covariance kernel.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require incidental presentation choices. Deduct substantially when block-independence cancellation or the finite-dimensional CLT is merely named without derivation; propagate a missing covariance computation to the limit only when the limiting covariance is consequently unsupported.
