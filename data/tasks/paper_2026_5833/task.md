# Problem

## Setup

Let \(d,m\) be positive integers. Fix a known matrix \(A\in\mathbb R^{m\times d}\) with nontrivial kernel, a known positive-definite noise covariance \(\Gamma\), and a positive-definite Gaussian regularizer \(\rho=\mathcal N(\mu_\rho,\Sigma_\rho)\). Let \(X\in\mathbb R^d\) have Gaussian truth law \(p_*=\mathcal N(\mu_*,\Sigma_*)\), with \(\Sigma_*\) positive definite, and let \(Y\in\mathbb R^m\) satisfy
\[
p(y\mid x)=\mathcal N(y;Ax,\Gamma).
\]

Put \(B=\ker(A)\) and \(k=\operatorname{rank}(A)\). Let \(N\in\mathbb R^{d\times(d-k)}\) have orthonormal columns spanning \(B\), and let \(U\in\mathbb R^{d\times k}\) have orthonormal columns spanning \(\operatorname{row}(A)\). Write \(x=Ur+Nb\), where \(r=U^Tx\) and \(b=N^Tx\).

Define the induced measurement marginal, legacy posterior, and posterior-sample curation law by
\[
p_*^Y(y)=\int p(y\mid x)p_*(x)\,dx,
\qquad
\pi_\rho(x\mid y)=\frac{p(y\mid x)\rho(x)}{\int p(y\mid x')\rho(x')\,dx'},
\]
\[
q_\rho(x)=\int p_*^Y(y)\pi_\rho(x\mid y)\,dy.
\]

Fix a unit vector \(v\in B\), and put \(R=U^TX\) and \(V=v^TX\). Under law \(j\in\{\rho,*\}\), let \(m_j(r)\) and \(s_j(r)>0\) denote the conditional mean and standard deviation of \(V\mid R=r\), using the Gaussian conditional versions. If \(k=0\), \(R\) takes its sole value in \(\mathbb R^0\), and conditioning on \(R\) means taking the unconditional law.

Fix \(0<\alpha<1\). Let \(\Phi\) be the standard normal cumulative distribution function and set \(z=z_{1-\alpha/2}=\Phi^{-1}(1-\alpha/2)\). Define
\[
I_\rho(r)=[m_\rho(r)-z s_\rho(r),\ m_\rho(r)+z s_\rho(r)],
\]
\[
C_*(r)=\Pr_*\{V\in I_\rho(r)\mid R=r\},\qquad
D_*(r)=(1-\alpha)-C_*(r).
\]
Thus a positive coverage deficit \(D_*(r)\) means undercoverage.

For identifiability, vary \((\mu_*,\Sigma_*)\) over all Gaussian truth parameters with \(\Sigma_*\) positive definite, holding \(A,\Gamma,\rho,U,N,v,\alpha\) fixed. A quantity is identifiable from \(p_*^Y\) if any two such truth parameters with the same measurement marginal give the same quantity. A deterministic archive formed from measurements means a fixed measurable function of those measurements and the fixed known objects, with the same function used under every candidate truth. When more than one measurement is considered, the measurements are independent draws from \(p_*^Y\).

## Task

Prove the following integrated theorem.

1. For almost every \(r\),
\[
q_\rho(b\mid r)=\rho(b\mid r).
\]
Consequently, \(I_\rho(r)\) is the central conditional interval of level \(1-\alpha\) under the curated law, and its truth conditional coverage is
\[
C_*(r)=\Phi\!\left(\delta(r)+z\frac{s_\rho(r)}{s_*(r)}\right)-\Phi\!\left(\delta(r)-z\frac{s_\rho(r)}{s_*(r)}\right),
\qquad
\delta(r)=\frac{m_\rho(r)-m_*(r)}{s_*(r)}.
\]
At \(\delta(r)=0\), coverage is below nominal exactly when \(s_\rho(r)<s_*(r)\). For fixed \(\alpha\) and width ratio \(s_\rho(r)/s_*(r)\), coverage decreases as \(|\delta(r)|\) grows.

2. The quantities \(s_*(r)\), \(\delta(r)\), and \(D_*(r)\) are not identifiable from \(p_*^Y\). In particular, distinct positive-definite Gaussian truth parameters can have the same \(A\mu_*\) and \(A\Sigma_*A^T\), hence the same measurement law, while differing in blind conditional means or variances and in coverage. Therefore no statistic of measurements, or of a deterministic archive formed from them, can distinguish all cases of inherited blind undercoverage from its absence.
