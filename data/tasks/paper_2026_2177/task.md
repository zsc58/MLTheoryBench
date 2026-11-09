# Problem

## Setup

Let \(I\subset\mathbb R\) be an interval and \(\mu\) a finite positive Borel measure on \(I\) with infinite support and all polynomial moments finite. Let \(p_r\) be the degree-\(r\) orthonormal polynomial in \(L^2(\mu)\) with positive leading coefficient. Fix \(n\in\mathbb N_0\) and an integer \(d\ge2\), and let \(\mathcal K=\{0,1,\ldots,n\}^d\). Define \(p_k(x)=\prod_{j=1}^d p_{k_j}(x_j)\), let \(\mathcal H_n^{(d)}\) be their span with the \(L^2(\mu^{\otimes d})\) inner product, and set
\[
K_n^{(d)}(x,z)=\prod_{j=1}^d\left(\sum_{r=0}^n p_r(x_j)p_r(z_j)\right).
\]
Let \(N\) be a positive integer, \(C>0\), \(x_i\in I^d\), and \(y_i\in\{-1,1\}\) for \(1\le i\le N\). Let \(\alpha=(\alpha_1,\ldots,\alpha_N)\) be any solution of the binary soft-margin SVM dual problem
\[
\max_{a\in\mathbb R^N}\left\{
\sum_{i=1}^N a_i-\frac12\sum_{i=1}^N\sum_{j=1}^N a_i a_j y_i y_j K_n^{(d)}(x_i,x_j)
:\ 0\le a_i\le C\ (1\le i\le N),\ \sum_{i=1}^N a_i y_i=0
\right\}.
\]
Define
\[
h(x)=\sum_{i=1}^N\alpha_i y_iK_n^{(d)}(x_i,x),\quad P_{i,k}=p_k(x_i),\quad s_i=\alpha_i y_i.
\]

## Task

Prove that \(h\in\mathcal H_n^{(d)}\) and has the exact unique expansion
\[
h(x)=\sum_{k\in\mathcal K}c_kp_k(x),\qquad c_k=\sum_{i=1}^N\alpha_i y_i p_k(x_i),
\]
and, in vector form, \(c=P^Ts\). Establish the basis and kernel properties needed in the proof.
