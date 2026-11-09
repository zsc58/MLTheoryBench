# Problem

## Setup

For \(R>0\), let
\[
B_R=\{x\in\mathbb R^d:\|x\|_2\le R\},
\qquad
\mathbb S^{d-1}=\{x\in\mathbb R^d:\|x\|_2=1\}.
\]
For a function \(h\) on \(D\subseteq\mathbb R^d\), define
\[
\operatorname{Lip}_D(h)
 =\sup_{x\ne x'\in D}
 \frac{|h(x)-h(x')|}{\|x-x'\|_2}.
\]

Let \(\phi:\mathbb R\to\mathbb R\) be a continuous piecewise-linear function with \(K\) affine pieces. For \(m\ge1\), let \(\mathcal F_m\) be the class of functions
\[
f(x)=\sum_{k=1}^m a_k\phi(\langle w_k,x\rangle+b_k)
      +\langle v,x\rangle+c,
\]
where \(a_k,b_k,c\in\mathbb R\) and \(w_k,v\in\mathbb R^d\) are unrestricted. Set
\[
M=(K-1)m+1.
\]

Let \((x_i,y_i)_{i=1}^n\) be iid observations, with \(|y_i|\le1\) almost surely, and define
\[
\sigma^2=\mathbb E\!\left[\operatorname{Var}(y_i\mid x_i)\right]>0,
\qquad
\widehat R_n(f)=\frac1n\sum_{i=1}^n(f(x_i)-y_i)^2.
\]
Consider either of the following two cases:

- **Spherical case:** \(d\ge3\), \(x_i\) is uniform on \(\mathbb S^{d-1}\), and \(D=\mathbb S^{d-1}\).
- **Gaussian case:** \(x_i\sim N(0,I_d/d)\), \(D=B_2\), and the additional dimension condition below is imposed.

## Task

Prove that there are absolute constants \(C_0,c_0>0\) with the following property. For every
\[
0<\varepsilon\le\sigma^2,
\qquad 0<\delta<1,
\qquad
n\ge C_0\varepsilon^{-2}\log(8/\delta),
\]
and, in the Gaussian case, additionally
\[
d\ge2\log(8n/\delta),
\]
the following event has probability at least \(1-\delta\): every \(f\in\mathcal F_m\) satisfying
\[
\widehat R_n(f)\le\sigma^2-\varepsilon
\]
obeys
\[
\operatorname{Lip}_D(f)
\ge
c_0\varepsilon
\sqrt{\frac{n}{M\log(C_0Mnd/\varepsilon)}}.
\]
No bound on the network parameters may be assumed.
