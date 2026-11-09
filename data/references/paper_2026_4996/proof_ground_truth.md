# Reference Proof

## Proof Structure and Obligations

1. Derive the inverse-propensity representation of population target value. The analogous proxy identity is included for completeness, not as an additional public conclusion.
2. Transfer the one-sided certificate to every deterministic policy and then to population mixtures.
3. Establish the score's conditional mean, the exact weighted classification identity, and the Bayes characterization, including ties and measurability.
4. Prove the score range and bounded-loss normalization, derive the scalar exponential estimate, and construct one measurable event that controls every posterior at the fixed temperature.
5. Prove the bounded entropy variational identity and use its equality condition to establish existence, the normalized density, and uniqueness of the optimizer.

All these obligations are closed below. No specialized external result is left as an unsupported proof step.

## 1. Identification

Write \(\pi_a(X)=\pi(a\mid X)\). For each action, consistency and conditional ignorability give
\[
\begin{aligned}
\mathbb E\left[\frac{R^*\mathbf 1\{A=a\}}{\pi_a(X)}\mid X\right]
&=\frac{\mathbb E[R^*(a)\mathbf 1\{A=a\}\mid X]}{\pi_a(X)}\\
&=\frac{\mathbb E[R^*(a)\mid X]\Pr(A=a\mid X)}{\pi_a(X)}
=\mathbb E[R^*(a)\mid X].
\end{aligned}
\]
The divisions are legitimate because \(\pi_a\ge\epsilon>0\), and all rewards and weighted terms are integrable. Multiplying by \(\mathbf 1\{d(X)=a\}\), summing over the two actions, and taking expectations yields
\[
\mathbb E\left[\frac{R^*\mathbf 1\{A=d(X)\}}{\pi(A\mid X)}\right]
=\mathbb E[R^*(d(X))]=V^*(d).
\]
For completeness, define privately \(V(d)=\mathbb E[R(d(X))]\). The identical computation using proxy consistency and ignorability yields
\[
V(d)=\mathbb E\left[\frac{R\mathbf 1\{A=d(X)\}}{\pi(A\mid X)}\right].
\]

## 2. Certificate Transfer

Since both \(R^*\ge0\) and \(R^*\ge R-U\),
\[
R^*\ge (R-U)_+=R_\ell.
\]
Multiplying by the nonnegative inverse-propensity policy indicator and applying the preceding identity gives, for every measurable deterministic policy,
\[
V^*(d)\ge V_\ell(d).
\]
Define privately \(V_\ell(d_Q)=\int V_\ell(d_\beta)Q(d\theta)\). Integration of the policy-wise inequality gives
\[
V^*(d_Q)\ge V_\ell(d_Q).
\]
This is a statement about the population mixture at the realized posterior, not an expectation over the learning data. No independent nuisance-estimation sample is used.

## 3. Exact Weighted Classification Reduction

All the score and label maps are jointly measurable: this follows from the measurability of \(u,\pi,f,\nu_a\), the product sigma-algebra, and the Borel sign map. Measurable conditional-mean versions exist in the stipulated covariate space. Initially, the crude bound \(|\Gamma_a^\alpha|\le 1+\epsilon^{-1}\) already guarantees integrability of the scores, risks, and constants.

For fixed \(a,\alpha\), conditioning on \(X\) gives
\[
\begin{aligned}
\mathbb E[\Gamma_a^\alpha\mid X]
&=\nu_{a,\alpha}(X)+\frac{\mathbb E[\mathbf 1\{A=a\}(R_\ell-\nu_{a,\alpha}(X))\mid X]}{\pi_a(X)}\\
&=\nu_{a,\alpha}(X)+\mu_a(X)-\nu_{a,\alpha}(X)=\mu_a(X).
\end{aligned}
\]
Here the denominator \(\pi(A\mid X)\) in the public definition equals \(\pi_a(X)\) on the only event where its residual term is nonzero. Thus
\[
\mathbb E[\Gamma_d^\alpha]=\mathbb E[\mu_{d(X)}(X)].
\]
A separate conditioning of the defining inverse-propensity expression for \(V_\ell(d)\) gives
\[
V_\ell(d)=\mathbb E[\mu_{d(X)}(X)].
\]
Consequently \(\mathbb E[\Gamma_d^\alpha]=V_\ell(d)\) for every fixed \(d,\alpha\).

