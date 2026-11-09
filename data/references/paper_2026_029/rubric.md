# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Discrete transport lower certificate (3 points).** Derives the least-star-shaped-majorant formula needed for positive arguments, constructs admissible finite perturbation couplings of the empirical atoms with the correct cost orientation d(y,x_i), and optimizes independently over radii and perturbation points. Proves the finite-p lower bound and the p=infinity endpoint. Infinite suprema must be handled by arbitrarily large finite increments or an equivalent rigorous approximation, not by assuming an infinite loss value is attained.
2. **Coupling/Jensen upper certificate (3 points).** Starts from an arbitrary admissible law with a defined extended loss expectation and a near-optimal coupling in Pi(Q,P_N). Justifies reduction to empirical components, or uses a valid equivalent argument on the stated measurable space. Bounds increments by the maximal rate, establishes the needed concave-majorant properties, and applies Jensen with its hypotheses checked. Handles both finite p and p=infinity, nonattainment of optimal transport, right limits, zero transport moment, and extended values. Continuity at positive arguments is applied only after establishing finiteness of the relevant concave majorant; an infinite certificate makes the corresponding upper inequality immediate.
3. **Exponent dynamics (2 points).** Proves the Wasserstein risk ordering and both certificate orderings for 1<=p<=p2<=infinity. Uses the same directed cost and coupling marginals for the Wasserstein comparison. Derives the concave-composition comparison for the finite-p upper certificates and handles the infinity endpoint using the correct right limits. Equality cases, including both exponents equal to infinity, must be covered.
4. **Finite-p dichotomy (2 points).** Uses positivity of the empirical weights and finiteness of the empirical index set to pass from finiteness of lb_p at one positive radius to finiteness of the maximal star-shaped majorant there. Produces a single finite affine majorant valid on the whole nonnegative half-line, or another valid global argument, and concludes simultaneous finiteness at every positive radius of the lower certificate, upper certificate, and robust excess risk. Proves the all-infinite alternative using the lower certificate. The zero-growth case must also be valid.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular measurable-partition construction. Standard elementary measure-theoretic and concavity facts may be used with their relevant hypotheses verified. However, merely naming the paper-specific majorant machinery or a specialized method does not establish the central reductions.

The cost is not assumed symmetric. Reversing coupling marginals while retaining the same cost is not justified. The space is not assumed standard Borel and singletons are not assumed measurable; an argument using conditional measures must be valid under the given finite-empirical setup or be replaced by an equivalent valid reduction. No measurable optimizer selection over a continuum of empirical points is needed.

Do not impose boundedness or global integrability of the loss, continuity of rate functions, or attainment of transport infima or pointwise suprema. The public expectation convention excludes only the undefined infinity-minus-infinity case and allows either defined infinite expectation. A claim of affine domination merely on each bounded interval does not by itself imply that a global least concave majorant is finite.

Propagate a missing lower or upper certificate dependency to downstream conclusions only when they are genuinely unsupported. Preserve credit for independent correct arguments. Readily repairable notation or endpoint omissions should be distinguished from using an unstated substantive hypothesis.
