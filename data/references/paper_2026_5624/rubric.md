# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the strategic-risk decomposition, including the zero-intercept consequence, and proves the universal irreducible lower bound for every support and every nonnegative ridge parameter. Any existence claims used for the benchmark minima must be valid.
- **2 points:** Establishes the support-restriction decomposition \(\mathcal V(J)-\mathcal V=p(J)-[g([d])-g(J)]\) by completing the covariance quadratic and minimizing the resulting support objective. Covers the full support and the empty support, whose predictive loss is \(\beta_0^T\Sigma\beta_0\), not generally zero.
- **4 points:** Proves the fixed-support scalar-ridge approximation controlled by the stated \(B_C(J)h(J)^2\). The reference route derives the generalized-ridge oracle condition, compares it with the ordinary-ridge path in whitened coordinates, and converts distance to objective excess with valid constants. Establishes the existence of the oracle and finite-parameter attainment of the displayed ridge minimum, and remains valid when the restricted signal or heterogeneity is zero.
- **2 points:** Correctly combines the support and scalar-ridge terms to obtain the upper bound for every support and both exact \(\epsilon\)-optimality consequences, with an actual finite ridge parameter.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or separate case splits when an argument already covers the boundary cases uniformly. A claim that ordinary ridge is close to the support oracle without deriving a bound controlled by the stated heterogeneity quantity does not satisfy the third core step.

Continuity alone does not establish that a function on \([0,\infty)\) attains its minimum. A correct proof must justify finite-parameter attainment of the minimum appearing in the claim; an elementary argument from the ridge closed form is sufficient. Likewise, strict convexity alone does not establish existence of a minimizer, although coercivity of the displayed support objective readily does so. Treat an otherwise correct proof's omitted routine attainment argument as a repairable omission, not as evidence that the theorem is false.

An infimum bound alone must not be used to assert an exact finite-parameter \(\epsilon\)-guarantee without an attainment or finite-witness argument. A direct finite witness is sufficient for that consequence, while the minimum appearing in the theorem must also be well-defined. No assumption of positive signal, positive heterogeneity, independent projection residuals, diagonal matrices, or commuting covariance and inverse-cost matrices may be introduced. The retained manipulation matrix is \((C^{-1})_{JJ}\), not \((C_{JJ})^{-1}\).

Do not require additional results about quantitative irreducible-gap bounds, exact ridge-optimality characterizations, two-level costs, algorithms, or cost uncertainty; those are outside the frozen claim.
