# Problem

## Setup

Fix integers \(m,n,T\ge 1\) and a decay parameter \(\beta\in[0,1)\). For a sequence of random matrices \(X_1,\ldots,X_T\) of the same size, define
\[
\mathsf{EMA}_\beta[X_{1:T}]=(1-\beta)\sum_{t=1}^T\beta^{T-t}X_t,
\]
where \(\beta^0=1\), including when \(\beta=0\).
Let \(G_t:\Omega\to\mathbb R^{m\times n}\) be square-integrable random matrices on a common probability space with sample space \(\Omega\), meaning \(\mathbb E\|G_t\|_F^2<\infty\). Let \(A\in\mathbb R^{m\times m}\) and \(B\in\mathbb R^{n\times n}\) be fixed symmetric positive-definite matrices, and set
\[
Z_t=AG_tB.
\]
Assume the two EMA second-moment matrices
\[
\mathsf{EMA}_\beta\!\left[\mathbb E(G_tB^2G_t^\top)\right]_{t=1}^T,
\qquad
\mathsf{EMA}_\beta\!\left[\mathbb E(G_t^\top A^2G_t)\right]_{t=1}^T
\]
are full rank (and hence positive definite).

For any sequence \(X_t\) of compatible square-integrable random matrices, say that it is *time-averaged orthogonal in expectation* when
\[
\mathsf{EMA}_\beta\!\left[\mathbb E(X_tX_t^\top)\right]_{t=1}^T=I,
\qquad
\mathsf{EMA}_\beta\!\left[\mathbb E(X_t^\top X_t)\right]_{t=1}^T=I,
\]
with identity dimensions determined by \(X_t\).

## Task

Prove the following integrated characterization. The transformed sequence \(\{Z_t\}_{t=1}^T\) is time-averaged orthogonal in expectation if and only if
\[
A=\left(\mathsf{EMA}_\beta\!\left[\mathbb E(G_tB^2G_t^\top)\right]_{t=1}^T\right)^{-1/2},
\qquad
B=\left(\mathsf{EMA}_\beta\!\left[\mathbb E(G_t^\top A^2G_t)\right]_{t=1}^T\right)^{-1/2},
\]
where each inverse square root is the unique symmetric positive-definite one. These equations are coupled through the dependence of the first right-hand side on \(B\) and the second on \(A\).
