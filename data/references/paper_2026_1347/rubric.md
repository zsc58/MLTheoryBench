# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes by induction that affine propagation, exact ReLU graph operations, and compatible constrained products preserve the shared initial-state coupling and produce the exact state-pair HZ S_x(X,t). The proof must formulate the invariant fiberwise over the shared equality-variable block, account for the common block at every constrained product, and use sound preactivation intervals.
- **2 points:** Derives exact forward and backward reachable sets by the correct coordinate restrictions and projections, including the relevant HZ closure argument.
- **3 points:** Proves that triangle-relaxed unstable ReLU graphs contain the exact graphs fiberwise over the shared equality-variable block, and propagates this inclusion through affine maps, constrained products, intersections, and projections. Correctly handles global ranking over all unstable coordinates encountered for the computed horizon, the condition N_b>=N_t, and monotone tightening as N_b increases.
- **2 points:** Applies restriction and projection to obtain relaxed forward/backward over-approximations, with inclusion, exactness at the full binary limit, and monotonicity.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat reversal of the N_b monotonicity direction or omission of the shared-initial-state coupling as theorem-critical errors. Treat use of unsound or N_b-dependent interval bounds, failure to specify a fixed ranking/tie-break, or replacement of the required fiberwise invariant by ordinary projected-set inclusion as a material gap in the relaxed proof.
