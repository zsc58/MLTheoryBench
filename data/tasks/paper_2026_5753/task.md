# Problem

## Setup

Let `J:R^d -> R` be twice continuously differentiable, have a minimizer `Q_*` with `J(Q_*)=0`, and satisfy `m I <= nabla^2 J(q) <= L I` for all `q`, where `0<m<=L` are constants. Let `sigma>0`, let `W_t` be standard `d`-dimensional Brownian motion, and let `Q_t` solve

`dQ_t = -nabla J(Q_t) dt + sigma dW_t`.

Define

`Z=integral_{R^d} exp(-2J(q)/sigma^2) dq`,

and assume the Gibbs probability measure

`pi(dq)=Z^{-1} exp(-2J(q)/sigma^2) dq`

is well defined. Write `nu_t` for the law of `Q_t`, and let `u_t=d nu_t/d pi` whenever this density exists. Denote the reversible Langevin generator and its transition semigroup by

`mathcal{L}=(sigma^2/2) Delta - nabla J dot nabla`, `P_t=exp(t mathcal{L})`,

with `P_t` self-adjoint on `L^2(pi)`, positivity preserving, and `P_t 1=1`. The scalar `L` in the Hessian bound is distinct from the operator `mathcal{L}`.

Let `a_H:R^d -> [0,infinity)` be measurable, satisfy `a_H(Q_*)=0`, and suppose `J(q)>=psi(a_H(q))` for a strictly increasing function `psi:[0,infinity) -> [0,infinity)` with `psi(0)=0`. For a fixed `alpha>0`, define the unsafe set `A_H={q:a_H(q)>alpha}` and assume `0<pi(A_H)<1`.

Assume `nu_0` is absolutely continuous with respect to `pi`, with density `u_0`, and define `chi_0^2=integral (u_0-1)^2 d pi<infinity`. Define the set-specific rate by

`lambda_A = sup{lambda>=0 : ||P_t(1_A-pi(A))||_{L^2(pi)} <= ||1_A-pi(A)||_{L^2(pi)} exp(-lambda t) for every t>=0}`,

where `A=A_H`.

## Task

Prove that for every `t>=0`,

`|nu_t(A_H)-pi(A_H)| <= sqrt(chi_0^2 pi(A_H)(1-pi(A_H))) exp(-lambda_A t) <= sqrt(chi_0^2 pi(A_H)) exp(-lambda_A t)`.

In particular,

`nu_t(A_H) <= pi(A_H) [1 + sqrt(chi_0^2/pi(A_H)) exp(-lambda_A t)]`.

Moreover, if `M=||u_0||_{L^infinity(pi)}<infinity`, then for every `t>=0`,

`nu_t(A_H) <= min{ M pi(A_H), pi(A_H)+sqrt(chi_0^2 pi(A_H)) exp(-lambda_A t)}.`

Under the stated strong-convexity bound, also establish that `lambda_A>=m`.
