# Problem

## Setup

Let \(d\ge 1\) be an integer. Let the target law be \(\mu=\mathcal N(0,I_d)\), and let \(\sigma_0=\mathcal N(0,\Sigma_0)\) with \(\Sigma_0\) symmetric positive definite. For a centered absolutely continuous law \(\sigma\) with finite second moment and a unit vector \(\theta\), write \(\theta_\#\sigma\) for its one-dimensional projection and let \(t_\theta^\sigma\) be the monotone quadratic-cost transport from \(\theta_\#\sigma\) to \(\theta_\#\mu\). If \(P=[\theta_1,\ldots,\theta_d]\) is an orthonormal basis, define
\[
T_{\sigma,P}(x)=\sum_{i=1}^d t_{\theta_i}^\sigma(\theta_i^\top x)\,\theta_i.
\]
Let \(P_1,P_2,\ldots\) be independent Haar-uniform orthonormal bases and let
\(\gamma_k=(k+1)^{-\alpha}\), where \(0<\alpha<1\). Define
\[
\sigma_{k+1}=\big((1-\gamma_k)\operatorname{Id}+\gamma_k T_{\sigma_k,P_{k+1}}\big)_\#\sigma_k,
\qquad k\ge0.
\]
Define the sliced-Wasserstein objective
\[
F(\sigma)=\frac d2\,SW_2^2(\sigma,\mu),
\]
where \(SW_2^2\) is the spherical average of the one-dimensional squared Wasserstein distances. The expectation below is over the sampled bases.

## Task

Prove the following bounds for every \(k\ge1\):

1. If \(0<\alpha<2/3\), then for every \(0<\varepsilon<\min\{\alpha,1-\alpha\}\), there is a constant \(C<\infty\) such that
\[
\mathbb E[F(\sigma_k)]\le C\,k^{-(1-\alpha-\varepsilon)}.
\]

2. If \(2/3<\alpha<1\), then there is a constant \(C<\infty\) such that
\[
\mathbb E[F(\sigma_k)]\le C\,k^{-(2\alpha-1)}.
\]

The constants may depend on \(d,\Sigma_0,\alpha\) and, in the first regime, on \(\varepsilon\), but not on \(k\).
