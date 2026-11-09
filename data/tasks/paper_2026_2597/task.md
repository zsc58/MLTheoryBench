# Problem

## Setup

Fix an integer $m\ge 2$, an integer $k_1\ge 1$, and a compact set $K\subset\mathbb R^{k_1}$. An input is an $m\times k_1$ array $X$ with rows $X_1,\ldots,X_m\in K$. A permutation matrix $P$ acts by permuting rows, and a map $g:K^m\to\mathbb R^m$ is permutation preserving if $g(PX)=Pg(X)$ for every such $P$. Equip $\mathbb R^m$ with the sup norm. If $K$ is empty, take the uniform errors below to be $0$.

## Task

Prove the following theorem. For every continuous permutation-preserving $g:K^m\to\mathbb R^m$ and every $\varepsilon>0$, there exist finite dimensions $q,r$ and continuous maps $\phi:K\to\mathbb R^q$, $\rho_2:\mathbb R^q\to\mathbb R^r$, and $\rho_1:K\times\mathbb R^r\to\mathbb R$ such that
\[
\widetilde g_i(X)=\rho_1\!\left(X_i,\rho_2\!\left(\sum_{j\ne i}\phi(X_j)\right)\right),\qquad i=1,\ldots,m,
\]
satisfies $\widetilde g(PX)=P\widetilde g(X)$ for every permutation $P$ and
\[
\sup_{X\in K^m}\|g(X)-\widetilde g(X)\|_\infty<\varepsilon.
\]
When $k_1=1$, the same form can represent $g$ exactly, so the supremum error is zero.
