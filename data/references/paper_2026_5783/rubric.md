# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Quadratic oracle and hardness estimates.** Correctly derive the pairwise quadratic static-oracle formula and establish the asymptotic hardness bounds for the two-arm alternative and every later-arm alternative. Provide valid allocations or an equivalent derivation, including the case in which there are no later arms. Quantitatively verify that any later-arm challenger terms are nonbinding. Merely asserting the bounds without allocations or an equivalent derivation does not earn full credit.
- **3 points: Incompatible-alternative allocation obstruction.** Compute the baseline-to-alternative information sums, combine them with the hardness estimates uniformly over allocations, and solve the resulting allocation max-min problem to obtain the reciprocal factor `C_K^{-1}`. Connect this bound to the assumed adaptive information inequality, either first in the quadratic model or after transfer to the given family. This is the central bottleneck.
- **3 points: Transfer to a general natural exponential family.** Prove the uniform local quadratic divergence comparison, place a suitably centered and scaled construction inside the mean domain, justify localization of the pairwise alternative minimizers, compare true and quadratic static hardnesses, and show that the scale and variance factors cancel. Account for the fact that the transformed parameter domain can be a proper interval rather than all of `R`. A generic appeal to Taylor expansion without uniformity and hardness comparison is insufficient.
- **2 points: Final lower bound and consequences.** Complete the limit and quantifier argument for every consistent family, then correctly derive both failure of uniform static-oracle attainment and nonexistence of a complexity for any class containing the static-proportion families. For the latter, derive `H<=H_so` and explain why finite achievable ratios force consistency even if the class itself is not restricted to consistent families.

# Evaluator Notes

Accept any complete proof under the stated assumptions, including a construction or parametrization different from the reference proof. Do not require incidental constants used only to verify that later-arm challenger terms are nonbinding.

The static-allocation exponent identity and adaptive information inequality are explicit public hypotheses; their proofs are not required. Other theorem-critical intermediate results must be derived rather than merely attributed to a specialized method or a paper-specific lemma.

The proof must justify that the oracle hardness used as a benchmark is finite and positive. This may follow within the pairwise-minimization argument and need not appear as a separate lemma. Ordinary extended-value cases for error probabilities and ratios must be handled consistently.

A flawed derivation of an intermediate statement need not erase credit for a later step if that statement is independently proved. Conversely, the allocation obstruction, uniform local transfer, and use of the adaptive information inequality are theorem-critical; naming them without verifying their quantitative conclusions is a major gap.

Do not require attainment of the worst-instance supremum. The requested conclusion concerns the supremum itself, and the construction may approach its lower bound along a sequence of instances.
