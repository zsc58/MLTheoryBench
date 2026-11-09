# Problem

## Setup

Work on `R^d`, where `d` is a positive integer. Let `pi` and `rho` be strictly positive `C^1` probability densities with finite second moments, and set

`u(x)=pi(x)/rho(x),     s(x)=nabla log u(x).`

Let `f:(0,infinity)->R` be twice differentiable and strictly convex, with `f(1)=0`. For strictly positive probability densities `q` of finite second moment for which the integral is finite, define

`F(q)=integral q(x)f(pi(x)/q(x)) dx,     a(z)=z^2 f''(z).`

Assume `F(rho)<infinity` and that its first variation at `rho` exists. Let `v` be the associated, unrescaled 2-Wasserstein gradient-flow velocity at `rho`, assumed to exist with

`integral rho(x)||v(x)||^2 dx < infinity.`

For a random vector `X` with density `rho`, let `rho_h` be the density of `X+h v(X)`, with `v` held fixed at the initial density `rho`. Assume these densities exist for all sufficiently small `|h|`, and set `rho_0=rho`.

Fix thresholds `0<epsilon<delta`, which remain fixed as `h->0`. Define

`B={x:pi(x)>=delta},     A={x:pi(x)>=delta, rho(x)<=epsilon}.`

For any probability density `q`, define

`H(q)=integral pi(x)1_B(x)[epsilon-q(x)]_+ dx,`

where `[z]_+=max{z,0}`.

Assume `v` is `C^1` on an open neighbourhood `U` of `B`, and that `{x in B:rho(x)=epsilon}` has Lebesgue measure zero. The first-order regime in this problem is specified by the following regularity assumption: as `h->0`, the density difference quotients

`(rho_h-rho)/h`

converge in `L^1_loc(U,dx)` and in `L^1(B,pi(x)dx)`. Local convergence means `L^1` convergence on every compact subset of `U`; the weighted norm is `integral_B pi(x)|g(x)|dx`.

Suppose `a(u(x))>0` for Lebesgue-almost every `x in A`. Assume the ordinary derivative `a'(z)` exists at every `z in u(A)` for which `a(z)>0`. Define

`E(z)=z a'(z)/a(z)     for z in u(A) with a(z)>0,`

and

`C(x)=-div(rho s)(x)/(rho(x)||s(x)||^2)`

on the set `{x in A:a(u(x))>0, ||s(x)||>0}`. Divergence here is classical at its stated evaluation points. All almost-everywhere assertions about subsets of `R^d` use Lebesgue measure unless otherwise specified.

## Task

Prove the following integrated claim.

The Wasserstein velocity factorizes, as an equality of velocity fields up to equality rho-almost everywhere, as

`v(x)=a(u(x))s(x).`

Moreover, in the specified first-order regime, as `h->0`,

`H(rho_h)=H(rho)-h G+o(h),`

where

`G=integral_A pi(x)rho(x)a(u(x))||s(x)||^2[C(x)-E(u(x))] dx.`

The integrand is defined to be zero on the zero-score set `{x in A:||s(x)||=0}` and on the null set `{x in A:a(u(x))=0}`.

Consequently, if `C(x)>=E(u(x))` almost everywhere on `{x in A:a(u(x))>0, ||s(x)||>0}`, and this inequality is strict on a positive-measure subset on which `pi rho a(u)||s||^2` is positive, then `G>0` and `H(rho_h)<H(rho)` for every sufficiently small `h>0`.
