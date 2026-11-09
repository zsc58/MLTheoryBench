# Reference Proof

## Proof Structure

Use a fixed cutoff to construct a globally smooth lower-bounded objective whose derivative equals `mu` on a right half-line. Choose independent, mean-zero two-point noise. Bound the exponentially weighted noise numerator using a precise martingale moment inequality. A recent negative outlier supplies a lower bound for the squared-gradient accumulator, while weighted Cauchy-Schwarz bounds every normalized update. Combine these estimates without assuming independence between the numerator and the recent-outlier event. Finally, use the deterministic nonnegative schedule and Markov's inequality to obtain the claimed expected stationarity bound.

The construction below works with the universal choices

`c=1/4`, `c_0=1`, `C_K=2`, and `C_p=8 exp(5/2)`.

In particular, the constant denoted by `C_p` can be chosen uniformly over `p in (1,2)`.

## Step 1: Objective and quantitative scales

Define a continuously differentiable cutoff `h:R->[0,1]` as follows. It is zero for `z<=-1`, one for `z>=-1/2`, and on `-1<z<-1/2` it equals

`h(z)=3r^2-2r^3`, where `r=2z+2`.

The values and first derivatives match at both endpoints. In the transition interval,

`h'(z)=12r(1-r)`,

so `sup_z |h'(z)|=3`. A continuously differentiable cutoff is sufficient because the required objective is `C^2`.

Set

`F(y)=mu R integral_(-infinity)^(y/R) h(z) dz`.

This integral is finite at every finite `y`, and `F` is nonnegative and zero for `y<=-R`. Moreover,

`F'(y)=mu h(y/R)`, `F''(y)=(mu/R)h'(y/R)`.

Thus `F` is `C^2`, lower bounded, and satisfies `0<=F'<=mu`, with `F'(y)=mu` whenever `y>=-R/2`. Its global smoothness is

`L=3mu/R`.

The integral of `h` over `[-1,-1/2]` is `1/4`, and its integral over `[-1/2,0]` is `1/2`. Therefore

`Delta=F(0)-inf F=(3/4)mu R`,

and

`Delta L=(9/4)mu^2`.

These identities establish every requested two-sided comparison. The bounded second derivative also gives the source's global one-dimensional clean smoothness condition.

## Step 2: Oracle, information timing, and moments

With `q=rho_2 log(1/delta)` and `M=sigma q^(-1/p)`, take independent draws at each time with

`xi_t=-M` with probability `q`,

`xi_t=qM/(1-q)` with probability `1-q`.

The assumptions imply `0<q<=1/2`, so this law is well defined. It is independent of the prescribed step-size sequence and of the past. Since `y_t` is measurable with respect to `H_(t-1)`, the oracle `g_t=F'(y_t)+xi_t` is conditionally unbiased:

`E[xi_t | H_(t-1)]=-qM+(1-q)qM/(1-q)=0`.

Also,

`E[|xi_t|^p | H_(t-1)] = qM^p + q^p M^p/(1-q)^(p-1)`

`= sigma^p [1+(q/(1-q))^(p-1)] <= 2sigma^p`.

This is a valid one-sample instance of the source's clean conditional moment model. No infinite-variance requirement is present. The function and this noise law do not depend on the horizon.

## Step 3: Exponential numerator and its moment estimate

Expanding the recursions gives

`a_t=rho_1 sum_(s=1)^t beta_1^(t-s)g_s`,

`b_t=rho_2 sum_(s=1)^t beta_2^(t-s)g_s^2`.

A weight with exponent zero is one, including when `beta_1=0`.

Write `a_t=S_t+N_t`, where

`S_t=rho_1 sum_(s=1)^t beta_1^(t-s)F'(y_s)`,

`N_t=rho_1 sum_(s=1)^t beta_1^(t-s)xi_s`.

Although `S_t` is random, its bound is pathwise. The nonnegative weights and `0<=F'<=mu` give

`0<=S_t<=mu rho_1 sum_(j=0)^(t-1) beta_1^j=mu(1-beta_1^t)<=mu`.

We use the following precise standard martingale moment inequality: if `X_1,...,X_n` are real martingale differences with finite `p`-th moments, where `1<p<2`, then

`E|sum_(j=1)^n X_j|^p <= 2 sum_(j=1)^n E|X_j|^p`.

For completeness, this bound follows from an elementary scalar estimate. For `r=p-1 in (0,1)`, the function `phi(x)=sign(x)|x|^r`, with `phi(0)=0`, satisfies

`|phi(x)-phi(y)|<=2^(1-r)|x-y|^r`.

For arguments of the same sign, this follows from subadditivity of the power `r`; for opposite signs it follows from concavity applied to their two absolute values. Integrating the derivative of `|x|^p` along the segment from `x` to `x+y` consequently gives

`|x+y|^p <= |x|^p + p sign(x)|x|^(p-1)y + 2|y|^p`.

Apply this estimate to a partial sum and the next martingale difference. The linear term has expectation zero by conditioning on the preceding history. Its integrability follows from the finite `p`-th moments. Iteration proves the displayed moment inequality.

For each fixed `t`, the variables `rho_1 beta_1^(t-s)xi_s`, indexed by `s=1,...,t`, are martingale differences with respect to `H_s`, because the coefficients are deterministic and the noises have conditional mean zero. All required moments are finite. Therefore

