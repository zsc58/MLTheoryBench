# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the prescribed cell path distance and its metric identification, derives the cell-edge bound for a parent at depth ell, and obtains domination by the address-tree metric. The correct exponents are s^ell for the cell-edge upper bound and s^{ell+1} for the tree edge. A valid direct tail proof need not separately state metric domination.
- **3 points:** Sums the geometric tail from parent depth L, extends the distance-to-truncation bound to every point of the completion, proves compactness using finite nets and completeness, and obtains the Hausdorff truncation estimate with the stated constant.
- **3 points:** Constructs or rigorously justifies the finite-window vector-valued ReLU interpolant, verifies its complexity, and proves by induction that the rollout exactly matches all true centers and cells through depth L. Repeated centers must have a single field output. A generic scalar projection followed by an explicit vector-valued linear spline is a complete acceptable construction and gives stronger complexity than requested.
- **2 points:** Chooses L_epsilon, verifies the epsilon-error, and correctly translates the finite-window bounds into the stated width and depth rates. Euclidean separation and diameter must be used for B_L. Stronger bounds, including bounded depth with width O(K^L), fully satisfy the requested upper bounds. Interpret epsilon rates asymptotically as epsilon decreases to zero.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or use of the source's specialized external interpolation lemma. Naming a nonstandard interpolation theorem without deriving the relevant bound or verifying its precise hypotheses is not itself a completed interpolation step; an explicit elementary construction is sufficient.

Treat omission of either exact finite-depth agreement or the completed-space error bound as a major gap. Exact equality of parent cells and all sibling centers determines the child cells even in the presence of ties. Do not require continuity, Lipschitz regularity, positive cell-edge weights, or an ell_p residual upper bound: none is an assumption of the task. The Euclidean CFG bounds must not be silently replaced by ell_p bounds.

Y_L uses the restriction of the full completed cell metric, not necessarily the intrinsic shortest-path metric of a finite rollout graph. Metric identification may merge vertices whose centers differ; exact center and cell agreement is still required at the address level before this identification. Do not penalize use of the singleton constant-map convention, and do not require an aspect-ratio estimate when a stronger interpolation construction makes it unnecessary.

All theorem-critical reference-proof obligations are explicitly closed. No private GT quality warning remains.
