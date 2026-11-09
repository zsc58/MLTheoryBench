# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly reduce the bias-free ReLU controller to the two effective gains, derive the discounted two-state quadratic cost representation on the buffered stability set, and identify the unique optimal scalar LQR gain.
- **2 points:** Establish the gain-space analytical properties needed for descent: smoothness, the performance-gap/quadratic-growth bound, the PL inequality, and a uniform gradient bound. Justify the gain-gradient and performance identities for sign-switching trajectories, including the discounted second-moment occupancy weights. A specialized external policy-gradient corollary is not by itself a proof of PL unless its applicable statement and hypotheses are established; a direct derivation is acceptable.
- **3 points:** Prove the high-probability initialization and weight-dynamics control, including Gaussian backbone lower bounds, bounded weight mass, radius/displacement induction, and a quantitative sign-crossing error bound. The bad-set thresholds must apply to the cutoff defined in the task. Merely naming concentration or sign stability earns little credit.
- **2 points:** Derive the neural update decomposition into gain-space descent, second-order remainder, and crossing error, and show that the benign-regime inequalities absorb these perturbations while preserving the buffered stability set for all iterates. Handle a zero first-layer weight consistently with the specified derivative convention.
- **1 point:** Combine smoothness and PL descent to obtain the stated factor rho_m^k and use quadratic growth to prove the explicit convergence bound for both gains, with probability at least 1-e^{-C_0 m} and for every iteration.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat unsupported assertions of the switched-system gradient or performance identities as gaps in the gain-space step; either a direct calculation or an audited result with verified hypotheses can close them. Treat omission of the sign-crossing control or replacement of the benign-regime induction by an unsupported appeal to a named method as a theorem-critical gap. A bound for the crossing error at step k+1 must not be assumed before the cumulative gradient path through that step has been established.
