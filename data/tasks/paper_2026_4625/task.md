# Problem

## Setup

Fix integers \(d,m\ge 1\), a vector \(a\in\mathbb R^m\), and a map \(g:\mathbb R^d\to\mathbb R^m\) whose component Hessians exist. For every finite sample count \(n\ge1\), locations \(z=(z_1,\ldots,z_n)\in(\mathbb R^d)^n\), and real weights \(w=(w_1,\ldots,w_n)\in\mathbb R^n\), define
\[
F(z,w)=\left\|a-\sum_{i=1}^n w_i g(z_i)\right\|^2,
\qquad r(z,w)=a-\sum_{i=1}^n w_i g(z_i).
\]
Vector norms are Euclidean. Matrix norms are the induced operator norms, and the norm of a third derivative is its operator norm as a trilinear form on the Euclidean location space.

Assume that, for every finite sample count \(n\ge1\) and every \(w\in\mathbb R^n\), the map \(z\mapsto F(z,w)\) is three-times differentiable on all of \((\mathbb R^d)^n\). Assume that fixed constants \(\ell,\rho>0\), independent of the sample count, locations, and weights, satisfy
\[
\|\nabla_z^2F(z,w)\|\le \ell,
\qquad \|\nabla_z^3F(z,w)\|\le \rho
\]
for every such \(n,z,w\), including the augmented representations used after splitting.

Define, for each sample,
\[
S_i(z,w)=-2w_i\sum_{p=1}^m r_p(z,w)\,\nabla^2 g_p(z_i).
\]
For \(\epsilon>0\), call \((z,w)\) an \(\epsilon\)-second-order stationary point with respect to the locations when
\[
\|\nabla_zF(z,w)\|\le\epsilon,
\qquad
\lambda_{\min}(\nabla_z^2F(z,w))\ge-\sqrt{\rho\epsilon}.
\]

Initialize at a finite representation \((z^0,w^0)\) and write \(F_0=F(z^0,w^0)\). Choose fixed step sizes satisfying
\[
0<\eta_g\le1/\ell,
\qquad
0<\eta\le(3/2)\sqrt{\epsilon/\rho},
\]
and set \(\epsilon_H=\sqrt{\rho\epsilon}\).

While \(\|\nabla_zF\|>\epsilon\), perform the update \(z\leftarrow z-\eta_g\nabla_zF\), leaving the weights unchanged. When the gradient norm is at most \(\epsilon\), inspect the splitting matrices. If some \(i\) satisfies \(\lambda_{\min}(S_i)<-\epsilon_H\), choose any such sample and a unit minimum-eigenvalue eigenvector \(v\), replace that sample by two offspring of weights \(w_i/2\) at \(z_i+\eta v\) and \(z_i-\eta v\), and return to the gradient phase. If no such sample exists, stop. Count one gradient update or one splitting step as one iteration.

## Task

Prove that this procedure reaches an \(\epsilon\)-second-order stationary point after at most
\[
O\!\left(\frac{F_0}{\sqrt{\rho}\,\eta^2}\,\epsilon^{-1/2}\right)
\]
splitting steps and \(O(\epsilon^{-2})\) total iterations, with fixed step-size, smoothness, and initial-loss factors understood in the big-O notation.
