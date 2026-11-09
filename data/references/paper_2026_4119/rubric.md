# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Justify the occupation-domain compactness and the needed cost continuity and affinity, then establish finite continuous convex external regret and its equivalence to all non-deviation inequalities. If using the differentiable proof route, justify the envelope derivative from unique maximizers. Accept an alternative valid convex-analytic argument that does not need the envelope derivative.
2. **3 points:** Establish strong duality and saddle attainment under strict feasibility. Verify the minimax hypotheses or give another complete duality argument. Pair a constrained primal optimizer with a dual optimizer, and prove feasibility, complementary slackness, and optimal moderator value. Derive, or otherwise justify, the multiplier control needed in the rate argument.
3. **3 points:** Establish that the updates exist; derive valid primal and dual inequalities for the coefficient 1/2 and dual step size N^{-1/2}; control the increment term and telescope. Use the specified old-dual averaging convention to obtain the uniform O(N^{-1/2}) gap on every bounded multiplier interval with a constant independent of the interval bound apart from the stated factor.
4. **2 points:** Prove the separate regret and moderator-objective upper rates, uniformly bound averaged multipliers using strict feasibility, extract a convergent subsequence, and show that every subsequential limit is a saddle point with optimal feasible primal component.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. No particular potential, strict convexity, strong convexity, or uniqueness of a primal update may be required. A run is restarted for each horizon N from the same initial pair and potential.

The source iteration has primal coefficient 1/2. Its primal average uses indices 1 through N, while its dual average uses indices 0 through N-1. Do not silently change either convention. An alternative indexing argument is acceptable only if its error is explicitly controlled and it proves the stated averages.

The projected-dual three-point inequality controls (lambda-lambda^{n+1})ER(rho^{n+1}); reversing this sign is not a valid step. The increment cross term must be handled explicitly. Compactness alone does not justify boundedness of an unspecified differentiable Bregman divergence; here it follows from the public continuity and bounded continuous flat-derivative assumptions.

Existence of a continuous flat derivative is not equivalent to affinity or convexity. Cost affinity follows from integration against the probability-law variable. Likewise, an arbitrary minimizer of L at a dual optimum need not be a saddle primal optimizer.

A regret-plus-objective-gap inequality alone does not prove the requested separate regret rate. A valid route uses an optimal multiplier lambda*, the lower bound Gamma0(rho)-VLP+lambda* ER(rho)>=0, and the gap comparator lambda*+1. Do not assume that an infeasible iterate has objective at least VLP, or that external regret is always nonnegative.

Naming minimax, a specialized occupation theorem, the envelope theorem, or mirror descent without an applicable statement and verified hypotheses is insufficient. Standard probability compactness, bounded-variation compactness, and minimax results may be used with their relevant hypotheses checked. The specialized Nash-existence and probabilistic-realization branches are unnecessary: strict feasibility supplies nonemptiness.

Propagate missing duality or telescoping arguments to claims that depend on them, but score independently justified later bounds and limit arguments. There are no unresolved private reference-proof obligations.
