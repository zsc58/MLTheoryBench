# Problem

## Setup

Let `T`, `K`, and `m` be positive integers, and let `delta in (0,1)`. Write `Delta_K={x in R^K_+:sum_a x(a)=1}` and let `u` be the uniform distribution on the `K` arms. All logarithms are natural except for `log_2`.

Let `F_t` be the history before round `t`. The learner's strategy `x_t` is determined by previously revealed feedback and is `F_t`-measurable. At round `t`, loss and constraint vectors `ell_t in [0,1]^K` and `g_{t,i} in [-1,1]^K`, for `1<=i<=m`, are generated with conditional means

`bar ell_t=E[ell_t|F_t]`,  `bar g_{t,i}=E[g_{t,i}|F_t]`.

Their conditional distributions may vary arbitrarily with the past and with `t`. The learner then samples `A_t` using fresh randomization: conditional on `F_t` and the current vectors, `A_t` has distribution `x_t`. The learner incurs `ell_t(A_t)` and receives the complete loss and constraint vectors only at the end of the round.

Define

`C_i=min_{v in [-1,1]^K}sum_{t=1}^T||bar g_{t,i}-v||_1`,  `C=max_i C_i`,

and let `g_i^circ` be a minimizer. Assume almost surely that some simplex strategy has `bar g_{t,i}^T x<0` for every `t,i`. Define

`rho=max_{x in Delta_K}min_{t,i}(-bar g_{t,i}^T x)>0`,

and let `x^diamond` attain it. These definitions and the feasibility assumption are interpreted pathwise when the conditional means are random.

Let

`OPT=min_{x in Delta_K:sum_t bar g_{t,i}^T x<=0 for all i}sum_t bar ell_t^T x`,

`R_T=sum_t ell_t(A_t)-OPT`,

`V_T=max_i sum_t[bar g_{t,i}^T x_t]^+`, where `[z]^+=max{z,0}`.

For simplex vectors define

`D_KL(p||q)=sum_a p(a) ln(p(a)/q(a))`,

with a zero summand when `p(a)=0`, and value `+infinity` if `p(a)>0=q(a)` for some `a`.

Write `n_t=t-1`. Set `hat g_{1,i}=0` and `X_1=Delta_K`. For `2<=t<=T`, define

`hat g_{t,i}=n_t^{-1}sum_{s<t}g_{s,i}`,

`xi_t=4sqrt(ln(TKm/delta)/n_t)`,

`X_t={x in Delta_K:(hat g_{t,i}-xi_t 1)^T x<=0 for every i}`,

where `1` denotes the all-ones vector.

Initialize `x_1=u` and set `eta=sqrt(ln(KT)/T)`. After observing round `t`, for `1<=t<T`, if `X_{t+1}` is nonempty, compute

`p_{t+1}=argmin_{x in X_{t+1}}{ell_t^T x+(1/eta)D_KL(x||x_t)}`.

If `X_{t+1}` is empty, set `p_{t+1}=u`. Then set

`x_{t+1}=(1-1/T)p_{t+1}+(1/T)u`.

No update is performed after round `T`; in particular, when `K=T=1`, the value `eta=0` is not used in an optimization objective.

## Task

Prove that this algorithm, without knowing `C`, satisfies, with probability at least `1-3delta`,

`R_T<=4log_2(T)sqrt(T ln(KT))+(2C/rho)log_2(T)+4sqrt(T ln(TK/delta))`,

and, with probability at least `1-delta`,

`V_T<=2+2C+C ln(T)+16sqrt(T ln(TKm/delta))`.
