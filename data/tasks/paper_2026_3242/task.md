# Problem

## Setup

Let d>=1 be an integer. Let f:R^d->R be C^2, with L-Lipschitz gradient for some 0<L<infinity, equivalently ||nabla^2 f(x)||_op<=L. Assume that f(x)+(M/2)||x||^2 is convex for some M>=0. Let
\[
Z=\int_{\mathbb R^d}e^{-f(x)}\,dx\in(0,\infty),\qquad
\nu(dx)=Z^{-1}e^{-f(x)}dx,
\qquad \gamma(dy)=(2\pi)^{-d/2}e^{-\|y\|^2/2}dy.
\]
Assume that nu has finite second moment and satisfies the alpha-Talagrand inequality
\[
\frac\alpha2W_2^2(\lambda,\nu)\le \mathrm{KL}(\lambda\|\nu)
\quad\text{for every probability law }\lambda\text{ with finite second moment},
\]
where 0<=M<alpha<infinity. Here
\[
W_2^2(\lambda,\nu)=\inf_{\pi\in\Pi(\lambda,\nu)}\int\|x-z\|^2\,\pi(dx,dz),
\]
with Pi(lambda,nu) the set of couplings of lambda and nu, and
\[
\mathrm{KL}(\lambda\|\nu)=\int\log(d\lambda/d\nu)\,d\lambda
\]
when lambda is absolutely continuous with respect to nu, with value +infinity otherwise.

Hamiltonian dynamics on (x,y) in R^{2d} are
\[
\dot x_t=y_t,\qquad \dot y_t=-\nabla f(x_t),
\]
with flow map Phi_t. One randomized Hamiltonian step from a position law mu samples (x_0,y_0) from mu tensor gamma, independently draws an integration time tau, evolves by Phi_tau, and returns the position coordinate. Let D_T^{tri} have density 2(T-t)/T^2 on [0,T], and let D_T^{exp} have density T^{-1}exp(-t/T) on [0,infinity). At every iteration, the Gaussian momentum and integration time are fresh draws independent of each other and of the preceding history.

Assume the initial position law mu_0 is absolutely continuous with full support and admits a strictly positive density, has finite second moment, and satisfies KL(mu_0||nu)<infinity. Let mu_K denote the unconditional position law after K iterations.

## Task

Prove that for either choosing tau from D_T^{tri} at every step or choosing tau from D_T^{exp} at every step, for every integer K>=0 and every T>0,
\[
\mathrm{KL}(\mu_K\|\nu)\le C_T^K\,\mathrm{KL}(\mu_0\|\nu),
\qquad
C_T=\frac{2}{3-M/\alpha}\left(1+\frac1{\alpha T^2}\right).
\]
Consequently, let epsilon>0 and write H_0=KL(mu_0||nu). With
\[
T=\frac2{\sqrt{\alpha-M}},\qquad
K=\begin{cases}
0,&H_0\le\varepsilon,\\[2mm]
\displaystyle\left\lceil\frac{\log(H_0/\varepsilon)}{\log\!\left(1+\frac{\alpha-M}{5\alpha-M}\right)}\right\rceil,&H_0>\varepsilon,
\end{cases}
\]
prove that KL(mu_K||nu)<=epsilon. Define the total integration time by S_K=sum_{k=1}^K tau_k, with S_0=0. Prove that S_K<=KT=2K/sqrt(alpha-M) almost surely for triangular times, and E[S_K]=KT for exponential times.

In particular, writing r=M/alpha, for H_0>0 and fixed r, as epsilon/H_0 tends to zero, the triangular total-time bound and the exponential expected total time are
\[
O_r\!\left((\alpha-M)^{-1/2}\log(H_0/\varepsilon)\right).
\]
The subscript r permits the implicit constant to depend on r; no uniformity as r approaches 1 is asserted.
