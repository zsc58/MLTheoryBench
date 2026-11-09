# Reference Proof

## Proof Structure and Obligations

The five obligations are: (1) identify the oracle objective and its minimum, including the infinite-norm endpoint; (2) establish the simultaneous empirical-standard-deviation event using an explicitly stated independent concentration result; (3) compare the empirical allocation with the oracle, controlling both variance and bounded-increment contributions; (4) justify conditioning, integer feasibility, the budget, and the final probability; and (5) substitute the exploration prescription and bound every remainder uniformly in the confidence parameter. Each obligation is closed below. No specialized unproved dependency is used.

Write `L=log(4dm/delta)`, `L_d=log(4d/delta)`, `D=d sum_a d_a`, and `T'=T-n_0D`. Choose a fixed oracle minimizer `a*(i)` for each coordinate and put

`g_i=min_a d_a v_{i,a}^2=d_{a*(i)}v_{i,a*(i)}^2`, `c_i^*=d_{a*(i)}`.

All these quantities are positive. For finite `p`, put `r=2p/(p+2)`; for `p=infinity`, put `r=2`. For any positive exponent `r`, the notation `||u||_r` means `(sum_i |u_i|^r)^(1/r)`, whether or not it is a norm.

## 1. Oracle Allocation

For a fixed coordinate mass `lambda_i=sum_a lambda_{i,a}`, its information satisfies

`sum_a lambda_{i,a}/(d_a v_{i,a}^2) <= lambda_i/g_i`.

Equality is obtained by placing all this mass on `a*(i)`. Since the objective decreases when any coordinate information increases, it suffices to optimize over coordinate masses.

For finite `p`, the reduced objective before the increasing power `2/p` is

`sum_i g_i^(p/2) lambda_i^(-p/2)`.

It diverges if any coordinate mass vanishes, has a finite value at a strictly positive allocation, and is strictly convex on the positive simplex. Thus its interior stationary point is the global minimizer. The multiplier equations give

`lambda_i^* = g_i^(p/(p+2)) / sum_l g_l^(p/(p+2))`.

Substitution yields

`Gamma_p=(sum_i g_i^(p/(p+2)))^((p+2)/p)`.

For `p=infinity`, if `min_i lambda_i/g_i=t`, then `1=sum_i lambda_i>=t sum_i g_i`. Equality is achieved by `lambda_i=g_i/sum_l g_l`, so `Gamma_infinity=sum_i g_i`.

In all cases,

`sqrt(Gamma_p)=||(sqrt(g_i))_i||_r`.

This also establishes that the extended-real minimization in the public task has a finite, positive, attained minimum.

## 2. Simultaneous Variance Control

The independent empirical-standard-deviation concentration result used here is the following statement, recorded in theory_007 and in the source at L000299-L000303. If `Z_1,...,Z_n` are independent copies of a variable supported on an interval of length `M`, with variance `v^2`, `n>=2`, and

`hat V=[2n(n-1)]^(-1) sum_{r!=s}(Z_r-Z_s)^2`,

then, for `rho in (0,1)`,

`P(|sqrt(hat V)-v| > M sqrt(2log(2/rho)/(n-1))) <= rho`.

This is a standard independent concentration result, not a paper-specific theorem. Its hypotheses hold for every first-stage sample: the sampling length is deterministic, the draws are independent copies with the required support, and `n_0>=2`. The statistic has exactly the stated normalization; in particular, each pairwise squared difference has expectation `2v^2`, so `E[hat V]=v^2`.

Apply this result with `rho=delta/(2dm)` and take a union bound. There is an event `E`, measurable with respect to the first-stage data, of probability at least `1-delta/2`, on which

`|hat v_{i,a}-v_{i,a}|<=eta`

for every pair. Consequently,

`v_{i,a}<=bar v_{i,a}<=v_{i,a}+2eta`.

Also, `bar v_{i,a}>=eta>0` holds without conditioning on `E` because the empirical standard deviation is nonnegative.

## 3. Stability of the Empirical Allocation

On `E`, define

`bar g_i=d_{hat a(i)}bar v_{i,hat a(i)}^2=min_a d_a bar v_{i,a}^2`,

`S=sum_i bar g_i^alpha`, `hat lambda_i=bar g_i^alpha/S`,

and

`F=||(sqrt(bar g_i))_i||_r`.

Let

`a=||(sqrt(d_{hat a(i)}) v_{i,hat a(i)}/sqrt(hat lambda_i))_i||_p`,

`b=||(d_{hat a(i)}/hat lambda_i)_i||_p`,

with maximum norms when `p=infinity`.

Since `v<=bar v`, replacing the true variance by the inflated one and substituting the proxy-optimal allocation gives `a<=F`. For finite `p`, the resulting norm is `S^((p+2)/(2p))=F`; for `p=infinity`, it is `sqrt(S)=F`.

Empirical source minimality and the variance sandwich imply

