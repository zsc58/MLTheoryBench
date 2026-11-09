# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Gaussian-convolution approximation (2 points).** Truncate and renormalize an arbitrary density, mollify by a narrow Gaussian, and prove the resulting element of \(\mathcal G\) is arbitrarily close in \(L^1\).
2. **Score regularity and flow construction (3 points).** Represent the VP marginal of the selected Gaussian convolution as a Gaussian mixture, derive the score-Hessian identity, bound the posterior covariance using the compact support, and obtain a finite bound uniformly over every finite interval including \(t=0\). Establish the continuity equation for the VP marginal and use the characteristic/Jacobian identity to prove that the probability-flow ODE transports the initial density to the marginal. Then construct the global bi-Lipschitz \(C^1\) flow and its inverse.
3. **Gaussian-limit pullback (3 points).** Apply the finite-second-moment VP KL estimate, Pinsker, and bijective pushforward invariance to prove convergence of the inverse Gaussian pullback to the selected convolution density in \(L^1\).
4. **Universal conclusion (2 points).** Combine the two approximation errors with a triangle inequality, retaining the asserted score regularity and bi-Lipschitz properties, to obtain the stated result for every density and tolerance.

# Evaluator Notes

Accept a complete valid alternative proof. The score-Hessian calculation and the continuity-equation/characteristic transport bridge are theorem-critical obligations; they may be established by equivalent arguments. Do not require the reference proof's incidental presentation choices.
