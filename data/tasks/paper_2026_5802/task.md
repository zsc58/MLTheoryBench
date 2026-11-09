# Problem

## Setup

Let H>0 and B,sigma,zeta_*,tau>=0 be finite real parameters, written below as \(H,B,\sigma,\zeta_*,\tau\). Let \(M,K,R\ge1\) be integers and \(T=KR\).

On a finite-dimensional Euclidean space, client objectives \(F_m\) are differentiable, convex, and H-smooth, and \(F=M^{-1}\sum_{m=1}^M F_m\) has a minimizer \(x^*\) with \(\|x^*\|\le B\). Local SGD is initialized at the origin: \(x_0^m=0\) for every client.

Each client m has a fixed sampling distribution. Its samples \(\xi_t^m\) are drawn independently across clients and time, independently of all earlier samples. For every fixed x, its measurable stochastic gradient satisfies
\[
\mathbb E_{\xi}[g_m(x;\xi)]=\nabla F_m(x),\qquad
\mathbb E_{\xi}\|g_m(x;\xi)-\nabla F_m(x)\|^2\le\sigma^2.
\]
Assume, for the same minimizer x*,
\[
\frac1M\sum_m\|\nabla F_m(x^*)\|^2\le\zeta_*^2,
\]
and
\[
\frac1M\sum_m\|[\nabla F_m(x)-\nabla F_m(y)]-[\nabla F(x)-\nabla F(y)]\|^2
\le\tau^2\|x-y\|^2\qquad\text{for all }x,y.
\]

With a constant step size eta, vanilla Local SGD uses
\[
x_{t+1}^m=
\begin{cases}
x_t^m-\eta g_m(x_t^m;\xi_t^m),&(t+1)\bmod K\ne0,\\
\displaystyle\frac1M\sum_{n=1}^M[x_t^n-\eta g_n(x_t^n;\xi_t^n)],&(t+1)\bmod K=0.
\end{cases}
\]
Define
\[
\hat x=\frac1{TM}\sum_{t=0}^{T-1}\sum_{m=1}^M x_t^m,
\qquad
\bar x_R=\frac1M\sum_{m=1}^M x_{KR}^m.
\]
Thus \(\bar x_R\) denotes the synchronized state after R rounds, not a time average.

## Task

Prove the following integrated theorem.

1. **Upper bound.** For every instance satisfying the setup, choose
\[
\eta=\min\left\{\frac1{2H},(24H\tau^2K^3R)^{-1/3},
\left(\frac{B^2M}{3\sigma^2KR}\right)^{1/2},
\left(\frac{B^2}{12H\zeta_*^2K^3R}\right)^{1/3},
\left(\frac{B^2}{6H\sigma^2K^2R}\right)^{1/3}\right\}.
\]
A term whose denominator is zero is interpreted as \(+\infty\), including when its numerator is also zero. If the resulting eta is zero, the update formula is used with eta=0. Then
\[
\mathbb E[F(\hat x)-F(x^*)]\le18\left[
\frac{HB^2}{KR}+\frac{(H\tau^2)^{1/3}B^2}{R^{2/3}}
+\frac{\sigma B}{\sqrt{MKR}}
+\frac{(H\zeta_*^2B^4)^{1/3}}{R^{2/3}}
+\frac{(H\sigma^2B^4)^{1/3}}{K^{1/3}R^{2/3}}
\right].
\]

2. **Matching lower mechanisms.** There is a universal constant c>0, independent of all parameters, with the following properties. Each assertion is a separate experiment with M=2, deterministic exact gradients, and zero initialization.

(a) For every H>0, B,tau>=0, and integer R>=1, there exist differentiable convex H-smooth quadratic objectives \(F_1,F_2:\mathbb R^2\to\mathbb R\) satisfying the setup with \(\sigma=0\), \(\zeta_*=0\), and second-order heterogeneity at most tau, such that simultaneously for every integer K>=1 and every eta>0,
\[
F(\bar x_R)-F(x^*)\ge c\min\{HB^2/R,\tau B^2/\sqrt R\}.
\]
The objectives may depend on H,B,tau,R, but not on K or eta.

(b) For every H>0, B,zeta_*>=0, and integer R>=1, there exist differentiable convex H-smooth objectives \(F_1,F_2:\mathbb R^3\to\mathbb R\) satisfying the setup with \(\sigma=0\), \(\tau=0\), and optimum-gradient heterogeneity at most \(\zeta_*\), such that simultaneously for every integer K>=2 and every eta>0,
\[
F(\bar x_R)-F(x^*)\ge c\min\left\{HB^2,\frac{\zeta_*^2}{H},\frac{(H\zeta_*^2B^4)^{1/3}}{R^{2/3}}\right\}.
\]
The objectives may depend on \(H,B,\zeta_*,R\), but not on K or eta.
