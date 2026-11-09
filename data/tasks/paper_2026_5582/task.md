# Problem

## Setup

Let \(d,K,m\) be positive integers, put \(n=Kd\), and fix \(\lambda>0\) and \(S>0\). At round \(t\), let \(\mathcal X_t\subset\mathbb R^d\) be a finite action set.

A sketched procedure stores
\[
H_t=\lambda I_n+U_tD_tU_t^\top,
\qquad
D_t=\operatorname{diag}(\mu_1,\ldots,\mu_m),
\]
where \(U_t\in\mathbb R^{n\times m}\) has orthonormal columns and \(\mu_j\ge0\). Write each column of \(U_t\) in \(K\) consecutive blocks of length \(d\).

The action-dependent quantity to be evaluated for every \(x\in\mathcal X_t\) is
\[
\bigl\|H_t^{-1/2}(I_K\otimes x)\bigr\|_2^2,
\]
where \(\|\cdot\|_2\) denotes the matrix operator norm.

The parameter update uses another positive-definite low-rank-plus-ridge matrix
\[
G_t=\lambda I_n+Q_t\Gamma_tQ_t^\top,
\qquad
\Gamma_t=\operatorname{diag}(\alpha_1,\ldots,\alpha_q),
\]
where \(Q_t\in\mathbb R^{n\times q}\) has orthonormal columns, \(\alpha_j\ge0\), and \(q\le m+K\). Given an unconstrained vector \(w'\in\mathbb R^n\), the update is
\[
\operatorname*{argmin}_{\|w\|_2\le S}\frac12(w-w')^\top G_t(w-w').
\]
Each round forms its sketched factors by appending at most \(K\) columns to a retained factor and computing a thin spectral decomposition. Arithmetic costs are measured in the standard dense model, with numerical accuracy suppressed when counting dependence on \(d,K,m\). Space counts maintained state and auxiliary working memory, excluding the externally supplied action set and storage for reported outputs.

## Task

Prove the following integrated efficiency theorem.

The action-dependent operator norm can be reduced exactly to the largest eigenvalue of a positive-semidefinite \(K\times K\) matrix and evaluated, for each action, in
\[
O(Kdm+K^2m+K^3)
\]
time. The constrained metric projection equals \(w'\) when \(\|w'\|_2\le S\); otherwise it can be reduced to a one-dimensional equation having a unique positive root, from which the exact projection is recovered using the stored low-rank factors.

Together with the thin spectral updates, these reductions yield total working space
\[
O(Kd(m+K))
\]
and per-round time
\[
O\!\left(|\mathcal X_t|(Kdm+K^2m+K^3)+Kd(m+K)^2\right).
\]
When \(|\mathcal X_t|\) is treated as constant or its action-evaluation term is non-dominating, the dependence on \(d,m,K\) is \(O(Kd(m+K)^2)\).
