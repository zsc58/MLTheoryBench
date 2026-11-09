# Reference Proof

## Proof Structure

1. Use the assumed measurable quotient predictor to factor population and empirical risks, then apply pushforward integration.
2. Construct conditional posterior densities from the parameter-space density and a prior disintegration. Derive the KL chain rule, including its extended-value interpretation and the nonnegative within-fiber term.
3. Verify the standard bounded-loss PAC–Bayes inequality with the stated constants, apply it on the quotient, and compare certificates by monotonicity.

The spaces, quotient map, predictor family, and loss are fixed when the certification sample is drawn. This is the fixed-construction setup used by the source. A prior chosen using randomness independent of the certification sample can be treated conditionally on that choice. The resulting conditional guarantee also gives the corresponding joint guarantee upon averaging. No independence of the posterior from the certification sample is required.

## Complete Proof

### 1. Risk identities

Use the measurable quotient predictor assumed in the problem; predictor invariance alone is not being used as a theorem asserting existence of a measurable factor. The bounded measurable quotient loss makes the quotient population and empirical risks measurable. Since \(f_\theta=\bar f_{\pi(\theta)}\),
\[
R(\theta)=\bar R(\pi(\theta)),\qquad
\widehat R_S(\theta)=\widehat{\bar R}_S(\pi(\theta)).
\]
For every bounded measurable function \(v\) on \(\mathcal U\), the definition of pushforward gives
\[
\int_{\mathcal U}v(u)\,\bar Q(du)
=\int_\Theta v(\pi(\theta))\,Q(d\theta).
\]
Applying this to the two risks proves
\[
\mathbb E_QR=\mathbb E_{\bar Q}\bar R,\qquad
\mathbb E_Q\widehat R_S=\mathbb E_{\bar Q}\widehat{\bar R}_S.
\]
These identities hold for every sample and every posterior, not merely on a high-probability event.

### 2. Conditional densities and the extended-value KL identity

Fix an arbitrary admissible posterior, after fixing the sample if necessary. If \(A\subseteq\mathcal U\) is measurable and \(\bar P(A)=0\), then \(P(\pi^{-1}(A))=0\), hence \(Q(\pi^{-1}(A))=0\). Thus \(\bar Q\ll\bar P\).

Let \(r=dQ/dP\), taking a nonnegative measurable version that is finite \(P\)-almost everywhere. Standard Borel disintegration supplies a probability kernel \(K_u=P(\cdot\mid u)\), concentrated on the fiber \(\pi^{-1}(u)\) for \(\bar P\)-almost every \(u\). Define
\[
a(u)=\int_\Theta r(\theta)\,K_u(d\theta).
\]
The function \(a\) is measurable, has integral one under \(\bar P\), and satisfies
\[
\bar Q(A)=\int_A a(u)\,\bar P(du).
\]
Consequently \(a=d\bar Q/d\bar P\), and \(0<a(u)<\infty\) for \(\bar Q\)-almost every \(u\).

On those fibers define
\[
L_u(d\theta)=\frac{r(\theta)}{a(u)}K_u(d\theta).
\]
On the exceptional set choose an arbitrary probability-kernel version, for example \(K_u\). The formula defines a measurable probability kernel on the relevant full-measure set. For measurable \(B\subseteq\Theta\) and \(A\subseteq\mathcal U\), disintegration of \(P\) gives
\[
\int_A L_u(B)\,\bar Q(du)
=\int_{B\cap\pi^{-1}(A)}r(\theta)\,P(d\theta)
=Q(B\cap\pi^{-1}(A)).
\]
Fibers with \(a=0\) contribute zero, and the remaining exceptional set is null. Therefore \(L_u\) is a regular conditional distribution of \(Q\) given \(\pi\). Uniqueness of regular conditional probabilities on standard Borel spaces identifies it with the conditional law used in the problem, for \(\bar Q\)-almost every \(u\). In particular,
\[
Q(\cdot\mid u)\ll P(\cdot\mid u),\qquad
h_u(\theta):=\frac{dQ(\cdot\mid u)}{dP(\cdot\mid u)}(\theta)
=\frac{r(\theta)}{a(u)}
\]
on the relevant fibers. It follows that
\[
\log r(\theta)=\log a(\pi(\theta))+\log h_{\pi(\theta)}(\theta)
\quad\text{for }Q\text{-almost every }\theta.
\]
All three logarithms here are finite pointwise on a suitable set of full \(Q\)-measure, although their positive-part integrals can be infinite.

