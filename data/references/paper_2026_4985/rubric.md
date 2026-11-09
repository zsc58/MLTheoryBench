# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the stated signed source problem, correctly defines the binary 2x2 block construction and the positive integer threshold `T=st+D`, and explains polynomial size and computation, including the threshold's finite integer encoding.
- **3 points:** Proves the forward implication by sign-normalized one-hot nonnegative factors and computes each block error as `1+|M_ij-u_i v_j|`.
- **3 points:** Proves the converse for arbitrary nonnegative real factors by extracting paired-coordinate differences and establishing both identity and anti-identity block lower bounds, with all signs and zero cases covered.
- **2 points:** Sums the block inequalities to obtain the exact yes-instance equivalence and concludes NP-hardness under the polynomial reduction.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The blockwise lower bound is theorem-critical; merely naming a triangle-inequality argument without establishing both block cases is insufficient. An explicit symmetry argument may establish one block case from the other.

The two source-problem premises are expressly assumed in the public task; their external proofs are not required. The reduction must depend only on the input instance, not on a supplied or computed feasible witness. Witness choices in the correctness proof do not need to be computed by the reduction.

Do not assume that arbitrary feasible target factors are binary, strictly positive, or bounded. Zero coordinates and zero paired differences are allowed. A clear polynomial-size argument for the binary matrix and integer threshold suffices; no particular bit-complexity formula is required.
