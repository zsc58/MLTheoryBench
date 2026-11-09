# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly reformulates the temperature objective as Euclidean projection onto the hypersimplex and establishes existence and uniqueness. Addresses the singleton case `k=n`, including `n=1`, explicitly or through a valid general argument.
- **3 points:** Establishes a complete optimality argument supporting the projection characterization. The reference route obtains the common-shift clipping representation and verifies that some shift enforces the sum, without assuming multiplier uniqueness. Award equivalent credit for an alternative argument that establishes the same needed optimality conclusions.
- **2 points:** Proves that sorted scores yield sorted projected coordinates, including ties and the singleton feasible case. Monotonicity of clipping is one valid route; a complete exchange argument or other valid proof is equally acceptable.
- **1 point:** Correctly concludes that the same point is the unique minimizer over the bounded, prescribed-sum monotone feasible set.
- **2 points:** Justifies the requested PAV-based computation with both the box constraints and the prescribed sum enforced, and proves its `O(n log n)` running time. The reference route uses bounded PAV on commonly shifted sorted data and an exact breakpoint sweep to find the shift. An alternative valid constrained-PAV implementation or a valid reduction to PAV with the same total bound earns full credit.

# Evaluator Notes

Accept complete valid alternative proofs and redistribute the mechanism-specific credit as appropriate; do not require KKT or clipping merely because the reference proof uses them. A solver must nevertheless justify every conclusion in the public task.

Ordinary PAV on the unshifted sorted data, even followed by clipping, need not enforce the prescribed sum. Merely naming a bounded, fixed-sum PAV theorem without an applicable statement and verified hypotheses does not close this obligation. A valid independent exact projection algorithm may supply useful partial progress, but it does not by itself establish the specifically requested PAV computation unless its connection to an appropriate PAV procedure is justified.

For a breakpoint implementation, equal events must be handled consistently and flat intervals must not cause division by zero. An accuracy-dependent numerical search alone does not establish the stated exact `O(n log n)` bound without further analysis. Measure complexity in the conventional arithmetic-operation and comparison model, not as an unstated bit-complexity guarantee.

Neither uniqueness of the scalar multiplier nor global differentiability is required. The public parameter range is `1<=k<=n`; no proof of an additional `k=0` case is required. The reference proof has no unresolved theorem-critical obligations.