To justify integration without assuming finite KL, observe that any density \(t\) of one probability measure relative to another satisfies
\[
\int t(\log t)^-\,d\nu
=\int_{0<t<1}-t\log t\,d\nu\leq 1/e.
\]
This applies to \(r\), to \(a\), and on each relevant fiber to \(h_u\). Integrating the conditional bound under \(\bar Q\) also bounds the negative part of the conditional logarithm by \(1/e\). Thus the preceding logarithmic equality may be integrated and disintegrated in the extended sense without an undefined subtraction of infinities. It yields
\[
\begin{aligned}
\mathrm{KL}(Q\|P)
&=\int_{\mathcal U}\log a(u)\,\bar Q(du)
 +\int_{\mathcal U}\int_\Theta\log h_u(\theta)\,L_u(d\theta)\,\bar Q(du)\\
&=\mathrm{KL}(\bar Q\|\bar P)
 +\int_{\mathcal U}\mathrm{KL}(L_u\|K_u)\,\bar Q(du)\\
&=\mathrm{KL}(\bar Q\|\bar P)+\Delta_\pi.
\end{aligned}
\]
The conditional integral is measurable by the kernel construction. Its value is independent of the chosen conditional versions: the posterior versions agree \(\bar Q\)-almost everywhere, and the prior versions agree \(\bar P\)-almost everywhere and hence also \(\bar Q\)-almost everywhere.

For any probability density \(t\), the inequality \(t\log t-t+1\geq0\), with \(0\log0=0\), proves nonnegativity of relative entropy. Therefore \(\Delta_\pi\geq0\) and
\[
\mathrm{KL}(\bar Q\|\bar P)\leq\mathrm{KL}(Q\|P).
\]
If \(\mathrm{KL}(Q\|P)<\infty\), both terms on the right-hand side of the additive identity are finite, so subtraction gives
\[
\mathrm{KL}(\bar Q\|\bar P)=\mathrm{KL}(Q\|P)-\Delta_\pi.
\]
No subtraction is used when both quantities on the proposed difference could be infinite.

### 3. Audited PAC–Bayes inequality and certificate comparison

The standard independent ingredient is the following bounded-loss inequality. For a fixed measurable hypothesis space \(H\), a fixed jointly measurable loss \(L:H\times\mathcal Z\to[0,1]\), an i.i.d. sample of size \(n\geq1\), and a sample-independent prior \(\mu\), there is an event of probability at least \(1-\delta\) on which every posterior \(\nu\ll\mu\) satisfies
\[
\mathbb E_\nu r_H\leq\mathbb E_\nu\widehat r_{H,S}
+\sqrt{\frac{\mathrm{KL}(\nu\|\mu)+\log(1/\delta)+\log n+2}{2n-1}}.
\]
Here \(r_H(h)=\mathbb E L(h,Z)\) and \(\widehat r_{H,S}(h)=n^{-1}\sum_i L(h,Z_i)\). Infinite KL gives an infinite right-hand side. The event is common to all posteriors, so sample-dependent posteriors are allowed.

For completeness, the exact constants and uniformity can be verified by a routine bounded-variable argument. If \(Y\in[0,1]\), the logarithm of the moment-generating function of \(Y-\mathbb EY\) has value and derivative zero at zero and second derivative equal to a variance under an exponential tilt. This variance is at most \(1/4\), since every probability measure supported on \([0,1]\) has variance at most \(1/4\). Integrating the second-derivative bound gives
\[
\mathbb E\exp(s(\mathbb EY-Y))\leq\exp(s^2/8),\qquad s\geq0.
\]
Independence and exponential Markov inequality, optimized at \(s=4t\), therefore imply, for each fixed \(h\) and \(t\geq0\),
\[
\Pr\{r_H(h)-\widehat r_{H,S}(h)>t\}\leq e^{-2nt^2}.
\]
Put \(d_h(S)=(r_H(h)-\widehat r_{H,S}(h))_+\) and \(\lambda=2n-1>0\). Tail integration gives
\[
\begin{aligned}
\mathbb E_S e^{\lambda d_h(S)^2}
&=1+\int_0^\infty 2\lambda t e^{\lambda t^2}\Pr\{d_h(S)>t\}\,dt\\
&\leq1+\frac{\lambda}{2n-\lambda}=2n.
\end{aligned}
\]
Define \(M(S)=\int_H e^{\lambda d_h(S)^2}\,\mu(dh)\). Measurability and Tonelli's theorem give \(\mathbb E_S M(S)\leq2n\). Hence the measurable event \(M(S)\leq2n/\delta\) has probability at least \(1-\delta\).

