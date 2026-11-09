# Problem

## Setup

Let \(n\ge 1\), and let
\[
E\subseteq\{(i,j):1\le j\le i\le n\}
\]
contain every diagonal index \((i,i)\). For each \((i,j)\in E\), let \(b_{ij}\in\mathbb R\) be an observed value and let \(v_{ij}>0\) be its known noise variance.

For a real symmetric positive-semidefinite matrix \(X\in\mathbb S_+^n\), define
\[
\ell(X)=\sum_{(i,j)\in E}\frac{(X_{ij}-b_{ij})^2}{2v_{ij}},
\qquad
\mathcal M=\operatorname*{argmin}_{X\in\mathbb S_+^n}\ell(X).
\]
Consider the reconstruction problem
\[
\operatorname*{maximize}_{X\in\mathcal M}\ \log\det X,
\]
where \(\log\det X=-\infty\) for singular \(X\).

Assume that \(\mathcal M\) contains at least one positive-definite matrix.

## Task

Prove that the reconstruction problem has a unique solution \(X^\star\). Moreover, writing \(Q^\star=(X^\star)^{-1}\), prove that for all distinct \(i,j\),
\[
Q^\star_{ij}=0
\quad\text{whenever}\quad
(i,j)\notin E\ \text{and}\ (j,i)\notin E.
\]
