# Problem

## Setup

Let \(P\in\mathbb R^{n\times n}\) be a row-stochastic matrix. Let \(P_{\mathbb C}\) denote its complexification and, for each eigenvalue \(\lambda\), let
\[
E_\lambda=\ker(P_{\mathbb C}-\lambda I)^n
\]
be its generalized eigenspace. Define the real peripheral subspace
\[
\mathcal K=\left(\bigoplus_{|\lambda|=1}E_\lambda\right)\cap\mathbb R^n.
\]

For a real \(P\)-invariant subspace \(L\), write \(\overline P_L\) for the operator induced by \(P\) on \(\mathbb R^n/L\), and write \([x]_L\) for the class of \(x\). Let \(\rho(A)\) denote the spectral radius of an operator \(A\).

Define the Cesaro operator
\[
C=\lim_{T\to\infty}\frac1T\sum_{t=0}^{T-1}P^t.
\]
For a reward vector \(r\in\mathbb R^n\), set \(\rho=Cr\), and call \(h\) its normalized bias if
\[
r=\rho+(I-P)h,\qquad Ch=0.
\]

Let \(G:\mathbb R^n\to\mathbb R^n\) be any linear projection satisfying
\[
G^2=G,
\qquad \ker G=\mathcal K.
\]

## Task

Prove the following theorem.

For every real \(P\)-invariant subspace \(L\),
\[
\rho(\overline P_L)<1
\quad\Longleftrightarrow\quad
\mathcal K\subseteq L.
\]
Consequently, \(\mathcal K\) is the unique least, and hence unique inclusion-minimal, invariant subspace producing strictly stable quotient dynamics.

For every \(r\in\mathbb R^n\), there is a unique pair
\[
(g,v)\in\mathcal K\times\operatorname{ran}G
\]
such that
\[
r=g+(I-P)v.
\]
Equivalently, \(v\) is the unique element of \(\operatorname{ran}G\) satisfying
\[
v=G(r+Pv),
\qquad g=r-(I-P)v.
\]

The normalized bias \(h\) exists uniquely. For the same pair \((g,v)\), there is a unique
\[
\psi\in\mathcal K\cap\ker C
\]
such that
\[
g=\rho+(I-P)\psi.
\]
Furthermore,
\[
h=v+\psi-Cv,
\qquad Gh=v,
\qquad g=\rho+(I-P)(I-G)h.
\]
