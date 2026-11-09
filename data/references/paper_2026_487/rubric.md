# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs one valid family of 0-1 MILPs with O(n) variables, chosen independently of epsilon for the fixed score floor, and correctly derives the LP values, fractional candidates, and integer optimum needed for the argument.
- **2 points:** Proves that the baseline strong-branching policy follows the intended branching sequence and that best-bound selection and incumbent pruning yield a tree of at most 2n+1 generated nodes, respecting the prescribed tie-breaks.
- **3 points:** Establishes well-defined finite scores and the uniform error guarantee at every candidate of every node in both complete generated trees, not merely at nodes through depth n. For the reference construction, this includes proving that v-variables are never branched on, that both candidate children remain feasible, that scaling saturates the score floor, and that the perturbation strictly redirects branching. Accept an equivalent rigorous argument or a different valid mechanism.
- **3 points:** Computes or suitably bounds the LP value after d redirected branches, proves feasibility and non-pruning for the required levels, verifies that the selected variables are fractional, and obtains at least 2^{n+1}-1 generated nodes.

# Evaluator Notes

Accept any complete valid alternative construction or proof satisfying the same quantifier order, policy conventions, finite-score uniform-error guarantee, and tree-size bounds. The instance family must work for every positive tolerance; permitting the instances themselves to depend on epsilon does not establish the stated family-level claim.

A proof of score agreement only through depth n is insufficient because the task quantifies over both complete trees, including feasible bound-pruned nodes with candidates. Scaling does not make an infinite strong-branching score finite: a child-loss bound must first justify child feasibility or otherwise rigorously resolve the relevant scoring domain. In the reference construction, the required feasibility follows from the invariant that no v-variable is ever fixed by branching.

Do not require uniqueness of an LP optimizer where it is unnecessary. In particular, fixing w_1=0 leaves multiple optimal choices of the other two w-coordinates, although u=1/2 and v=1 hold in every optimum. A valid proof must handle the chosen LP-solution convention, rather than assume this entire block optimum is unique.

Merely asserting sensitivity of argmax decisions or exponential growth without establishing the necessary score comparisons and non-pruning conditions does not earn the corresponding core-step credit. A later step may receive credit if its required conclusion is independently established despite an error in an earlier derivation.
