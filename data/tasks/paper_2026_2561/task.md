# Problem

## Setup

Let d be a positive integer, let X=R^d, and let nu be a probability measure on X with a strictly positive differentiable density pi with respect to Lebesgue measure. Fix z in X.

Let `F:[0,1] x X x X -> X` be C^1 in t and C^2 in its final spatial argument, with these derivatives jointly continuous, and suppose

`F(0,z,x)=z` and `F(1,z,x)=x`.

Write `F_t(x)=F(t,z,x)`. For every `t in (0,1]`, assume F_t is a diffeomorphism of X onto X. Let `D_xF_t` denote its spatial Jacobian matrix. Define the pushforward measure by

`nu_t(A)=nu(F_t^{-1}(A))`

for Borel sets A, and define its density by

`pi_t(y)=pi(F_t^{-1}(y)) |det D_xF_t(F_t^{-1}(y))|^{-1}`.

Define

`u_t(y)=partial_t F_t(F_t^{-1}(y))`.

Assume that pi_t, its first time derivative, and its first and second spatial derivatives are jointly continuous on `(0,1] x X`. Assume also that u_t and its spatial Jacobian `D_yu_t` are jointly continuous there. At t=1, time derivatives are interpreted from the left. All gradients, divergences, and Laplacians below are with respect to y.

Let `sigma:(0,1] -> [0,infinity)` be a finite-valued deterministic Borel function such that

`integral_a^b sigma_t^2 dt < infinity` whenever `0<a<=b<=1`.

Define

`b_t(y)=u_t(y)+(sigma_t^2/2) grad log pi_t(y)`.

## Task

Prove that, for every `t in (0,1]` and `y in X`,

`partial_t pi_t + div(pi_t u_t)=0`,

and

`partial_t pi_t=-div(pi_t b_t)+(sigma_t^2/2) Delta pi_t`.

Consequently, let `0<t_0<=T<=1`. Suppose the Itô SDE

`dX_t=b_t(X_t)dt+sigma_t dW_t`,

with initial law having density pi_{t_0}, admits a nonexplosive weak solution on `[t_0,T]` and is unique in law there. Here W is a standard d-dimensional Brownian motion relative to the solution's filtration. Prove that X_t has density pi_t for every `t in [t_0,T]`.
