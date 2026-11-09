# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the feasible constant-size uniform model to establish MDL_T(Y)<=m+c_U at both relevant dimensions. Correctly respects the MDL definitions and obtains the optimizer description-length bound needed for the reduction. Optimizer existence and finite expected loss follow from the same comparison and finiteness of the set of bounded-length programs.
- **3 points:** Constructs valid polynomial-time likelihood-threshold tests for the MDL optimizer, or for another adequately justified polynomial-description-length model family. Establishes the uniform counting bound and validly transfers it using non-uniform security. The advice must be polynomial in k. When using the eventual security convention, justifies a single starting index for the thresholds used at each k, for example by advising a maximizing threshold.
- **3 points:** Derives the explicit lower bound H_T(G(U_k))>=n-2-n epsilon(k) with a valid real-valued tail, shortfall, or equivalent argument. Applies the result to the log-loss of the two-part-code optimizer, not to an incorrectly redefined entropy.
- **2 points:** Derives S_T(G(U_k))<=c+n epsilon(k), and combines the seed and output comparisons to prove the stated entropy increase with one fixed constant depending only on the coding machine and uniform implementation.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions; the threshold route is not mandatory if an alternative establishes all requested conclusions. Equivalent correct steps receive the associated credit without requiring the reference proof's order or notation.

The public entropy lower bound has the explicit additive constant 2. A proof establishing only n-C-n epsilon(k) for an unspecified C>2 does not fully prove that target. Constants in the other two conclusions may be enlarged as permitted by their existential fixed constant c. Strict inequalities stronger than the public non-strict bounds are acceptable.

A finite model description is not, by itself, a polynomial advice-length bound for a dimension-dependent family. It suffices to bound the MDL optimizer's length; do not require a reduction for every unrestricted feasible program. Non-uniformity permits advice containing an optimizer without an efficient optimization algorithm.

Negative log-probabilities can be nonintegral even when probabilities have finite binary expansions. Do not accept the integer tail-sum identity as an equality for arbitrary real-valued log-loss. A pointwise one-unit discretization bound or a correct integral argument resolves this issue. The expression 2+sum_{t=1}^n 2^{-t} is not at most 2.

Security is eventual for each fixed non-uniform family, not a pointwise universal bound over all polynomial resource budgets. The proof must not obtain simultaneous thresholds merely by taking a maximum of starting indices over an expanding collection without justification. The target requires only one sufficiently large starting index for the fixed setup, and does not require that index to be uniform in G or T.
