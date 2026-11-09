# Problem

## Setup

Let d,p,n be positive integers, with x∈R^d and θ∈R^p. Let w:R^d→(0,∞) be continuously differentiable and bounded, with bounded gradient. Let
\[
q(x\mid\theta)=\exp\{T(x)^\top\theta+b(x)\},
\]
where T:R^d→R^p and b:R^d→R are twice continuously differentiable. This is an unnormalized representative of a density: assume
\[
0<Z(\theta):=\int_{\mathbb R^d}q(x\mid\theta)\,dx<\infty
\quad\text{for every }\theta\in\mathbb R^p.
\]

Assume there is a positive continuously differentiable probability density p0 on R^d such that, for every θ,
\[
w\nabla\log p_0,\quad w\nabla_x\log q(\cdot\mid\theta)\in L^2(p_0),
\]
where h∈L²(p0) means ∫||h(x)||²p0(x)dx<∞. Also assume that the vector field
\[
F_\theta(x)=p_0(x)w(x)^2\nabla_x\log q(x\mid\theta)
\]
and each of its first partial derivatives are absolutely Lebesgue integrable componentwise on R^d.

Assume there are finite nonnegative constants C,C′ such that, for all x,
\[
\max\left\{
\bigl(\|\nabla_xT(x)\|_F\|\nabla_xb(x)\|_2\bigr)^{1/2},
\|\nabla_x^2T(x)\|_F^{1/2},
\|\nabla_xT(x)\|_F
\right\}\le\frac{C}{w(x)},
\]
\[
\|\nabla_x(w(x)^2)\|_2\,\|\nabla_xT(x)\|_F\le C'.
\]
Here ∇xT is the p-by-d Jacobian; ||∇x²T||F is the square root of the sum of squares of all entries of its p-by-d-by-d second-derivative tensor. Matrix Frobenius norms have the analogous meaning.

Let μ∈R^p, let Σ be a symmetric positive-definite p-by-p matrix, let the prior be π0=N(μ,Σ), and let β>0.

For a positive continuously differentiable probability density f and a positive continuously differentiable function g for which the expectation is finite, define the weighted score-matching divergence
\[
\operatorname{SM}_w(f\|g)
=\mathbb E_f\!\left[w(X)^2\|\nabla\log g(X)-\nabla\log f(X)\|_2^2\right].
\]
Under the stated integrability conditions, its empirical objective for comparing p0 with q(·|θ), up to a parameter-independent constant, is
\[
L_n(\theta)=\frac1n\sum_{i=1}^n\left[
w(x_i)^2\|\nabla_x\log q(x_i\mid\theta)\|_2^2
+2\nabla_x\!\cdot\!\left(w(x_i)^2\nabla_x\log q(x_i\mid\theta)\right)
\right].
\]
Define the generalized posterior
\[
\pi_n(\theta\mid x_{1:n})\propto
\exp\{-\beta nL_n(\theta)\}\pi_0(\theta).
\]
For j∈{1,…,n} and z∈R^d, let x1:n^(j←z) denote the sample with xj replaced by z, and define
\[
\operatorname{PIF}_{\rm KL}(z)=
\operatorname{KL}\!\left(
\pi_n(\cdot\mid x_{1:n})\,\middle\|\,
\pi_n(\cdot\mid x_{1:n}^{(j\leftarrow z)})
\right).
\]

## Task

Prove the following integrated theorem. For every data set x1:n∈(R^d)^n, the posterior is Gaussian,
\[
\pi_n(\cdot\mid x_{1:n})=\mathcal N(m_n,C_n),
\]
with
\[
C_n^{-1}=\Sigma^{-1}+2\beta\sum_{i=1}^n
w(x_i)^2\,\nabla T(x_i)\nabla T(x_i)^\top,
\]
\[
m_n=C_n\left[
\Sigma^{-1}\mu-2\beta\sum_{i=1}^n\left(
w(x_i)^2\nabla T(x_i)\nabla b(x_i)
+\operatorname{div}_x\!\left(w(x_i)^2\nabla T(x_i)\right)
\right)\right],
\]
where the divergence of a p-by-d matrix-valued function is taken row-wise. Moreover, for every fixed n, index j∈{1,…,n}, and original sample, the posterior is KL-robust to an arbitrary single-observation outlier:
\[
\sup_{z\in\mathbb R^d}\operatorname{PIF}_{\rm KL}(z)<\infty.
\]
