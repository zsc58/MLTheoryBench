# Reference Proof

## Proof Obligations and Audited Inputs

The theorem-critical obligations are: (1) identify the evolved density and the centered occupancy pairing for the stated L2 initial data; (2) justify decay at the actual supremum defining the local rate, including finiteness and endpoint attainment; (3) derive the sharp and relaxed deviation estimates and the multiplicative upper bound; (4) establish the conditional bounded-density ceiling and the minimum; and (5) obtain the lower bound on the local rate with the correct Langevin normalization and without differentiating an indicator.

The standard independent inputs are the spectral theorem for a self-adjoint operator and the strongly log-concave Poincare inequality. Their relevant statements and applications are given below. The Langevin transition-semigroup and Dirichlet-form facts are those of the supplied setup and source machinery. No conductance comparison, volume hypothesis, quadratic example, or nonstandard external dependency is used.

## 1. Density Evolution and Centered Pairing

Write `A=A_H`, `p=pi(A)`, and `phi=1_A-p`. Measurability of the alarm makes `A` measurable. Since `0<p<1`,

`||phi||_2^2=p(1-p)>0`, `integral phi d pi=0`.

Because `u_0` is a probability density and `chi_0^2<infinity`, it is nonnegative, has integral one, and satisfies

`||u_0||_2^2=1+chi_0^2`, `||u_0-1||_2^2=chi_0^2`.

Self-adjointness and preservation of constants give invariance of `pi`: for `f in L^2(pi)`,

`integral P_t f d pi = <P_t f,1>_pi = <f,P_t1>_pi = integral f d pi`.

As a transition semigroup, `P_t` satisfies `(P_t f)^2<=P_t(f^2)` for bounded real `f`. Integrating and using invariance proves L2 contractivity; truncation extends it to all of `L^2(pi)`.

For every bounded measurable `f`, the transition-semigroup property and self-adjointness give

`integral f d nu_t = integral u_0 P_t f d pi = <P_tu_0,f>_pi`.

Positivity and invariance show that `P_tu_0` is a nonnegative density of integral one. Thus, for every `t>=0`,

`nu_t << pi`, `u_t=P_tu_0` in `L^2(pi)`.

This argument does not require a classical density derivative at time zero. Preservation of constants and centering now yield

`nu_t(A)-p = <u_t-1,phi>_pi = <P_t(u_0-1),phi>_pi = <u_0-1,P_t phi>_pi`.

The last equality is precisely where reversibility places the semigroup on the fixed set's centered indicator.

## 2. The Local Rate Is Finite and Its Endpoint Is Attained

Let `B=-mathcal{L}` be the self-adjoint generator with sign reversed. L2 contractivity of its semigroup implies that `B` is nonnegative. The standard spectral theorem therefore supplies a finite positive scalar measure `mu_phi` on `[0,infinity)` such that

`mu_phi([0,infinity))=||phi||_2^2`,

`||P_t phi||_2^2=integral exp(-2s t) d mu_phi(s)`.

This statement applies to every L2 vector; membership in the generator or Dirichlet-form domain is not required. Here the measure is nonzero because `p(1-p)>0`.

Set `b=inf supp(mu_phi)`. A nonzero finite measure on `[0,infinity)` has nonempty support containing a finite point, so `0<=b<infinity`. Its mass is supported in `[b,infinity)`, and consequently

`||P_t phi||_2^2 <= exp(-2b t)||phi||_2^2`

for every `t>=0`. Hence `b` is admissible in the definition of `lambda_A`.

Conversely, let `r>b` and choose `c` with `b<c<r`. By the definition of the support infimum, `mu_phi([0,c])>0`. If `r` were admissible, then for every `t>=0`,

`mu_phi([0,c]) exp(-2c t) <= ||P_t phi||_2^2 <= ||phi||_2^2 exp(-2r t)`.

After multiplication by `exp(2c t)` and passage to `t -> infinity`, this would imply `mu_phi([0,c])=0`, a contradiction. Thus no `r>b` is admissible. We have proved

`lambda_A=b<infinity`,

`||P_t phi||_2 <= exp(-lambda_A t)||phi||_2` for every `t>=0`.

In particular, using the supremum itself is justified, including at time zero.

## 3. Deviation and Occupancy Bounds

Apply Cauchy-Schwarz to the pairing from Section 1 and the endpoint estimate from Section 2:

`|nu_t(A)-p| <= ||u_0-1||_2 ||P_t phi||_2 <= sqrt(chi_0^2) exp(-lambda_A t)||phi||_2`.

