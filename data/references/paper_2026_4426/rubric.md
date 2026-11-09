# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Kernel-PCR/KGC spectral identification (2 points).** Uses the centered Gram eigendecomposition to identify the KGC and all-positive-component KPCR column spaces or projectors, for both X and Z. Handles the zero-rank case without an undefined inverse.
2. **Actual GRBF normalization and Nyström representation (3 points).** Uses row-normalized GRBF activations and the product-normalized kernel. Establishes a valid kernel and the invertible right-factor relation between the activation and Nyström feature matrices for each of X and W. A proof through equality of Gram-factor ranges is equally acceptable.
3. **PCA and additive unrestricted regression (3 points).** Justifies that retaining all positive components preserves each centered feature column space, including rank-deficient cases. Passes to the restricted model and the unrestricted concatenation of the separate X and W blocks. Correctly handles the intercept and nonunique coefficients, and obtains equality of fitted values and residual sums of squares.
4. **Integrated representation conclusion and residual comparison (2 points).** Concludes that the stated KGC regressions and the stated additive normalized-GRBF regressions have their respective KPCR representations. Establishes equality of the residual-error difference and the F ratio when q>0, n-p_U>0, and RSS_U>0, using ranks of full fitted spaces including the intercept.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular matrix square root beyond the positive-definite convention in the task.

Do not reward replacing row normalization by square-root symmetric normalization, identifying the normalized cross-Gram matrix directly with the activation matrix, or replacing the additive unrestricted model by a joint Gaussian feature construction on Z. These alter the defined regressions.

Repeated dummy indices in separate normalization sums are harmless. The issue is the values and powers of the normalization factors, not the letters used for bound indices.

Do not require full column rank of centered feature matrices or uniqueness of least-squares coefficients. The two row-normalized activation blocks each contain the constant vector in their spans, so their concatenation necessarily has a redundant coefficient direction. An unsupported ordinary inverse for that concatenation is not valid.

Do not require a claim that arbitrary eigenvalue truncation preserves these representations. Do not require equality of KGC and GRBF fitted spaces with each other, equality of their original significance-testing procedures, equality with a separately fitted joint-design KPCR model, out-of-sample prediction equivalence, causal-identification guarantees, or an F null distribution. None is a target.
