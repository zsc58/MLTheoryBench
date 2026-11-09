# Problem

## Setup

Fix `alpha in (0,1)` and a probability space under a law `Q`, carrying filtrations `(F_t)_{t>=0}` and `(G_t)_{t>=0}` such that `G_t` is contained in `F_t` for every `t>=0`. At each integer time `t>=1`, let `q_t` be an `F_{t-1}`-measurable real-valued forecast and let `Y_t` be an `F_t`-measurable real-valued outcome. Define the hit residual

`e_t = 1{Y_t <= q_t} - alpha`.

Assume `e_t` is `G_t`-measurable. Thus `e_t` belongs to `{-alpha,1-alpha}`. Define

`mu_t = E_Q[e_t | G_{t-1}]`.

Let `x_t in R^d` be `G_{t-1}`-measurable and satisfy `||x_t||_2 <= R`, `Q`-almost surely for every `t`, where `R>0`. Set

`C = {u in R^d : ||u||_2 <= 1/(2R)}`.

A feature-dependent betting learner selects a `G_{t-1}`-measurable `u_t in C` and has wealth

`W_0=1`,

`W_T = product_{t=1}^T (1 + <u_t,x_t> e_t)`.

For a fixed `u in C`, define

`ell_t(u) = -log(1 + <u,x_t> e_t)`,

`Reg_T(u) = sum_{t=1}^T [ell_t(u_t)-ell_t(u)]`,

and the predictable quadratic edge

`a_t^Q(u) = <u,x_t> mu_t - <u,x_t>^2`.

Assume the learner has a deterministic pathwise regret bound: for every `u in C` and every integer `T>=1`,

`Reg_T(u) <= r_T`,

where `(r_T)` is deterministic.

Fix `kappa in (0,1]` and an integer `t_0>=1`. Assume there exists a fixed `u_* in C` such that, `Q`-almost surely,

`a_t^Q(u_*) >= kappa` for every `t>=t_0`.

For `gamma in (0,1)`, define

`sigma_gamma = inf{T>=1 : W_T >= 1/gamma}`

with `inf(empty set)=infinity`. Define `N_gamma(r)` to be the smallest integer `n>=t_0` such that

`log(1/gamma)+2(t_0-1)+r_T <= kappa T/2`

for every integer `T>=n`; set `N_gamma(r)=infinity` if no such integer exists.

## Task

Prove the following integrated detection theorem. If `N_gamma(r)<infinity`, then for every integer `T>=N_gamma(r)`,

`Q(sigma_gamma>T) <= exp(-kappa^2 T/2)`.

Consequently,

`Q(sigma_gamma<infinity)=1`

and

`E_Q[sigma_gamma] <= N_gamma(r)+4/kappa^2`.
