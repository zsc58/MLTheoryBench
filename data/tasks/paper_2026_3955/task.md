# Problem

## Setup

Let \(X\in\mathbb R^{n\times n}\) be symmetric and entrywise nonnegative. Let \(E\subseteq\{1,\ldots,n\}^2\) be a symmetric set of observed indices, and define the masking operator
\[
(P_E(A))_{ij}=\begin{cases}A_{ij},&(i,j)\in E,\\0,&(i,j)\notin E.\end{cases}
\]
For a rank parameter \(r\ge1\), let \(U,V\in\mathbb R^{n\times r}_+\), and let \(\lambda>0\). Define
\[
F(U,V)=\tfrac12\|P_E(X-UV^\top)\|_F^2+\tfrac\lambda2\|U-V\|_F^2,
\]
and
\[
G(W)=\tfrac12\|P_E(X-WW^\top)\|_F^2,\qquad W\in\mathbb R^{n\times r}_+.
\]
A critical point means that zero belongs to the gradient plus the normal cone of the nonnegative orthant constraint. Let \(\sigma_n(A)\) denote the smallest eigenvalue of a symmetric matrix \(A\).

## Task

Prove the following theorem. If \((U^*,V^*)\) is a critical point of \(F\) and
\[
\|P_E(U^*V^{*\top})\|_F<2\lambda+\sigma_n(P_E(X)),
\]
then \(U^*=V^*\), and this common matrix is a critical point of \(G\).
