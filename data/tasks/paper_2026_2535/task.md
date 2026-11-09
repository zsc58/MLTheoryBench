# Problem

## Setup

Let \(M\) be a measurable manifold and let \((X_t)_{t\in\mathbb Z}\) be a stationary sequence with marginal law \(\pi\) on \(M\). Let \(k:M\times M\to\mathbb R\) be symmetric and positive definite, with
\[
K_0:=\sup_{x\in M}k(x,x)<\infty,
\]
and suppose its feature map \(x\mapsto k(x,\cdot)\) into the RKHS \(H\) is Bochner measurable. For any probability measure \(\mu\) for which the Bochner integral exists, write
\[
m_\mu:=\int_M k(x,\cdot)\,\mu(dx),\qquad \mathrm{MMD}_k^2(\mu,\nu):=\|m_\mu-m_\nu\|_H^2.
\]
Define
\[
m_\pi:=\int_M k(x,\cdot)\,\pi(dx),\qquad \phi(x):=k(x,\cdot)-m_\pi.
\]
Then \(\int\phi\,d\pi=0\) and \(\phi\) is bounded. For every \(\ell\in\mathbb Z\), define
\[
\gamma_\ell:=\mathbb E\langle\phi(X_0),\phi(X_\ell)\rangle_H,
\]
and assume \(\gamma_0>0\) and \(\sum_{\ell=1}^{\infty}|\gamma_\ell|<\infty\). Let \(\widehat\pi_n:=n^{-1}\sum_{t=1}^n\delta_{X_t}\),
\[
R_n:=\mathbb E\,\mathrm{MMD}_k^2(\widehat\pi_n,\pi),
\]
and define
\[
\mathrm{ESS}^{(n)}_k:=
\begin{cases}
\gamma_0/R_n,&R_n>0,\\
+\infty,&R_n=0.
\end{cases}
\]

## Task

Prove the following integrated theorem. For every \(n\ge1\),
\[
R_n=\frac1{n^2}\left[n\gamma_0+2\sum_{\ell=1}^{n-1}(n-\ell)\gamma_\ell\right],
\]
and, whenever the denominator (equivalently \(R_n\)) is positive,
\[
\mathrm{ESS}^{(n)}_k=\frac{n^2\gamma_0}{n\gamma_0+2\sum_{\ell=1}^{n-1}(n-\ell)\gamma_\ell},
\]
with the stated infinite value when it is zero. Moreover, letting
\[
\sigma_k^2:=\gamma_0+2\sum_{\ell=1}^{\infty}\gamma_\ell,
\]
we have \(\sigma_k^2\ge0\) and \(nR_n\to\sigma_k^2\). If \(\sigma_k^2>0\), then
\[
\frac{\mathrm{ESS}^{(n)}_k}{n}\to\frac{\gamma_0}{\sigma_k^2}
=\left(1+2\sum_{\ell=1}^{\infty}\frac{\gamma_\ell}{\gamma_0}\right)^{-1};
\]
if \(\sigma_k^2=0\), then \(R_n=o(n^{-1})\) and \(\mathrm{ESS}^{(n)}_k/n\to+\infty\) along indices with \(R_n>0\) (while it is already infinite when \(R_n=0\)).
