# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Replay identity and factorization (2 points).** Derives the replay log-sum-exp identity with an additional partition term, subtracts the retained-duplicate baseline, and proves the susceptibility factorization. Justifies averaging the remainder despite the unbounded Gaussian generator. For the quantitative target, obtains a remainder constant independent of sufficiently large beta after allowing a beta-dependent epsilon threshold, or proves an equivalent bound.
2. **Rotation-averaged energy rise (2 points).** Uses stationarity and the Gaussian skew covariance to compute the second-order rotation coefficient, and derives or otherwise correctly controls its dependence on off-memory weights. Tracks beta factors when passing from a fixed-beta Taylor expansion to a large-beta comparison. An unqualified leakage remainder cannot be treated as beta-uniform without justification.
3. **Localized branches and rise comparison (3 points).** Uses the branches converging to their indexed memories to justify the outlier and cluster softmax-weight estimates, including the relative estimates for exponentially small weights. Shows that the cluster and outlier rotation coefficients approach the same positive limit and that their difference is strictly positive for large beta. A local contraction argument closes existence and uniqueness in the reference proof, but it is not a separately required contribution if the solution validly works with the branches specified in the task.
4. **Susceptibility hierarchy and final ordering (3 points).** Obtains the five susceptibility scales, proves the strict self-replay comparison by controlling its difference rather than merely its common leading term, and proves all three divergent ratios and the cross-type ratio-one limit. Transfers coefficient comparisons to actual gains for each sufficiently large fixed beta and sufficiently small positive epsilon. Uses the public task's epsilon-first iterated limits.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, exact intermediate notation, or a particular method of establishing localization.

The fixed configuration is not allowed to vary with beta. In particular, c approaching an endpoint or N growing with beta is outside this task. No assertion about the opposite iterated limit, with beta tending to infinity at fixed positive epsilon, is required or sufficient.

The replay memory is counted as an additional copy at the identity rotation. A proof that silently removes that duplicate changes the quantity being proved.

Convergence of a branch to its memory alone cannot be substituted into an exponential and used to claim a relative 1+o(1) weight estimate; the needed beta-scaled control must be justified. Likewise, a pointwise Taylor estimate with an uncontrolled random constant does not by itself justify averaging.

The first strict replay gap is exponentially small in beta. Common leading-order self-replay formulas do not establish its sign, and small-epsilon remainders must be handled with the stated beta-dependent thresholds. Neither a beta-independent epsilon threshold nor a particular explicit joint scaling is required.

The private proof contains no unresolved obligation. Award full credit to any proof that establishes the complete public contract, even if it bypasses the reference proof's Hessian or susceptibility organization.