`E|N_t|^p <= 4sigma^p rho_1^p sum_(j=0)^(t-1) beta_1^(pj)`.

For `0<=beta_1<1`, one has `beta_1^p<=beta_1`, and hence

`rho_1^p sum_(j=0)^(t-1) beta_1^(pj) <= rho_1^p/(1-beta_1^p) <= rho_1^(p-1)`.

Taking the `p`-th root and using the elementary comparison of first and `p`-th moments yields

`E|N_t| <= 4^(1/p)sigma rho_1^((p-1)/p) <= 4sigma rho_1^((p-1)/p)`.

Consequently,

`E|a_t|<=mu+4sigma rho_1^((p-1)/p)`.

## Step 4: Normalized updates and the recent-outlier event

Define `u_t=a_t/sqrt(b_t)`, with the stated zero-over-zero convention, and `u_t^+=max(u_t,0)`.

Weighted Cauchy-Schwarz applied to the exponential representations gives

`a_t^2 <= rho_1^2 [sum_(s=1)^t (beta_1^2/beta_2)^(t-s)] [sum_(s=1)^t beta_2^(t-s)g_s^2]`

`<= [rho_1^2/(rho_2(1-beta_1^2/beta_2))] b_t = C_beta^2 b_t`.

The weights involving `beta_2` are positive, and the geometric ratio is less than one by assumption. If `b_t=0`, its positive-weight representation implies that all gradients through time `t` vanish, so `a_t=0` as well. Thus the convention is sufficient and

`|u_t|<=C_beta`

holds on every trajectory. In particular, for every finite time the iterates are finite and the displacements used below are integrable.

Let `K=ceil(2/rho_2)`. For `t>K`, let `A_t` be the event that at least one of `xi_(t-K+1),...,xi_t` equals `-M`. Independence of the noise draws gives

`P(A_t^c)=(1-q)^K<=exp(-qK)<=delta^2<=delta`,

since `qK>=2 log(1/delta)`.

For `0<rho_2<=1/2`, integration of `1/(1-r)` over `[0,rho_2]` gives `log(1-rho_2)>=-2rho_2`. Also `rho_2 K<=2+rho_2<=5/2`. Therefore

`beta_2^K=(1-rho_2)^K>=exp(-5)`.

On `A_t`, choose an outlier time `s` in the stated window. The bound `F'(y_s)<=mu` and the assumption `M>=2mu` imply

`|g_s|=|F'(y_s)-M|>=M/2`.

Since `0<=t-s<=K-1`, its contribution to the accumulator yields

`b_t>=rho_2 beta_2^(t-s)g_s^2>=exp(-5)rho_2 M^2/4`.

No independence between `a_t` and `A_t` is needed. Split the expectation over `A_t` and its complement, use the preceding deterministic denominator bound on `A_t`, and use `|u_t|<=C_beta` on the complement:

`E[u_t^+]<=E|u_t|`

`<= [2exp(5/2)/(sqrt(rho_2)M)] E|a_t| + C_beta P(A_t^c)`

`<= 2exp(5/2)(mu/sigma+4rho_1^((p-1)/p)) rho_2^(-1/2)q^(1/p) + C_beta delta`.

Substituting `q=rho_2 log(1/delta)` and using `1/p-1/2=(2-p)/(2p)` proves

`E[u_t^+] <= C_p(mu/sigma+rho_1^((p-1)/p)) rho_2^((2-p)/(2p))(log(1/delta))^(1/p)+C_beta delta`

with `C_p=8exp(5/2)`. For `t<=K`, the deterministic bound gives `E[u_t^+]<=C_beta`.

## Step 5: Displacement and stationarity

Fix any integer `T>K` for which the public displacement condition holds. Define

`D_T=sum_(s=1)^T alpha_s E[u_s^+]`.

The estimates from Step 4 and the public condition, with `c=1/4`, imply exactly

`D_T<=R/4`.

For every `t<=T`, the iteration and `y_1=0` give

`(-y_t)_+ = (sum_(s<t) alpha_s u_s)_+ <= sum_(s<t) alpha_s u_s^+`.

Here nonnegativity of the step sizes is essential. Because they are deterministic, taking expectations gives

`E[(-y_t)_+]<=sum_(s<t) alpha_s E[u_s^+]<=D_T`.

Markov's inequality, applied to the nonnegative integrable variable `(-y_t)_+`, now gives

`P(y_t<-R/2)<=2E[(-y_t)_+]/R<=1/2`.

On the complementary event `F'(y_t)=mu`. Consequently

`E|F'(y_t)|>=mu P(y_t>=-R/2)>=mu/2`.

Averaging over `t=1,...,T` proves the desired inequality. The argument applies to every admissible horizon using the same function and oracle, and Step 1 already establishes the simultaneous smoothness and initial-gap comparisons.

## Closure Check

All theorem-critical obligations are closed: objective construction and scales; oracle independence, unbiasedness and moments; the exponential representations and zero-denominator case; the uniformly bounded martingale moment estimate; compatible window and probability constants; the dependent numerator/event decomposition; and the deterministic nonnegative-schedule displacement argument. There is no unresolved specialized dependency.
