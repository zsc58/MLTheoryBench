# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly derives the exact identity theta-theta_{-S}=W(S)/G(S) from the full and retained normal equations, defines the auxiliary quantities from the given pairs, and verifies the positive-denominator condition.
- **2 points:** Shows that maximizing W(S)-eta G(S) is equivalent to the finite additive maximization obtained by selecting the k largest individual scores w_i+eta c_i. Tied scores must not require an unstated uniqueness assumption.
- **3 points:** Constructs an exact scalar-update procedure and proves finite, noncycling termination from every real initial scalar with the stated M+1 bound. A valid argument observes that every updated parameter is a feasible ratio at most the optimum, so after at most one initial adjustment the nonterminal updates strictly increase through distinct feasible values. The count must consistently distinguish value-changing updates, a possible final equal-value certification assignment, and subproblem calls.
- **2 points:** Establishes the zero-residual characterization and proves that the returned set is a globally optimal size-k influence set, not merely that the scalar stops changing.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

A residual-before-update implementation can prove at most M value-changing updates and at most M+1 subproblem calls. An update-before-test implementation can count the final equal-value assignment and prove at most M+1 ratio updates. Both satisfy the task when the procedure and counting convention are clear.

Do not require global monotonicity starting from an arbitrary scalar above the optimum: the first update can cross below the optimum, followed by increasing updates. An unsupported assertion of global monotonicity does not establish the termination step.

Exact zero residual, equivalently exact equality of the selected ratio and the current parameter, is a valid stopping criterion with arbitrary ties. Consecutive-set equality can be used as a sufficient certificate when justified by the update rule, but zero residual need not imply that consecutive selected sets are equal. A positive numerical tolerance alone does not certify exact global optimality.

The proof must cover arbitrary initialization and possible ties, including the case M=1. Do not impose statistical assumptions, uniqueness, absence of zero individual regressors, an oracle-recovery conclusion, or a per-iteration runtime bound not requested by the public task. A named fractional-programming method alone does not replace justification of its applicable hypotheses and the claimed finite bound.
