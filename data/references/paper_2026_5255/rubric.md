# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the stated objective's convexity, Lipschitz bound, and exact minimizer set, including that every matrix entry other than the first two diagonal entries is unrestricted at minimizers.
- **2 points:** Correctly reduces each matrix iteration to signed momentum on the two diagonal coordinates. Justifies the subgradient and momentum support and the polar-factor-to-sign identity under the rank-sized SVD convention, including zero entries. Correctly expresses the regularized effective step as a function of the matrix-gradient history, or of the vector-gradient history through its diagonal embedding.
- **4 points:** Gives a rigorous measure-zero exceptional-set argument for an arbitrary fixed history-dependent rule and establishes the low-momentum sign-dominance mechanism. In the reference route, this requires countability over finite gradient/sign histories, inclusion of the empty history, a noncircular induction excluding zero difference coordinates, and a correct momentum estimate using beta<1/2. Merely asserting genericity or naming an invariant is insufficient. An equally rigorous alternative argument receives full credit.
- **2 points:** Establishes preservation of the nonzero sum coordinate and a uniform positive objective gap, or an equivalent obstruction, and correctly concludes nonconvergence to a minimizer for both algorithms outside the exceptional set and for every permissible subgradient selection.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The functions defining the steps are fixed before initialization, but their values may depend on the entire indicated gradient history, including the current gradient. The exceptional set may depend on the fixed rule and algorithm; it need not be uniform over all rules. Do not impose monotonicity or measurability on the step functions.

For Algorithm B, positivity of the original step does not imply positivity of its effective step on arbitrary exceptional trajectories, since the momentum may vanish there. No proof of such global effective-step positivity is required. Along the non-exceptional trajectories in the reference proof, momentum dominance establishes that the effective steps are positive.

If momentum is unrolled, the correct weight attached to the time-j gradient or sign at time t is beta^(t-j), not beta^j. A proof using the recurrence directly to establish the same bound is equally valid. The endpoint beta=0 is included; beta=1/2 is not.
