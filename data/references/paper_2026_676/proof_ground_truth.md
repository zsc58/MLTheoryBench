# Reference Proof

## Contract and proof obligations

The functional scaling law is an explicit primitive assumption of this problem. No derivation of it from an SDE or a discrete sampling model is required or claimed. We must establish: (1) the intrinsic profile and its terminal exponent; (2) uniform two-sided convolution estimates in all three exponent regimes; (3) the final loss comparison; and (4) attainable optimal orders with matching lower bounds under the stability cap, including both equality boundaries.

All constants below may depend on the fixed profile, the fixed parameters, the stability cap, and the assumed FSL constants, but not on N or the admissible peak rate.

## 1. Intrinsic profile and terminal exponent

Write eta=eta_0, T=T_N, and define

`rho(x)=integral_0^x zeta(u)du`, `m=rho(1)`.

Then `Gamma_N(z)=eta N rho(z/N)` and `T=eta N m`. The cumulative function is continuous and nondecreasing. For `0<u<=m`, let `Q(u)=inf{x in [0,1]:rho(x)>=u}`, and set `Q(0)=0`. The public inverse definition gives

`phi_N(t)=eta bar_zeta(t/T)`, where `bar_zeta(y)=zeta(Q(my))`.

The profile is bounded between zero and one. These compositions are Lebesgue measurable: for a Borel representative of zeta the assertion follows from the monotonicity of Q. Changing that representative on a null set can change the composition only on its image under the Lipschitz function rho, which is again null. Choices at flat-clock levels affect at most countably many intrinsic times and do not change the convolution.

Choose `delta' in (delta,1)`. The positive lower tail bound implies `0<rho(delta')<m`. Set `a=rho(delta')/m`, so `0<a<1`. On `[delta',1]` the clock is strictly increasing, and integration of the two-sided tail bound gives

`c_- (1-x)^(gamma+1)/(gamma+1) <= m-rho(x) <= c_+ (1-x)^(gamma+1)/(gamma+1)`.

Consequently, for `y=rho(x)/m` in `[a,1]`,

`1-y asymp (1-x)^(gamma+1)`.

Putting `q=gamma/(gamma+1)` yields

`bar_zeta(y) asymp (1-y)^q`, for `a<=y<=1`.

In particular the intrinsic profile and its comparison constants are independent of N and eta. No positivity or monotonicity of the original profile before the terminal interval was used.

## 2. Convolution estimates

Put `p=2-1/beta`, so `1<p<2`, and write

`I_N=integral_0^T (1+T-t)^(-p) phi_N(t)dt`.

Split at `aT`, not at an arbitrary fraction that might precede the established intrinsic tail. On `[0,aT]`, boundedness of the profile gives

`0<=I_early<=C eta T^(1-p)`

for sufficiently large T. An early-region lower bound is unnecessary.

On `[aT,T]`, set `v=T-t`. The terminal estimate gives

`I_tail asymp eta T^(-q) J(T)`,

where

`J(T)=integral_0^((1-a)T) (1+v)^(-p) v^q dv`.

For sufficiently large T, the integral over `[0,1]` is a fixed positive finite constant. On `[1,(1-a)T]`, its integrand is comparable to `v^(q-p)`. Elementary integration therefore gives

- `J(T) asymp T^(1+q-p)` if `q-p>-1`;
- `J(T) asymp log T` if `q-p=-1`;
- `J(T) asymp 1` if `q-p<-1`.

Since `q-p+1=1/beta-1/(gamma+1)`, these cases correspond respectively to `beta<gamma+1`, `beta=gamma+1`, and `beta>gamma+1`.

In the first case the terminal contribution is comparable to `eta T^(1-p)`. In the second it is comparable to `eta T^(-q) log T`, with `q=p-1`. In the third it is comparable to `eta T^(-q)`, with `q<p-1`. Thus in every case the terminal contribution controls the early upper bound. Defining

`alpha=min{beta,gamma+1}`, `r=1-1/alpha`, `ell=1{beta=gamma+1}`,

we conclude

`I_N asymp eta T^(-r) (log T)^ell`.

These comparisons hold uniformly in eta whenever T exceeds a fixed threshold.

## 3. Loss scaling

