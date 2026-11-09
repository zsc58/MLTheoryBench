# Reference Proof

## Proof Structure and Obligations

1. Recover every projected distribution from equality of kinked-activation expectations using only admissible shifts, including support endpoints and atoms.
2. Deduce equality of the original probability measures from characteristic-function uniqueness.
3. Verify finiteness and measurability of the empirical suprema and derive an explicit product-cover bound with controlled dimension dependence.
4. Bound the expectation of the centered empirical-process supremum by ghost-sample symmetrization and an audited entropy bound, then apply bounded differences to that centered supremum.
5. Use separation and the deterministic vanishing threshold to establish the quantitative fixed-alternative power statement, with the stated constant dependencies.

All five obligations are closed below. No specialized paper-specific external theorem is assumed.

## Complete Proof

Write Rf=\int f\,dR. All functions and norms in this proof are restricted to B^d. In the public slope regime, \Lambda=1; retaining \Lambda in envelope and sensitivity bounds reproduces the requested tail constant.

### 1. Separation through projections

Choose \ell_*=\ell_{\min}<1. If D(P,Q)=0, then for every unit vector \theta and every t\in[-1,1],
\[
\mathbb E\phi_{\ell_*}(\theta^\top X-t)=\mathbb E\phi_{\ell_*}(\theta^\top Y-t).
\]
Fix \theta and write U=\theta^\top X and V=\theta^\top Y. Both are supported on [-1,1]. Let t\in(-1,1) be a common continuity point of their distribution functions, and choose 0<\delta<t+1. Both shifts -t and -t+\delta then belong to [-1,1]. Define
\[
r_{\delta,t}(u)=\frac{\phi_{\ell_*}(u-t+\delta)-\phi_{\ell_*}(u-t)-\ell_*\delta}{(1-\ell_*)\delta}.
\]
Direct evaluation gives
\[
r_{\delta,t}(u)=
\begin{cases}
0,&u\le t-\delta,\\
1+(u-t)/\delta,&t-\delta<u\le t,\\
1,&u>t.
\end{cases}
\]
Thus
\[
0\le\mathbb E r_{\delta,t}(U)-\Pr(U>t)\le\Pr(t-\delta<U\le t),
\]
and the analogous bound holds for V. Equality of the two discriminator expectations at both admissible shifts implies \mathbb E r_{\delta,t}(U)=\mathbb E r_{\delta,t}(V). The two right-hand bounds tend to zero at a common continuity point, proving \Pr(U\le t)=\Pr(V\le t).

A probability distribution has at most countably many atoms: for each positive integer k it has only finitely many atoms of mass at least 1/k. Therefore, for every t\in[-1,1), there is a decreasing sequence of common continuity points in (-1,1) tending to t. Right-continuity proves CDF equality there, including at -1. At t\ge1 both CDFs equal one, and at t<-1 both equal zero. Hence U and V have the same distribution for every unit \theta.

We use the standard independent uniqueness theorem for characteristic functions: two Borel probability measures on \mathbb R^d with equal functions a\mapsto\int e^{ia^\top z}\,dR(z) are equal. Its hypotheses hold here. For a\ne0, put \theta=a/\|a\|_2; equality of the projected laws gives equality of the characteristic functions at a, and at a=0 both equal one. Thus P=Q. Conversely, P=Q immediately gives D(P,Q)=0.

### 2. Envelope, parameter covers, and measurability

