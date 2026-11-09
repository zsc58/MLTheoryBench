# Reference Proof

## Proof Structure

1. Express natural-only and augmented GLS estimation errors as linear transforms of their residual vectors, obtaining the two covariance formulas and the reported-coordinate covariance-risk expression.
2. Block-invert the joint residual covariance. Its Schur complement yields augmented information as the natural information plus a positive-semidefinite term; inverse Loewner order then gives covariance-risk non-deterioration.
3. For one auxiliary direction, reduce the update to rank one and apply the Woodbury identity to obtain the exact gain quotient and its positive denominator.
4. State the population covariance-risk scope explicitly, distinguishing it from bias-inclusive MSE and finite-sample test loss.

## Complete Proof

Fix the horizon and suppress its index. All covariance comparisons below are for a fixed candidate \(U\). Let
\[
W=\begin{bmatrix}W_{yy}&K\\K^T&R\end{bmatrix}\succ0,
\qquad H=\begin{bmatrix}S\\U^T\end{bmatrix}.
\]
Write the forecast vector as \(\hat z=Hb+e\), where \(e=(e_y,e_c)\) has covariance \(W\). The population GLS estimator is
\[
\hat b_U=(H^TW^{-1}H)^{-1}H^TW^{-1}\hat z.
\]
Therefore \(\hat b_U-b=(H^TW^{-1}H)^{-1}H^TW^{-1}e\). Using \(\operatorname{Cov}(e)=W\),
\[
\operatorname{Cov}(\hat b_U-b)=(H^TW^{-1}H)^{-1}H^TW^{-1}WW^{-1}H(H^TW^{-1}H)^{-1}=(H^TW^{-1}H)^{-1}=:\Sigma_U.
\]
The same calculation with \(H=S\) and covariance \(W_{yy}\) gives \(\Sigma_0=(S^TW_{yy}^{-1}S)^{-1}\). No zero-mean or independence assumption is used: the state cancels from the estimation error, which is a fixed linear transform of the residual vector. Reported errors are \(S(\hat b-b)\), hence their covariances are \(S\Sigma_US^T\) and \(S\Sigma_0S^T\). Consequently the covariance-risk gain equals
\[
\operatorname{tr}\!\left(Q(S\Sigma_0S^T-S\Sigma_US^T)\right)
=\operatorname{tr}\!\left(Q_b(\Sigma_0-\Sigma_U)\right),\quad Q_b=S^TQS,
\]
by cyclicity of trace.

Partition \(W\) as above and set
\[
T=R-K^TW_{yy}^{-1}K,\qquad M=U-S^TW_{yy}^{-1}K.
\]
For every nonzero \(v\in\mathbb R^k\), positive definiteness of \(W\) gives
\[
v^TTv=
\begin{bmatrix}-W_{yy}^{-1}Kv\\v\end{bmatrix}^{T}
W
\begin{bmatrix}-W_{yy}^{-1}Kv\\v\end{bmatrix}>0.
\]
Thus \(T\succ0\). The positive-definite block inverse formula gives
\[
W^{-1}=\begin{bmatrix}W_{yy}^{-1}+W_{yy}^{-1}KT^{-1}K^TW_{yy}^{-1}&-W_{yy}^{-1}KT^{-1}\\-T^{-1}K^TW_{yy}^{-1}&T^{-1}\end{bmatrix}.
\]
Multiplying by \(H\) on both sides yields
\[
H^TW^{-1}H=S^TW_{yy}^{-1}S+MT^{-1}M^T=:I_0+MT^{-1}M^T\succeq I_0.
\]
Indeed, the four additional terms in this multiplication are
\[
S^TW_{yy}^{-1}KT^{-1}K^TW_{yy}^{-1}S
-S^TW_{yy}^{-1}KT^{-1}U^T
-UT^{-1}K^TW_{yy}^{-1}S
+UT^{-1}U^T,
\]
which factor as \(MT^{-1}M^T\). This matrix is positive semidefinite because \(T^{-1}\succ0\).

Both information matrices are positive definite: they are symmetric positive semidefinite weighted Gram matrices and are invertible by assumption. Inversion reverses Loewner order on positive-definite matrices. Explicitly, if \(B\succeq A\succ0\), then \(C=A^{-1/2}BA^{-1/2}\succeq I\), so \(C^{-1}\preceq I\) and \(B^{-1}=A^{-1/2}C^{-1}A^{-1/2}\preceq A^{-1}\). Applying this with \(A=I_0\) and \(B=H^TW^{-1}H\) gives
\[
\Sigma_U=(H^TW^{-1}H)^{-1}\preceq I_0^{-1}=\Sigma_0.
\]
Congruence by \(S\) preserves the order for reported covariances. Also \(Q_b=S^TQS\succeq0\). Writing \(\Delta=\Sigma_0-\Sigma_U\succeq0\),
\[
G(U;Q)=\operatorname{tr}(Q_b\Delta)
=\operatorname{tr}(Q_b^{1/2}\Delta Q_b^{1/2})\ge0.
\]
This proves the general claim without requiring \(Q\), \(M\), or the covariance reduction to have full rank.

For one direction, write \(U=u\), \(K=\kappa\), and \(R=r\), with \(u^TDu=1\) for the fixed \(D\succ0\). This normalization specifies the candidate domain; it is not an assumption of independence or oracle scale invariance. The following algebra uses only the well-posed population covariance systems. Then
\[
T=\tau=r-\kappa^TW_{yy}^{-1}\kappa>0,
\qquad M=\tilde u=u-S^TW_{yy}^{-1}\kappa.
\]
Thus
\[
\Sigma_u^{-1}=\Sigma_0^{-1}+\tau^{-1}\tilde u\tilde u^T.
\]
The rank-one Woodbury identity gives
\[
\Sigma_0-\Sigma_u
=\frac{\Sigma_0\tilde u\tilde u^T\Sigma_0}{\tau+\tilde u^T\Sigma_0\tilde u}
=\frac{xx^T}{\tau+\tilde u^Tx},\qquad x=\Sigma_0\tilde u.
\]
Its denominator is strictly positive because \(\tau>0\) and \(\tilde u^T\Sigma_0\tilde u\ge0\). In particular, this application does not require \(\tilde u\ne0\). Substitution into the trace expression and \(\operatorname{tr}(Q_bxx^T)=x^TQ_bx\) yields
\[
G(u;Q)=\frac{x^TQ_bx}{\tau+\tilde u^Tx}.
\]
The numerator is nonnegative because \(Q_b\succeq0\). Thus the displayed gain is nonnegative and has the stated dependence on adjusted target exposure, complementary residual noise, and baseline uncertainty. When \(Q=0\) or \(\tilde u=0\), the gain is zero and the denominator remains positive.

Finally, this is a result about population covariance risk under correctly specified, unregularized GLS. The residuals need not be unbiased. The argument does not control changes in squared bias or the effects of estimating covariance weights and applying finite-sample stabilization. Consequently it does not, by itself, guarantee non-deterioration of bias-inclusive MSE or finite-sample test loss.
