# Problem

## Setup

Let n,m,d be positive integers. Let \(x_1,\ldots,x_n\in\mathbb R^d\) and \(y_1,\ldots,y_m\in\mathbb R^d\), and write \(c(a,b)=\tfrac12\|a-b\|^2\). Let \(Q^*=(Q^*_{ij})\) minimize
\[
\sum_{i=1}^n\sum_{j=1}^m Q_{ij}c(x_i,y_j)
\]
over all \(Q_{ij}\geq0\) satisfying \(\sum_jQ_{ij}=1/n\) and \(\sum_iQ_{ij}=1/m\). Define the indexed values
\[
t_i=n\sum_{j=1}^m Q^*_{ij}y_j,\qquad 1\leq i\leq n.
\]

Independently, let \(\mu\) be an absolutely continuous probability measure on \(\mathbb R^d\) with finite second moment, let \(v_1,\ldots,v_m\in\mathbb R^d\), and let \(b_j>0\) with \(\sum_jb_j=1\). Put \(\nu=\sum_jb_j\delta_{v_j}\). For \(g\in\mathbb R^m\), define
\[
F(g)=\sum_{j=1}^m b_jg_j+\int \min_{1\leq l\leq m}\{c(x,v_l)-g_l\}\,d\mu(x).
\]
Let \(g\in\mathbb R^m\) be any maximizer of \(F\), and define Laguerre cells
\[
C_j(g)=\{x:c(x,v_j)-g_j\leq c(x,v_l)-g_l\ \text{for every }l\}.
\]
Let \(S_g:\mathbb R^d\to\mathbb R^d\) be any measurable selection satisfying
\[
S_g(x)\in\{v_j:x\in C_j(g),\ 1\leq j\leq m\}
\qquad\text{for every }x\in\mathbb R^d,
\]
with arbitrary tie resolution subject to measurability.

A graph is cyclically monotone if for every finite cyclic list \((x_t,w_t)_{t=1}^\ell\) from the graph,
\[
\sum_{t=1}^\ell\langle x_t,w_t\rangle\geq\sum_{t=1}^\ell\langle x_t,w_{t+1}\rangle,
\qquad w_{\ell+1}=w_1.
\]

## Task

Prove that the two graphs \(\{(x_i,t_i):1\leq i\leq n\}\) and \(\{(x,S_g(x)):x\in\mathbb R^d\}\) are cyclically monotone.
