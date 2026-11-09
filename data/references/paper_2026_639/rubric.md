# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Projection optimality system.** Correctly handles infeasible and nominally feasible cases, proves binding in the nontrivial case, and derives the positive-part formula and both multiplier equations. Justifies necessity and sufficiency of the optimality conditions, including the feasible endpoint beta=min b. Polyhedral KKT with its hypotheses checked is sufficient; an unsupported appeal to strict feasibility is not. A direct constructive existence argument together with a valid optimality certificate is also acceptable.
- **4 points: Piecewise-affine path and breakpoint bound.** Rigorously establishes the normalization path, its affine formula on a fixed active set, the needed geometric properties, valid initialization and active-set transitions, and O(n) pieces with O(n) work per piece. The source's at-most-2n breakpoint argument or a valid sharper bound is acceptable. Naming an active-set or parametric method without deriving or justifying these properties earns little credit for this step. An analytical finite-subset representation is not itself an efficient algorithm; the proof must avoid enumerating exponentially many subsets.
- **2 points: Exact projection recovery.** Shows that the remaining moment equation is affine on each path piece, that a finite nonnegative solution exists, and that scanning the pieces recovers the exact optimizer and value in O(n^2). Handles flat pieces and beta=min b. If using a whole-real-line path, clips intervals to the nonnegative domain, skips empty intersections, and handles singleton intersections directly. Does not require an interior point of an empty or singleton interval, use an untrimmed midpoint outside the required domain, or perform arithmetic with infinity.
- **2 points: Bellman reduction and total complexity.** Checks the compact-convex bilinear minimax hypotheses, proves the projection-sum threshold equivalence including infeasible projections, applies the nondegeneracy promise only to nontrivial instances, and obtains coordinatewise additive epsilon accuracy through bisection on [0,U]. Includes initialization/output costs and obtains O(mn^3 [1+log(max{1,U/epsilon})]), covering U=0 and epsilon>=U.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, traversal direction, or sharper breakpoint count. A downstream step may receive credit when its needed premise is independently proved, even if an earlier attempted derivation of that premise was flawed. Missing the active-path construction or its quadratic bound is a theorem-critical gap. No credit should depend on identifying the source paper or reproducing its algorithm numbering. All obligations in the replacement reference proof are closed; there is no unresolved private GT dependency.
