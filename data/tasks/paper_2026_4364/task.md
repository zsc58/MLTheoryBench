# Problem

## Setup

Fix integers N>=0 and k>=1. On a probability space, let F_N be the sigma-field representing the information available at forecasting origin N. Let the future innovation sequence (xi_{N+1},xi_{N+2},...) be independent of F_N and consist of iid Laplace(0,1) random variables, with density (1/2)exp(-|x|).

Assume that the finite real-valued fitted trajectories hat c(t), hat Phi(t), and hat b(t), for integer t>=N+1, are F_N-measurable, with hat b(t)>0 almost surely. Let y_N be a finite real-valued F_N-measurable random variable. Define the forecast path recursively by
\[
\hat y_N=y_N,\qquad
\hat y_t=\hat c(t)+\hat\Phi(t)\hat y_{t-1}+\hat b(t)\xi_t.
\]
Define its conditional-mean path by
\[
m_t(\omega)=\int_{\mathbb R}x\,\mathbb P(\hat y_t\in dx\mid F_N)(\omega).
\]
Here a conditional mean is an integral under the conditional distribution, with finite absolute first moment almost surely; unconditional integrability is not required. Equivalently, the path is given by
\[
m_N=y_N,\qquad m_t=\hat c(t)+\hat\Phi(t)m_{t-1}.
\]
For 1<=j<=k, set
\[
a_{j,k}=\hat b(N+j)\prod_{r=j+1}^{k}\hat\Phi(N+r),\qquad
s_{j,k}=|a_{j,k}|,
\]
where an empty product equals one. All assertions about conditional distributions and probabilities below are understood almost surely.

## Task

Prove the following integrated theorem. With e_{N+k}=hat y_{N+k}-m_{N+k},
\[
e_{N+k}=\sum_{j=1}^{k}a_{j,k}\xi_{N+j},\qquad
\mathbb E[e^{it e_{N+k}}\mid F_N]
=\prod_{j=1}^{k}(1+a_{j,k}^{2}t^{2})^{-1}
\quad(t\in\mathbb R).
\]
If the scales s_{1,k},...,s_{k,k} are strictly positive and pairwise distinct almost surely, define
\[
A_{j,k}=\prod_{\ell\ne j}\frac{s_{j,k}^{2}}{s_{j,k}^{2}-s_{\ell,k}^{2}}.
\]
Then, conditional on F_N, e_{N+k} has density
\[
f_k(x)=\frac12\sum_{j=1}^{k}A_{j,k}s_{j,k}^{-1}e^{-|x|/s_{j,k}},
\qquad x\in\mathbb R,
\]
and for every x>=0 its conditional CDF is
\[
F_k(x):=\mathbb P(e_{N+k}\le x\mid F_N)
=1-\frac12\sum_{j=1}^{k}A_{j,k}e^{-x/s_{j,k}}.
\]
Moreover, under this same distinct-positive-scale condition, for every fixed alpha in (0,1) there is an F_N-measurable radius q_{k,alpha}>0, unique up to almost sure equality, satisfying
\[
\mathbb P(|e_{N+k}|\le q_{k,\alpha}\mid F_N)=\alpha.
\]
For almost every history, this radius is equivalently the unique solution q in [0,infinity) of
\[
\sum_{j=1}^{k}A_{j,k}e^{-q/s_{j,k}}=1-\alpha.
\]
The interval [m_{N+k}-q_{k,alpha},m_{N+k}+q_{k,alpha}] has exact conditional coverage alpha for the fitted forecast path:
\[
\mathbb P\!\left(
\hat y_{N+k}\in[m_{N+k}-q_{k,\alpha},m_{N+k}+q_{k,\alpha}]
\mid F_N\right)=\alpha.
\]
