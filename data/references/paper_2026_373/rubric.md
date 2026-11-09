# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Definitions and fixed-point setup (1 point):** Correctly identifies the invariant law, empirical measure, collage residual, sampling error, and the fixed-point identity for the contractive transfer operator.
2. **Empirical-to-invariant comparison (2 points):** Applies the triangle inequality and transfer-operator contractivity to obtain W2(pi_theta, rho_n) <= kappa_theta W2(pi_theta, rho_n) + r_n(theta).
3. **Central fixed-point rearrangement (5 points):** Correctly uses kappa_theta < 1 to isolate the distance and derive W2(pi_theta, rho_n) <= r_n(theta)/(1-kappa_theta), with all metric and operator arguments valid.
4. **Final generalization bound (2 points):** Applies the second triangle inequality and identifies the sampling term to conclude W2(pi_theta, rho) <= r_n(theta)/(1-kappa_theta) + s_n.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The contraction/rearrangement step is theorem-critical; naming contractivity without deriving the residual inequality is insufficient.
