# Problem

## Setup

Let \(d\ge1\) be an integer, let \(L_0,L_1\ge0\), \(\rho\ge1\), and \(\sigma\ge0\). Let \(\xi\) have a fixed distribution \(\mathcal D\), and let \(\ell(x,\xi)\) be a sampled objective, differentiable in \(x\). Define
\[
f(x)=\mathbb E_{\xi\sim\mathcal D}[\ell(x,\xi)],\qquad g(x,\xi)=\nabla_x\ell(x,\xi).
\]
Assume that the sampled objective and oracle gradient are measurable, that the displayed expectations are finite for every fixed \(x\), and that \(f:\mathbb R^d\to\mathbb R\) is differentiable and bounded below. Assume it has a minimizer \(x^*\), with \(f^*=f(x^*)\), and that \(x^*\) also minimizes \(\ell(\cdot,\xi)\) almost surely. In particular, \(g(x^*,\xi)=0\) almost surely.

Assume that for all \(x,y\) with \(\|y-x\|\le1/L_1\),
\[
f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\tfrac12(L_0+L_1\|\nabla f(x)\|)\|y-x\|^2.
\]
When \(L_1=0\), this condition is imposed for every \(x,y\). All norms are Euclidean. For every \(x\), assume
\[
\mathbb E[g(x,\xi)]=\nabla f(x),\qquad
\mathbb E\|g(x,\xi)\|^2\le\rho\|\nabla f(x)\|^2+\sigma^2.
\]

Fix a deterministic initial point \(x^0\), positive integers \(B,N\), and deterministic parameters \(\eta>0\), \(c>0\), and \(\lambda>0\). At iteration \(k\), draw \(B\) fresh i.i.d. samples \(\xi_1^k,\ldots,\xi_B^k\) from \(\mathcal D\), independently of the history before that iteration, and form
\[
\bar g_k=\frac1B\sum_{i=1}^B g(x^k,\xi_i^k),\qquad F_0=f(x^0)-f^*.
\]

Define \(C_c(v)=v\min\{1,c/\|v\|\}\) for \(v\ne0\), and \(C_c(0)=0\). Define \(R_\lambda(v)=v/(\|v\|+\lambda)\). Consider either of the iterations
\[
x^{k+1}=x^k-\eta C_c(\bar g_k),\qquad x^{k+1}=x^k-\eta R_\lambda(\bar g_k),
\]
run for \(N\) steps. Expectations below are over all samples used by the respective iteration. In the step-size restrictions below, a zero denominator means that the upper bound on \(\eta\) is \(+\infty\).

## Task

Prove the following integrated theorem for every \(N\ge1\):

1. If \(B\ge72(\rho-1)\) and \(\eta\le[9(L_0+L_1c)]^{-1}\), then the clipped iteration satisfies
\[
\min_{0\le k<N}\mathbb E\|\nabla f(x^k)\|
\le \sqrt{\frac{18F_0}{\eta N}}+\frac{18F_0}{\eta cN}+\frac{6\sqrt2\,\sigma}{\sqrt B}+\frac{9\sigma^2}{cB}.
\]

2. If \(B\ge64(\rho-1)\) and \(\eta\le\lambda/(L_0+L_1\lambda)\), then the normalized iteration satisfies
\[
\min_{0\le k<N}\mathbb E\|\nabla f(x^k)\|
\le \frac{4F_0}{\eta N}+\frac{8\sigma}{\sqrt B}+6\lambda.
\]

In particular, when \(\sigma=0\), the stochastic residual terms vanish in both bounds.
