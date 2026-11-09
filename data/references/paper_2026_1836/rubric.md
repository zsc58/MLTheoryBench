# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (2 points):** Derives the coordinate-restricted smoothness/descent inequality for an axis pushforward from the stated projected coordinate-smoothness assumption. Uses the Wasserstein differential along the pushforward path and bounds the pairing using U_i on the gradient difference, obtaining the quadratic remainder L_i||U_iT||^2/2. Does not assume a full-gradient Lipschitz bound or that the displacement is an optimal transport map.
- **Step 2 (3 points):** Applies probabilities p_i=L_i/L_sum and steps 1/L_i, averages the coordinate decrease inequalities, and uses orthogonality to obtain conditional decrease ||grad_W E[mu_k]||^2/(2L_sum). Telescopes and bounds the pathwise minimum by the arithmetic average to establish the expected-minimum stationarity bound, with expectation outside the minimum. Establishes pathwise monotonicity and thus E[mu_K]<=E[mu_0].
- **Step 3 (2 points):** In the geodesically convex case, uses an optimal coupling, Cauchy-Schwarz, and the infimum distance to the minimizer set to obtain gap<=R_0||grad_W E||. Derives the expected reciprocal-gap recurrence and the bound 2L_sum R_0^2/K. Does not require a nearest minimizer to exist, and handles a zero expected gap before taking reciprocals.
- **Step 4 (3 points):** Derives the m-PL inequality from m-strong geodesic convexity using the optimal-coupling inequality and Young's inequality or completing the square. Under PL, combines it with conditional expected descent to obtain the factor 1-m/L_sum and the stated expected-gap bound. Handles zero initial gap separately or otherwise justifies nonnegativity of the contraction factor; includes the case m=L_sum without adding a new public assumption.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Naming coordinate descent, smoothness, convexity, or PL without deriving the anisotropic expected-decrease mechanism is insufficient.

The coordinate smoothness hypothesis controls only the projected gradient difference. A proof that silently substitutes an unprojected full-gradient bound has not established Step 1 under the stated assumptions. It is enough to justify the velocity-field chain rule for the relevant pushforward path; reproducing the reference proof's conditional-velocity construction is not mandatory if an equivalent valid justification is given.

The public target is E[min_k ||g_k||^2], not min_k E||g_k||^2. A valid proof of the latter, stronger bound is acceptable when it also explains or uses E[min_k ||g_k||^2]<=min_k E||g_k||^2. Do not require that stronger bound.

The bounded-sublevel condition is required only in the geodesically convex branch. The global minimizer need not be unique, and its distance from a given iterate need not be attained. Do not require an assumption m<=L_sum: positive initial gap forces it through the descent/PL inequality, while zero initial gap is already solved.

Minor omissions of routine zero-gap cases may warrant the 8-9 range under the scoring guide; they must not be treated as counterexamples to the public theorem. Full credit requires the strong-geodesic-convexity branch as well as the PL branch. The source's erroneous equality in conditional averaging and its incorrect attribution to Jensen are not required or accepted as mathematical steps.
