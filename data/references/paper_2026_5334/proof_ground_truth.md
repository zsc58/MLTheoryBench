# Reference Proof

## Proof Structure and Obligations

The proof must close four stages: (1) compute the first variation and identify the Wasserstein velocity; (2) identify the first-order derivative of the frozen Euler density and differentiate the deficit functional in the specified integration regime; (3) justify the derivative domains, factor the flux, and handle the zero-score and null zero-weight sets; and (4) establish a finite positive coefficient and strict decrease. All four stages are proved below.

## Complete Proof

### 1. First variation and velocity

Let `u=pi/rho`. Take a smooth compactly supported perturbation `phi` with `integral phi=0`. For sufficiently small real `t`, `rho+t phi` remains positive, normalized, and of finite second moment. Its divergence value is finite because the density is unchanged off the compact support of `phi`, and the perturbed densities and ratios stay in compact positive ranges on that support. Continuity of `f` and `f'` on those ranges justifies differentiation under this compactly supported integral. Thus

`d/dt F(rho+t phi)|_(t=0) = integral phi(x)[f(u(x))-u(x)f'(u(x))] dx.`

A first variation is therefore `g(x)=f(u(x))-u(x)f'(u(x))`, up to an additive spatial constant.

We use the standard Wasserstein gradient identity in its first-variation form: when the associated finite-energy Wasserstein gradient-flow velocity exists, it is the negative spatial gradient of the first variation. This is the unrescaled gradient-flow convention, not a unit-speed normalization. The setup assumes existence of the first variation and of this velocity; the representative just computed is spatially differentiable because `f` is twice differentiable and `u` is C1. No theorem asserting existence or convergence of a nonlinear flow is being invoked.

For the scalar function `g_0(z)=f(z)-z f'(z)`, one has `g_0'(z)=-z f''(z)`. Consequently,

`v = -nabla g = u f''(u) nabla u = u^2 f''(u) s = a(u)s`

as an equality of Wasserstein velocity fields. Since `rho` is everywhere positive, equality rho-almost everywhere is also equality Lebesgue-almost everywhere. Also, convexity gives `a(z)>=0`.

### 2. Euler density derivative and deficit expansion

Set `B={pi>=delta}` and let `U` be the regularity neighbourhood in the task. Write `d_h=(rho_h-rho)/h`. Let `b` be its local L1 limit on `U`, and let `c` be its limit in `L1(B,pi dx)`. On every compact subset of `U`, `pi` is bounded. Local L1 convergence therefore implies convergence in the weighted L1 norm restricted to the part of that compact set lying in `B`. Uniqueness of limits and a compact exhaustion of `U` give `b=c` almost everywhere on `B`. In particular,

`integral_B pi |b| dx < infinity`,

and `d_h` converges to `b` in that weighted norm.

We identify `b` without assuming a density-flux expansion. For a smooth test function `phi` compactly supported in `U`, the definition of the Euler pushforward gives

`integral phi(y)d_h(y)dy = integral rho(x)[phi(x+h v(x))-phi(x)]/h dx.`

The integrand on the right converges pointwise to `rho v dot nabla phi`. Its absolute value is bounded by `rho ||v|| sup||nabla phi||`. This bound is integrable because the finite-energy assumption and Cauchy-Schwarz imply `integral rho ||v||<infinity`. Dominated convergence, followed by local L1 convergence on the left, yields

`integral phi b = integral rho v dot nabla phi = -integral phi div(rho v).`

The last equality is ordinary integration by parts with compact support in `U`, where `rho v` is C1. Hence

`b=-div(rho v)`

almost everywhere on `U`. This is a derivative at `h=0`; it does not assert that the entire frozen Euler family solves a continuity equation with the same Eulerian velocity for nonzero `h`.

Let `psi(z)=[epsilon-z]_+`, defined for all real `z`. It is 1-Lipschitz. Therefore

`integral_B pi |psi(rho_h)-psi(rho+h b)| dx <= integral_B pi |rho_h-rho-h b| dx = o(|h|).`

