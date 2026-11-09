# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly differentiates the surrogate, establishes strict convexity from \(H\succ0\), \(ZZ^T\succ0\), and \(N>0\), and solves the first-order condition to identify its unique global minimizer as \(W-W^*\).
- **4 points:** Derives the matrix-sign representation using a compact SVD of the displacement and positivity of the compressed curvature, or an equivalent valid argument. Justifies why a positive-definite middle factor contributes no additional matrix-sign factor, and covers zero displacement.
- **3 points:** Evaluates the isotropic-proxy substitution, obtains the proportional right-preconditioned matrix-sign update, and derives the iteration by identifying the effective learning rate. Distinguishes the modeled update from the exact minimizer unless the actual covariance identity holds. Handles zero proxy scale directly rather than applying positive-scalar invariance at zero.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the particular SVD notation or differentiation route used in the reference proof. A valid replacement for the SVD positivity argument receives full credit.

Do not award credit for merely naming a method without deriving the required identities. Omission of strict-convexity/uniqueness or a justified matrix-sign identity is theorem-critical and propagates to downstream claims when unsupported.

The isotropic relation is a modeling substitution, not an additional exact identity for arbitrary displacement. A proof that treats the proxy update as the exact minimizer without the actual identity \(\Sigma_W=cI_m\) does not establish the requested distinction. When that actual identity holds, identifying the two updates is correct.

Positive-scalar invariance does not hold at scalar zero for nonzero matrices. Nevertheless, the formula for the proxy update remains valid at \(c=0\) because its prefactor is zero. The effective learning rate from absorption is \(\eta_t=\alpha_t\sqrt{c_t}\), hence zero when \(c_t=0\). An otherwise complete proof omitting only these readily supplied zero-case explanations belongs in the 8-9 range.

No proof about a true loss Hessian, external curvature approximation, convergence, descent, stochastic sampling, or numerical matrix-sign implementation is required. In particular, Assumption 1 does not justify identifying an underlying loss Hessian with the surrogate Hessian.
