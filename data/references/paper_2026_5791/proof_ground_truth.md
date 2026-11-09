# Reference Proof

## Proof Structure

For ridge regularization, write the normal equations as \((A+2\lambda I)x=c\), bound the inverse spectrally, and compute that \(\|c\|_2\) is independent of the chain length. For the gauge-invariant estimator, introduce edge differences privately; both terms of its objective then separate, allowing every difference to be minimized explicitly.

## Complete Proof

Let \(D=D_L\) and \(r=r_L\). The ridge objective has Hessian
\[
D^TD+2\lambda I.
\]
For any nonzero vector \(v\),
\[
v^T(D^TD+2\lambda I)v=\|Dv\|_2^2+2\lambda\|v\|_2^2>0.
\]
Thus the quadratic has a unique minimizer, characterized by
\[
(D^TD+2\lambda I)x_R=D^Tr.
\]
Set \(A=D^TD\succeq0\) and \(c=D^Tr\). Since every eigenvalue of \(A+2\lambda I\) is at least \(2\lambda\),
\[
\|(A+2\lambda I)^{-1}\|_{2\to2}\le \frac1{2\lambda},
\qquad
\|x_R\|_2\le \frac{\|c\|_2}{2\lambda}.
\]
From the definitions of \(D\) and \(r\), for \(L\ge2\), the three distinct nonzero coordinates are
\[
c_0=-1,\qquad c_1=1,\qquad c_L=1,
\]
and every other coordinate is zero. In particular, at \(L=2\) this is \((-1,1,1)^T\), and for every allowed \(L\),
\[
\|c\|_2=\sqrt3.
\]
Therefore
\[
\Delta_R(\lambda)
\le 2\|x_R\|_\infty
\le 2\|x_R\|_2
\le \frac{\sqrt3}{\lambda}
\le \frac{2\sqrt3}{\lambda}.
\]
The constant is independent of \(L\). Explicitly,
\[
0\le\sup_{L\ge2}\Delta_R(\lambda)\le\frac{\sqrt3}{\lambda}\longrightarrow0
\quad\text{as }\lambda\to\infty.
\]

For the second estimator, define edge differences
\[
d_i=u_i-u_{i+1},\qquad 0\le i\le L.
\]
Because \(u_{L+1}=1\), these coordinates determine the interior potential through
\[
u_i=1+\sum_{j=i}^L d_j.
\]
Conversely, every vector of real gaps gives a unique admissible interior potential by this formula, so minimizing over gaps is equivalent to minimizing over \(x\).

The definitions of \(D\), \(r\), and \(\mathcal E\) give
\[
\|Dx-r\|_2^2=(d_0+1)^2+\sum_{i=1}^L d_i^2,
\qquad
\mathcal E(u)=\sum_{i=0}^L d_i^2.
\]
Thus, with \(\tau_L=2L+1\),
\[
J_S(d)=\frac12(d_0+1)^2
 +\frac12\sum_{i=1}^L d_i^2
 +\frac{\lambda}{\tau_L}\sum_{i=0}^L d_i^2.
\]
This separable quadratic has Hessian \((1+2\lambda/\tau_L)I\), which is positive definite. It therefore has a unique global minimizer. For every \(i\ge1\), the minimizer satisfies \(d_i^*=0\). The remaining first-order condition is
\[
d_0^*+1+\frac{2\lambda}{\tau_L}d_0^*=0,
\]
so
\[
d_0^*=-\frac{\tau_L}{\tau_L+2\lambda}.
\]
It follows that \(u_i^*=1\) for \(1\le i\le L\), whereas
\[
u_0^*=1+d_0^*=\frac{2\lambda}{\tau_L+2\lambda}.
\]
Since \(0<u_0^*<1\) and there is at least one interior index in \(\{1,\ldots,L\}\), the interior maximum is 1 and the interior minimum is \(u_0^*\). Consequently,
\[
\Delta_S(\lambda)
=1-u_0^*
=\frac{\tau_L}{\tau_L+2\lambda}
=\frac{2L+1}{2L+1+2\lambda}.
\]
For each fixed \(\lambda>0\),
\[
1-\Delta_S(\lambda)=\frac{2\lambda}{2L+1+2\lambda}\longrightarrow0
\quad\text{as }L\to\infty.
\]
This proves both claims and their stated limiting conclusions.

## Private Source-Normalization Audit

The ridge objective uses the source's displayed coefficient convention: one half of the squared residual plus \(\lambda\) times the squared magnitude. Its derivative consequently produces \(2\lambda I\). The source appendix's displayed \(\lambda I\) is a local factor error if the numerical parameter is held fixed; the correction preserves the source's stated bound.

For the second estimator, the source appendix has data normalization \(b_{\mathrm{sc}}=\|r\|_2^2=2\). Its objective is
\[
\frac14\|Dx-r\|_2^2+\frac{\lambda}{2\tau_L}\mathcal E(u).
\]
Multiplying the entire objective by 2 gives exactly the public objective and does not change its minimizer. No source repair of the second estimator is needed. In particular, the full pinned energy must be retained: writing it in interior matrix coordinates gives \(x^T(L_G)_{II}x-2x_L+1\), not merely \(x^T(L_G)_{II}x\).
