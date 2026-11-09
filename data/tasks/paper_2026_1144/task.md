# Problem

## Setup

Let `m` be a positive integer, let `X` be a nonempty closed convex subset of `R^d`, and choose `x_0` in `X`. Let `F(x)=sum_{i=1}^m F_i(x)`, where `F` is continuously differentiable, `F_*:=inf_{x in X} F(x)>-infinity`, and each `F_i` is L-smooth on `X`:
`||grad F_i(x)-grad F_i(y)|| <= L||x-y||`.

For each agent `i` and time `t=0,1,...`, let `d_i(t)` be an integer in `{0,...,t}`. The server receives the stale stochastic estimate `G_i(x_{d_i(t)},xi_i(d_i(t)))`, forms
`v_t=sum_{i=1}^m G_i(x_{d_i(t)},xi_i(d_i(t)))`,
and updates
`x_{t+1}=Pi_X(x_t-a_t v_t)`.

For each `s`, write `F_s=sigma(x_s)` and define
`bar G_i(s)=E[G_i(x_s,xi_i(s)) | F_s]`.
The estimator sample at time `s` is independent of `x_s`; the estimator-sample process is independent of the delay process. The delay variables are independent across agent-time pairs. These timing conventions apply when a stale timestamp is selected.

Assume that there are constants `G,C` in `(0,infinity)` and `kappa` in `(0,1)` such that, for every agent `i`, every time `t`, and all times `r,s`,
`E[||G_i(x_t,xi_i(t))||^2 | F_t] <= G`,
`||bar G_i(r)-bar G_i(s)|| <= L||x_r-x_s||`,
`||bar G_i(t)-grad F_i(x_t)|| <= b_t`,
`E[(t-d_i(t))^2] <= C`, and `d_i(t)>=kappa t`.
Here `(b_t)` is a nonnegative nonincreasing sequence. The stepsizes `(a_t)` are positive and nonincreasing.

## Task

Define
`H_t:=a_t^(-1)[x_t-Pi_X(x_t-a_t grad F(x_t))]`.
Prove that if `sum_{t=0}^infinity a_t=infinity` and
`lim_{t->infinity} a_{ceil(kappa t)}/a_t=bar a>0`, then, as `T->infinity`,
`(1/(T+1))sum_{t=0}^T E||H_t||^2 = O((sum_{t=0}^T[a_t+a_t^2+a_t b_t^2])/(T a_T))`.

In particular, for `a_t=a_0/(t+1)^alpha` with `a_0>0` and `0<alpha<1`, the ratio condition holds and the bound is `O(1)` for nonincreasing `(b_t)`.