On this event, take any \(\nu\ll\mu\) of finite KL and define the probability measure
\[
\mu_S^*(dh)=\frac{e^{\lambda d_h(S)^2}}{M(S)}\mu(dh).
\]
Its density is strictly positive, and its logarithm is bounded because \(0\leq d_h\leq1\). Nonnegativity of \(\mathrm{KL}(\nu\|\mu_S^*)\) consequently gives
\[
\lambda\mathbb E_\nu d_h(S)^2
\leq\mathrm{KL}(\nu\|\mu)+\log M(S)
\leq\mathrm{KL}(\nu\|\mu)+\log(2n/\delta).
\]
Thus
\[
\mathbb E_\nu(r_H-\widehat r_{H,S})
\leq\mathbb E_\nu d_h
\leq\sqrt{\mathbb E_\nu d_h^2}
\leq\sqrt{\frac{\mathrm{KL}(\nu\|\mu)+\log(2n/\delta)}{2n-1}}.
\]
Since \(\log2\leq2\), this implies the stated inequality. The same event works for every \(\nu\), including posteriors selected after observing \(S\); posteriors of infinite KL satisfy the claimed inequality trivially. The argument also covers \(n=1\).

Apply this independently verified inequality with \(H=\mathcal U\), \(\mu=\bar P\), \(\nu=\bar Q\), and \(L(u,z)=\ell(\bar f_u,z)\). All hypotheses hold: the quotient loss is measurable and bounded, the sample is i.i.d., \(\bar Q\ll\bar P\), and \(\bar P\) is sample-independent because \(P\) is sample-independent and \(\pi\) is fixed. Consequently, with probability at least \(1-\delta\),
\[
\mathbb E_{\bar Q}\bar R
\leq\mathbb E_{\bar Q}\widehat{\bar R}_S
+C_{n,\delta}(\mathrm{KL}(\bar Q\|\bar P)).
\]
The risk identities and KL decomposition proved above hold on this event as well, since they hold for every sample. Finally, \(C_{n,\delta}\) is nondecreasing on \([0,\infty]\), so
\[
\mathbb E_{\bar Q}\widehat{\bar R}_S
+C_{n,\delta}(\mathrm{KL}(\bar Q\|\bar P))
\leq
\mathbb E_Q\widehat R_S
+C_{n,\delta}(\mathrm{KL}(Q\|P)).
\]
This comparison remains valid when the parameter-space KL is infinite, and the quotient bound can still be finite in that case. For finite parameter-space KL, the decrease in KL is exactly \(\Delta_\pi\); this is not, in general, the numerical decrease in the square-root certificate.

## Obligation Closure and Source Repair

- Measurability and both risk-transfer identities are established in Section 1.
- Quotient absolute continuity, conditional absolute continuity, and the density factorization are derived in Section 2.
- Conditional-version independence, nonnegativity, and legitimate extended-value integration are established in Section 2.
- The external bounded-loss inequality is stated with its complete applicable contract and independently verified in Section 3, including the exact constants, \(n=1\), and posterior uniformity.
- Sample-independent prior admissibility, the certificate comparison, and the finite/infinite-KL cases are established in Section 3.

The source's unqualified subtractive identity at L000093 must be read in the locally corrected form: the additive identity holds generally, and the displayed finite-KL subtraction follows when the parameter-space KL is finite. This repair is recorded under theory_006. It does not change the current public task or the source's comparison proof, which already uses the KL inequality rather than subtraction. No theorem-critical proof obligation remains unresolved.
