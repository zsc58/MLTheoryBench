# Problem

## Setup

Fix a positive integer horizon \(T\). An online algorithm is a sequence of deterministic functions \(a_t:\mathbb R^{t-1}\to[-1,1]\), which may depend on \(T\). On each round \(t\), it chooses \(x_t=a_t(g_1,\ldots,g_{t-1})\), then observes a gradient \(g_t\in\mathbb R\) and incurs loss \(g_tx_t\). Write
\[
s_t=\sum_{i=1}^t g_i,\qquad s_0=0,\qquad
\operatorname{Loss}_T=\sum_{t=1}^Tg_tx_t.
\]

Let \(h:\mathbb R\to\mathbb R\) be a convex 1-Lipschitz function fixed before play. For \(\mu\in\mathbb R\) and \(\sigma>0\), let \(f_{\mu,\sigma,h}\) be the unique bounded solution of
\[
\sigma^2 f'(x)-(x-\mu)f(x)=h(x)-\mathbb E[h(\mu+\sigma Z)],\qquad x\in\mathbb R,
\]
where \(Z\sim N(0,1)\).

Choose \(\rho_0>0\) before play. On round \(t\), choose \(\rho_t\) as a deterministic function of \(g_1,\ldots,g_{t-1}\), subject on every history to
\[
0\le\rho_t\le\rho_{t-1},\qquad \rho_t>0\text{ if }t<T,
\]
and put \(c_t=\rho_{t-1}^2-\rho_t^2\). Define the algorithm by
\[
x_t=\mathbb E_Z\!\left[f_{s_{t-1},\rho_{t-1},h}(s_{t-1}+\rho_t Z)\right],
\qquad t=1,\ldots,T.
\]
Here and in the claims below, \(\mathbb E_Z\) integrates only over a standard normal variable, with the gradient history and the resulting scale values held fixed.

## Task

Prove the following integrated theorem.

1. For every admissible rule for choosing the scales and every gradient sequence in \(\mathbb R^T\), the actions above are feasible and
\[
\operatorname{Loss}_T\le -\mathbb E_Z h(s_T+\rho_T Z)+\mathbb E_Z h(\rho_0 Z)
+\sum_{t=1}^T\left[
\frac{\sqrt{2/\pi}\,\max\{g_t^2-c_t,0\}}{\rho_{t-1}}
+\frac{2c_t|g_t|+|g_t|^3}{\rho_{t-1}^2}
\right].
\]

2. There is an absolute constant \(C>0\), independent of the horizon, algorithm and function, such that for every positive integer \(T\), every online algorithm in the class defined above, and every 1-Lipschitz function \(h:\mathbb R\to\mathbb R\) (not necessarily convex), some sequence \(g_t\in\{-1,1\}\) satisfies
\[
\operatorname{Loss}_T> -h\!\left(\sum_{t=1}^T g_t\right)+\mathbb E_Z h(\sqrt T\,Z)-C.
\]
