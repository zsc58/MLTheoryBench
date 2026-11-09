# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Fixed-regime reconstruction differentiation (2 points).** Correctly holds the numerical reconstruction vectors fixed, differentiates the squared residual objective, and obtains the operator Hessian \(\Delta P\mapsto\eta\Delta P G_A\), equivalently \(\eta G_A\otimes I_d\) in column-stacked coordinates. Does not differentiate the reconstruction activations through their reference-point cosine definition.
2. **Cosine Hessians and local-block aggregation (4 points).** Correctly differentiates the selected clustering cosines rather than freezing them. For \(\alpha_s=v_{t(s)}^{\mathsf T}q_j\), obtains the local contribution \(c_s\|p_j\|_2^{-2}[\alpha_s I_d+q_jv_{t(s)}^{\mathsf T}+v_{t(s)}q_j^{\mathsf T}-3\alpha_s q_jq_j^{\mathsf T}]\), or a mathematically equivalent derivation. Explains the absence of cross-prototype clustering derivatives, aggregates with \(A_j=\sum_{s:k(s)=j}c_s\alpha_s\), and obtains the requested block formula and total Hessian. The relation \(q_j^{\mathsf T}t_j=0\), if used, must follow from the definitions rather than from an added alignment hypothesis. Handles zero-weight or absent selected terms and unsupported local blocks.
3. **Normalized surrogate factorization (3 points).** Works on the same nonempty supported index set for \(D\) and \(G_{A,S}\), uses \(D\succ0\) to justify its square root and inverse square root, proves \(H_{\rm tan}=D^{1/2}(I_{|S|}+M)D^{1/2}\), and identifies the symmetrically preconditioned matrix as \(I_{|S|}+M\).
4. **Spectral conditioning conclusion (1 point).** Establishes \(G_{A,S}\succeq0\) and hence \(M\succeq0\), uses the spectral-norm condition number, and proves \(\kappa(I_{|S|}+M)\le1+\lambda_{\max}(M)\). Does not require \(G_{A,S}\) to be invertible or apply extreme-eigenvalue notation to an empty matrix.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The exact block formula, the cross/local separation, and the normalized condition bound are theorem-critical; merely naming a Hessian or preconditioning method is insufficient.

Replacing activation-weighted mass by \(\sum_s c_s\), dropping the cosine factor multiplying the identity matrix, or assuming all selected directions align with their prototype changes a core step and is not a valid proof of the stated general case. Equivalent direct differentiation of the aggregated linear-in-direction clustering objective is acceptable and need not separately display every pairwise Hessian.

The unsupported-index conclusion concerns the clustering block \(B_j\), not necessarily the reconstruction contribution. The conditioning conclusion concerns the explicitly defined surrogate on supported coordinates, not the full Euclidean Hessian. No monotonicity claim across different training outcomes, local-defect bound, or attribution result is required. When the supported set is empty, only the Hessian assertion applies.
