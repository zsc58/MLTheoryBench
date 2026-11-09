# Reference Proof

## Audit Status

This reference derives the statistical, likelihood, gradient, optimization, and computational sampling steps below. In particular, Section 8 supplies the interval-truncated Gaussian implementation that revision 1 left open. No specialized cited theorem is treated as closing a proof obligation merely by name. Computational costs use the source's real-valued model, including elementary real-function evaluation and internal continuous randomization; no bit-complexity assertion for unspecified encodings of arbitrary real samples is added.

## 1. Contract and Basic Bounds

The observed joint law is the original independent pair `(X,xi)` conditioned on `Y=<w*,X>+xi` belonging to `S*`. Write

\[
a=\mathbb E_D p_*(X)\ge\alpha,\qquad p_T(x)=\Pr\{N(\langle w^*,x\rangle,1)\in T\},\qquad p_*=p_{S^*}.
\]

All feature expectations below that are labeled `obs` use the observed feature law, not `D`. In particular,

\[
\mathbb E_{\rm obs} f(X)=a^{-1}\mathbb E_D[p_*(X)f(X)],\qquad \mathbb E_{\rm obs}f\le\alpha^{-1}\mathbb E_Df\quad(f\ge0).
\]

Consequently, with

\[
H=d\Lambda^2/\alpha,
\]

we have `E_obs ||X||^2<=H`, and `E_obs <u,X>^4<=M^4||u||^4/alpha`. These conditioning factors must not be omitted.

Bounds smaller than one may be padded to one for resource estimates. If `R_w=0`, return zero. In the remaining argument let

\[
\Gamma=1+\sigma+\beta+\Lambda+M+\rho^{-1}+\alpha^{-1}.
\]

Every occurrence of a polynomial in `Gamma` means a universal polynomial, independent of the unknown distribution and survival set.

The standard independent probabilistic facts used below are the following. A scalar random variable with psi_2 norm at most `K` has tail at most `2 exp(-c t^2/K^2)`. Products of variables with psi_2 bounds `K_1,K_2` have psi_1 norm at most `K_1 K_2`, without requiring independence. A sample mean of iid centered psi_1 variables of norm at most `K` has deviation probability at most `2 exp[-c n min(t^2/K^2,t/K)]`. Applying this bound to coordinates or to a fixed finite sphere net gives vector-mean and second-moment-matrix concentration with polynomial sample bounds. The interval uniform-convergence fact used in Section 4 is stated there. All applications use fresh iid batches, and the corresponding scalar variables have the bounds established next.

For a unit projection, conditioning gives

\[
\mathbb E_{\rm obs}\exp\{\langle u,X-\mathbb E_DX\rangle^2/\sigma^2\}\le2/\alpha
\]

when `sigma>0`; a zero centered projection is handled directly. Jensen rescaling and adding the bounded mean give the uncentered projection bound

\[
\|\langle u,X\rangle\|_{\psi_2,\rm obs}\le K_x,
\qquad K_x=C(1+\sigma+\beta)\sqrt{\log(e/\alpha)}.
\]

The same conditioning argument applied to the original Gaussian noise gives an observed residual bound `K_xi=C sqrt(log(e/alpha))`. Thus

\[
\|Y\|_{\psi_2,\rm obs}\le K_y=R_wK_x+K_\xi,
\qquad W:=\mathbb E_{\rm obs}\|YX\|^2\le C dK_y^2K_x^2.
\]

These estimates include `alpha=1`; a factor `sqrt(log(1/alpha))` without an additive constant would not.

Two Gaussian estimates needed below have elementary proofs. If two unit-variance Gaussian means differ by `b`, Cauchy-Schwarz applied to their likelihood ratio gives

\[
p_\mu(T)\ge p_\nu(T)^2e^{-(\mu-\nu)^2}.
\]

