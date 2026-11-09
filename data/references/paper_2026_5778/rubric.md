# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Conditional inclusion cancellation.** Converts perturbed scores to independent exponential clocks, conditions on clocks outside a fixed `K`-set, identifies the relevant `(n-K+1)`-st outside order statistic and the observed threshold, and proves that the reciprocal inclusion factors cancel exactly. Merely asserting generic importance weighting without this rank-conditioned argument does not earn full credit.
- **2 points: Differentiation and gradient identity.** Gives the joint retained-set/threshold density or an equivalent rigorous formulation, cancels the potentially singular factors in `widehat L f_theta`, supplies an integrable local envelope, and validly obtains the score-plus-pathwise gradient identity. A purely formal score-function assertion without controlling parameter-dependent estimator terms is incomplete.
- **2 points: Exponential-race integral and factorization.** Derives the integral for `P_theta(S)` from the event that `S` contains the smallest clocks, then substitutes it and correctly obtains the `h_i,c_i` factorization of `F(x)`.
- **3 points: Reward-sorted dynamic program and complexity.** Partitions subsets by their smallest reward-ordered index, establishes the meanings and updates of both `E_s` and `G_s`, obtains the displayed formula for `F`, and justifies `O(n log n+nKQ)` time. The solution must distinguish the exact integral and exact nodewise subset collapse from the generally approximate finite-node quadrature.

# Evaluator Notes

Accept any complete alternative proof under exactly the stated assumptions. Do not require the reference proof's notation or incidental presentation choices. Award a later core step when its conclusion is independently established even if an earlier attempted derivation is flawed. Missing the conditional threshold argument, a valid differentiation justification, or the weighted dynamic-program invariant is theorem-critical rather than cosmetic.

The integral's finiteness may be justified directly by its probability representation and the finite subset sum; a separate tail asymptotic is not required. If a solution uses such an asymptotic, multiple items attaining the smallest probability contribute additively to its leading coefficient. Omitting that multiplicity is a readily repairable local coefficient error when the integrability argument otherwise remains valid. The source's corresponding coefficient error is corrected in the private reference proof; reproducing or discussing that source correction is not a solver obligation.
