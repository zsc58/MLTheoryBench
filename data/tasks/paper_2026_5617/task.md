# Problem

## Setup

Let \(d\geq1\) be an integer and \(\mu\in\mathbb R^d\). Let \(X\sim N(\mu,\Lambda)\), where \(\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_d)\) and \(\lambda_j>0\). Let
\[
Y=f(X)+\epsilon,
\]
where \(f:\mathbb R^d\to\mathbb R\) is measurable and belongs to \(L^2(N(\mu,\Lambda))\), and \(\epsilon\) is real-valued, centered, square-integrable, and independent of \(X\). Instead of \(X\), observe
\[
\widetilde X=X+\eta,
\]
where \(\eta\sim N(0,\Sigma_\eta)\), \(\Sigma_\eta=\operatorname{diag}(\sigma_1^2,\ldots,\sigma_d^2)\), \(\sigma_j^2>0\), and \(\eta\) is independent of \((X,Y)\). Define
\[
\rho_j=\frac{\lambda_j}{\lambda_j+\sigma_j^2}.
\]

Write \(\mathbb N_0=\{0,1,2,\ldots\}\). For a multi-index \(\alpha\in\mathbb N_0^d\), write \(|\alpha|=\sum_j\alpha_j\) and define
\[
h_\alpha(z)=\prod_{j=1}^d\frac{\operatorname{He}_{\alpha_j}(z_j)}{\sqrt{\alpha_j!}},
\]
where \(\operatorname{He}_n\) denotes the probabilists' Hermite polynomial. Let
\[
f(x)=\sum_{\alpha\in\mathbb N_0^d}c_\alpha h_\alpha\bigl(\Lambda^{-1/2}(x-\mu)\bigr)
\]
be its \(L^2(N(\mu,\Lambda))\) Hermite expansion, so that
\[
c_\alpha=\mathbb E\left[f(X)h_\alpha\bigl(\Lambda^{-1/2}(X-\mu)\bigr)\right].
\]

Let \(g^*(\widetilde X)=\mathbb E[Y\mid\widetilde X]\), let
\[
R_{\rm Bayes}=\inf_q\mathbb E[(Y-q(\widetilde X))^2],
\]
where the infimum is over measurable functions \(q:\mathbb R^d\to\mathbb R\) satisfying \(\mathbb E[q(\widetilde X)^2]<\infty\), and let
\[
R_{\rm lin}^*=\inf_{a\in\mathbb R,\,b\in\mathbb R^d}
\mathbb E[(Y-a-b^\top\widetilde X)^2].
\]
All expectations are under the joint law specified above.

## Task

Prove that the Bayes predictor has the expansion
\[
g^*(\widetilde x)=\sum_{\alpha\in\mathbb N_0^d}c_\alpha
\left(\prod_{j=1}^d\rho_j^{\alpha_j/2}\right)
h_\alpha\bigl((\Lambda+\Sigma_\eta)^{-1/2}(\widetilde x-\mu)\bigr)
\]
in \(L^2\) under the law of \(\widetilde X\). Prove moreover the exact identity
\[
R_{\rm lin}^*-R_{\rm Bayes}
=\sum_{|\alpha|\geq2}c_\alpha^2\prod_{j=1}^d\rho_j^{\alpha_j},
\]
where the sum is over \(\alpha\in\mathbb N_0^d\) with \(|\alpha|\geq2\).
