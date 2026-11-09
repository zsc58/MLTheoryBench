# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly constructs the pair-coordinate lift, including its embedding in $Q_n$, proves that the fibers are nonempty and that the induced graph is $(k-1)$-regular, and provides exactly $k$ distinct coordinate groups. Covers $k=2$, where the unmodified incident-coordinate groups coincide; an unused padded coordinate can distinguish them without changing their relevant graphs.
2. **3 points:** Proves the lower bound: each group-relevant graph is a disjoint union of stars with deterministic optimum one, and a density or direct averaging argument forces some fixed vertex to have expected total out-degree at least $(k-1)/2$ for any randomized orientation. Identifies a group containing all incident edges of that vertex and obtains the price consequence. It is enough to use the elementary lower-bound direction of the orientation-density result.
3. **3 points:** Establishes the simultaneous suitable-vertex property, for example through the coordinate-counting inequality with factor $2\sqrt n$, the restriction of each violating group to incident coordinates, density monotonicity, and a contradiction. Correctly handles isolated vertices and vacuous group constraints.
4. **2 points:** Produces a single deterministic orientation with all required group bounds. In the reference peeling argument, edges must point from earlier to later removals, so the current relevant degree equals the final relevant out-degree. Uses induced-subgraph density monotonicity and $\rho(G^S)\le\operatorname{opt}_S(G)$ to obtain the price bound for eligible groups. Respects the empty-graph conventions and the domain of the price.

# Evaluator Notes

Accept a complete valid alternative proof and award equivalent credit for the same mathematical obligations. Do not require the reference construction's choice of distinguished fiber label, its notation, or use of the full external orientation-density theorem.

A missing lower construction, missing justification for the universal orientation, or missing conversion to the price bound is theorem-critical unless replaced by a valid alternative argument. The particular coordinate-counting presentation is not mandatory when another complete argument proves the same claim.

The denominator is a deterministic optimum; do not replace it by the randomized optimum. The price need not be at least one. The maximum over vertices is outside expectation, and the lower-bound vertex must be chosen for the distribution rather than separately for each realized orientation.

The lower target requires distinct coordinate sets, not distinct relevant edge sets. Distinguishing the two groups by an inactive coordinate when $k=2$ is valid. Do not count repeated copies of the same coordinate set as different members of the family.

Under the public out-degree convention, directing edges toward earlier removals does not justify the current-degree identity. Full credit requires a correct direction or a separately valid alternative argument. Likewise, a sum of the fiber labels cannot be excluded by asserting that its parity is odd, and equality with density does not hold for an arbitrary orientation. Readily repairable local slips or omitted boundary cases should be assessed under the 8-9 band rather than treated as complete proofs without repair.