`sqrt(bar g_i)<=sqrt(c_i^*)(v_{i,a*(i)}+2eta)=sqrt(g_i)+2eta sqrt(c_i^*)`.

Put `U=||(sqrt(g_i))_i||_r=sqrt(Gamma_p)` and `V=||(sqrt(c_i^*))_i||_r`.

If `p>=2`, then `r>=1`, and Minkowski gives

`F<=U+2V eta`.

Set `C_1=2V` in this regime.

If `1<=p<2`, then `r in [2/3,1)`. Coordinatewise subadditivity gives

`F<=(U^r+(2V eta)^r)^(1/r)`.

For positive `A,B`, integration of the derivative of `t^(1/r)` gives

`(A+B)^(1/r)-A^(1/r) <= (B/r)(A+B)^(1/r-1)`.

Because `1/r-1 in (0,1/2]`, subadditivity of that power further bounds this by

`(B/r)(A^(1/r-1)+B^(1/r-1))`.

Using `A=U^r` and `B=(2V eta)^r` therefore gives

`F<=U+C_1 eta+C_2 eta^r`,

where

`C_1=2V/r`, `C_2=2^r U^(1-r)V^r/r`.

This derivation holds for every `eta>0`; it does not assume `eta<1`.

For the bounded-increment contribution, `bar v>=eta` implies

`d_{hat a(i)}<=bar g_i/eta^2`.

For finite `p`,

`||(bar g_i/hat lambda_i)_i||_p = S (sum_i bar g_i^(2alpha))^(1/p) <= S^(1+2/p)=F^2`,

using `sum_i y_i^2<=(sum_i y_i)^2` with `y_i=bar g_i^alpha`. For `p=infinity`, `bar g_i/hat lambda_i=S`, so the same conclusion holds directly. Hence

`b<=eta^(-2)F^2`.

Squaring the bound for `F` gives

`a<=sqrt(Gamma_p)+C_1 eta+1_{p<2}C_2 eta^r`,

`b<=3[Gamma_p eta^(-2)+C_1^2+1_{p<2}C_2^2 eta^(2r-2)]`.

All constants here depend only on the permitted fixed-instance quantities. The argument remains valid for arbitrarily small positive true variances and requires no gap between the best and second-best sources.

## 4. Integer Feasibility, Conditional Concentration, and Budget

The empirical standard deviations are finite, and their inflation is strictly positive. Thus the tie-broken sources, proxy masses, and second-stage counts are measurable functions of the first-stage data, with every proxy mass positive.

Let `D_hat=sum_i d_{hat a(i)}` and `T_eff=T'-D_hat`. Since `D_hat<=D`, `n_0>=2`, and `T>=2n_0D`,

`T_eff>=T-n_0D-D>=T/4>0`.

The specified counts are positive integers and satisfy

`n_i>=T_eff hat lambda_i/d_{hat a(i)}`.

Moreover,

`sum_i d_{hat a(i)} n_i <= D_hat+T_eff sum_i hat lambda_i=T'`.

Adding the exploration cost proves the total cost is at most `T` on every realization.

Condition on the first-stage sigma-field. All selected sources and counts are now fixed. The unused observations remain independent, and each coordinate's selected observations have mean `theta_i`, variance `v_{i,hat a(i)}^2`, and support in `[0,M]`. This is why the data-dependent allocation does not invalidate concentration.

The bounded-variable concentration statement used from theory_006 is: for independent centered variables `Z_j` with `|Z_j|<=h` and total variance `V`,

`P(|sum_j Z_j|>sqrt(2Vt)+(h/3)t)<=2exp(-t)`.

For completeness, the bounded-variable moment expansion gives `log E exp(u sum_j Z_j)<=V u^2/[2(1-hu/3)]` for `0<u<3/h`. Taking `u=sqrt(2t/V)/(1+(h/3)sqrt(2t/V))` proves the upper-tail statement; applying it to the negatives and taking a union bound proves the displayed two-sided statement. Here the conditional variance is positive. Minkowski's inequality is applied only to the genuine `l_p` norm with `p>=1`; the maximum-norm endpoint follows directly.

Apply this concentration statement to each second-stage mean, with total variance `v_{i,hat a(i)}^2/n_i`, increment bound `M/n_i`, and `t=L_d`. A union bound over the coordinates has conditional failure probability at most `delta/2`. On its success event,

`||hat theta-theta||_p <= sqrt(2L_d/T_eff) a + M L_d b/(3T_eff)`.

Combining this with `E` yields, with unconditional probability at least `1-delta`,

`||hat theta-theta||_p <= sqrt(2L_d/T_eff)[sqrt(Gamma_p)+C_1 eta+1_{p<2}C_2 eta^r]`

`  + (M L_d/T_eff)[Gamma_p eta^(-2)+C_1^2+1_{p<2}C_2^2 eta^(2r-2)]`.