Direct computation gives

`||phi||_2^2=p(1-p)^2+(1-p)p^2=p(1-p)`.

Therefore

`|nu_t(A)-p| <= sqrt(chi_0^2 p(1-p)) exp(-lambda_A t) <= sqrt(chi_0^2 p) exp(-lambda_A t)`.

The relaxed upper side is

`nu_t(A) <= p+sqrt(chi_0^2 p) exp(-lambda_A t)`.

Since `p>0`, this is algebraically equivalent to

`nu_t(A) <= p[1+sqrt(chi_0^2/p) exp(-lambda_A t)]`.

The multiplicative expression rewrites this relaxed one-sided upper bound; it is a consequence, not a converse, of the sharper absolute-deviation estimate.

## 4. The Bounded-Density Ceiling

If `M=||u_0||_infinity<infinity`, then `0<=u_0<=M` almost everywhere. Applying positivity preservation to both `u_0` and `M1-u_0`, and using `P_t1=1`, gives

`0<=u_t=P_tu_0<=M` almost everywhere.

Thus

`nu_t(A)=integral_A u_t d pi<=Mp`.

Intersecting this upper bound with the relaxed upper bound in Section 3 proves

`nu_t(A)<=min{Mp,p+sqrt(chi_0^2 p) exp(-lambda_A t)}`

for every `t>=0`.

## 5. Strong Convexity Gives the Rate Lower Bound

The standard strongly log-concave Poincare inequality states: if a probability measure has density proportional to `exp(-V)`, with `V` twice continuously differentiable and `nabla^2 V>=rho I` for `rho>0`, then

`Var(f)<=rho^{-1} integral |nabla f|^2 d pi`

for functions in the weighted Sobolev form domain.

Here `V=2J/sigma^2` and `rho=2m/sigma^2`. The hypotheses hold because `J` is C2, `sigma>0`, `m>0`, the Hessian lower bound holds everywhere, and `pi` is the specified probability measure.

For compactly supported smooth `f`, integration by parts using `nabla pi=-(2/sigma^2)pi nabla J` gives the Langevin Dirichlet form

`E(f)=-<f,mathcal{L}f>_pi=(sigma^2/2) integral |nabla f|^2 d pi`.

For the Langevin realization this extends by closure to its form domain, where `E(f)=||B^{1/2}f||_2^2`. The Poincare inequality therefore becomes

`Var_pi(f)<=m^{-1} E(f)`.

This verifies the normalization: the semigroup rate is `m`, not `2m/sigma^2`.

The centered subspace reduces the semigroup and its spectral projections because constants are fixed and the operators are self-adjoint. On centered form-domain vectors the preceding inequality says

`E(f)>=m||f||_2^2`.

To see its spectral consequence, suppose the restriction of `B` to the centered subspace had a nonzero spectral projection on `[0,c]` for some `c<m`. A nonzero vector in that range belongs to the form domain and would satisfy both `E(f)<=c||f||_2^2` and `E(f)>=m||f||_2^2`, a contradiction. Taking the union over `c<m` excludes all centered spectral mass below `m`.

Since `phi` is centered, `supp(mu_phi)` is contained in `[m,infinity)`. Section 2 then gives

`lambda_A=inf supp(mu_phi)>=m`.

No Dirichlet energy of the indicator itself has been used.

## Endpoint Alternative and Boundary Checks

A valid alternative to Section 2 uses the public supremum definition directly. L2 contractivity makes rate zero admissible. Strong continuity at zero and `phi!=0` give a time `s>0` with `||P_s phi||_2>0`. Every admissible rate `r` then satisfies

`r <= s^{-1} log(||phi||_2/||P_s phi||_2)`.

Thus the supremum is finite. Taking a sequence of admissible rates tending to that supremum and passing to the limit in the defining inequality for each fixed `t>=0` establishes decay at `lambda_A`. This proves the needed endpoint estimate without requiring a spectral-measure construction; the rate lower bound still follows from the audited Poincare consequence.

All displayed bounds include `t=0`. If `chi_0^2=0`, then `u_0=1` almost everywhere and invariance gives `nu_t=pi`, so the deviation bounds hold with zero right-hand side. If `M=1`, normalization and `0<=u_0<=1` likewise force stationarity. Infinite `M` does not affect the unconditional bounds. The cases `p=0` and `p=1` are excluded exactly as in the task and source local-rate definition. No additional restriction on the measurable boundary of `A` is needed.

All five theorem-critical obligations are closed. There is no unresolved private proof dependency.
