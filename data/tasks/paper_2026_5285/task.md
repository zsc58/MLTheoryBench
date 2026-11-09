# Problem

## Setup

Fix `d in N`, `p in [1,infinity]`, `r in [1,infinity)` with `r<=p`, and `tau>0`; use the convention `1/infinity=0`. Equip `R^d` with a fixed norm `||.||`.

For `s in [1,infinity]`, let `P_s(R^d)` be the Borel probability measures with finite `s`th moment when `s<infinity`, and bounded support when `s=infinity`. Write `Pi(rho,rho')` for the couplings of two measures and `F#rho` for the pushforward of `rho` by a measurable map `F`. All Wasserstein distances use the fixed norm: for `s<infinity`,

`W_s(rho,rho') = inf_{eta in Pi(rho,rho')} (integral ||x-y||^s deta(x,y))^(1/s)`,

and

`W_infinity(rho,rho') = inf_{eta in Pi(rho,rho')} ess sup_{(x,y)~eta} ||x-y||`.

For `gamma in Pi(rho_0,rho_1)` and `gamma' in Pi(rho'_0,rho'_1)`, with all four marginals in `P_s(R^d)`, define

`W'_s(gamma,gamma') = (W_s(rho_0,rho'_0)^s + W_s(rho_1,rho'_1)^s)^(1/s)` when `s<infinity`,

and

`W'_infinity(gamma,gamma') = max{W_infinity(rho_0,rho'_0), W_infinity(rho_1,rho'_1)}`.

For probability measures `P,Q` on the same Borel space, define `KL(P || Q)=integral f log(f) dQ` if `P` is absolutely continuous with respect to `Q`, where `f=dP/dQ`, and define `KL(P || Q)=+infinity` otherwise. Use the natural logarithm and `0 log 0=0`.

Let `h:R^d times R^d -> [0,infinity)` be Borel. For endpoint measures `rho_0,rho_1`, define

`E_tau(rho_0,rho_1) = inf_{gamma in Pi(rho_0,rho_1)} [ integral h(x_0,x_1) dgamma + tau KL(gamma || rho_0 tensor rho_1) ]`,

and denote an optimizer by `gamma^tau_{rho_0,rho_1}`.

Assume that `h` is admissible with a finite constant `lambda>=0`: for every `rho_0,rho'_0,rho_1,rho'_1 in P_p(R^d)` and every `gamma in Pi(rho_0,rho_1)`, `gamma' in Pi(rho'_0,rho'_1)`,

`|integral h dgamma - integral h dgamma'| <= lambda W'_p(gamma,gamma')`.

Let `mu_0,mu_1 in P_p(R^d)` satisfy the transport inequality

`W'_r(gamma,gamma') <= kappa KL(gamma || gamma')^(1/(2r))`

for some finite `kappa>=0` and all `gamma,gamma' in Pi(mu_0,mu_1)` having finite `KL(gamma || gamma')`. Comparisons with infinite relative entropy impose no restriction, including when `kappa=0`.

For `i in {0,1}`, let `B_i` be a finite nonempty subset of `R^d` and let `R_i:R^d -> B_i` be a measurable map that assigns every point to a closest anchor. Set `nu_i=R_i#mu_i`, and define

`e_i = (integral ||x-R_i(x)||^p dmu_i(x))^(1/p)` when `p<infinity`,

and `e_i = ess sup_{x~mu_i} ||x-R_i(x)||` when `p=infinity`. Define

`E_p=(e_0^p+e_1^p)^(1/p)` when `p<infinity`,

and `E_p=max{e_0,e_1}` when `p=infinity`.

## Task

Prove the following integrated stability claim. Simultaneously,

`W_p(mu_i,nu_i)<=e_i` for each `i in {0,1}`,

`|E_tau(mu_0,mu_1)-E_tau(nu_0,nu_1)| <= lambda E_p`,

and

`W'_r(gamma^tau_{mu_0,mu_1},gamma^tau_{nu_0,nu_1}) <= 2^(1/r-1/p) E_p + kappa(2lambda E_p/tau)^(1/(2r))`.
