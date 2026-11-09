# Problem

## Setup

Let \(M\ge 1\) and \(n\ge 1\), and set
\[
\mathcal H=(\mathbb R^n)^{M+1}.
\]
Write \(h=(h_0,\ldots,h_M)\in\mathcal H\). Let \(F:\mathcal H\to\mathbb R^n\) be a measurable map, and define the exact one-step update \(T:\mathcal H\to\mathcal H\) by
\[
T(h)=(h_1,\ldots,h_M,F(h)).
\]

Let \(Z\) be an \(\mathcal H\)-valued random variable. Let \(a_0,\ldots,a_M\ge0\). For a history-to-history predictor \(R=(R_0,\ldots,R_M):\mathcal H\to\mathcal H\), define
\[
\mathcal L(R)=\mathbb E\!\left[\sum_{j=0}^{M}a_j\|R_j(Z)-[T(Z)]_j\|_2^2\right].
\]

Let \(Q:\mathcal H\to\mathcal H\) and \(g:\mathcal H\to\mathbb R^n\) be measurable maps. Assume that the scalar random variables
\[
a_j\|Q_j(Z)-[T(Z)]_j\|_2^2\quad (j=0,\ldots,M)
\]
and
\[
a_M\|g(Z)-F(Z)\|_2^2
\]
are integrable.

Define
\[
B_g(h)=(h_1,\ldots,h_M,g(h)).
\]

## Task

Prove the following integrated claim:
\[
\mathcal L(Q)
=
\mathbb E\!\left[\sum_{j=0}^{M-1}a_j\|Q_j(Z)-Z_{j+1}\|_2^2\right]
+
\mathbb E\!\left[a_M\|Q_M(Z)-F(Z)\|_2^2\right],
\]
and, in particular,
\[
\mathcal L(B_g)=\mathbb E\!\left[a_M\|g(Z)-F(Z)\|_2^2\right].
\]
