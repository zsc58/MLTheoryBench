# Problem

## Setup

Let \(X\in\mathbb R^{m\times n}\) have rank \(r\), with \(1\le r\le\min\{m,n\}\). For each positive integer \(k\), let \(\mathbf1_k\in\mathbb R^k\) be the all-ones vector. Define
\[
\Delta^{r\times n}=\{H\in\mathbb R^{r\times n}:H\ge0,\ \mathbf1_r^TH=\mathbf1_n^T\}.
\]
A feasible nonnegative factorization is a pair \((W,H)\) with \(W\in\mathbb R^{m\times r}\), \(W\ge0\), \(H\in\Delta^{r\times n}\), and \(X=WH\). Among feasible pairs, maximize \(\det(HH^T)\). Assume \((W,H)\) is such a maximizer and that \(H\) is sufficiently scattered in the following sense. With
\[
C=\{x\in\mathbb R^r:x\ge0,\ \mathbf1_r^Tx\ge\sqrt{r-1}\,\|x\|_2\},
\]
we have \(C\subseteq\operatorname{cone}(H)\), and whenever an orthogonal matrix \(R\) satisfies \(\operatorname{cone}(H)\subseteq\operatorname{cone}(R)\), the matrix \(R\) is a permutation matrix. Here \(\operatorname{cone}(H)\) is the conic hull of the columns of \(H\), and \(\operatorname{cone}(R)\) is the conic hull of the columns of \(R\).

## Task

Prove that every other feasible pair \((\widetilde W,\widetilde H)\) attaining the same maximum determinant is obtained from \((W,H)\) by permuting the components: there exists a permutation matrix \(P\) such that
\[
\widetilde W=WP^{-1},\qquad \widetilde H=PH.
\]
