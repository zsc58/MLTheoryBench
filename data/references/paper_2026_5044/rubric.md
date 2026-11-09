# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes the empirical Wasserstein expectation dual over gamma greater than or equal to zero, with a valid justification of strong duality and the empirical supremum terms. The reference proof supplies an explicit finite-empirical transport-budget argument, including finiteness and the connection between conditional transport laws and the Wasserstein constraint. An equivalent rigorous derivation is acceptable.
- **2 points:** Justifies restricting the infimum to gamma greater than one. Shows divergence below one, finiteness above one, and that the value at one is obtained as the right limit, including extended-real boundary cases. Does not assume every dataset has a point outside the centroid convex hull or that an interior dual minimizer always exists.
- **3 points:** Establishes the simplex identity, correctly justifies any minimax exchange, and evaluates the quadratic supremum to obtain the displayed minimum, including attainment on the closed simplex. An invocation of the standard continuous convex-concave minimax theorem is sufficient when its relevant statement and hypotheses are supplied and checked. Alternative direct arguments receive equal credit.
- **2 points:** Uses local optimality in the free center coordinates and the interior gamma coordinate to derive both displayed first-order conclusions. Divides by cluster mass only when positive and selects the positive root using gamma greater than one and r greater than zero. Does not require assignment coordinates to be strictly positive.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's exact organization or auxiliary notation. Merely naming Wasserstein duality or a specialized external dependency without a derivation closing its required use is not a completed strong-duality step. Merely naming minimax without checking the relevant compactness, convexity/concavity, and continuity hypotheses is likewise insufficient.

The public task defines WC directly using the nearest-center loss. A partition-reduction proof is optional context and must not be required for full credit. Likewise, a proof of the convex-hull characterization of endpoint finiteness, the constrained barycentric formula at the endpoint, a saddle-support characterization, or a worst-case-distribution construction is not independently required when all displayed public claims have been established.

Assignments may lie on simplex faces. Local minimality is relative to the displayed feasible set; only the robustness parameter is required to be interior in an inequality-constrained coordinate. If all residuals vanish, the positive gamma derivative excludes an interior local minimizer rather than invalidating the conditional conclusion. Empty clusters impose no centroid quotient condition.

Treat omission of either optimality conclusion or of a justification for excluding the boundary gamma=1 from the infimum as theorem-critical. Do not demand global optimality of a given local minimizer, uniqueness of assignments, distinct centers, an iid sampling model, a generic-position assumption, or hypotheses from the separate concentration and convergence results. An arbitrary best-response assignment at a maximizing point is not automatically a saddle assignment; if that assertion is used, the missing maximizing condition must also be verified.
