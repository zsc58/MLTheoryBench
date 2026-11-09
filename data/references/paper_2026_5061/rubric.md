# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses full column rank to justify a positive-definite empirical covariance and a valid orthogonal eigendecomposition, constructs a whitening factor L, and establishes (A^T A)^(-1) = (1/n) L L^T (or an equivalent identity).
- **2 points:** Defines the transformed response vector p and correctly derives the least-squares coefficient and prediction in the factorized form beta = Lp and A beta = ALp.
- **4 points:** Gives an explicit valid identification of W_Q, W_K, W_V, W_FFN, and W_P from the constructed factors, and performs the central matrix-algebra substitution showing the linear-Transformer output reduces to ALp.
- **2 points:** Concludes exactly that the resulting output equals A(A^T A)^(-1)A^T y for every permitted A and y, with dimensions and quantifiers handled correctly.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental notation or ordering. A named method without the whitening identity, parameter construction, and equality verification is insufficient.