Also, conditioning a Gaussian on a set of Gaussian mass `p>0` gives a density bounded by `L_0=1/(p sqrt(2pi))`. Any density bounded by `L_0` has at least half its mass at distance at least `1/(4L_0)` from its mean. Its variance is therefore at least `1/(32L_0^2)`, and in particular at least `p^2/12`. Gaussian conditional moments are finite, so the mean and variance used here exist.

## 2. Warm Start and Projection

Use an independent observed batch to compute empirical OLS, declaring failure if its empirical second moment is singular. Set

\[
\Sigma=\mathbb E_{\rm obs}XX^\top,\qquad b=\mathbb E_{\rm obs}[(Y-\langle w^*,X\rangle)X].
\]

For each unit vector `u`, independence before conditioning and Cauchy-Schwarz imply

\[
|u^\top b|\le\alpha^{-1}\mathbb E|\xi\langle u,X\rangle|\le\Lambda/\alpha.
\]

Hence `||b||<=Lambda/alpha`. Let `Sigma_hat` and `b_hat` be the analogous empirical quantities. Although `b_hat` is not computed using knowledge of `w*`, the empirical identity

\[
\widetilde w-w^*=\widehat\Sigma^{-1}\widehat b
\]

holds exactly for the computable OLS estimator. The residual-projection products have psi_1 norm at most `K_xi K_x`; squared feature projections have psi_1 norm at most `K_x^2`. The concentration facts in Section 1, a coordinate union bound for `b_hat`, and a fixed sphere-net bound for `Sigma_hat` therefore give, with a polynomial number of samples and failure probability at most `eta`,

\[
\widehat\Sigma\succeq\rho^2I/2,\qquad \|\widehat b-b\|\le\Lambda/\alpha.
\]

On this event `||w_tilde-w*||<=4Lambda/(rho^2 alpha)`. Define

\[
K=B(\widetilde w,6\Lambda/(\rho^2\alpha)),\qquad h=12\Lambda/(\rho^2\alpha).
\]

Then `w* in K`, every `w in K` satisfies `||w-w*||<=h`, and `K` is a computable closed convex ball. The displacement bound is its diameter. The inverse-matrix estimate used here is `||Sigma_hat^{-1}||<=2/rho^2`, not the reciprocal of the largest eigenvalue of `Sigma_hat`.

## 3. Smooth Reference Responses

For any `w`, let `F_w` be the law obtained by drawing `X~D_obs` and then an independent untruncated response `Z~N(<w,X>,1)`. Let `F=F_{w*}`. Reference samples from `F_wtilde` are available by discarding the response of a fresh observed pair and generating a new Gaussian response.

Here is the smoothness calculation, including its endpoint constants. Let `v=w-w*`, `||v||<=h`, and let `a_T=F(T)>0`. The Gaussian comparison gives

\[
F_w(T)\ge\mathbb E_{\rm obs}[p_T(X)^2e^{-\langle v,X\rangle^2}].
\]

The projection tail bound permits a cutoff `t=C h K_x sqrt(log(C/a_T))` for which `Pr_obs(|<v,X>|>t)<=a_T^2/2`. Jensen gives `E_obs p_T^2>=a_T^2`; hence

\[
F_w(T)\ge\tfrac12a_T^2e^{-t^2}\ge c e^{-Ch^2K_x^2}a_T^{2+Ch^2K_x^2}.
\]

Taking a root shows

\[
F(T)\le s^{-1}F_w(T)^{1/q}
\]

for an absolute `s>0` and `q=C(1+h^2K_x^2)>=1`. Zero target mass is immediate. This uses the same bounded-shift argument as the source, with the additive constant retained.

## 4. Learning the Set with the Actual Positive Experiment

Let `Q` denote the response marginal of an actual observed pair. It is generally false that `Q=F conditioned on S*`. The feature law in `F` has already been reweighted by survival.

What is true, and sufficient, is that for every measurable `A subset S*`,

\[
F(A)=a^{-1}\mathbb E_D[p_*(X)p_A(X)]\le a^{-1}\mathbb E_Dp_A(X)=Q(A).
\]

Also `Q(S*)=1`.