Outside the null threshold set, the quotients

`[psi(rho+h b)-psi(rho)]/h`

converge to `-b 1_{rho<epsilon}`. Their absolute values are bounded by `|b|`, which is integrable for the measure `pi 1_B dx`. Dominated convergence thus gives

`H(rho_h)-H(rho) = -h integral_B pi b 1_{rho<epsilon} dx + o(h)`

`= -h integral_A pi[-div(rho v)] dx + o(h).`

The second equality uses the null threshold set. Denote the last integral coefficient by `G_0`. It is finite, indeed absolutely integrable, by the weighted integrability of `b`. The functional itself is always finite: `0<=H(q)<=epsilon` for every probability density `q`.

### 3. Derivative domains, flux factorization, and exceptional sets

We first justify the classical divergence defining `C`, without imposing C1 regularity on `s`. The score `s` is continuous because `pi` and `rho` are positive C1 densities. Fix `x` in `A` with `a(u(x))>0`. The function `a` is differentiable at `u(x)`, so `a(u)` is differentiable at `x` and its denominator stays positive in a sufficiently small neighbourhood of `x`. The quotient `v/a(u)` is therefore differentiable at `x`.

This quotient equals `s` almost everywhere nearby. A continuous function agreeing almost everywhere with a function differentiable at `x` has the same first-order approximation at `x`: the differentiability estimate holds on the full-measure equality set, and its linear error bound extends to every nearby point by continuity of the continuous function. This also identifies their values at `x`. Thus `s` is differentiable at the relevant positive-weight points, and the classical divergence in `C` exists there. The same observation justifies differentiating the almost-everywhere velocity identity at these points.

Product and chain rules now give, on this domain,

`-div(rho a(u)s) = -a(u)div(rho s)-rho a'(u)nabla u dot s`

`= -a(u)div(rho s)-rho a'(u)u||s||^2.`

Where additionally `||s||>0`, the definitions of `C` and `E` yield

`-div(rho v) = rho a(u)||s||^2[C-E(u)].`

It remains to justify the zero-score extension. We use the inherited C1 velocity, not an additional C1 hypothesis on the score. For a scalar C1 function restricted to a coordinate line, its derivative is zero at every accumulation point of its zero set, by taking difference quotients along zeros. The remaining, isolated zeros are countable on each line. Fubini therefore shows that each coordinate derivative vanishes almost everywhere on the scalar function's zero set. Applied to every component of `v`, this gives `Dv=0` almost everywhere on `{v=0}`. Hence

`div(rho v)=nabla rho dot v+rho div v=0`

almost everywhere on that set.

On the positive-weight part of `A`, `s=0` implies `v=0` by the factorization and the pointwise identification above. Thus the density-flux contribution vanishes almost everywhere on the zero-score part of `A`. Finally, `{x in A:a(u(x))=0}` is null by the assumed almost-everywhere positivity. Assigning the regional integrand zero there does not change any integral.

Combining these observations gives

`G_0 = integral_A pi rho a(u)||s||^2[C-E(u)] dx = G`,

with exactly the extensions specified in the task. In particular, the claimed integral is finite and the expansion of `H` has the asserted coefficient.

### 4. Strict improvement

Under the comparison assumption, the extended integrand defining `G` is nonnegative almost everywhere. It is strictly positive on the stipulated positive-measure subset. A nonnegative integrable function positive on a set of positive measure has strictly positive integral, so `G>0`.

Write the scalar expansion as `H(rho_h)-H(rho)=-hG+R(h)`, where `R(h)/h->0`. For all sufficiently small positive `h`, `|R(h)|<=hG/2`, and therefore

`H(rho_h)-H(rho)<=-hG/2<0.`

The permitted step size may depend on the fixed densities, functional, and thresholds; no uniform bound is claimed. If `A` is empty or the positive-prefactor set is null, the strictness hypothesis cannot hold, so these degenerate cases cause no exception.
