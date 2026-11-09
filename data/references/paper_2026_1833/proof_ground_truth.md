# Reference Proof

## Proof Structure

1. Differentiate the quadratic surrogate, establish strict convexity, and identify its unique minimizer.
2. Prove the displacement-weighted matrix-sign formula, including zero displacement and arbitrary positive rank.
3. Evaluate the isotropic-proxy substitution, distinguish it from an exact minimizer assertion, and derive the learning-rate rescaling, including zero proxy scale.

## Complete Proof

Let \(R=ZZ^T\), \(D=W-W^*\), and \(\Sigma=DD^T\). The assumptions give \(N>0\), \(H\succ0\), \(R\succ0\), and \(G=HDR/N\).

### 1. Exact minimization

For
\[
J(Q)=-\operatorname{tr}(QG^T)+\frac1{2N}\operatorname{tr}(HQRQ^T),
\]
symmetry of \(H\) and \(R\) gives
\[
\nabla J(Q)=-G+HQR/N.
\]
For any nonzero perturbation \(\Delta\), the Hessian quadratic form is
\[
\frac1N\operatorname{tr}(H\Delta R\Delta^T)
=\frac1N\|H^{1/2}\Delta R^{1/2}\|_F^2>0.
\]
The strict inequality follows because both square-root factors are invertible. Thus \(J\) is strictly convex. The stationary equation \(HQR/N=G\) has the solution \(Q=D\) by the assumed gradient relation. It is the unique global minimizer. Equivalently, direct expansion gives
\[
J(D+\Delta)-J(D)=\frac1{2N}\|H^{1/2}\Delta R^{1/2}\|_F^2,
\]
which also proves existence and uniqueness.

This argument concerns the exact Hessian of the surrogate. It does not assume equality with the Hessian of an underlying loss.

### 2. Matrix-sign representation

If \(D=0\), then \(G=0\), \(\Sigma=0\), and the proposed representation equals zero by the stated convention, proving the result in this case.

Otherwise let \(D=USV^T\) be a compact SVD of rank \(r>0\). The columns of \(U\) and \(V\) are orthonormal and \(S\) is positive diagonal. Consequently
\[
\Sigma^{1/2}=USU^T.
\]
The matrix \(B=U^THU\) is positive definite: for every nonzero \(x\in\mathbb R^r\), \(Ux\ne0\) and \(x^TBx=(Ux)^TH(Ux)>0\). The gradient relation therefore yields
\[
\Sigma^{1/2}GR^{-1}
=\Sigma^{1/2}HD/N
=U C V^T,
\qquad C=SBS/N\succ0.
\]
Orthogonally diagonalize \(C=P\Lambda P^T\), where \(P\) is orthogonal and \(\Lambda\) is positive diagonal. Then
\[
UCV^T=(UP)\Lambda(VP)^T
\]
is a compact SVD, and hence
\[
\operatorname{msgn}(\Sigma^{1/2}GR^{-1})
=(UP)(VP)^T=UV^T.
\]
Multiplication on the left by \(\Sigma^{1/2}\) gives
\[
\Sigma^{1/2}\operatorname{msgn}(\Sigma^{1/2}GR^{-1})
=USU^TUV^T=USV^T=D.
\]
Together with the first part, this proves the claimed formula for the unique minimizer \(Q^*\).

### 3. Isotropic-proxy substitution

By definition of the substitution in the task,
\[
Q_{\mathrm{iso}}=\sqrt c\,\operatorname{msgn}(\sqrt c\,GR^{-1}).
\]
For any matrix \(X\) and scalar \(a>0\), multiplying the positive singular values in a compact SVD by \(a\) leaves its matrix sign unchanged; for \(X=0\) this also follows from the zero convention. Thus, if \(c>0\),
\[
Q_{\mathrm{iso}}=\sqrt c\,\operatorname{msgn}(GR^{-1}).
\]
If \(c=0\), both sides of this last equality are zero directly. No invariance of the matrix sign under multiplication by zero is asserted.

This is an evaluation of the modeled update. If the actual identity \(\Sigma=cI_m\) holds, then the representation proved above implies \(Q_{\mathrm{iso}}=Q^*\). Without that identity, substituting the proxy does not establish that \(Q_{\mathrm{iso}}\) minimizes the original \(J\).

At iteration \(t\), the same calculation gives
\[
Q_{\mathrm{iso},t}=\sqrt{c_t}\,\operatorname{msgn}\!\left(G_t(Z_tZ_t^T)^{-1}\right).
\]
Therefore the update \(W_{t+1}=W_t-\alpha_tQ_{\mathrm{iso},t}\) becomes
\[
W_{t+1}=W_t-\eta_t\operatorname{msgn}\!\left(G_t(Z_tZ_t^T)^{-1}\right),
\qquad \eta_t=\alpha_t\sqrt{c_t}.
\]
For \(c_t>0\), every nonnegative effective learning rate is obtainable by this rescaling. If \(c_t=0\), the substituted update is zero and the rescaling gives \(\eta_t=0\); one cannot infer an arbitrary nonzero effective learning rate by absorbing a zero scale.

## Source Contract and Dependency Audit

The smooth-loss setup motivates the displayed surrogate; it adds no further hypothesis to this finite-dimensional conditional theorem. The source's curvature construction is internally explicit: with fixed activations and output Hessian blocks \(H_{ts}\), the linear output Jacobians are \(A_t=z_t^T\otimes I_m\). The chain rule gives the parameter Hessian \(N^{-1}\sum_{t,s}A_t^TH_{ts}A_s=N^{-1}\sum_{t,s}(z_tz_s^T)\otimes H_{ts}\). Dropping the off-diagonal blocks and replacing each diagonal block by their average \(H\) produces \((ZZ^T/N)\otimes H\). These are modeling approximations, not an exact equality for an arbitrary underlying loss. The task assumes the resulting gradient relation directly, so no external curvature theorem is needed to close its proof.

The source proof's use of the actual loss Hessian at L000192 is locally repaired by using the surrogate Hessian, as recorded under theory_004. The isotropic-proxy interpretation follows the express qualifications at L000196-L000214 and L000543. All required proof obligations are closed above.
