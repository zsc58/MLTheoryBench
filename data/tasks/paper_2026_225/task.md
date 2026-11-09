# Problem

## Setup

Let \(d\geq1\) be an integer and \(\Phi\) a nonempty parameter set. Let \(p\) be a positive differentiable density on \(\mathbb R^d\) whose score can be evaluated. Let \(q(dz)\) be a fixed sampleable probability law on a measurable space \(\mathcal Z\). For each \(\phi\in\Phi\), suppose that \(X\mid Z=z\) has a positive differentiable density \(q_\phi(x\mid z)\) on \(\mathbb R^d\), with a conditional sampler and evaluable density and score. The conditional densities and their \(x\)-derivatives are jointly measurable in \((x,z)\). Define
\[
q_\phi(x)=\int_{\mathcal Z}q_\phi(x\mid z)q(dz).
\]
Assume this marginal is finite, positive, and differentiable. For every \(\phi\), \(x\), and coordinate \(j\), assume \(z\mapsto\partial_{x_j}q_\phi(x\mid z)\) is absolutely integrable against \(q(dz)\), and that differentiation with respect to \(x_j\) may pass through the integral defining \(q_\phi(x)\).

Write
\[
s_p(x)=\nabla_x\log p(x),\qquad
s_{q_\phi}(x)=\nabla_x\log q_\phi(x),\qquad
s_{q_\phi(\cdot\mid z)}(x)=\nabla_x\log q_\phi(x\mid z).
\]
No evaluation access to the marginal density or marginal score is assumed.

Let \(k:\mathbb R^d\times\mathbb R^d\to\mathbb R\) be an evaluable continuous positive-semidefinite kernel. Let \(\mathcal H_0\) be its RKHS and \(\mathcal H=\mathcal H_0^{\otimes d}\) its Cartesian product, equipped with the sum of the component inner products. For every \(\phi\in\Phi\), assume
\[
\int k(x,x)q_\phi(x)\,dx<\infty,
\qquad
\int\|s_p(x)-s_{q_\phi}(x)\|^2q_\phi(x)\,dx<\infty,
\]
and
\[
\int_{\mathcal Z}\int_{\mathbb R^d}
\sqrt{k(x,x)}\,
\|s_p(x)-s_{q_\phi(\cdot\mid z)}(x)\|
q_\phi(x\mid z)\,dx\,q(dz)<\infty.
\]
Here \(\|\cdot\|\) denotes the Euclidean norm. Define the kernel integral operator on \(L^2(q_\phi;\mathbb R^d)\), componentwise, by
\[
(S_{q_\phi,k}h)(\cdot)=\int k(\cdot,y)h(y)q_\phi(y)\,dy.
\]
Define the score-difference form of the RKHS kernel Stein discrepancy by
\[
\operatorname{KSD}_k(q_\phi\|p)
=\sup_{\|f\|_{\mathcal H}\leq1}
\mathbb E_{X\sim q_\phi}
[f(X)^\top(s_p(X)-s_{q_\phi}(X))].
\]

Consider the minimax optimization problem
\[
\min_{\phi\in\Phi}\ \max_{f\in\mathcal H}\
\mathbb E_{X\sim q_\phi}
\left[2f(X)^\top(s_p(X)-s_{q_\phi}(X))-\|f\|_{\mathcal H}^2\right].
\]
The outer minimization denotes the optimization problem; attainment of an outer minimum is not assumed.

## Task

Prove the following integrated theorem. For every \(\phi\in\Phi\), the inner maximization has a unique optimizer and, for every \(x\in\mathbb R^d\),
\[
f_\phi^*(x)
=\mathbb E_{Y\sim q_\phi}\left[k(x,Y)(s_p(Y)-s_{q_\phi}(Y))\right]
=\mathbb E_{(Y,Z)}\left[k(x,Y)(s_p(Y)-s_{q_\phi(\cdot\mid Z)}(Y))\right],
\]
where \((Y,Z)\) has joint law \(q_\phi(y\mid z)\,dy\,q(dz)\). Moreover,
\[
\begin{aligned}
&\max_{f\in\mathcal H}\mathbb E_{q_\phi}
\left[2f(X)^\top(s_p(X)-s_{q_\phi}(X))-\|f\|_{\mathcal H}^2\right]\\
&\qquad=\operatorname{KSD}_k(q_\phi\|p)^2\\
&\qquad=\mathbb E\Big[k(X,X')\big\langle
s_p(X)-s_{q_\phi(\cdot\mid Z)}(X),\
s_p(X')-s_{q_\phi(\cdot\mid Z')}(X')
\big\rangle\Big],
\end{aligned}
\]
where \((X,Z)\) and \((X',Z')\) are independent draws from \(q_\phi(x\mid z)\,dx\,q(dz)\), and \(\langle\cdot,\cdot\rangle\) is the Euclidean inner product.

Consequently, minimizing the RKHS minimax objective over \(\Phi\) is equivalent to minimizing this conditional-score kernel expectation: the infima agree, and the sets of minimizing parameters agree whenever minima are attained. Explain why the conditional-score expectation is estimable by Monte Carlo using the stated sampling and evaluation access.