We give the direct interval argument so that no unproved positive-only theorem is invoked. The standard independent interval uniform-convergence facts used here are: unions of at most `J` real intervals have VC dimension `2J`; iid samples give uniform absolute probability error at most `u` with `O((J log(1/u)+log(1/eta))/u^2)` samples, up to harmless logarithms; and a sample-consistent member of such a class has probability at most `u` with `O((J log(1/u)+log(1/eta))/u)` samples. The latter assertion applies to a class of missed sets with zero empirical mass. These follow by counting interval endpoint patterns on an ordered sample, symmetrization, and the scalar binomial bounds. They require only iid sampling, measurability, and finite interval complexity, all present here.

Fix desired pre-clipping error `tau/2`. Put `gamma=(s tau/4)^q`, and take `r=ceil(2(k-1)/gamma)` when `k>1`, with `r=0` for `k=1`. Draw independent positive responses from `Q` and reference responses from `F_wtilde`. Sort positives, form their consecutive gaps, and delete the `r` gaps containing the largest reference counts. Use sufficiently many positives that their number exceeds `r+1`. Return the remaining part of the positive-sample hull, retaining endpoints. Gaussian response marginals are continuous, so endpoint choices have zero population mass.

Call this set `S'`. It contains every positive sample and has at most `r+1` intervals. The missed set `S*\S'` belongs to a class of unions of at most `k+r+1` intervals. Positive-sample consistency and the interval bound give `Q(S*\S')<=tau/4`, and therefore `F(S*\S')<=tau/4` by domination.

For false positives, every part of the hull outside `S*` lies in a positive-sample gap crossing a true negative component. There are at most `k-1` such gaps. Any gap that remains after deletion has empirical reference mass at most `1/(r+1)`, because at least `r` deleted gaps have counts no smaller than its own. Thus the union of retained crossing gaps has empirical reference mass at most `(k-1)/(r+1)<=gamma/2`. Uniform convergence for unions of at most `k-1` intervals bounds its true reference mass by `gamma`. Smoothness then gives

