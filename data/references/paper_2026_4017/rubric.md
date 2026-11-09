# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Schur-stage diffeomorphism and determinant factorization (2 points).** Establish positivity, recursive decoding, uniqueness, smoothness in both directions, and $\det\Theta=\prod_j e^{s_j}=e^v$. Smoothness may be justified briefly from the explicit formulas and strict positivity of the recovered pivots.
2. **Determinant-only Jacobians (2 points).** Derive the triangular unit intermediate Jacobian, account for the unit absolute determinant of the independent coordinate transformation between $s$ and $(v,d_2,\ldots,d_p)$, and obtain $J_{x\to\Theta}=e^v$ and $J_{x\to\Sigma}=e^{-pv}$. A correctly stated standard symmetric-matrix inversion Jacobian may be used, or it may be derived directly.
3. **Stage-local Fisher-Rao metric (3 points).** Derive the exact sum of $\frac12(ds_j)^2$ and $e^{-s_j}(dr_j-r_jds_j)^\top\Sigma_{j-1}(dr_j-r_jds_j)$. A recursive proof must retain the predecessor metric in the full stage identity and justify the absence of mixed differential terms when predecessor coordinates vary. Calculating only the frozen-predecessor slice and asserting that the slices sum, without establishing the required orthogonality or full recursion, does not completely close this step.
4. **Metric determinant and flat normalized volume (3 points).** Compute the stage block determinants in $(s,r)$ coordinates, combine them to obtain $2^{-p/2}e^{-(p-1)v/2}dv\,dd\,dr$, and show that $\rho=e^{-v/p}r$ makes the density constant. The normalization must use the correct change-of-variables direction; its full derivative is block triangular despite the dependence on $v$.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the inverse-Jacobian claim or of the normalization argument as a substantive loss; theorem-critical errors in the metric decomposition or determinant calculation are major. Distinguish the full metric on a stage from the incremental contribution of that stage. The metric blocks may depend on earlier coordinate values even though there are no mixed differential terms between stages in $(s,r)$ coordinates. Do not require such block diagonality after replacing $s$ by $(v,d)$.

The theorem includes $p=1$. A proof whose scalar base case and empty-sum/product conventions already cover it need not give a separate paragraph. No probabilistic, spectral, sparsity, or additional regularity assumptions are part of this task.
