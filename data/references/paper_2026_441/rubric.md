# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly expands the normalized recursion through second order and obtains the drift correction. Controls the accumulated remainder and establishes uniform-path proximity to a properly regularized truncated scheme, for example by a martingale maximal estimate and discrete Gronwall. A direct tightness and generator proof for the exact chain is an equally valid alternative.
- **2 points:** Computes the limiting joint conditional covariance, identifies the common-matrix-noise SDE using a diffusion or martingale-problem argument with its hypotheses verified, and proves sphere invariance and uniqueness/nonexplosion as needed. If a nonspherical truncated scheme is used, its ambient drift must be handled correctly before restricting to the sphere. The radial Itô calculation must retain the off-sphere martingale term or be replaced by a valid alternative invariance argument.
- **2 points:** Derives the closed overlap drift and quadratic variation for both interaction rules, including the common-noise quadratic covariation, and correctly relates overlap limits to the clustering events. In the normalized rule the Brownian coefficient is sqrt(2)rho(1-r^2)sqrt(e^{2theta}+e^{2theta r})/(e^theta+e^{theta r}); equivalently, its quadratic-variation rate has the corresponding factor 2. A state-dependent time-change argument is acceptable if justified.
- **3 points:** Rigorously establishes the endpoint scale asymptotics or an equivalent boundary analysis, the strict threshold d-2<cosh(2theta), finite-time endpoint inaccessibility, and exhaustive endpoint convergence and probabilities. Handles the equality case, d=2, theta=0, and the absorbing endpoint initial states. Merely taking limits of finite-level hitting probabilities without justifying long-time convergence is insufficient for full credit.

# Evaluator Notes

Accept any complete valid alternative proof; do not require an auxiliary truncated recursion when the exact-chain argument closes the same obligations. Merely naming diffusion approximation or boundary classification without checking the required characteristics, well-posedness, or endpoint integrability does not earn the corresponding full step.

A supremum of pointwise mean-square errors does not by itself imply convergence in probability in the uniform path metric. A maximal estimate, tightness argument, or another valid replacement is needed.

The second-order truncated drift at an ambient configuration is rho^2||a_i||^2(3||x_i||^2-d-2)x_i/2. Its restriction to the sphere is the target drift. Do not require a proof to identify these two ambient formulas; they are not equal away from the sphere.

The missing sqrt(2) in the source's normalized overlap coefficient is an audited local source error and must not be treated as the scoring ground truth. At theta=0 the normalized and averaged models are identical, providing a useful consistency check. A failure to derive or otherwise validly establish the overlap diffusion leaves the phase-transition argument unsupported.

Minor algebraic errors may receive substantial credit when they are locally repairable and do not alter the final threshold or conclusions. Award full credit only when the proof actually supports both interaction rules and the full stated convergence and clustering claims.
