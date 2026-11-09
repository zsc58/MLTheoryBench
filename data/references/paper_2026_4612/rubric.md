# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the exact mode-wise trace identity, including the factor \(D_{\ne m}\), from the empirical covariance and the specified unfolding. A block expansion, direct multi-index calculation, or equivalent valid argument is acceptable. Any regrouping of an arbitrary mode must be coordinate-consistent; simultaneous permutation of the precision and empirical covariance is valid.
- **2 points:** Obtains the recursive Kronecker log-determinant identity with exponents \(D_{\ne r}\). Applying the correctly stated standard determinant identity to the SPD factors or proving the formula directly from product eigenvalues is sufficient.
- **3 points:** Substitutes both identities into the full objective, isolates the mode-dependent terms, and obtains the precise penalty rescaling \(\lambda_m/D_{\ne m}\) and \(\rho_m/D_{\ne m}\), up to an additive constant independent of the block and a positive factor. Preserves the stated empirical normalization and does not insert extra sample-count weights.
- **2 points:** Establishes convexity of the objective on the product of SPD cones and explains why sequential exact block minimizations, whenever the relevant minimizers exist, give the alternating procedure using the other factors' current values.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its optional mode-product computation.

The target is exact objective equivalence, convexity, and identification of the block-update procedure. It does not require a universal existence theorem, ADMM convergence, convergence of the outer iterations, or a global optimum of the joint nonconvex problem. Do not award credit for inferring attainment merely from convexity. Conversely, a proof is not incomplete because it does not prove attainment or convergence.

Do not require positive regularization, positive-definite empirical covariances, additional sample independence, or scale-identifiability constraints. These are not assumptions of the task. The argument must remain applicable to the stated zero-penalty and singular-covariance cases, and its conventions must cover \(M=1\), \(T=1\), and dimensions equal to one. A uniform argument covering these cases is sufficient; separate case discussions and the reference's nonattainment example are not required.
