# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct core step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important obligations remain missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted details.
- **10:** Fully correct.

# Core Steps

1. **Normalized coefficient expansion and Gaussian evaluation — 2 points.** Establishes the coefficientwise expansion with the correct training and population normalizations, using the empirical loss as the gradient-flow driver in both cases. Correctly evaluates the Gaussian averages or uses an equivalent rigorous method, explains the resulting polynomial supports, and obtains the variance exponent. Any use of Wick pairing must verify the independent centered Gaussian covariance structure. No analytic convergence of an infinite averaged Taylor series is required.

2. **Realizability and noncancellation — 3 points.** For every allowed s_D, q_n, and q_m, proves that a monomial with q_sigma=2(s_D+1) and q_p=s+s_D-q_n-q_m+1 occurs. A diagrammatic proof must justify both the availability of its merged ring and a complete edge pairing, including the separate surviving p-index leaves; simply declaring that the remaining p-indices are paired is insufficient. Explains why contributions to a collected monomial cannot cancel. Accept an equivalent construction or algebraic proof.

3. **Exact Pareto characterization and population/train distinction — 3 points.** Supplies a valid global exponent bound and proves both directions of the characterization: the listed exponents are undominated, and every other exponent is dominated by a listed one. In the reference route this is the connected quotient-graph bound followed by comparison with a realized frontier point having the same variance, latent, and sample coordinates. Correctly accounts for the distinct normalization factors and proves that precisely q_m=0 is absent for population orders s>=1. Handles s=0 and establishes P_0=widehat P_0. An equivalent optimality argument receives full credit; the particular graph method is not mandatory.

4. **Geometry and formal regime classification — 2 points.** Identifies the triangle-times-interval geometry, with training prisms nondegenerate for s>=1, population prisms nondegenerate for s>=2, and triangles at the remaining orders. Matches all five named scaling conditions to the correct facets by maximizing the monomial weights, proves that no additional basic facets/regimes occur, and explains lower-dimensional nonempty face intersections. Applies the classification to the joint formal coefficient hierarchy rather than claiming five distinct facets at every individual order or asserting unproved trajectory convergence.

# Evaluator Notes

Accept a complete valid alternative proof and do not require the reference proof's incidental notation or presentation. A proof of exact support geometry must not receive full optimality credit merely for showing that the listed points cannot be dominated; it must also exclude other Pareto points. The population deletion must be justified together with the different sample normalization, not inferred from the informal statement that one factor lacks data edges.

The five regime names are defined by scaling conditions in the task. Full geometry credit requires their mathematical correspondence with facets, not just listing the names. At training order zero and population orders zero and one, the height coordinate is fixed; recognizing these cases is correct, not a contradiction to the repaired task.

All leading sets are defined from collected symbolic monomial supports. Do not require absence of cancellation after numerical specialization of dimension or variance parameters. Do not award extra obligations for convergence of limiting trajectories, spectral formulas, or the solution of particular learning regimes: these are outside the task. The reference proof has no unresolved theorem-critical obligation.
