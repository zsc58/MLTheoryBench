# Reference Proof

## Scope and obligations

The target consists of the reserve-conditional contamination-estimation argument, the finite-sample false-positive certificate, the finite-sample density-based power bound, and the two-world converse. It does not require the source's separate population-checkability assertion for reserve-averaged quantities or its asymptotic drift-floor commentary.

The obligations are:

1. Establish the conditional expectation and concentration of the correctly normalized contamination estimate.
2. Prove false-positive validity with the prescribed empirical quantile, including overflow.
3. Account for empirical-quantile rounding, establish the required threshold containment, and prove the power implication without conditioning on the density event.
4. Specify the common observable law and prove the converse for every threshold, including the endpoint pi=0.

All four obligations are closed below.

## Standard concentration facts

For iid random variables Y_1,...,Y_n taking values in [0,1], Hoeffding's inequality gives
\[
\Pr\left(\overline Y-\mathbb E\overline Y>t\right)\le e^{-2nt^2},\qquad t>0.
\]
For an iid real-valued sample with CDF F and empirical CDF F_n, the one-sided and two-sided DKW inequalities give
\[
\Pr\left(\sup_x(F_n(x)-F(x))>t\right)\le e^{-2nt^2},
\qquad
\Pr\left(\sup_x|F_n(x)-F(x)|>t\right)\le2e^{-2nt^2}.
\]
These are the standard independent concentration results used here. Given the reserve, the window remains iid from the specified mixture, so all these statements apply conditionally on the reserve as well.

## 1. Conditional contamination bound

Fix a realized reserve R satisfying the stated conservativity condition. All probabilities in the calibration argument are conditional on this reserve. Write
\[
Y_i=\mathbf1\{p_R(S_i)>\lambda\},\qquad
\overline Y=n^{-1}\sum_iY_i,
\qquad
d_n=\sqrt{\frac{\log(2/\eta)}{2n}},
\qquad
\varepsilon_n=d_n+\frac1n.
\]
The indicators are iid given R, with common mean
\[
\mu_R=(1-\pi)\bigl[(1-\lambda)-\varepsilon_{\rm dr}(R)\bigr]
       +\pi\kappa_\lambda(R).
\]
The estimator is \(\widehat\pi_\lambda=1-\overline Y/(1-\lambda)\), hence
\[
\mathbb E[\widehat\pi_\lambda\mid R]
=\pi+\frac{(1-\pi)\varepsilon_{\rm dr}(R)-\pi\kappa_\lambda(R)}{1-\lambda}
\ge\pi.
\]
Put \(h_n=\sqrt{\log(2/\eta_1)/(2n)}\), so \(c_n=h_n/(1-\lambda)\). Hoeffding gives
\[
\Pr(\overline Y-\mu_R>h_n\mid R)\le\eta_1/2.
\]
Outside this exceptional event,
\[
\widehat\pi_\lambda+c_n\ge\mathbb E[\widehat\pi_\lambda\mid R]\ge\pi.
\]
Because \(0\le\pi<1\), clipping a number at least pi to [0,1] preserves that inequality. Therefore
\[
\Pr(\widehat\pi_{\rm up}<\pi\mid R)\le\eta_1/2\le\eta_1.
\]
No reserve-averaged concentration claim is used.

## 2. False-positive certificate

Let
\[
a_n=1-\alpha(1-\widehat\pi_{\rm up}),\qquad
q_n=a_n+\varepsilon_n.
\]
The one-sided DKW event
\[
F_{\rm mix}(t)\ge F_n(t)-d_n\quad\text{for every real }t
\]
has conditional probability at least \(1-\eta/2\).

If \(q_n>1\), the procedure outputs \(+\infty\), whose ID tail probability is zero. If \(q_n\le1\), the empirical generalized inverse satisfies \(F_n(\widehat\tau)\ge q_n\). Consequently, on the DKW event,
\[
F_{\rm mix}(\widehat\tau)
\ge q_n-d_n
=a_n+1/n
\ge a_n.
\]
It follows that
\[
(1-\pi)\Pr_{F_{\rm ID}}(S>\widehat\tau)
\le\Pr_{F_{\rm mix}}(S>\widehat\tau)
\le\alpha(1-\widehat\pi_{\rm up}).
\]
On \(\widehat\pi_{\rm up}\ge\pi\), division by \(1-\pi>0\) proves the false-positive bound. A union bound gives failure probability at most \(\eta/2+\eta_1\), as requested. The sharper estimate \(\eta/2+\eta_1/2\) is also available.

This is a statement about the tail law of a fresh observation, not the empirical false-positive fraction in the calibration window. If the reserve condition holds almost surely, integrating the conditional bound over R gives the same unconditional guarantee. If it holds only on a reserve event of probability at least \(1-\delta_R\), the unconditional failure bound instead incurs an additional \(\delta_R\); no such unbudgeted claim is made in the public task.

## 3. Power