For z\in B^d, |\theta^\top z+\mu|\le2, and consequently |f(z)|\le2\Lambda. For slopes in [-1,1], the activation is 1-Lipschitz in its argument and
\[
\|f_{\theta,\mu,\ell}-f_{\theta',\mu',\ell'}\|_\infty
\le\|\theta-\theta'\|_2+|\mu-\mu'|+2|\ell-\ell'|.
\]
For any r>0, a maximal r-separated subset of the unit sphere is an r-net with at most (1+2/r)^d points. Indeed, the disjoint open balls of radius r/2 around its points lie in the ball of radius 1+r/2, and comparison of volumes gives this bound. The same one-dimensional argument bounds an r-net of any interval of length at most two by 1+2/r. These statements also cover d=1 and singleton slope intervals.

Taking r=u/4 in all three parameter coordinates gives
\[
N(u,\mathcal F,\|\cdot\|_\infty)\le(1+8/u)^{d+2},\qquad u>0.
\]
The parameter space is compact and has a countable dense subset. The parameter Lipschitz inequality shows that every empirical or population expectation appearing here is continuous in the parameters. Every supremum can therefore be taken over that fixed countable subset. The random suprema are measurable and bounded, so their expectations and all subsequent conditional expectations are well defined.

### 3. The centered empirical-process expectation

Define
\[
S_{n,m}=\sup_{f\in\mathcal F}|(P-\widehat P_n)f-(Q-\widehat Q_m)f|.
\]
The inequality between differences of suprema and suprema of differences gives
\[
|\widehat D_{n,m}-D(P,Q)|\le S_{n,m}.
\]
This is the centered quantity whose expectation vanishes; the empirical IPM itself need not have a vanishing expectation under an alternative.

For a deterministic sample z_1,\ldots,z_k, let
\[
\|h\|_{2,z}=\left(k^{-1}\sum_{i=1}^k h(z_i)^2\right)^{1/2},\qquad
\widehat R_k(\mathcal H;z)=\mathbb E_\sigma\sup_{h\in\mathcal H}k^{-1}\sum_{i=1}^k\sigma_i h(z_i),
\]
where the \sigma_i are independent uniform signs. Take \mathcal H=\{0\}\cup\mathcal F\cup(-\mathcal F). This converts the signed supremum exactly into the absolute Rademacher supremum for \mathcal F. Moreover,
\[
N(u,\mathcal H,\|\cdot\|_{2,z})\le3(1+8/u)^{d+2},\qquad
\sup_{h\in\mathcal H}\|h\|_{2,z}\le2.
\]

The standard independent entropy inequality used here is the following conservative form of the source's Dudley bound: for a separable class containing zero, with empirical L2 norm bounded by b, there is a universal constant K such that
\[
\widehat R_k(\mathcal H;z)\le\frac K{\sqrt k}\int_0^{2b}\sqrt{\log N(u,\mathcal H,\|\cdot\|_{2,z})}\,du
\]
when the integral is finite. One may obtain this form from the source's truncated formulation by choosing its envelope parameter c=4b and sending the truncation to zero. The class is separable by the preceding continuity argument, contains zero by construction, and satisfies the envelope condition with b=2.

Let
\[
J=\int_0^4\sqrt{\log(1+8/u)}\,du.
\]
This is a finite numerical constant: on (0,4], 1+8/u\le12/u, and substitution u=4e^{-v} bounds J by
\[
4\int_0^\infty e^{-v}\sqrt{\log3+v}\,dv
\le4\int_0^\infty e^{-v}(\sqrt{\log3}+1+v)\,dv<\infty.
\]
It follows that, uniformly over the sample,
\[
\widehat R_k(\mathcal H;z)
\le\frac K{\sqrt k}\left(4\sqrt{\log3}+\sqrt{d+2}\,J\right)
\le A\sqrt{d/k}
\]
for a universal positive constant A, since d\ge1.

For completeness, symmetrization is derived rather than merely cited. For i.i.d. Z_1,\ldots,Z_k with law R, let Z'_1,\ldots,Z'_k be an independent copy. Conditional Jensen's inequality and then independent swaps of each pair give
\[
\begin{aligned}
\mathbb E\sup_f|(R-\widehat R_k)f|
&\le\mathbb E\sup_f\left|k^{-1}\sum_i(f(Z'_i)-f(Z_i))\right|\\
&=\mathbb E\sup_f\left|k^{-1}\sum_i\sigma_i(f(Z'_i)-f(Z_i))\right|\\
&\le2\mathbb E_Z\widehat R_k(\mathcal H;Z)
\le2A\sqrt{d/k}.
\end{aligned}
\]
The equality uses the identical independent distributions within each pair. The triangle inequality and the same bound for the P and Q samples now imply
\[
\mathbb E S_{n,m}\le2A\sqrt d\left(n^{-1/2}+m^{-1/2}\right).
\]
Choose c_d=2A\sqrt d. In particular,
\[
\mathbb E|\widehat D_{n,m}-D(P,Q)|\le c_d\left(n^{-1/2}+m^{-1/2}\right).
\]

### 4. Concentration

Replacing one X observation changes S_{n,m} by at most 4\Lambda/n, and replacing one Y observation changes it by at most 4\Lambda/m, using the envelope and the inequality for differences of suprema.

The standard independent bounded-differences inequality states that a measurable function W of independent inputs, with coordinate sensitivities a_i, satisfies
\[
\Pr\{|W-\mathbb EW|\ge\varepsilon\}\le2\exp\left(-2\varepsilon^2/\sum_i a_i^2\right).
\]
All hypotheses were verified above and in the sampling assumptions. Here the sum of squared sensitivities is 16\Lambda^2(1/n+1/m). Consequently,
\[
\Pr\{S_{n,m}-\mathbb ES_{n,m}>\varepsilon\}
\le2\exp\left(-\frac{\varepsilon^2nm}{8\Lambda^2(n+m)}\right).
\]
Combining this with the expectation bound and |\widehat D_{n,m}-D(P,Q)|\le S_{n,m} proves the stated uniform estimation inequality for every positive integer n,m and every \varepsilon>0.

### 5. Fixed-alternative power and constants

Fix P\ne Q and put \Delta=D(P,Q)>0. Since the threshold is a deterministic sequence tending to zero, eventually \eta_{\alpha,n}\le\Delta/2. On the event T_n=0,
\[
|\widehat D_{n,n}-\Delta|>\Delta/2.
\]
Markov's inequality and the expectation bound therefore give the source's quantitative estimate
\[
\Pr(T_n=0)\le\frac{4c_d}{\Delta\sqrt n}
\]
for all sufficiently large n. For the fixed discriminator class this already proves the power rate and convergence.

The public statement lists P,Q,d, but not the slope interval, as possible dependencies of c_3. This causes no problem: the estimation tail permits a universal choice of c_3, with the onset allowed to depend on the fixed interval and threshold sequence. Indeed, increase the onset so that 2c_d/\sqrt n\le\Delta/4. Applying the estimation bound with \varepsilon=\Delta/4 and \Lambda=1 gives
\[
\Pr(T_n=0)\le2\exp(-n\Delta^2/256).
\]
For each fixed \Delta>0, this is at most n^{-1/2} for all sufficiently large n. Thus c_3=1 is admissible, in particular satisfying the stated dependency restriction, and \Pr(T_n=1)\to1. Negative or zero thresholds cause no difficulty: the same event inclusion holds, and a nonpositive threshold simply makes the nonrejection event empty.