\[
F(S'\setminus S^*)\le s^{-1}\gamma^{1/q}\le\tau/4.
\]

For `k=1`, the positive-sample hull is contained in the true interval and the false-positive term vanishes. These arguments establish `F(S' triangle S*)<=tau/2`.

Up to logarithms, `O(gamma^{-2}(k+log(1/eta)))` samples suffice: the positive-consistency requirement is of order `(k+r)/tau`, which is dominated by this bound because `gamma<=tau`. Sorting gives polynomial time and the interval count is polynomial in `k,tau^{-1}` with exponent polynomial in `Gamma`.

For bounded support, the response generated under `F` has psi_2 norm at most `C(1+R_w)K_x`. Choose the known radius

\[
L=R_{\rm set}=C(1+R_w)K_x\sqrt{\log(C/\tau)}
\]

so that `F([-L,L]^c)<=tau/2`, and return `S=S' intersect [-L,L]`. The inclusion

\[
((S'\cap[-L,L])\triangle S^*)\subseteq(S'\triangle S^*)\cup[-L,L]^c
\]

proves `E_obs p_(S triangle S*)<=tau`. The output remains a polynomial-size explicitly represented interval union. This step uses no membership access to `S*`.

## 5. Objective, Domain, and Curvature

Assume from now on that preprocessing succeeded. Choose `tau<alpha/2`. Since

\[
\mathbb E_{\rm obs}p_* =\mathbb E_Dp_*^2/a\ge a\ge\alpha,
\]

we have `F(S intersect S*)>=alpha-tau>0`. Consequently `S intersect S*` has positive Lebesgue measure. Every unit-variance Gaussian assigns positive mass to it and to `S`. Thus all conditional distributions in

\[
L_S(w)=-\mathbb E_{X\sim D_{\rm obs}}\mathbb E_{Y\sim N(\langle w^*,X\rangle,1,S\cap S^*)}\log N(Y;\langle w,X\rangle,1,S)
\]

are well-defined. The outer feature law remains `D_obs`; it is not reconditioned on the estimated set. Bounded response support and finite feature moments justify differentiation on compact parameter balls. Finiteness of the log normalizer also follows by integrating the Gaussian density over a fixed positive-measure bounded subset of `S`.

Writing the Gaussian density in exponential-family form and differentiating its log normalizer gives

\[
\nabla L_S(w)=\mathbb E_{\rm obs}[(m_S(w,X)-m_{S\cap S^*}(w^*,X))X],
\]

\[
\nabla^2L_S(w)=\mathbb E_{\rm obs}[\operatorname{Var}(N(\langle w,X\rangle,1,S))XX^\top].
\]

Here `m_T(w,x)` is the corresponding conditional response mean. These formulas also prove convexity.

For completeness, the source's weighted curvature argument is as follows. For a unit vector `u`, the Gaussian estimates in Section 1 give

\[
u^\top\nabla^2L_S(w)u\ge c\mathbb E_{\rm obs}[p_S^4 e^{-2\langle w-w^*,X\rangle^2}\langle u,X\rangle^2].
\]

Let `r(X)=p_(S triangle S*)(X)`. Since `p_S>=p_*-p_(S*\S)`, expansion gives a lower bound consisting of the same expression with `p_*^4`, minus `C E_obs[r(X)<u,X>^2]`. For `g=e^{-2<w-w*,X>^2}<u,X>^2`, change of measure and weighted Holder imply

\[
\mathbb E_{\rm obs}[p_*^4g]\ge\frac{\alpha^5}{\Lambda^8}(\mathbb E_{\rm obs}g)^5.
\]

Indeed `E_D[p_*^5 g]>=(E_D[p_*g])^5/(E_Dg)^4`, `E_D[p_*g]=a E_obs g`, and `E_Dg<=Lambda^2`; the resulting factor `a^4` is at least `alpha^5`. Weighted Jensen, identifiability, and Cauchy-Schwarz give

\[
\mathbb E_{\rm obs}g\ge\rho^2\exp[-2M^4\|w-w^*\|^2/(\alpha\rho^2)].
\]

Finally, splitting according to `r<=b` gives

\[
\mathbb E_{\rm obs}[r\langle u,X\rangle^2]\le b\Lambda^2/\alpha+M^2\sqrt{\tau/(\alpha b)}.
\]

Optimizing `b` yields the source's order `M^(4/3)Lambda^(2/3)tau^(1/3)alpha^(-2/3)`. Thus

\[
\nabla^2L_S(w)\succeq\left[c\frac{\alpha^5\rho^{10}}{\Lambda^8}e^{-10M^4\|w-w^*\|^2/(\alpha\rho^2)}-C\frac{M^{4/3}\Lambda^{2/3}\tau^{1/3}}{\alpha^{2/3}}\right]I.
\]

Use `||w-w*||<=h` on `K`. Choose `tau` so the error is at most half the positive term, and call the resulting uniform curvature lower bound `mu`. Then `mu^{-1}<=exp(poly(Gamma))`. This substitution uses the actual ball diameter and does not require the source's inconsistent numerical constants.

## 6. Gradient Perturbation and the Constrained Minimizer

Let

\[
A=\{x:p_*(x)\ge\alpha\tau^{1/3},\quad p_{S\triangle S^*}(x)\le\tau^{2/3}\}.
\]

The density formula bounds the observed probability of the first bad event by `tau^(1/3)`; Markov bounds the second by the same amount. Hence `Pr_obs(A^c)<=2tau^(1/3)`.

If `tau^(1/3)<=alpha/2`, then on `A`, `p_S>=p_*-p_triangle>=alpha tau^(1/3)/2`. The conditional Gaussian on `S intersect S*` is the Gaussian on `S` further conditioned on `S*`. Their TV distance equals `p_(S\S*)/p_S`, which is at most `2tau^(1/3)/alpha` on `A`. Both responses lie in `[-L,L]`; their means consequently differ by at most `4L tau^(1/3)/alpha` there, and by at most `2L` everywhere. It follows that

\[
\|\nabla L_S(w^*)\|\le CL\sqrt H\left(\tau^{1/3}/\alpha+\tau^{1/6}\right)=:A_\tau.
\]

This proof does not incorrectly upper-bound `p_*` by its good-set lower threshold.

Continuity on the compact ball gives a constrained minimizer `w_S`. Strong monotonicity and its constrained first-order condition imply

\[
\mu\|w_S-w^*\|^2\le\langle\nabla L_S(w^*),w^*-w_S\rangle,
\qquad \|w_S-w^*\|\le A_\tau/\mu.
\]

Choose `tau` so this distance is at most `epsilon/12`.

## 7. Gradient Bias and Moments

At a query `w`, take two independent fresh observed pairs `(X_1,Y_1),(X_2,Y_2)`. Use Section 8 to generate `Z_tilde` conditional on `X_2`, supported on `S`, with TV error at most `zeta` from `N(<w,X_2>,1,S)`, and return

\[
G(w)=\widetilde Z X_2-Y_1X_1.
\]

Let `P` have feature marginal `D_obs` and conditional response `N(<w*,X>,1,S intersect S*)`. Its TV distance from the actual observed joint law is

\[
\mathbb E_{\rm obs}\frac{p_{S^*\setminus S}(X)}{p_*(X)}\le2\sqrt{\tau/\alpha}.
\]

To see the inequality, split according to `p_triangle<=b`: the contribution is at most `b E_obs(1/p_*)+tau/b<=b/alpha+tau/b`; take `b=sqrt(alpha tau)`. The generated and ideal second response laws have joint TV distance at most `zeta` because their feature marginals agree and the conditional error is uniformly bounded.

Couple the two pairs of joint laws. The mismatch probability is at most

\[
t_\tau=2\sqrt{\tau/\alpha}+\zeta.
\]

The three responses belonging to `S` have absolute value at most `L`; the actual observed response has product second moment at most `W`. Cauchy-Schwarz on the mismatch event gives

\[
\|\mathbb E G(w)-\nabla L_S(w)\|\le(3L\sqrt H+\sqrt W)\sqrt{t_\tau}=:B.
\]

Independently of this coupling, bounded support immediately gives

\[
\mathbb E\|G(w)\|^2\le2L^2H+2W=:V.
\]

This avoids the invalid source inference from average survival to pointwise survival. Take `zeta=tau`, and choose the set error as well as this tolerance so `B<=mu epsilon/1000`. Changing only `zeta` cannot remove the set-error component of `B`.

The estimates are uniform over the projection ball. With fresh pairs and fresh conditional randomization, they therefore hold conditional on the full past at every adaptive query.

## 8. Efficient Supported Interval-Truncated Gaussian Sampling

We now derive the implementation rather than invoke the specialized citation. Given a positive-measure explicitly represented interval union `S`, a mean `m`, and `0<zeta<1`, translate to `T=S-m`. Merge overlapping components, discard zero-length components, and split at `-1` and `1`. Endpoint choices have zero Gaussian probability; retain an interior point of a positive-length component for the fallback below. There are at most `J+2` pieces when the merged union has `J` intervals.

Use the unnormalized standard Gaussian density

\[
f(z)=e^{-z^2/2}\mathbf 1_T(z).
\]

Define a piecewise envelope `e(z)` as follows.

- On a central piece `[a,b] subset [-1,1]`, let `e(z)=1`. Its envelope integral is `b-a`, and its normalized proposal is uniform on the piece.
- On a positive-tail piece `[a,b]` with `a>=1`, let

\[
e(z)=e^{-a^2/2}e^{-a(z-a)}.
\]

Writing `ell=b-a`, its integral is

\[
E_{a,b}=e^{-a^2/2}\frac{1-e^{-a\ell}}a.
\]

For an infinite upper endpoint interpret `e^{-a ell}=0`. A normalized proposal is `z=a+t`, where, for an independent uniform `U` in `(0,1)`,

\[
t=-a^{-1}\log\bigl(1-U(1-e^{-a\ell})\bigr).
\]

- Reflect a negative-tail piece through zero and use the positive-tail construction, then reflect its proposal back.

All envelope integrals are finite and positive for positive-length pieces. Let `E` be their sum. Select a piece with probability equal to its envelope integral divided by `E`, and generate its normalized proposal. The resulting proposal density is `e/E` on `T`.

On a central piece the acceptance ratio `f/e` is `exp(-z^2/2)>=exp(-1/2)`. On a positive-tail piece it is

\[
\frac{f(a+t)}{e(a+t)}=e^{-t^2/2}\le1.
\]

The normalized tail proposal is an exponential variable of rate `a>=1` conditioned on `t<=ell`. If `ell<=1`, then `Pr(t<=1)=1`; otherwise

\[
\Pr(t\le1)=\frac{1-e^{-a}}{1-e^{-a\ell}}\ge1-e^{-1}.
\]

Thus the conditional acceptance probability on every tail piece, and by reflection every negative-tail piece, is at least

\[
c_0=e^{-1/2}(1-e^{-1})>0.
\]

The same lower bound holds on central pieces and therefore for their envelope mixture. Accept the proposed point using a fresh uniform variable and the displayed ratio. For every measurable `A`, the probability of proposing and accepting in `A` is `E^{-1} integral_A f`; consequently the accepted point has exactly the standard Gaussian law conditioned on `T`.

Repeat independently for

\[
N=\left\lceil c_0^{-1}\log(1/\zeta)\right\rceil
\]

attempts. If none is accepted, return the fixed interior point of `T`. The fallback probability is at most `(1-c_0)^N<=zeta`. Conditional on acceptance within the cap, the returned point still has the exact target law, since each attempt has the same accepted-point law. Hence the final distribution is a mixture of the target law and a supported fallback of weight at most `zeta`, and its TV distance from the target is at most `zeta`. Translate back by `m`. Support is preserved even on the fallback event; zero Gaussian mass at endpoints causes no difficulty.

This is not ordinary rejection from an untruncated Gaussian: its acceptance probability is bounded below by `c_0`, not by the survival probability. The envelope integrals and proposals use arithmetic, comparisons, elementary exponential/logarithmic evaluations, and uniform randomization in the same real-valued computational model as the source. Sorting and merging cost `O(J log J)`. Computing the envelope weights costs `O(J)`, and even selecting each proposal piece by a linear scan gives deterministic total cost `O(J log J+J log(1/zeta))`. Thus the implementation is polynomial in `J,log(1/zeta)` and in particular satisfies the source's weaker requirement of polynomial dependence on `J,log(1/a_0),log(1/zeta)` for any supplied positive Gaussian-mass lower bound `a_0`. It does not require that lower bound as an input. No CDF oracle or unsupported inverse-CDF complexity assertion is used.

For completeness, the preceding mass-parameter applicability check also remains valid. We have `E_obs p_S>=alpha-tau>=alpha/2`. By `E_obs||X||^2<=H`, a ball of squared radius `8H/alpha` has complement probability at most `alpha/8`. Therefore it contains a point `x_0` with `p(x_0,w*;S)>=alpha/4`: otherwise expected survival would be at most `alpha/4+alpha/8`, a contradiction. For every `x` and `w in K`, Gaussian comparison gives

\[
p(x,w;S)\ge(\alpha/4)^2\exp[-(\langle w,x\rangle-\langle w^*,x_0\rangle)^2].
\]

Also `||w||<=R_w+h`. Observed projection tails, or their coordinate union bound, bound `||X||^2` polynomially in `d,Gamma,log(1/eta)` with probability `1-eta`. Thus `log(1/p(X,w;S))` has the claimed high-probability polynomial bound uniformly over allowed parameter queries. These checks justify the source's mass-dependent formulation as well, but are not needed to give the envelope sampler its deterministic operation-count bound.

On an unsuccessful preprocessing event, the algorithm may return an arbitrary answer if its computed set is empty or has zero length. On the successful event, Section 5 guarantees positive measure, so every sampling call above is well-defined. All later moment and bias bounds apply to the actual capped sampler, including its fallback; they do not condition away that fallback or assume an uncapped implementation.

## 9. Projected SGD and Amplification

Condition on successful preprocessing. For a query at `w_(t-1)`, write its conditional mean as `grad L_S(w_(t-1))+b_t`, with `||b_t||<=B`, and its conditional second moment at most `V`. Use the source's update

\[
w_t=\Pi_K(w_{t-1}-\eta_tG_t),\qquad\eta_t=1/(\mu t).
\]

Let `r_t=||w_t-w_S||`. Projection nonexpansiveness, strong monotonicity, and constrained optimality give `<grad L_S(w),w-w_S> >=mu||w-w_S||^2`. Using `2B r<=mu r^2+B^2/mu` therefore yields

\[
\mathbb E[r_t^2\mid\mathcal F_{t-1}]\le(1-\mu\eta_t)r_{t-1}^2+\eta_tB^2/\mu+\eta_t^2V.
\]

Induction gives `E r_t^2<=B^2/mu^2+V H_t/(mu^2 t)`, where `H_t` is the harmonic sum. For the average of the post-update iterates, Jensen implies

\[
\mathbb E\|\bar w-w_S\|^2\le B^2/\mu^2+CV\log^2(eT)/(\mu^2T).
\]

Choosing `T` polynomially large makes a run lie within `epsilon/12` of `w_S` with probability at least `9/10`, by Markov. This is a complete elementary PSGD derivation; no specialized convergence theorem is invoked.

Run independent fresh-sample repetitions conditional on the same preprocessing. With `O(log(1/delta))` repetitions, a Chernoff bound ensures at least `3/5` are within radius `epsilon/12` of `w_S`. Select any returned point having at least `3/5` of all outputs within twice that radius. Such a point exists; its neighbor set intersects the good outputs, so its distance from `w_S` is at most `epsilon/4`. Together with `||w_S-w*||<=epsilon/12`, this is less than the required `epsilon`.

Allocate failure probability to the warm start, the two set-learning uniform-convergence events, and amplification, with total at most `delta`. The sampler's deterministic attempt cap introduces no separate runtime event: its supported fallback is already included in the uniform TV, bias, and moment bounds. Repetitions use two observed pairs per gradient call.

## 10. Accuracy and Resource Composition

The choices required above are explicit inequalities: the curvature error is at most half its positive term; `tau^(1/3)<=alpha/2`; `A_tau<=mu epsilon/12`; and `(3L sqrt(H)+sqrt(W))sqrt(2sqrt(tau/alpha)+tau)<=mu epsilon/1000`. Because `L` grows only as `(1+R_w)poly(Gamma)sqrt(log(C/tau))`, all hold for a choice

\[
\tau=\exp[-P(\Gamma)]\left(\frac{\varepsilon}{C d(1+R_w)}\right)^{C_0}
\]

with a sufficiently large universal constant `C_0` and universal polynomial `P`. The smoothness exponent is polynomial in `Gamma`; the interval learner, optimization count, and the explicit sampler costs therefore fit

\[
\operatorname{poly}(d,R_w,k,\varepsilon^{-1},\log(1/\delta))^{\operatorname{poly}(\sigma,\beta,\rho^{-1},\alpha^{-1},\Lambda,M)}.
\]

Warm-start concentration and sorting/linear algebra fit the same bound. The algorithm needs no knowledge of `D,S*`, or `w*`, and no unobserved pairs. Combining the preprocessing, optimization, amplification, and error bounds gives the stated Euclidean accuracy with probability at least `1-delta` and the required sample and runtime bounds. The specialized computational obligation left open in revision 1 is closed by Section 8.
