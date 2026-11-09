# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Convex simplex formulation and convexity (2 points):** Rewrites the objective as $-\sum_i q_i\log(1+e^\beta r_i)$ on the probability simplex, respects the continuous extension at zero, and correctly establishes convexity. Existence of a minimizer may be established by continuity and compactness or by constructing and verifying an optimizer later.
2. **KKT threshold characterization (4 points):** Justifies valid KKT conditions, handles active and inactive coordinates, establishes positivity of the normalization multiplier before dividing by it, and derives $r_i=(q_i/\zeta-e^{-\beta})_+$, equivalently the thresholded form. The argument must allow $q_i=0$ and must not rely on an undefined quotient such as $0/0$. Merely naming KKT or thresholding earns no credit for this step.
3. **Normalization and cutoff equation (2 points):** Uses the simplex normalization to obtain $\tau=e^{-\beta}\sum_i(q_i-\tau)_+$ and the stated rescaling formula.
4. **Existence, uniqueness, and optimality conclusion (2 points):** Proves the cutoff is uniquely defined in $(0,\max_i q_i)$, including the needed continuity and endpoint signs and a valid strict-monotonicity argument or equivalent reasoning. Establishes global optimality by verifying the constructed solution's KKT conditions, by a direct convexity inequality, or by combining existence of a minimizer with the exhaustive characterization. Correctly interprets the formula as subtracting the cutoff, truncating at zero, and normalizing.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or named optimization machinery if an elementary argument closes the same obligations.

The allowed cases include $K=1$, zero empirical masses, repeated masses, and masses exactly equal to the cutoff. A uniform argument covering these cases suffices; separate case calculations are not required. Finite real $\beta$ is arbitrary, and no limiting analysis in $\beta$ is requested.

Distinguish a small omitted justification, such as an otherwise immediately recoverable multiplier-positivity argument, from reliance on an invalid division that leaves an allowed case unproved. Apply the overall scoring guide accordingly.

The threshold formula generally changes the relative proportions of surviving empirical masses. Merely deleting low-mass coordinates and normalizing the original surviving $q_i$ is not the claimed optimizer.
