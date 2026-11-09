# Problem

## Setup

Let \(N,d,d_v\) be positive integers. Let \(X\in\mathbb R^{N\times d}\), let \(W^Q,W^K\in\mathbb R^{d\times d_v}\), and define
\[
Q=XW^Q,\qquad K=XW^K,\qquad S=\frac{\alpha}{\sqrt{d_v}}(QK^\top-KQ^\top),
\]
where \(\alpha\in\mathbb R\). Set
\[
U=\operatorname{span}(\operatorname{col}Q,\operatorname{col}K),\qquad r=\dim U\le\min(N,2d_v),
\]
and let \(C\in\mathbb R^{N\times r}\) have orthonormal columns spanning \(U\).

Set \(m=2d_v\) and \(M=[Q,K]\in\mathbb R^{N\times m}\). For any \(\epsilon>0\) and nonnegative integer \(T\), define the normalized Newton--Schulz iterates by
\[
M_0=\frac{M}{\|M\|_F+\epsilon},\qquad
M_{k+1}=\frac12M_k(3I_m-M_k^\top M_k)\quad(0\le k<T),\qquad B=M_T,
\]
where \(\|M\|_F=(\sum_{i,j}M_{ij}^2)^{1/2}\).

Let \(p=\min(N,m)\), and denote all \(p\) singular values of \(B\), including zeros, by \(\sigma_1(B),\ldots,\sigma_p(B)\). Assume \(0\le\sigma_i(B)\le1\) for all \(i\). Define
\[
G=B^\top SB,\qquad Y=I_N+B(e^G-I_m)B^\top.
\]
Here \(e^H\) denotes the matrix exponential, \(I_j\) is the \(j\)-dimensional identity, and \(\|\cdot\|_2\) denotes the spectral/operator norm. If \(r=0\), use the empty \(N\)-by-\(0\) basis matrix, with the exponential of the \(0\)-by-\(0\) matrix equal to \(I_0\) and products through this zero-dimensional space equal to zero.

## Task

Prove the integrated theorem:

1. The full exponential is exactly represented on the query-key subspace by
\[
e^S=I_N+C\bigl(e^{C^\top SC}-I_r\bigr)C^\top.
\]
2. The finite-matrix map \(Y\) obeys
\[
\|Y^\top Y-I_N\|_2
\le(e^{\|S\|_2}-1)^2\max_{1\le i\le p}\left|\sigma_i(B)^2\bigl(\sigma_i(B)^2-1\bigr)\right|
\le\frac14(e^{\|S\|_2}-1)^2.
\]