This exact finite bound is the starting point for the final comparison. In particular, the variance-mismatch contribution before bounding the residual budget is `2 M C_1 sqrt(L_d L/((n_0-1)T_eff))`; its factor of two and its `n_0-1` denominator must not be dropped.

## 5. Exploration Substitution and Uniform Remainder Control

It is not enough to say that omitted terms decay faster when `delta` is fixed: the public constants must be independent of `delta`. The following elementary comparison handles the entire feasible parameter range, including `eta>=1` and the minimum exploration length.

Define

- for `p>=2`, `e=2/3` and `kappa=2^(1/3)`;
- for `1<=p<2`, `e=(3p+2)/(4p+4)` and `kappa=2^(p/(2p+2))`.

Then the public real prescription is exactly

`N=kappa (M^2 L)^e T^(1-e)`.

Put `x=M sqrt(L/T)`. Consequently,

`N/T=kappa x^(2e)`.

The rounded prescription satisfies

`N<=n_0<=N+2`, `N/2<=n_0-1<=N+1`.

To control the additive constants uniformly, let `nu=min_{i,a} v_{i,a}>0`. Boundedness implies `v_{i,a}^2<=M^2/4`, so `M^2>=4nu^2`. Also, feasibility gives `T>=4D`, and `L>=log(4)`. Therefore

`N>=N_*:=kappa (4nu^2 log(4))^e (4D)^(1-e)>0`.

This lower bound depends only on permitted fixed-instance quantities. Thus `n_0`, `n_0+1`, and `n_0-1` are bounded above by fixed-instance multiples of `N`. More precisely,

`sqrt(2/[kappa(1+1/N_*)]) x^(1-e) <= eta <= (2/sqrt(kappa)) x^(1-e)`.

The budget assumption and `n_0>=N` also imply

`x<=[1/(2D kappa)]^(1/(2e))=:X`.

Both sides of the comparison for `eta`, and the upper bound `X`, are independent of `T` and `delta`.

For the leading term, put `z=(n_0D+D_hat)/T`. We have `0<=z<=3/4` and `z<=C N/T` for a permitted fixed-instance constant `C`. Since the derivative of `(1-z)^(-1/2)` is at most four on this interval,

`T_eff^(-1/2)-T^(-1/2)<=4z T^(-1/2)`.

Hence the change in the leading term is at most a fixed-instance multiple of

`(sqrt(Gamma_p)/M) x^(1+2e)`.

Use `T_eff>=T/4`, `L_d<=L`, and the two-sided comparison for `eta` in all remaining terms of the finite bound. They are bounded by fixed-instance multiples of the following expressions:

- the linear variance-mismatch term: `M^(-1) C_1 x^(2-e)`;
- when `p<2`, the quasi-norm variance-mismatch term: `M^(-1) C_2 x^(1+r(1-e))`;
- the inverse-square inflation term: `M^(-1) Gamma_p x^(2e)`;
- the constant bounded-increment term: `M^(-1) C_1^2 x^2`;
- when `p<2`, the remaining bounded-increment term: `M^(-1) C_2^2 x^(2+(2r-2)(1-e))`.

For `p>=2`, `2-e=2e`. For `p<2`, direct substitution gives

`1+r(1-e)=2e`,

`2-e>=2e`,

`2+(2r-2)(1-e)=2e+2r(1-e)>2e`.

Also `2>=2e`, and the leading-budget loss has exponent `1+2e>2e`. Because `0<x<=X`, each of these powers is bounded by a fixed-instance multiple of `x^(2e)`. Since `Gamma_p>0`, the coefficients involving `sqrt(Gamma_p)`, `C_1`, and `C_2` can be absorbed into a permitted constant multiplying `Gamma_p`. Thus every correction, including rounding and residual-budget loss, is bounded by

`C_inst (Gamma_p/M) x^(2e)`.

Finally,

`(Gamma_p/M) x^(2e)=Gamma_p M^(2e-1) L^e/T^e`.

For `p>=2`, this is `Gamma_p M^(1/3) L^(2/3)/T^(2/3)`. For `1<=p<2`, it is `Gamma_p M^(p/(2p+2)) L^((3p+2)/(4p+4))/T^((3p+2)/(4p+4))`. The exact leading term is `sqrt(2Gamma_p L_d/T)` in both cases. This proves the two asserted bounds uniformly in all feasible `T,delta`, with precisely the allowed constant dependencies.

## Source-Repair Accounting

The source's oracle denominator-index correction remains the previously recorded repair for theory_004. The integer implementation repair for theory_005 is made explicit by the minimum-two ceiling and the reserved observation per selected pair. The source-local arithmetic loss at L000386 is repaired by retaining the exact variance-mismatch term, rather than propagating its incorrect numerical simplification. The source's use of `tau<1` at L000412 is unnecessary: the full stability bound and the last section cover both sides of that threshold. These are local repairs within the original allocation-comparison and concentration proof architecture. There are no unresolved reference-proof obligations.
