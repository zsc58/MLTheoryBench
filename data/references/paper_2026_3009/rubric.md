# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Pointwise quantile optimality (3 points).** Derive the upper bound on each action's worst-case utility at conditional coverage at least t and show utility-threshold sets attain theta(x,t). Justify quantile coverage and threshold attainment. Handle t=0 using the fixed upper bound and empty-set convention; the argument must also apply at t=1.
2. **Universal scalar reduction (2 points).** Prove equivalence of universal policy coverage with E[min_a P(Y(a) in C(X,a)|X)]>=1-alpha, using a measurable finite-action minimizing policy, and reduce the objective to E[theta(X,t(X))]. Verify the converse threshold reconstruction. An alternative proof establishing the necessary universal upper bound and an attaining construction earns equivalent credit without explicitly stating full scalar equivalence.
3. **Multiplier allocation (3 points).** Establish the dual bound and existence of a minimizing beta*. Justify pointwise maximum attainment and the derivative or equivalent continuity argument needed to derive E[g(X,beta*)]=1-alpha. For the dual-derivative route, verify upper semicontinuity, compactness, the maximum-derivative formula, passage through expectation, and exclusion of beta*=0 using uniqueness and theta(x,0)=u_max. Merely naming Lagrange duality or a maximum-derivative formula without verifying its relevant hypotheses does not close this step.
4. **Set reconstruction and both optima (2 points).** Construct C*, verify universal and policy-coupled coverage, and prove attainment of the universal optimum and optimality over arbitrary policy-coupled-feasible systems. For the latter, bound the selected action's worst-case utility using its own conditional coverage and the same scalar optimum, or supply an equivalent valid argument.

# Evaluator Notes

Accept any mathematically valid alternative proof and allocate credit by equivalent mathematical achievements rather than requiring the reference proof's presentation order. Missing quantile attainment, an adequate universal upper-bound/reconstruction argument, the mean-coverage multiplier characterization, or the policy-coupled upper bound is theorem-critical unless replaced by a valid alternative argument.

The fixed finite u_max is an upper bound and need not equal the utility supremum. Empty sets are allowed. Do not assume continuous utility distributions, atomless feature laws, strict monotonicity, concavity of theta, randomized allocations, or simultaneous uniqueness outside one common null set for every beta. The assumption is uniqueness almost surely at each fixed beta. Endpoint and measurability details may be supplied by short correct arguments; penalize omissions according to whether they leave a genuine logical gap.
