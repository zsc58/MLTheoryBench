# Problem

## Setup

Let \(d\) be a positive integer, let \(R\in\mathbb R^d\), and let \(\beta>0\). Let \(U^*,U_\eta:\mathbb R^d\to\mathbb R\) be differentiable potentials, where \(U^*\) is the true potential of mean force and \(U_\eta\) is a learned potential. Define
\[
Z^*=\int_{\mathbb R^d}e^{-\beta U^*(R)}\,dR,
\qquad
Z_\eta=\int_{\mathbb R^d}e^{-\beta U_\eta(R)}\,dR,
\]
and assume \(0<Z^*,Z_\eta<\infty\). The true and learned equilibrium densities, with respect to Lebesgue measure, are
\[
p^*(R)=\frac{1}{Z^*}e^{-\beta U^*(R)},
\qquad
p_\eta(R)=\frac{1}{Z_\eta}e^{-\beta U_\eta(R)}.
\]
Assume \(p_\eta\) is absolutely continuous with respect to \(p^*\), and assume the gradient error is square-integrable under \(p_\eta\), meaning
\[
\int_{\mathbb R^d}p_\eta(R)
\left\|\nabla_R U_\eta(R)-\nabla_R U^*(R)\right\|_2^2\,dR<\infty.
\]
Here \(\|\cdot\|_2\) is the Euclidean norm.

For a probability density \(q\) absolutely continuous with respect to \(p^*\), define
\[
D_{\mathrm{KL}}(q\|p^*)
=\int_{\mathbb R^d}q(R)\log\frac{q(R)}{p^*(R)}\,dR,
\]
with zero-density contributions interpreted as zero and with the value \(+\infty\) permitted.

Assume \(p^*\) satisfies the following logarithmic Sobolev inequality with constant \(\rho>0\): for every strictly positive differentiable probability density \(q\) on \(\mathbb R^d\), absolutely continuous with respect to \(p^*\), for which
\[
\int_{\mathbb R^d}q(R)
\left\|\nabla_R\log\frac{q(R)}{p^*(R)}\right\|_2^2\,dR<\infty,
\]
one has
\[
D_{\mathrm{KL}}(q\|p^*)\leq
\frac{1}{2\rho}\int_{\mathbb R^d}q(R)
\left\|\nabla_R\log\frac{q(R)}{p^*(R)}\right\|_2^2\,dR.
\]

## Task

Prove that
\[
D_{\mathrm{KL}}(p_\eta\|p^*)\leq
\frac{\beta^2}{2\rho}\,
\mathbb E_{R\sim p_\eta}
\left[\left\|\nabla_R U_\eta(R)-\nabla_R U^*(R)\right\|_2^2\right].
\]
