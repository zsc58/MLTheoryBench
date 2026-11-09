# Problem

## Setup

Let \(m,n,N\) be positive integers. Let \(W,W^*\in\mathbb R^{m\times n}\), \(Z=[z_1,\ldots,z_N]\in\mathbb R^{n\times N}\), \(G\in\mathbb R^{m\times n}\), and symmetric \(H\in\mathbb R^{m\times m}\) with \(H\succ0\). Assume \(R:=ZZ^T\succ0\) and
\[
G=H(W-W^*)R/N.
\]
For \(Q\in\mathbb R^{m\times n}\), define the quadratic surrogate
\[
J(Q)=-\operatorname{tr}(QG^T)+\frac1{2N}\operatorname{tr}(HQRQ^T).
\]
Let \(\Sigma_W=(W-W^*)(W-W^*)^T\), and let \(\Sigma_W^{1/2}\) denote its positive-semidefinite square root. For a compact SVD \(X=U_XS_XV_X^T\) retaining precisely the positive singular values, define \(\operatorname{msgn}(X)=U_XV_X^T\), and set \(\operatorname{msgn}(0)=0\).

## Task

Prove that \(J\) has the unique minimizer
\[
Q^*=\Sigma_W^{1/2}\operatorname{msgn}\!\left(\Sigma_W^{1/2}G(ZZ^T)^{-1}\right),
\]
and that this minimizer equals \(W-W^*\) under the assumed gradient relation.

For \(c\ge0\), let \(Q_{\mathrm{iso}}\) denote the update obtained by replacing \(\Sigma_W\) with \(cI_m\) in the displayed expression for \(Q^*\). This replacement is a modeling proxy, not an assertion that the actual displacement second moment equals \(cI_m\). Prove that \(Q_{\mathrm{iso}}\) is a nonnegative scalar multiple of
\[
\operatorname{msgn}\!\left(G(ZZ^T)^{-1}\right),
\]
and determine that scalar for every \(c\ge0\). When the actual identity \(\Sigma_W=cI_m\) holds, identify \(Q_{\mathrm{iso}}\) with \(Q^*\).

For each integer \(t\ge0\), let \(W_t,G_t\in\mathbb R^{m\times n}\), let \(Z_t\in\mathbb R^{n\times N_t}\) with \(N_t\) a positive integer and \(Z_tZ_t^T\succ0\), and let \(c_t,\alpha_t\ge0\). Define \(Q_{\mathrm{iso},t}\) by the same proxy substitution using \(G_t,Z_t,c_t\). Show how the update \(W_{t+1}=W_t-\alpha_tQ_{\mathrm{iso},t}\) can be written as
\[
W_{t+1}=W_t-\eta_t\operatorname{msgn}\!\left(G_t(Z_tZ_t^T)^{-1}\right),
\]
by determining the effective learning rate \(\eta_t\).
