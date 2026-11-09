# Problem

## Setup

Fix a prompt `q` and a finite integer horizon `T>=1`. For each `s=1,...,T`, let `x_s` range over a nonempty finite or countable token space. Let `m_s(x_s|q,x_{<s})` be a finite nonnegative transition factor, not necessarily normalized over `x_s`, and let `psi_s(x_{1:s},q)` be finite and nonnegative. Define
`a_s(x_{1:s}|q)=m_s(x_s|q,x_{<s}) psi_s(x_{1:s},q)`,
`tildePi(x_{1:T}|q)=product_{s=1}^T a_s(x_{1:s}|q)`.
Assume `0<Z:=sum_{x_{1:T}} tildePi(x_{1:T}|q)<infinity`, and set `Pi=tildePi/Z`.

Let each `r_s(x_s|q,x_{<s})` be a probability transition, and sample `X_{1:T}` from
`R(x_{1:T}|q)=product_{s=1}^T r_s(x_s|q,x_{<s})`.
Assume that, for every complete path, `tildePi(x_{1:T}|q)>0` implies `R(x_{1:T}|q)>0`. Define the full importance weight
`W_T=product_{s=1}^T [a_s(X_{1:s}|q)/r_s(X_s|q,X_{<s})]`,
and assume `E_R[W_T^2]<infinity`. Ratios defining random weights are evaluated on sampled paths, where their denominators are positive almost surely; values on proposal-null paths are immaterial.

For `t=0,...,T`, define
`gamma_t^prf(x_{1:t})=product_{s=1}^t a_s(x_{1:s}|q)`,
`L_t(x_{1:t})=sum_{x_{t+1:T}} product_{s=t+1}^T a_s(x_{1:s}|q)`,
and
`gamma_t^look(x_{1:t})=sum_{x_{t+1:T}} tildePi(x_{1:T}|q)`.
The suffix sums are extended nonnegative sums. Empty products are one, and summation over an empty suffix has one term. In particular, `gamma_0^prf=1`, `L_T=1`, and `L_0=Z`.

Set `F_t=sigma(X_{1:t})`, with `F_0` the trivial sigma-field, and define
`W_t^prf=product_{s=1}^t [a_s(X_{1:s}|q)/r_s(X_s|q,X_{<s})]`,
`A_t={gamma_t^prf(X_{1:t})>0}`.
Define `W_t^look=W_t^prf L_t(X_{1:t})` on `A_t` and zero on `A_t^c`. Every weighted expression below involving `L_t` or its estimation error is defined to be zero on `A_t^c`; it is not evaluated there by multiplying zero by an infinite or undefined expression.

Fix finite nonnegative constants `C_t`, one for each `t=0,...,T`, and let `J>=1` be an integer. For each `t`, let `U_t` be auxiliary randomness conditionally independent of `X_{t+1:T}` given `F_t`. Let `hat L_t` be a finite real-valued random variable measurable with respect to `sigma(F_t,U_t)`. Under the conditional auxiliary law at each prefix of positive proposal probability, assume
`E[hat L_t|F_t]=L_t(X_{1:t})` on `A_t`, and `E[hat L_t|F_t]=0` on `A_t^c`,
and
`E[(hat L_t-L_t(X_{1:t}))^2|F_t] <= C_t/J` on `A_t`.
The error variable in the last display is defined as zero on `A_t^c`. Conditional moments of the auxiliary estimates mean moments under these prefixwise conditional laws. No independence among different `U_t` is required. When `J` varies, the constants `C_t` are held fixed.

Write `E_R` for expectation under the trajectory law and `E` for expectation under the joint law of the trajectory and auxiliary randomness. Random-variable identities and conditional assumptions are almost sure. Expectations of nonnegative squared errors, and the nonnegative upper bounds below, are allowed to equal `+infinity`.

## Task

Prove the following integrated theorem for every `t=0,...,T`:

1. The exact lookahead marginal satisfies
`gamma_t^look(x_{1:t}) = sum_{x_{t+1:T}} tildePi(x_{1:T}|q)`.
On prefixes with `gamma_t^prf(x_{1:t})>0`, it factors as `gamma_t^prf(x_{1:t}) L_t(x_{1:t})`; on zero prefixes it is zero.

2. `W_t^look=E_R[W_T|F_t]` and, for every square-integrable real `F_t`-measurable `Y`,
`E_R[(W_T-Y)^2]=E_R[Var_R(W_T|F_t)] + E_R[(Y-W_t^look)^2]`.
Consequently,
`E_R[(W_T-W_t^prf)^2]=E_R[Var_R(W_T|F_t)] + E_R[(W_t^prf)^2(L_t-1)^2]`,
and
`E[(W_T-W_t^prf hat L_t)^2]=E_R[Var_R(W_T|F_t)] + E[(W_t^prf)^2(hat L_t-L_t)^2]`
`<= E_R[Var_R(W_T|F_t)] + J^{-1} E_R[(W_t^prf)^2 C_t]`,
with `L_t` in these expressions evaluated at `X_{1:t}` and all zero-prefix terms interpreted by the stated convention.

Thus the exact lookahead weight is the minimum-MSE `F_t`-measurable approximation to the full importance weight, while the prefix-only and unbiased Monte Carlo lookahead weights have the displayed excess errors.
