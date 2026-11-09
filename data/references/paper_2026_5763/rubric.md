# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Linear-extension reduction.** Correctly encode a partial order as an acyclic transaction history, relate its probability to the number of linear extensions, and prove that the count can be recovered in polynomial time from an exact probability. Account for polynomial encoding and answer lengths on the reduction instances. Merely citing #P-hardness without a valid reduction earns no credit for this step.
- **2 points: Conditional telescoping reduction.** Add polynomially many consistent pairwise transactions to force a unique ordering, show all oracle queries have positive conditioning probability, and telescope the exact conditional probabilities to recover the original history probability.
- **4 points: History-probability approximation.** Derive the exponential-race/order-polytope integral, establish a quantitative positive lower bound, control truncation relatively, and verify the oracle, geometry, density-range, numerical-representation, and runtime hypotheses needed for randomized log-concave integration. A precise applicable standard integration theorem may be invoked without reproving it. This is the central bottleneck; invoking integration without these checks is materially incomplete.
- **2 points: Conditional ratio and FPRAS.** Handle impossible queries, approximate both history probabilities with suitable error and failure parameters, ensure that the estimator is defined on every execution and never returns zero on a feasible query, prove the ratio inequalities, and derive the stated runtime and polynomial-R FPRAS conclusion. Projection of each positive history estimate onto a known interval containing its true probability is one acceptable way to ensure totality, but is not required if another valid construction supplies it.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental constants, interval-separation argument, cutoff, projection, or presentation choices. A downstream step may receive credit if its required premise is established independently, even if the submitted derivation of that premise is flawed. Missing the exponential-race integral, relative truncation control, or polynomial integration conditions is a theorem-critical gap.

A high-probability relative-error guarantee alone does not ensure that a denominator estimate is positive on failure, nor that a feasible query never returns zero. Check these unconditional algorithmic requirements separately. If the only omission is a straightforward positive-output safeguard that leaves the successful estimates unchanged or improves them, treat it as a readily repairable omission rather than rejecting otherwise correct approximation reasoning. Likewise, an irrational cutoff can be replaced by a suitably bounded rational or integer upper cutoff; do not require the reference proof's particular implementation.

The empty history, empty offer set, outside-option queries, redundant transactions, and equal attractions require no additional restrictions. A proof may cover them through its general construction or by explicit elementary cases. The success guarantee is for each fixed input query, not a simultaneous guarantee for all possible queries.
