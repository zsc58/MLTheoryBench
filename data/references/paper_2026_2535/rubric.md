# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Centering and RKHS risk representation (2 points):** Correctly express empirical MMD as the squared RKHS norm of the average centered feature and take its expectation.
2. **Exact lag expansion (3 points):** Expand the Hilbert norm, use stationarity and lag symmetry, and count ordered pairs to derive the finite-sample risk identity.
3. **Finite-sample ESS (1 point):** Substitute the exact risk into the ESS definition, including the zero-risk/infinite-ESS convention.
4. **Long-run limit (3 points):** Use absolute summability and a justified dominated-convergence argument to obtain \(nR_n\to\sigma_k^2\ge0\) and the positive-\(\sigma_k^2\) ESS ratio.
5. **Degenerate case (1 point):** Establish \(R_n=o(n^{-1})\) and divergence of ESS/n along positive-risk indices when \(\sigma_k^2=0\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
