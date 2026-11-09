# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Experiment, estimator, and bias control (2 points).** Uses the full historical buffer and corrected estimator, symmetric feasible queries, predictable centers, zero initialization, and the average queried-loss regret. Establishes finite-difference control and a summably small expected comparator-bias contribution, and accounts for the shrunken-domain comparator. A valid bound is coordinate error at most L delta/2 and Euclidean conditional bias at most sqrt(d)L delta/2. The smaller dimension-free vector bias asserted in the old reference is not required.

2. **Historical-coordinate analysis (2 points).** Establishes the joint matching law for a specified coordinate and positive historical index, its initialization term, and the needed historical moment estimates. Distinguishes this joint probability from the marginal law of the matching time. Verifies an O(d) maximal expected prediction-error bound. Coupon-collector calculations are optional for this target; if used, they must cover small dimensions correctly.

3. **Gradient-variance conversion (3 points).** Obtains E[Vbar_T]<=C(dW_T+d^2) for linear losses by deterministic centering and historical-coordinate summation. Obtains Vbar_T<=C(d^2W_T+d^3) for convex losses, for example by observing that each positive matching time has at most one successor and zero occurs at most d times. Uses the task's supremum variance rather than substituting a random terminal mean into an identity requiring deterministic centering.

4. **Regret conversion in all regimes (3 points).** Justifies the prescribed adaptive linear/convex schedule and derives both square-root rates. Separately supplies a valid argument for eta_t=1/(lambda t) and the strongly convex rate O((d/lambda)log(2+dW_T)), with constants uniform in lambda and without an extra log d at arbitrarily small W_T. The reference accomplishes this through explicit projection algebra, a bounded-loss prefix, harmonic tail summation, and a lower bound on the supremum variance derived from strong convexity. These particular presentation choices are not mandatory, but a bare assertion of a standard logarithmic inequality or direct substitution of the coarse initialization term does not complete this step.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its optional sampling-gap discussion. Allocate partial credit within each core step for correct substantial components.

All three curvature regimes are required for full credit. The definition of W_T, the information timing, the actual estimator, the specified step sizes, and the queried-loss regret are part of the theorem contract. Proving only a modified algorithm or a realized-variance statement does not establish this task.

Elementary boundary handling is required: d=1, T=1, zero prediction error, and small variance cannot be excluded by importing the source table's nondegeneracy convention. A proof may use routine equivalent logarithmic baselines. No credit depends on proving the incorrect numerical constants or vector-bias rate in the unrepaired source.

The replacement reference proof explicitly closes every theorem-critical obligation; there is no unresolved private GT dependency.