By the assumed FSL and `(1+T)^(-s) asymp T^(-s)` for large T,

`E_N(eta) asymp T^(-s)+eta T^(-r)(log T)^ell`.

This proves the first target, including its uniformity along every admissible sequence.

## 4. Constrained optimal order

Let `d=1/alpha`, so `r=1-d` and `0<d<1`. Since `eta=T/(mN)`, the loss is uniformly comparable, for large T, to

`G_N(T)=T^(-s)+(mN)^(-1) T^d (log T)^ell`,

on `0<T<=m eta_max N`. All admissible sequences eventually lie in the range where this comparison holds.

### Hard regime: s<r

The upper bound on T gives `T^(-s)>=C N^(-s)`, proving a universal lower bound of that order. Choose any fixed peak in `(0,eta_max]`. Then `T asymp N`, and

`G_N(T) asymp N^(-s)+N^(-r)(log N)^ell asymp N^(-s)`

because `r-s>0`. Hence an order-one peak is order-optimal and `E_N^* asymp N^(-s)`. Conversely, achieving this order forces `T>=cN` by the signal lower bound, so an order-optimal peak is indeed of order one. No exact optimizer of an unspecified comparable loss is asserted.

### Easy regime without the logarithm: s>=r and ell=0

Set `H_N=N^(1/(s+d))`. Then `H_N^(s+d)=N` and

`N^(-1)H_N^d=H_N^(-s)`.

For any admissible T, if `T<=H_N`, the signal is at least `H_N^(-s)`. If `T>=H_N`, the noise is at least `m^(-1)H_N^(-s)`. This proves a uniform lower bound of order `H_N^(-s)`.

When `s>r`, `H_N/N` tends to zero, so choosing `T=H_N` is feasible for large N and attains the lower-bound order. When `s=r`, `H_N=N`; choose instead `T=kN` with a fixed `0<k<=m eta_max`. This has the same order and is feasible. Both choices diverge.

Thus

`eta_0^* asymp H_N/N = N^(-(s-1+1/alpha)/(s+1/alpha))`,

`E_N^* asymp H_N^(-s) = N^(-s alpha/(s alpha+1))`.

Equivalently, balancing in peak-rate coordinates gives the correctly signed equation

`eta_0^(s+1/alpha) asymp N^(r-s)`.

The signal and noise lower bounds also show that any order-optimal sequence in this regime has `T asymp H_N`.

### Easy regime with the logarithm: s>=r and ell=1

Set

`H_N=(N/log N)^(1/(s+d))`.

Then H_N tends to infinity and

`log H_N=(log N-log log N)/(s+d) asymp log N`.

Consequently

`N^(-1)H_N^d log H_N asymp H_N^(-s)`.

If `T<=H_N`, the signal gives the lower bound `H_N^(-s)`. If `T>=H_N`, monotonicity of `T^d log T` for `T>1` gives a noise lower bound of the same order. This argument does not replace log T by log N at arbitrary candidate rates.

Because `s+d>=1`, `H_N/N` tends to zero, including when `s=r`. Thus `T=H_N` is eventually feasible and attains the lower bound. Converting back to the peak rate gives

`eta_0^* asymp N^(-(s-1+1/alpha)/(s+1/alpha)) (log N)^(-1/(s+1/alpha))`,

`E_N^* asymp N^(-s alpha/(s alpha+1)) (log N)^(s alpha/(s alpha+1))`.

The corresponding correctly signed balance is

`eta_0^(s+1/alpha) log(m eta_0 N) asymp N^(r-s)`.

Finally, any order-optimal sequence must have `T>=cH_N` by the signal bound. For `T>=H_N`, its noise-to-candidate-noise ratio is at least `(T/H_N)^d`, so it also has `T<=CH_N`. Hence the displayed peak order is consistent with optimality, not just achievability.

## Source-local repairs incorporated

The proof uses the standing two-sided tail and a safely enlarged cutoff for theory_011; corrects the reversed exponent inequalities and cutoff notation in theory_012; and replaces the unsupported relative-error and exact-minimizer assertions in theory_013 with uniform order bounds. The two sign errors in the previous reference proof's balance equations were formalization errors, not errors in the source balance equations. All obligations of the public conditional theorem are closed.
