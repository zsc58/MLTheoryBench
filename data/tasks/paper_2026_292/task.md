# Problem

## Setup

Let \(X\subset\mathbb R^n\) be nonempty, compact, and convex. Let \(H:\mathbb R^n\to\mathbb R\) be \(\mu_H\)-strongly convex for some \(\mu_H>0\), and let \(f_j^i:\mathbb R^n\to\mathbb R\) be convex for clients \(i=1,\ldots,S\) and components \(j=1,\ldots,I_i\). Define
\[
F_i(x)=\sum_{j=1}^{I_i}f_j^i(x),\qquad F(x)=\sum_{i=1}^SF_i(x),\qquad m=\sum_{i=1}^SI_i.
\]
Let \(x^\star\) be the unique minimizer of \(H\) over \(\arg\min_{x\in X}F(x)\). On \(X\), selected subgradients of every \(f_j^i\) and of \(H\) have norms bounded by \(B_f\) and \(B_H\), the functions are \(L_f\)- and \(L_H\)-Lipschitz, and \(|H|\le M_H\). Put \(C_f=\max\{B_f,L_f\}\) and \(C_H=\max\{B_H,L_H,M_H\}\).

Starting from \(x_1\in\mathbb R^n\), let \(\gamma_k>0\), \(\lambda_k>0\). At round \(k\), choose \(H_k\in\partial H(x_k)\), broadcast \(x_k,H_k\), and initialize \(x_{k,1}^i=x_k\). For \(j=1,\ldots,I_i\), choose \(g_{k,j}^i\in\partial f_j^i(x_{k,j}^i)\) and set
\[
x_{k,j+1}^i=P_X\!\left(x_{k,j}^i-\gamma_kg_{k,j}^i-\frac{\gamma_k\lambda_k}{m}H_k\right),\qquad x_k^i=x_{k,I_i+1}^i,
\]
and let \(x_{k+1}=S^{-1}\sum_{i=1}^Sx_k^i\).

## Task

Prove that for every \(\varepsilon\in(0,1/2)\), if
\[
\gamma_k=\frac{\gamma_1}{k^a},\qquad \lambda_k=\frac{\lambda_1}{k^b},\qquad a=\frac12+\frac\varepsilon2,\quad b=\frac12-\varepsilon,
\]
with \(\gamma_1\lambda_1\mu_H\le 2m\), then the weighted average
\[
\bar x_K=\frac{\sum_{k=1}^K\gamma_kx_k}{\sum_{k=1}^K\gamma_k}
\]
satisfies
\[
F(\bar x_K)-F(x^\star)=O\!\left(K^{-(1/2-\varepsilon)}\right)\qquad(K\to\infty).
\]
