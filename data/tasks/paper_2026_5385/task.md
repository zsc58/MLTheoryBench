# Problem

## Setup

Fix \(K\ge2\) and let
\[
\Delta^{K-1}=\{p\in\mathbb R^K:p_i\ge0,\ \sum_{i=1}^Kp_i=1\}.
\]
For \(\alpha=(\alpha_1,\ldots,\alpha_K)\in(0,\infty)^K\), set \(\alpha_0=\sum_i\alpha_i\), let \(\pi\sim\operatorname{Dirichlet}(\alpha)\), and define \(\bar p=\alpha/\alpha_0\). For a fixed label \(y\in\{1,\ldots,K\}\), let \(\ell(\cdot,y)\) be twice continuously differentiable on an open neighborhood of \(\Delta^{K-1}\). Write \(H_\ell\) for its Hessian and assume, for finite \(M,G\), that for all \(u,v\in\Delta^{K-1}\),
\[
\|H_\ell(u,y)\|_{\mathrm{op}}\le M,\qquad \|H_\ell(u,y)-H_\ell(v,y)\|_{\mathrm{op}}\le G\|u-v\|_2.
\]
For \(q\in\mathbb R^K\), \(\operatorname{Diag}(q)\) denotes the diagonal matrix with diagonal q.

## Task

Prove that
\[
\mathbb E[\ell(\pi,y)]=\ell(\bar p,y)+\frac{1}{\alpha_0+1}L_1(\bar p,y)+R(\alpha,y),
\]
where
\[
L_1(\bar p,y)=\frac12\operatorname{tr}\!\left(H_\ell(\bar p,y)(\operatorname{Diag}(\bar p)-\bar p\bar p^\top)\right),
\]
and \(|R(\alpha,y)|\le G/[3(\alpha_0+1)]\). In particular, the discrepancy from the plug-in loss is \(O((\alpha_0+1)^{-1})\).
