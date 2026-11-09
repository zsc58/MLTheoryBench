# Problem

## Setup

Fix integers \(n\geq1\) and \(d>1\), and let \(A:(\mathbb R^d)^n\to\mathbb R^d\) be an arbitrary aggregation rule. For differentiable functions \(f_1,\ldots,f_n:\mathbb R^d\to\mathbb R\), define the induced field
\[
G_f(x)=A(\nabla f_1(x),\ldots,\nabla f_n(x)).
\]

A field \(T:\mathbb R^d\to\mathbb R^d\) is **monotone** if
\[
\langle x-y,T(x)-T(y)\rangle\geq0\qquad\text{for all }x,y\in\mathbb R^d.
\]
It is **co-coercive** if there is a constant \(\beta>0\) such that
\[
\langle x-y,T(x)-T(y)\rangle\geq\beta\|T(x)-T(y)\|^2\qquad\text{for all }x,y\in\mathbb R^d.
\]
A function is \(L\)-smooth when its gradient is \(L\)-Lipschitz.

Call \(A\) **positively affine** if there are constants \(\alpha_1,\ldots,\alpha_n\geq0\) and \(c\in\mathbb R^d\) such that
\[
A(z_1,\ldots,z_n)=\sum_{i=1}^n\alpha_i z_i+c
\qquad\text{for all }z_1,\ldots,z_n\in\mathbb R^d.
\]

## Task

Prove the following integrated characterization.

For every \(L>0\), the following three statements are equivalent:

1. For every collection of differentiable convex functions \(f_1,\ldots,f_n\), the field \(G_f\) is monotone.
2. For every collection of convex \(L\)-smooth functions \(f_1,\ldots,f_n\), the field \(G_f\) is co-coercive.
3. The rule \(A\) is positively affine.

Moreover, if these equivalent statements hold and \(A\) is permutation-invariant and idempotent, meaning
\[
A(z_{\pi(1)},\ldots,z_{\pi(n)})=A(z_1,\ldots,z_n)
\quad\text{for every permutation }\pi,
\]
and \(A(z,\ldots,z)=z\) for every \(z\in\mathbb R^d\), then
\[
A(z_1,\ldots,z_n)=\frac1n\sum_{i=1}^n z_i.
\]
