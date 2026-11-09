# Problem

## Setup

Fix an integer \(d\ge 1\), \(\sigma>0\), and \(a\in(0,1)\). Let \(p\) be a continuously differentiable, strictly positive probability density on \(\mathbb R^d\) satisfying
\[
\int_{\mathbb R^d}\|\nabla\log p(y)\|^2p(y)\,dy<\infty,
\]
and let
\[
q(z)=(2\pi\sigma^2)^{-d/2}\exp\!\left(-\frac{\|z\|^2}{2\sigma^2}\right).
\]

Let \(Y\sim p\) and \(Z\sim q\) be independent, and define
\[
X=\sqrt{1-a}\,Z+\sqrt a\,Y.
\]
Denote the density of \(X\) by \(m\). For each \(x\), let \(r_x\) be the conditional density of \(Y\) given \(X=x\), namely
\[
r_x(y)=\frac{(1-a)^{-d/2}
 q\!\left(\frac{x-\sqrt a\,y}{\sqrt{1-a}}\right)p(y)}{m(x)}.
\]

For a continuously differentiable, strictly positive density \(h\), write \(S_h=\nabla\log h\). When \(\mathbb E_{U\sim h}\|S_h(U)\|^2<\infty\), define
\[
F_h=\mathbb E_{U\sim h}[S_h(U)S_h(U)^\top].
\]
In particular, \(F_q=\sigma^{-2}I_d\).

Define
\[
D_x(y)=\frac{\sqrt a\,y-x}{\sigma^2(1-a)},
\qquad
T(y)=\frac{S_p(y)}{\sqrt a}.
\]
For \(A\in\mathbb R^{d\times d}\), set
\[
G_x^A(y)=A D_x(y)+(I_d-A)T(y).
\]
For a conditional random vector \(U\), use the trace-variance convention
\[
\operatorname{Var}(U)=\mathbb E\|U-\mathbb E U\|^2,
\]
and define
\[
J(A)=\mathbb E_{X\sim m}\!
 \left[\operatorname{Var}_{Y\sim r_X}\bigl(G_X^A(Y)\bigr)\right].
\]

## Task

Prove that \(J\) has the unique global minimizer
\[
A^*=a^{-1}F_p
\left((1-a)^{-1}F_q+a^{-1}F_p\right)^{-1}.
\]
