# Problem

## Setup

Fix a positive integer d and the time interval [0,1]. Let beta:[0,1]→(0,infinity) be a measurable deterministic function, written beta_t, and set
\[
V_t(z)=\tfrac{\beta_t}{2}\|z\|^2.
\]
Let p^(in) and p^(tar) be probability laws on R^d with finite first moments, with means
\[
\bar x^{(in)}=\int x\,p^{(in)}(dx),\qquad
\bar x^{(tar)}=\int x\,p^{(tar)}(dx).
\]

Assume there exists a well-posed regular self-consistent stochastic control solution with zero base drift, in the following sense. On a filtered probability space, W is a standard d-dimensional Brownian motion and X is a continuous adapted process satisfying
\[
dX_t=u_t(X_t)\,dt+dW_t,
\qquad \mathcal L(X_0)=p^{(in)},\quad \mathcal L(X_1)=p^{(tar)}.
\]
The drift u is a deterministic Borel vector field. Assume E||X_t||<infinity for every t∈[0,1], and define
\[
m_t=\mathbb E[X_t]\qquad(0\leq t\leq1).
\]
For 0<t<1, the law of X_t has a Lebesgue density p_t, satisfying
\[
\partial_t p_t=-\nabla\!\cdot(u_tp_t)+\tfrac12\Delta p_t
\]
in the distributional sense. No density is required at either endpoint.

There is a real-valued function J on (0,1)×R^d such that
\[
\partial_tJ_t+\tfrac12\Delta J_t-\tfrac12\|\nabla J_t\|^2+U_t=0,
\qquad u_t=-\nabla J_t,
\]
where
\[
U_t(x)=\int_{\mathbb R^d}V_t(x-y)p_t(y)\,dy
\]
is finite for every interior t and every x. The HJB equation holds for almost every t and every x.

The regularity and integrability requirements on this solution are as follows.

- J has jointly continuous spatial derivatives through order three on (0,1)×R^d. Both J and its spatial gradient are locally absolutely continuous in time. Their time derivatives commute with the first spatial derivative almost everywhere, and, for every compact K⊂R^d and 0<a<b<1,
  \[
  \int_a^b\sup_{x\in K}\bigl(|\partial_tJ_t(x)|+\|\partial_t\nabla J_t(x)\|\bigr)\,dt<\infty.
  \]
  The time-absolute-continuity statements are understood uniformly on compact spatial sets.
- For every interior t, E||u_t(X_t)||<infinity. For every 0<a<b<1,
  \[
  \mathbb E\int_a^b\left(
  \|u_t(X_t)\|+\|\partial_tu_t(X_t)\|
  +\|D_xu_t(X_t)\|\,\|u_t(X_t)\|
  +\|D_x^2u_t(X_t)\|
  \right)dt<\infty.
  \]
  Here D_xu and D_x^2u are the arrays of first and second spatial derivatives, with their Euclidean array norms. Time derivatives in this condition are taken almost everywhere.
- For every 0<a<b<1, the vector stochastic integral
  \[
  \left(\int_a^tD_xu_r(X_r)\,dW_r\right)_{a\leq t\leq b}
  \]
  is a true martingale with respect to the given filtration, not merely a local martingale.
- The endpoint convergence holds in L1:
  \[
  \lim_{t\downarrow0}\mathbb E\|X_t-X_0\|=0,
  \qquad
  \lim_{t\uparrow1}\mathbb E\|X_t-X_1\|=0.
  \]

The self-consistent guidance nu:[0,1]→R^d satisfies
\[
\nu_t=\mathbb E[X_t]\qquad(0\leq t\leq1).
\]

## Task

Prove that, for every t∈[0,1],
\[
\nu_t=m_t=(1-t)\bar x^{(in)}+t\bar x^{(tar)}.
\]
The identity must hold for every measurable positive schedule and arbitrary endpoint laws for which a solution satisfying the assumptions above exists.
