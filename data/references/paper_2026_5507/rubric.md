# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the sign partition and complementarity, including zero coefficient differences, to derive equal positive and negative coefficient masses. Relates each mass to the publicly defined total weight C_alpha and correctly expands the two components or otherwise accounts for their quadratic and kernel weights. The bias-free predictor identity may be verified as part of this step.
- **3 points:** Computes or otherwise proves the uniform Gaussian-kernel Hessian bounds and aggregates them with the balanced masses to establish convexity for rho >= 2 gamma exp(-3/2), including equality. Does not incorrectly require each individual h_i to be convex at this aggregate threshold.
- **3 points:** Establishes, for rho > 2 gamma exp(-3/2), the common strong-convexity lower bound mu=C_alpha[rho-2 gamma exp(-3/2)] and the global gradient-Lipschitz upper bound L=C_alpha(rho+gamma) for both components. Correctly uses positive semidefiniteness when passing from a largest-eigenvalue bound to an operator-norm bound.
- **2 points:** Derives the exact constrained-DCA decrease by mu times the squared step using feasible consecutive iterates and exact minimization. Justifies the relevant optimality and strong-convexity inequalities, or states an applicable finite-modulus DCA descent theorem and verifies its hypotheses. Existence of exact updates follows from continuity on the nonempty compact feasible set.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, use of an indicator, or a separately stated Gaussian lemma. The central curvature aggregation must be established, not merely attributed to a named method. The balanced-mass identity is no longer supplied as a public assumption; it must be justified when used. Do not require a separate proof of an identity that is merely the public definition of the predictor.

The standard exact-DCA descent principle may be invoked with finite valid strong-convexity constants a and b, giving decrease by (a+b)/2 times the squared step. Its relevant hypotheses include proper closed convex components, the stated strong-convexity bounds, feasible finite-valued iterates, and the exact subgradient/optimality relations. Taking a=b=mu suffices here.

Allow arbitrary nonempty closed bounded convex feasible sets, including lower-dimensional sets and singletons. An argument must not require an unstated interior assumption or silently evaluate infinity times zero: sigma(G+chi_Omega) can be infinite for a singleton. A proof using finite mu directly already covers this case and needs no separate singleton paragraph. Feasible initialization is part of the repaired public task. No statistical sampling model, distinctness of training locations, additional SVR optimality conditions, accumulation-point theorem, or numerical convergence analysis is required.
