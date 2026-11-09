# Problem

## Setup

Let \(L\ge2\) be an integer. Consider a chain with vertices \(0,1,\ldots,L,L+1\), and fix the boundary value \(u_{L+1}=1\). Write
\[
x=(u_0,\ldots,u_L)^T\in\mathbb R^{L+1}.
\]
Define the reduced chain residual operator \(D_L:\mathbb R^{L+1}\to\mathbb R^{L+1}\) by
\[
(D_Lx)_i=u_i-u_{i+1}\quad(0\le i<L),
\qquad (D_Lx)_L=u_L,
\]
and set
\[
r_L=(-1,0,\ldots,0,1)^T.
\]
Thus \(D_Lx-r_L\) is the residual associated with a unit source at the left endpoint and the pinned unit sink value.

For \(\lambda>0\), define the ridge estimate by
\[
x_R=\mathop{\rm argmin}_{x\in\mathbb R^{L+1}}
\left\{\frac12\|D_Lx-r_L\|_2^2+\lambda\|x\|_2^2\right\}.
\]

Define the gauge-invariant Dirichlet energy of the full potential by
\[
\mathcal E(u)=\sum_{i=0}^L (u_i-u_{i+1})^2,
\]
and let \(\tau_L=2L+1\), the trace of the interior symmetric unit-conductance chain Laplacian. Under the trace-normalized penalty convention, define
\[
x_S=\mathop{\rm argmin}_{x\in\mathbb R^{L+1}}
\left\{\frac12\|D_Lx-r_L\|_2^2
+\frac{\lambda}{\tau_L}\mathcal E(u)\right\}.
\]

For either estimate, define its interior dynamic range by
\[
\Delta=\max_{0\le i\le L}u_i-
       \min_{0\le i\le L}u_i.
\]

## Task

Prove the following regularization comparison:
\[
\Delta_R(\lambda)\le \frac{2\sqrt3}{\lambda},
\]
so the ridge range collapses as \(O(\lambda^{-1})\) with a constant independent of \(L\), whereas
\[
\Delta_S(\lambda)=\frac{2L+1}{2L+1+2\lambda}.
\]
In particular, prove that \(\Delta_R(\lambda)\to0\) as \(\lambda\to\infty\), uniformly in \(L\), while \(\Delta_S(\lambda)\to1\) for every fixed \(\lambda>0\) as \(L\to\infty\).
