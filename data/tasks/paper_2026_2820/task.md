# Problem

## Setup

Let `X` be a finite nonempty set and `Theta` a measurable parameter space. Let `g:X x Theta -> R` be a measurable model family. Suppose each section `g(x,.)` belongs to a real reproducing-kernel Hilbert space `H_Theta` with kernel `k_Theta`. Define

`H_G={h:X->R : h(x)=<w,g(x,.)>_{H_Theta} for all x, for some w in H_Theta}`,

with kernel

`k_G(x,x')=<g(x,.),g(x',.)>_{H_Theta}`

and norm

`||h||_{H_G}=inf{||w||_{H_Theta}: h(x)=<w,g(x,.)>_{H_Theta} for every x in X}`.

Write `phi(x)=g(x,.)` and `g_theta=g(.,theta)`. The fixed unknown objective is `f=g_{theta_star}` for some `theta_star in Theta`, and it has a unique maximizer `x_star` in `X`.

Let `Y` be the space of real-valued observations. The loss `ell(s,y)` is defined and twice differentiable in `s` on an interval containing all model outputs, for every `y in Y`, and satisfies

`ell''_y(s)>=alpha_ell>0`

throughout that interval. Write `ell'_y(s)` for its first derivative in `s`.

Fix a deterministic nondecreasing sequence of finite positive numbers `(lambda_t)_{t>=1}` and a constant `lambda_0>0` such that `lambda_0<=lambda_t` for every `t>=1`. At time zero draw `theta_{0,0}` from a fixed prior `Pi_0` and set `g_0=g_{0,0}=g_{theta_{0,0}}`.

The sequential experiment is as follows. At round `t>=1`, select

`x_t in argmax_{x in X} g_{t-1}(x)`

using the information available from the preceding round. Observe `y_t=f(x_t)+epsilon_t in Y`, where `epsilon_t` is integrable and `E[epsilon_t]=0`. Then draw a fresh `theta_{t,0}` with law `Pi_0`, independently of all information available before this draw, including the observations through round `t`. Set `g_{t,0}=g_{theta_{t,0}}`, choose

`theta_t in argmin_{theta in Theta} [(lambda_t/2)||g_theta-g_{t,0}||_{H_G}^2 + sum_{i=1}^t ell(g_theta(x_i),y_i)]`,

and set `g_t=g_{theta_t}`. Assume these minima are attained and all selections and displayed random quantities are measurable. The fitting and selection rules use only the information described in this experiment.

Let `(F_t)_{t>=0}` be its filtration after initialization and fitting at each round, with `g_0` measurable at time zero. In particular, `x_t` is `F_{t-1}`-measurable and `y_t`, `theta_{t,0}`, and `g_t` are `F_t`-measurable. Assume that for some fixed `sigma_ell>0`, almost surely,

`E[exp(s ell'_{y_t}(f(x_t))) | F_{t-1}] <= exp(s^2 sigma_ell^2/2)`

for every real `s` and every `t>=1`.

Define `rho(theta,theta')=||g_theta-g_theta'||_{H_G}`. Suppose there are constants `c_star,alpha_0,d_eff>0` and a nondecreasing function `psi_0:(0,infinity)->(0,infinity)` such that, for `theta_0` with law `Pi_0`,

`P(rho(theta_star,theta_0)<=a)>=c_star a^{d_eff}` for every `0<a<alpha_0`,

and

`P(rho(theta_star,theta_0)>psi_0(s))<=exp(-s)` for every `s>0`.

Let `k:X x X->R` be a positive-semidefinite kernel such that `k-k_G` is positive semidefinite. For `t>=1`, define

`K_t=[k(x_i,x_j)]_{i,j=1}^t`,

`k_t(x)=[k(x,x_i)]_{i=1}^t`,

and the nonnegative quantity `sigma_t(x)` by

`sigma_t^2(x)=k(x,x)-k_t(x)^T(K_t+(lambda_0/alpha_ell)I_t)^{-1}k_t(x)`.

At time zero set `sigma_0^2(x)=k(x,x)`, and use the empty-matrix convention `det(I_0+(alpha_ell/lambda_0)K_0)=1`.

## Task

Prove the following two assertions.

1. For every `delta in (0,1]`, with probability at least `1-delta`, simultaneously for every integer `t>=0` and every `x in X`,

   `|g_t(x)-f(x)|<=2 beta_t(delta) sigma_t(x)`,

   where

   `beta_t(delta)=sqrt(lambda_t/lambda_0)||f-g_{t,0}||_{H_G} + sigma_ell sqrt((2/(alpha_ell lambda_0)) log(det(I_t+(alpha_ell/lambda_0)K_t)^{1/2}/delta))`.

2. Suppose additionally that `lambda_t asymp (log t)^q` as `t->infinity` for some `q>1`, that `psi_0(s)=O(s^zeta)` as `s->infinity` for some `zeta>0`, and that `sum_{t=1}^infinity lambda_t^{-d_eff/2}=infinity`. Here `asymp` means that the ratio is bounded above and below by positive constants for all sufficiently large indices. For every `delta in (0,1]`, prove that, with probability at least `1-delta`,

   `R_T=sum_{t=1}^T [f(x_star)-f(x_t)] = O(sqrt(T)(log T)^{zeta+q(1+d_eff/4)})`.

   The last assertion means that there are finite deterministic constants `C_delta` and `T_delta`, allowed to depend on the fixed problem data, the regularization schedule, and `delta` but not on `T` or the realized sample path, such that on an event of probability at least `1-delta` the displayed regret is at most `C_delta sqrt(T)(log T)^{zeta+q(1+d_eff/4)}` for every integer `T>=T_delta`.