Use the two-sided DKW event
\[
\sup_t|F_n(t)-F_{\rm mix}(t)|\le d_n,
\]
which has conditional probability at least \(1-\eta\). Also restrict to the probability-one event that the continuous window scores are distinct. Define
\[
u_n=a_n+2\varepsilon_n,\qquad B_n=F_{\rm mix}^{-1}(u_n).
\]
The public density event is denoted by H.

First, if \(B_n=+\infty\), H cannot hold: a probability density cannot be bounded below by a positive constant on the whole half-line starting at the finite number \(\tau^*\). In particular, if \(q_n>1\), then \(u_n>1\), \(B_n=+\infty\), and the density implication imposes no assertion. The false-positive certificate remains valid because the output is +infinity.

Consider a realization on the DKW event and H. Then \(B_n\) is finite and \(q_n\le1\). By continuity of \(F_{\rm mix}\),
\[
F_{\rm mix}(B_n)\ge u_n.
\]
Thus
\[
F_n(B_n)\ge u_n-d_n=q_n+1/n\ge q_n,
\]
so \(\widehat\tau\le B_n\).

For the upper CDF level of the empirical quantile, let \(j=\lceil nq_n\rceil\). Distinct observations give
\[
F_n(\widehat\tau)=j/n\le q_n+1/n.
\]
Therefore
\[
F_{\rm mix}(\widehat\tau)
\le F_n(\widehat\tau)+d_n
\le q_n+1/n+d_n
=a_n+2\varepsilon_n.
\]
This is the rounding step missing from revision 0.

If \(\widehat\tau\le\tau^*\), monotonicity of the OOD tail makes the requested loss nonpositive, while its proposed upper bound is nonnegative. Otherwise \([\tau^*,\widehat\tau]\subseteq[\tau^*,B_n]\), so H supplies the needed density bounds throughout this interval. Continuity of the ID CDF gives
\[
F_{\rm ID}(\tau^*)=1-\alpha,
\qquad
F_{\rm mix}(\tau^*)\ge(1-\pi)(1-\alpha).
\]
Subtracting,
\[
F_{\rm mix}(\widehat\tau)-F_{\rm mix}(\tau^*)
\le\alpha\widehat\pi_{\rm up}+(1-\alpha)\pi+2\varepsilon_n.
\]
The lower mixture-density bound implies
\[
\underline\kappa(\widehat\tau-\tau^*)
\le F_{\rm mix}(\widehat\tau)-F_{\rm mix}(\tau^*).
\]
The upper OOD-density bound then gives
\[
\Pr_{F_{\rm OOD}}(S>\tau^*)-\Pr_{F_{\rm OOD}}(S>\widehat\tau)
\le\overline f_{\rm OOD}(\widehat\tau-\tau^*)
\le\frac{\overline f_{\rm OOD}}{\underline\kappa}
\left[\alpha\widehat\pi_{\rm up}+(1-\alpha)\pi+2\varepsilon_n\right].
\]
Thus H and failure of the power inequality can occur only outside the two-sided DKW event, up to a null tie event. Their joint probability is at most eta, and hence at most \(\eta+\eta_1\), as requested. No concentration inequality was conditioned on H. If H holds almost surely, this directly yields the stated ordinary high-probability power bound.

## 4. Converse

Let P have a continuous CDF, and use the lower generalized inverse to define \(\tau_B=P^{-1}(1-\alpha)\). Continuity gives \(P(S>\tau_B)=\alpha\), so Q is well defined. Write \(\overline P(t)=P(S>t)\) and similarly for Q and P'. Then
\[
\overline Q(t)=
\begin{cases}
1,&t<\tau_B,\\
\overline P(t)/\alpha,&t\ge\tau_B.
\end{cases}
\]
In both worlds the reserve has law \(P^{\otimes m}\), independently of the unlabeled window, and the window has law \((P')^{\otimes n}\). Any auxiliary random seed has the same independent law in both worlds. A common draw of these observables and the seed therefore produces the same output from the same measurable threshold rule. The rule receives no world label, latent ID/OOD labels, or world-specific side information.

For \(0<\pi<1\) and \(t<\tau_B\),
\[
P'(S>t)=(1-\pi)\overline P(t)+\pi
\ge(1-\pi)\alpha+\pi>\alpha.
\]
For \(t\ge\tau_B\), including \(t=+\infty\),
\[
P'(S>t)=[\pi+\alpha(1-\pi)]Q(S>t).
\]
These two cases prove the required pointwise inclusion. A threshold of -infinity has P' tail one and cannot satisfy its antecedent. At \(\pi=0\), the proposed ceiling is one, so the inclusion holds for every threshold as well.

Applying the pointwise inclusion to the coupled random output and taking probabilities proves the final assertion for every \(\beta\in[0,1]\).

## Source dependency qualification

The conditional argument above fully closes the portion of theory_013 used by this task. The source's additional population-checkability argument at L000231 is not established by the supplied reserve-DKW reasoning and is not invoked here. No specialized or nonstandard external result is needed to complete any obligation in this reference proof.
