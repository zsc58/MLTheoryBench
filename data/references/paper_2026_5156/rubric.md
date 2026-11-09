# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly reduces reward-law ambiguity to measurable pointwise mean-reward l_p balls, proving both directions and justifying finite returns and the expectation interchange. Establishes the comparator maximum, the adversarial supremum, and the outer infimum over prompts for the full measurable policy and ambiguity classes. Measurable approximate selections suffice for the two extrema stated as supremum and infimum; exact measurable optimizers for general p are not required.
- **3 points:** Derives the fixed-prompt formula Psi_p(z;r)=max_i{r_i-<z,r>+delta||e_i-z||_(p*)} by a valid dual-norm argument and simplex maximization; correctly obtains the p=1 formula and an attaining perturbation. Handles the endpoint exponents and does not apply a normalized support-function vector when its denominator is zero.
- **5 points:** Converts the p=1 minimization into the correct epigraph problem, proves existence and uniqueness of t_0 and the threshold feasibility condition, justifies reward-ordered allocation of slack, and analyzes the piecewise-linear objective to prove that the stated t* is an optimal threshold. Establishes that the displayed policy is simplex-valued and measurable and that pointwise optimality almost everywhere yields global optimality. The reasoning must cover reward ties, breakpoints, equality in the threshold condition, and n=1, either directly or through a uniform argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its order of argument, or its particular countable approximation construction. A valid measurable-selection theorem may replace that construction when its hypotheses are established.

A solution that merely states the threshold formula without proving feasibility, slack allocation, and optimal-threshold selection does not earn the full final core step. Award partial credit for independently correct parts of that argument.

A claimed global decomposition based only on arbitrary pointwise choices is incomplete unless their measurable admissibility, or an adequate measurable approximation, is justified. Check the adversary and policy separations separately. Do not require the solver to interchange the outer infimum with the adversarial supremum; that interchange is neither asserted nor needed.

The comparator is a policy selected for a fixed reward law, not a reward-realization-dependent decision rule. Do not accept moving its maximum inside the expectation over reward randomness without justification. Do not require independence of rewards across prompts, a global q-th moment, strictly ordered rewards, a finite prompt space, or any algorithmic sampling assumptions.

The positive-budget hypothesis excludes delta=0. Boundary and degenerate cases may be handled by arguments that already apply uniformly; separate case headings are not required. No claim about uniqueness of the optimal policy or about additional small- or large-budget limits is part of the task.
