# Problem

## Setup

Fix one forecast horizon. Let the latent state be \(b\in\mathbb R^n\), with natural measurements \(y=Sb\), where \(S\in\mathbb R^{m\times n}\). For a candidate matrix \(U\in\mathbb R^{n\times k}\) with integer \(k\ge1\), define auxiliary measurements \(c(U)=U^Tb\). A frozen forecasting oracle supplies \(\hat y\) and \(\hat c(U)\); write \(\hat z=[\hat y;\hat c(U)]=H_Ub+e\), with \(H_U=[S;U^T]\) and residual covariance
\[
W_U=\operatorname{Cov}(e)=\begin{bmatrix}W_{yy}&K_U\\K_U^T&R_U\end{bmatrix}.
\]
Assume all residuals have finite second moments, \(W_{yy}\succ0\), \(W_U\succ0\), and the normal matrices \(S^TW_{yy}^{-1}S\) and \(H_U^TW_U^{-1}H_U\) are invertible. Let \(Q\succeq0\) weight the reported measurement error. Population unregularized GLS uses the corresponding covariance-weighted least-squares estimator, and the reported forecast is \(S\hat b\). Define \(Q_b=S^TQS\), \(\Sigma_0=(S^TW_{yy}^{-1}S)^{-1}\), and \(\Sigma_U=(H_U^TW_U^{-1}H_U)^{-1}\). The covariance-risk gain is
\[
G(U;Q)=\operatorname{tr}\!\left(Q\,[S\Sigma_0S^T-S\Sigma_US^T]\right).
\]

## Task

Prove the following integrated theorem. For every admissible \(U\), population GLS augmentation satisfies
\[
\Sigma_U\preceq\Sigma_0\qquad\text{and}\qquad G(U;Q)\ge0.
\]
In the single-direction case \(k=1\), write \(U=u\), \(K_U=\kappa\), and \(R_U=r\). Let \(D\in\mathbb R^{n\times n}\) be a fixed symmetric positive-definite normalization matrix and assume \(u^TDu=1\). Define
\[
\tau=r-\kappa^TW_{yy}^{-1}\kappa,\quad \tilde u=u-S^TW_{yy}^{-1}\kappa,\quad x=\Sigma_0\tilde u.
\]
Show the exact identity
\[
G(u;Q)=\frac{x^TQ_bx}{\tau+\tilde u^Tx},
\]
with a strictly positive denominator. State explicitly that the result concerns population covariance risk under correctly specified GLS, not bias-inclusive MSE or finite-sample test loss.
