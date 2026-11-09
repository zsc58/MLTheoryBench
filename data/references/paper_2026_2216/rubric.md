# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the separated-action gap argument, proves T_delta is contained in X*, and proves Bellman invariance of the tube. A proof of the stronger contraction into T_(gamma delta) is sufficient but that stronger inclusion is not separately required.
- **3 points:** Rigorously connects the actual nonlinear Bellman error to dynamics transverse to the constant direction and identifies the projected Euclidean norm with distance to X_1. In the reference route, this includes deriving the exact stochastic-policy error recursion and its projection.
- **3 points:** Establishes the projected JSR upper bound by gamma and obtains a uniform estimate at every rate bar-rho+epsilon for the relevant transverse dynamics. In the reference route, this includes the projection-product identity, uniform deterministic product bounds, a justified common Lyapunov norm, and extension to stochastic-policy matrices. An equivalent rigorous product-based argument is equally acceptable.
- **2 points:** Obtains the stated exponential distance bound with a constant independent of the initialization and iteration index, then proves finite-time tube entrance and permanent optimal greedy-policy identification, including zero initial transverse distance.

# Evaluator Notes

Accept a complete valid alternative proof and allocate credit by the mathematical obligations above, not by incidental presentation choices. A solver need not construct the reference norm or introduce stochastic policies if another valid argument controls the actual nonlinear iteration at the claimed JSR-based rate.

If a proof uses stochastic-policy dynamics, a bound for deterministic modes alone is insufficient unless the proof justifies why it also controls those dynamics. Likewise, a common-norm construction must justify convergence, the norm or convexity property actually used, and the contraction estimate. These are substantive obligations, though elementary algebra may be compressed in an otherwise complete argument.

The public task explicitly requires tube inclusion and invariance; proving only eventual membership along one trajectory does not discharge the set-invariance claim. Do not require or award an assertion that X* itself is invariant, since this is not generally true. Permanent identification is guaranteed after tube entrance, not necessarily after the first iterate whose greedy policy happens to be optimal.

Neither strict inequality bar-rho<gamma, uniqueness of an optimal policy, nor any irreducibility or mixing assumption is required. Do not require an explicit logarithmic entrance-time formula. Treat a missing bridge from the matrix-family estimates to the actual nonlinear dynamics, or a missing tube-invariance argument, as theorem-critical unless a valid alternative argument supplies the same obligation.
