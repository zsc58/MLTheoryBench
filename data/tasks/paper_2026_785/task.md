# Problem

## Setup

Fix an integer \(d\ge1\) and a nonzero scalar \(\alpha\). Let
\[
\phi(v)_i=\max(v_i,\alpha v_i)
\]
act coordinatewise on \(\mathbb R^d\). Let \((W_n)_{n\ge1}\) be i.i.d. random \(d\times d\) matrices, and for a fixed nonzero input \(x\) define
\[
X_0=x,\qquad X_n=\phi(W_nX_{n-1}).
\]
Assume one of the following.

**(A) Entry-density law.** The entries of \(W_1\) are independent, each has a bounded density and finite second moment, and there is a common neighborhood of zero on which every entry density is bounded below by the same positive constant.

**(B) Scaled-orthogonal law.** \(W_1=\eta Q\) almost surely for some \(\eta\ne0\), where the law of \(Q\in O(d)\) is absolutely continuous with respect to Haar probability with a density bounded below by a positive constant.

Use the Euclidean norm and induced operator norm, and set \(N(W)=\max(\|W\|,\|W^{-1}\|)\) whenever \(W\) is invertible. Define the spherical state \(S_n=X_n/\|X_n\|\) and the transition kernel
\[
P(s,A)=\Pr\!\left\{\frac{\phi(W_1s)}{\|\phi(W_1s)\|}\in A\right\},\qquad s\in\mathbb S^{d-1},
\]
for Borel sets \(A\subseteq\mathbb S^{d-1}\).

## Task

Prove that \(P\) has a unique stationary probability \(\nu\), and that the stationary integral
\[
\lambda=\int_{\mathbb S^{d-1}}\mathbb E\big[\log\|\phi(W_1s)\|\big]\,\nu(ds)
\]
is finite. Prove that, for every fixed nonzero \(x\),
\[
\frac{1}{n}\log\|X_n\|\longrightarrow\lambda\quad\text{almost surely},
\]
and
\[
\sup_{x\ne0}\mathbb E\left[\left|\frac1n\log\frac{\|X_n\|}{\|x\|}-\lambda\right|\right]\longrightarrow0.
\]
Moreover, prove that there exists \(\gamma^2\ge0\) such that, for every fixed nonzero \(x\),
\[
\frac{\log\|X_n\|-n\lambda}{\sqrt n}\Rightarrow\mathcal N(0,\gamma^2).
\]
Here \(\Rightarrow\) denotes convergence in distribution.