Pointwise,
\[
\Gamma_d^\alpha=\frac{\Gamma_1^\alpha+\Gamma_{-1}^\alpha}{2}+\frac{d(X)D_\alpha}{2}.
\]
Because \(D_\alpha=W_\alpha Y_\alpha\) and both labels take values in \(\{-1,1\}\),
\[
d(X)D_\alpha=W_\alpha\bigl(1-2\mathbf 1\{d(X)\ne Y_\alpha\}\bigr).
\]
This remains true on \(\{D_\alpha=0\}\), since \(W_\alpha=0\), regardless of the tie label. Taking expectations proves
\[
V_\ell(d)=C_\alpha^\sharp-R_{01}^\alpha(d).
\]
For fixed \(\alpha\), the constant does not depend on \(d\), proving the optimization equivalence. It need not be constant as \(\alpha\) varies.

The policy \(d^\dagger(x)=\operatorname{sgn}(\mu_1(x)-\mu_{-1}(x))\) is measurable and maximizes the conditional certified reward. For every measurable \(d\),
\[
V_\ell(d^\dagger)-V_\ell(d)
=\mathbb E[\max\{\mu_1(X),\mu_{-1}(X)\}-\mu_{d(X)}(X)]\ge0.
\]
The integrand is nonnegative, so equality holds exactly when \(d(X)\) chooses a maximizing action almost surely. Either action is allowed when the conditional means tie.

## 4. Posterior-Uniform Concentration at a Fixed Temperature

### Range and normalization

If \(A\ne a\), then \(\Gamma_a^\alpha=\nu_{a,\alpha}(X)\in[0,1]\). If \(A=a\), writing \(p=\pi_a(X)\),
\[
\Gamma_a^\alpha=(1-p^{-1})\nu_{a,\alpha}(X)+p^{-1}R_\ell.
\]
Since \(1-p^{-1}\le0\) and both reward and nuisance lie in \([0,1]\),
\[
1-p^{-1}\le\Gamma_a^\alpha\le p^{-1}.
\]
Therefore every selected score satisfies
\[
1-\epsilon^{-1}\le\Gamma_d^\alpha\le\epsilon^{-1}.
\]
The auxiliary advantage bound can also be checked directly:
\[
D_\alpha=\nu_{1,\alpha}(X)-\nu_{-1,\alpha}(X)
+\frac{A}{\pi(A\mid X)}(R_\ell-\nu_{A,\alpha}(X)),
\qquad |D_\alpha|\le1+\epsilon^{-1}.
\]
Set \(c=\epsilon^{-1}\), \(K=2\epsilon^{-1}-1>0\), and
\[
\ell(\theta;Z)=\ell_{\rm val}(\theta;Z)=\frac{c-\Gamma_{d_\beta}^\alpha(Z)}{K}\in[0,1].
\]
Define
\[
L(\theta)=\mathbb E_Z[\ell(\theta;Z)],\quad
\widehat L_n(\theta)=\frac1n\sum_i\ell(\theta;Z_i),\quad
L(Q)=\int L(\theta)Q(d\theta),\quad
\widehat L_n(Q)=\int\widehat L_n(\theta)Q(d\theta).
\]
The bounded joint measurability just established permits the needed integrations and interchanges. The score identity from Section 3 gives
\[
V_\ell(d_Q)=c-KL(Q),\qquad
\widehat V_{\ell,n}(d_Q)=c-K\widehat L_n(Q).
\]

### Scalar exponential estimate

