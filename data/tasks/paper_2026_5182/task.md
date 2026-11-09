# Problem

## Setup

Let \(A\in\mathbb R^{d\times n}\), \(b\in\mathbb R^d\), and \(\mathcal B=\{0,1\}^n\). For \(z\in\mathcal B\), write \(\|z\|_0=\mathbf 1^\top z\). Define the exact feasible set
\[
\mathcal E=\{z\in\mathcal B:Az+b=0\}.
\]
Assume \(\mathcal E\neq\varnothing\), and let
\[
K=\min_{z\in\mathcal E}\|z\|_0.
\]
Fix \(\tau>0\) and define, for \(z\in\mathcal B\),
\[
Q_\tau(z)=\|Az+b\|_2^2+\tau^2\mathbf 1^\top z.
\]
For each integer \(k\) with \(0\le k<K\), define
\[
r_k=\min_{\substack{z\in\mathcal B\\\|z\|_0=k}}\|Az+b\|_2.
\]
Assume that
\[
r_k^2>\tau^2(K-k)\qquad\text{for every integer }k\text{ with }0\le k<K.
\]

## Task

Prove that every minimizer \(\widehat z\in\arg\min_{z\in\mathcal B}Q_\tau(z)\) belongs to \(\mathcal E\) and satisfies \(\|\widehat z\|_0=K\). Thus every surrogate minimizer is an exact feasible vector with the minimum possible number of flips.
