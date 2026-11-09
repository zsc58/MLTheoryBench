# Problem

## Setup

Let \(n\) be a positive integer. Let \(M_0,M_1,\ldots\) be independent random real symmetric \(n\times n\) positive-semidefinite matrices satisfying \(0\preceq M_t\preceq I\) almost surely and \(\mathbb E M_t=\bar M\) for a fixed matrix \(0\preceq\bar M\preceq I\). For \(x\in\mathbb R^n\), write \(\|x\|_{\bar M}^2=x^\top\bar Mx\). Vector norms without a subscript are Euclidean norms, and matrix norms are operator norms.

Let \(\Delta_0\in\mathbb R^n\) be deterministic and define \(\Delta_{t+1}=(I-M_t)\Delta_t\) for every integer \(t\ge0\). Define the deterministic matrix recursion
\[
N_0=\bar M,\qquad N_{t+1}=N_t(I-2\bar M)+\|N_t\|\,\bar M.
\]

## Task

Prove the following integrated theorem.

1. There is an absolute constant \(C>0\) such that every process above satisfies, for all integers \(t\ge0\),
\[
\mathbb E\|\Delta_t\|_{\bar M}^2\le C\,\mathbb E\|\Delta_0\|^2\,(t+2)^{-0.751}.
\]
Equivalently, the exponent is \(3/4+\theta\) with the choice \(\theta=0.001\).

2. There are an absolute constant \(c>0\) and a positive integer \(t_{\rm ref}\) such that, for every integer \(T\ge t_{\rm ref}\), the diagonal matrix
\[
\bar M^{(T)}=\operatorname{diag}(\rho_1,\ldots,\rho_T),\qquad
\rho_m=\tfrac12(1-e^{-3/(2m)}),
\]
produces through the displayed recursion matrices \(N_t^{(T)}\) obeying
\[
\|N_t^{(T)}\|\ge c\,(t+1)^{-0.753}\qquad(0\le t\le T).
\]
Furthermore, for each fixed real \(p\ge0.753\), there is no finite constant \(K>0\) such that
\[
\|N_t\|\le K(t+1)^{-p}
\]
holds simultaneously for every positive integer dimension \(n\), every real symmetric matrix \(0\preceq\bar M\preceq I\), and every integer \(t\ge0\), with \(N_t\) defined by the displayed deterministic recursion.