For completeness, let \(T\in[0,1]\) and define \(\psi(t)=\log\mathbb E[e^{t(T-\mathbb ET)}]\). Boundedness permits differentiation. Under the exponentially tilted law, \(\psi''(t)\) is the variance of \(T\), and
\[
\psi''(t)\le\mathbb E_t[(T-1/2)^2]\le1/4.
\]
Since \(\psi(0)=\psi'(0)=0\), Taylor's integral formula yields \(\psi(t)\le t^2/8\) for every real \(t\). Applying this with \(T=\ell(\theta;Z_i)\) and \(t=-\eta\), and using independence of the observations, gives
\[
\mathbb E\exp\{\eta n(L(\theta)-\widehat L_n(\theta))\}\le e^{\eta^2n/8}.
\]
The loss family is fixed before the sample: its certificate and parameter-indexed score functions are not fitted outside the stated parameter space.

### Bounded entropy identity

For any bounded measurable \(h:\Theta\to\mathbb R\), put
\[
Z_h=\int e^{h(\theta)}\Pi_0(d\theta),\qquad
\frac{d\Pi_h}{d\Pi_0}=\frac{e^h}{Z_h}.
\]
Boundedness gives \(0<Z_h<\infty\), a bounded log-density, and equivalence of \(\Pi_h\) and \(\Pi_0\). For any \(Q\ll\Pi_0\) with finite KL divergence,
\[
\mathrm{KL}(Q\Vert\Pi_h)=\mathrm{KL}(Q\Vert\Pi_0)-\int h\,dQ+\log Z_h.
\]
Relative entropy is nonnegative: if \(r=dQ/d\Pi_h\), integrate \(r\log r-r+1\ge0\) against \(\Pi_h\). Equality holds precisely when \(r=1\) almost everywhere, that is, when \(Q=\Pi_h\). Hence
\[
\int h\,dQ\le\mathrm{KL}(Q\Vert\Pi_0)+\log Z_h.
\]
For infinite KL the inequality is automatic; because \(h\) is bounded, the entropy identity also has an unambiguous extended-real interpretation. This proves the needed variational inequality and its equality condition rather than assuming a named optimizer theorem.

### One common event

Fix \(\delta,\eta,n\) as in the task, and let
\[
G(\theta)=\eta n(L(\theta)-\widehat L_n(\theta)),\qquad
M=\int e^{G(\theta)}\Pi_0(d\theta).
\]
This is a measurable random variable. Nonnegative integration and prior independence imply
\[
\mathbb E M\le e^{\eta^2n/8}.
\]
If the prior is independently randomized, the same argument is first conditional on its realization and then integrated. Markov's inequality therefore gives
\[
\Pr\{M\le\delta^{-1}e^{\eta^2n/8}\}\ge1-\delta.
\]
On this single event, apply the bounded entropy inequality to \(h=G\), which lies in \([-\eta n,\eta n]\). For every finite-KL posterior simultaneously,
\[
\eta n(L(Q)-\widehat L_n(Q))\le
\mathrm{KL}(Q\Vert\Pi_0)+\log(1/\delta)+\frac{\eta^2n}{8}.
\]
The event is defined through \(M\), not an uncountable intersection of posterior-specific events. Thus posterior selection using the same sample is permitted. Dividing by \(\eta n\) gives
\[
L(Q)\le\widehat L_n(Q)+\frac{\mathrm{KL}(Q\Vert\Pi_0)+\log(1/\delta)}{\eta n}+\frac\eta8.
\]
Substitution of the population and empirical value identities, followed by certificate transfer, proves
\[
V^*(d_Q)\ge\widehat V_{\ell,n}(d_Q)
-K\left[\frac{\mathrm{KL}(Q\Vert\Pi_0)+\log(1/\delta)}{\eta n}+\frac\eta8\right].
\]
Infinite-KL posteriors satisfy the conclusion trivially. There is no assertion that this event works simultaneously for every temperature or every sample size.

## 5. Exact Optimizer

Fix a realized sample and \(\eta>0\), and put
\[
S(\theta)=\widehat V_{\ell,n}(d_\theta),\qquad \tau=\frac{\eta n}{K}>0,\qquad
Z_\tau=\int e^{\tau S(\theta)}\Pi_0(d\theta).
\]
The score range gives \(1-c\le S\le c\), so
\[
0<e^{\tau(1-c)}\le Z_\tau\le e^{\tau c}<\infty.
\]
Define \(Q_\eta\) by \(dQ_\eta/d\Pi_0=e^{\tau S}/Z_\tau\). Its log-density is bounded, so \(\mathrm{KL}(Q_\eta\Vert\Pi_0)<\infty\). The entropy identity above yields
\[
\widehat V_{\ell,n}(d_Q)-\frac1\tau\mathrm{KL}(Q\Vert\Pi_0)
=\frac1\tau\log Z_\tau-\frac1\tau\mathrm{KL}(Q\Vert Q_\eta).
\]
This equality holds for finite-KL posteriors and extends with value \(-\infty\) when the original KL divergence is infinite. It is maximized exactly when \(Q=Q_\eta\), proving existence and uniqueness as a probability measure, with density equality understood up to prior-null sets. This is not a claim that the maximizing policy parameter is unique.

Finally,
\[
\sum_i\ell_{\rm val}(\theta;Z_i)=\frac{nc}{K}-\frac nK\widehat V_{\ell,n}(d_\theta).
\]
The exponentials in the task therefore differ by the positive factor \(e^{-\eta nc/K}\), independent of \(\theta\), which cancels upon normalization. This gives both stated density forms.

The proof covers \(n=1\), \(\epsilon=1/2\), zero certified rewards, tied scores or conditional means, arbitrary prior support, and infinite-KL competitors. Existence of the prior itself ensures a nonempty feasible set, since \(Q=\Pi_0\) is feasible.

## Private Source-Repair Note

The source concentration proof at L000493-L000495 must use \(s=-\eta n\), not \(s=\eta n\); the available scalar estimate holds for every real \(s\). The earlier reference proof already used the correct direction, but its source record did not disclose this local repair. The previously recorded auxiliary correction must also replace \(n c_{n,\delta}(Q)\) by \(c_{n,\delta}(Q)\) at both L000719 and L000724. The latter auxiliary bound is not needed for the fixed-temperature theorem proved here. Every variational application in this proof has a bounded exponent, so no unrestricted claim about potentially undefined differences of infinite expectations is invoked.
