# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Identifies the oracle and feasible posteriors, their empirical centers, the common covariance \((n\omega V_0)^{-1}\), and both \(o_P(1)\) BvM errors.
2. **2 points:** Uses the center-shift bound explicitly assumed in (A3), \(\|\hat\theta_{\mathrm{fe}}-\hat\theta_{\mathrm{or}}\|=O_P(r_n^2)\). Merely naming orthogonality without using this bound earns little credit.
3. **4 points:** Derives the equal-covariance Gaussian KL expression or an equivalent bound and obtains \(O_P(\sqrt n\,r_n^2)\) Gaussian total variation.
4. **2 points:** Applies the triangle inequality for the posterior bound and establishes total-variation convergence and feasible-centered BvM inheritance when \(r_n=o_P(n^{-1/4})\).

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the solver to derive the center-shift estimate from orthogonality or an external result: it is an explicit (A3) assumption. The nuisance rate may be random, and the little-o rate in the final condition is in probability.
