# Problem

## Setup

Fix integers $m,n\ge 1$ and write $r=\min(m,n)$. For $x\in\mathbb R^r$, let $E(x)\in\mathbb R^{m\times n}$ be the rectangular matrix whose first $r$ diagonal entries are $x_1,\ldots,x_r$ and whose other entries are zero. For $G\in\mathbb R^{m\times n}$, let $\sigma(G)=(\sigma_1(G),\ldots,\sigma_r(G))\in[0,\infty)^r$ be its singular values in nonincreasing order.

A map $U:\mathbb R^{m\times n}\to\mathbb R^{m\times n}$ is **bi-orthogonally equivariant** if
\[
U(PGQ^T)=P\,U(G)\,Q^T
\]
for every $G$ and every $P\in O(m),Q\in O(n)$.

A map $\widetilde\psi:\mathbb R^r\to\mathbb R^r$ is **absolutely symmetric** if $\widetilde\psi(Rx)=R\widetilde\psi(x)$ for every signed permutation matrix $R$. Its restriction to $[0,\infty)^r$ is denoted by $\psi$.

## Task

Prove the following characterization. A continuous map $U$ is bi-orthogonally equivariant if and only if there exists a continuous absolutely symmetric map $\widetilde\psi:\mathbb R^r\to\mathbb R^r$ such that, for every SVD $G=P E(\sigma(G))Q^T$,
\[
U(G)=P E(\psi(\sigma(G)))Q^T.
\]
The right-hand side must be independent of the chosen SVD.
