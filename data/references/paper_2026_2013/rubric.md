# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Aligns labels, defines the two misclassified masses, establishes total error t<=n/2, and uses the two-ball separation geometry. Equivalent parameterizations are acceptable.
- **3 points:** For squared loss, establishes an additive merge comparison retaining the separate subgroup costs, proves the balance-dependent bound M>=bt, controls the within-ball saving by 4R^2 per error, and obtains strict positivity from bm^2>4R^2. ANOVA with subgroup means is one valid route; their membership in the respective balls must be justified. A raw cross-pair lower bound alone does not establish the required additive comparison.
- **3 points:** For one-dimensional absolute loss, proves the separated-interval merge penalty, establishes the merge-count bound P>=2bt, controls deletion savings by 2R per error, and obtains strict positivity from bm>R. After ordering n_1<=n_2, the identity P=min(n_1,t) supplies a complete counting argument. Nonunique medians do not obstruct the proof.
- **2 points:** Concludes uniqueness of the partition up to labels in both cases and supplies explicit finite configurations with objective comparisons proving both necessity orders. Universal positive constants and a sufficiently small positive balance cutoff must be justified; their numerical values need not match the reference proof.

# Evaluator Notes

Accept any complete valid alternative proof. A named method or asserted paper-specific inequality without its required derivation does not satisfy a core step. Propagate a failed counting or merge estimate only to the affected loss case.

The two sufficient conditions are independent. Do not require the squared-loss condition in the absolute-loss proof. Centers are unconstrained continuous centers, not medoids, and the benchmark anchors need not be optimal centers. Only partition uniqueness is claimed.

Competitor cells are nonempty, but their intersections with benchmark clusters can be empty. A complete argument must handle these cases without taking the mean of an empty set; using the benchmark anchor completes the deletion estimates. The sufficient statements include R=0. Necessity is requested only for R>0 and sufficiently small feasible rational balances.

For the lower bounds, it suffices to compare the benchmark's exact profiled value with the cost of a feasible competing partition and feasible centers. The competing centers need not themselves be optimal. Preserve the exact ratio n_2/n_1=(1-b)/b when making finite-sample comparisons; an asymptotic substitution alone is not a proof of a finite inequality. Repeated locations are allowed, and integer cluster sizes, including any needed divisibility, must be realizable.

All obligations in this rubric are closed in the replacement reference proof; there is no unresolved private dependency.
