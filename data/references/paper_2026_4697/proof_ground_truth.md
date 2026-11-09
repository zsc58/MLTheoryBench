# Reference Proof

## Proof Structure

1. Recover each fresh batch mean from the cumulative releases and factor the trajectory density into conditional transition densities. Show that every factor except the insertion transition cancels, including the case of insertion at the first release.
2. Derive the surviving multivariate Gaussian log likelihood ratio and apply the Neyman-Pearson lemma with its hypotheses verified.
3. In one dimension, complete the square with a signed target displacement, integrate the rejection interval under both hypotheses, and use symmetry to obtain the formulas expressed in terms of m*. Handle all threshold and zero-displacement cases.
4. Derive the final-only Gaussian laws and repeat the calculation with q=nT. Explain dilution and check T=1.

## Complete Proof

### 1. Batch laws and isolation

All parameters, the target, and the insertion time are fixed. The replacement index is independent of the original Gaussian observations. Conditional on any value of that index, the modified insertion batch contains n-1 independent Gaussian vectors and the fixed target. Its batch-mean law does not depend on the index. Therefore, writing delta=z*-mu,
\[
\bar X_t\sim N_d(\mu,\Sigma/n)\quad\text{under }H_0,
\]
and under \(H_1^\tau\),
\[
\bar X_\tau\sim N_d\left(\mu+\frac{\delta}{n},\frac{n-1}{n^2}\Sigma\right),
\]
while every other batch mean retains its null law. Batch means remain independent under each hypothesis.

The releases satisfy
\[
\widehat\mu_1=\bar X_1,\qquad
\widehat\mu_t=\frac{t-1}{t}\widehat\mu_{t-1}+\frac1t\bar X_t\quad(t\ge2).
\]
Consequently the observed trajectory determines every batch mean:
\[
\bar X_1=\widehat\mu_1,\qquad
\bar X_t=t\widehat\mu_t-(t-1)\widehat\mu_{t-1}\quad(t\ge2).
\]

Factor the trajectory density into the density of the first release and the conditional densities of subsequent releases given their histories. For t>=2, independence of the fresh batch shows that the conditional law depends on the history only through the numerical value of the preceding cumulative mean. At any t other than tau, the fresh batch has the same law under both hypotheses, so these conditional densities agree. This remains true after insertion: the preceding state may have different marginal distributions, but the transition kernels evaluated at the same state agree.

At the insertion transition the affine transformation from the batch mean to the next release has the same Jacobian under both hypotheses, so its Jacobian cancels in the density ratio. At t=1 use the unconditional first-release density, not conditioning on an undefined release at time zero. Thus, if f_0 and f_1 are the two insertion-batch-mean densities,
\[
\frac{p(\widehat\mu_{1:T}\mid H_1^\tau)}{p(\widehat\mu_{1:T}\mid H_0)}
=\frac{f_1(\bar X_\tau)}{f_0(\bar X_\tau)}.
\]
Positive definiteness of Sigma and n>=2 ensure that these Gaussian densities, and the trajectory densities obtained through the invertible affine transformation, are everywhere positive.

### 2. Gaussian likelihood ratio and optimality

Put \(N_\tau=\bar X_\tau-\mu\), \(c=n/(n-1)\), and \(m^*=\delta^T\Sigma^{-1}\delta\). The centered null and alternative covariances are \(V_0=\Sigma/n\) and \(V_1=(n-1)\Sigma/n^2\), and the alternative mean is \(\delta/n\). The Gaussian density formula gives
\[
\ell_\tau
=\frac d2\log c+\frac n2N_\tau^T\Sigma^{-1}N_\tau
-\frac{n^2}{2(n-1)}(N_\tau-\delta/n)^T\Sigma^{-1}(N_\tau-\delta/n).
\]
Expanding the last quadratic form yields
\[
\ell_\tau=\frac d2\log c-\frac{n}{2(n-1)}N_\tau^T\Sigma^{-1}N_\tau
+cN_\tau^T\Sigma^{-1}\delta-\frac{m^*}{2(n-1)},
\]
which is the claimed observed log likelihood ratio.

The standard Neyman-Pearson lemma states that for two simple distributions with densities p_0 and p_1 relative to a common dominating measure, a test rejecting for p_1/p_0 above a threshold, with boundary randomization if necessary, maximizes power among tests of no greater Type-I error. Here both laws are fully specified because tau, z*, mu, and Sigma are fixed and known. The densities above provide a common Lebesgue dominating measure. The likelihood-ratio tests are measurable functions of the observed releases, so the lemma applies.

For completeness, the score is a constant minus a positive definite quadratic form centered at delta. Its finite level sets have Lebesgue measure zero, so its distribution has no atoms under either hypothesis. Varying the threshold gives every interior Type-I level; constant tests supply the endpoint levels zero and one. Thus no boundary randomization is needed for the displayed finite-threshold errors.

### 3. Exact scalar errors, including both target signs

Assume d=1 and write Sigma=sigma^2 with sigma>0. Define the signed quantities
\[
r=\frac{\sqrt n\,\delta}{\sigma},\qquad
Y=\frac{\sqrt n\,N_\tau}{\sigma}.
\]
Completing the square gives
\[
\ell_\tau=\frac12(m^*+\log c)-\frac{(Y-r)^2}{2(n-1)}.
\]
Hence its maximum is \(\gamma_{\max}=(m^*+\log c)/2\). For gamma>gamma_max the rejection region is empty. If gamma<=gamma_max, define
\[
b=\sqrt{(n-1)(m^*+\log c-2\gamma)}.
\]
The strict rejection region is
\[
r-b<Y<r+b.
\]
Its center is the signed value r, not necessarily the nonnegative value a=sqrt(n*m*).

Under H0, Y is standard normal. Therefore
\[
\alpha=\Phi(r+b)-\Phi(r-b).
\]
Under the alternative,
\[
Y\sim N(r/n,1/c).
\]
The standardized interval endpoints are
\[
(r\mp b-r/n)\sqrt c=\frac r{\sqrt c}\mp b\sqrt c.
\]
Integrating the two complementary tails yields
\[
\beta=\Phi\left(\frac r{\sqrt c}-b\sqrt c\right)
+\Phi\left(-\frac r{\sqrt c}-b\sqrt c\right).
\]
By \(\Phi(-x)=1-\Phi(x)\), the expression for alpha is unchanged when r is replaced by -r; the two terms in beta merely interchange. Both formulas therefore remain valid with r replaced by \(|r|=a=\sqrt{nm^*}\), proving the claimed formulas for every sign of delta.

At gamma=gamma_max, b=0 and the strict rejection interval is empty; the formulas give alpha=0 and beta=1. For larger thresholds the same errors hold. Equality boundaries have probability zero, so a non-strict convention would give identical errors. If delta=0, then r=a=0 and the same calculation applies without division by delta or its sign. For every fixed threshold, the resulting errors depend only on n and m*, not on tau or T.

### 4. Final-only observation and dilution

Continue in d=1. Put q=nT and \(W=\widehat\mu_T-\mu\). Under H0, the final sum contains q independent Gaussian observations; under the alternative it contains q-1 such observations and the fixed target. Thus
\[
W\sim N(0,\sigma^2/q)\quad(H_0),\qquad
W\sim N(\delta/q,(q-1)\sigma^2/q^2)\quad(H_1^\tau).
\]
The final-only log likelihood ratio is
\[
\ell_F=\frac12\log c_T-\frac{qW^2}{2(q-1)\sigma^2}
+\frac{q\delta W}{(q-1)\sigma^2}-\frac{m^*}{2(q-1)}
=\frac12(m^*+\log c_T)-\frac{q(W-\delta)^2}{2(q-1)\sigma^2},
\]
where \(c_T=q/(q-1)\). The same Neyman-Pearson argument applies to these two simple marginal laws.

For gamma<=gamma_max^(T)=(m*+log c_T)/2, the roots in the W coordinate are
\[
W_\pm=\delta\pm\sigma\sqrt{\frac{q-1}{q}}\sqrt{m^*+\log c_T-2\gamma}.
\]
Equivalently, with \(Y_T=\sqrt q\,W/\sigma\), \(r_T=\sqrt q\,\delta/\sigma\), and \(b_T=\sqrt{(q-1)(m^*+\log c_T-2\gamma)}\), rejection is the interval \(r_T-b_T<Y_T<r_T+b_T\). Under H0, Y_T is standard normal; under the alternative it has mean r_T/q and variance 1/c_T. Repeating the two interval integrations gives
\[
\alpha_F=\Phi(r_T+b_T)-\Phi(r_T-b_T),
\]
\[
\beta_F=\Phi\left(\frac{r_T}{\sqrt{c_T}}-b_T\sqrt{c_T}\right)
+\Phi\left(-\frac{r_T}{\sqrt{c_T}}-b_T\sqrt{c_T}\right).
\]
The same sign symmetry replaces r_T by \(a_T=|r_T|=\sqrt{qm^*}\). At the maximum threshold b_T=0, giving (alpha_F,beta_F)=(0,1); above it rejection is empty. Zero displacement is covered as before.

The inserted target has weight 1/n in the insertion batch mean but only 1/(nT) in the final mean. Its mean displacement is correspondingly reduced by a factor of T. Relative to the null standard deviation, its displacement changes from delta/(sigma*sqrt(n)) to delta/(sigma*sqrt(nT)); the relative variance reduction also changes from 1/n to 1/(nT). These facts explain dilution even when delta=0, when only the variance difference remains. The sequential test retains the insertion-batch experiment, whereas the final-only test averages across all nT observations. When T=1, q=n and the two tests and all their error formulas coincide.

## Source Repair Notes

The existing repair of theory_005 is retained: the multivariate quadratic coefficient is -n/[2(n-1)], as derived in the source appendix. A further local repair is recorded for theory_008: the roots at source line L000389 have incorrect center and half-width. The corrected roots above follow directly from the source's polynomial coefficients and yield its unchanged main-text error formulas. The signed-center correction in the reference proof is a formalization repair; the source itself uses a signed center at L000367.

## Obligation Closure

The proof explicitly establishes the batch laws and independence, observable recovery, likelihood-ratio cancellation including tau=1, every Gaussian coefficient, both scalar tail probabilities and sign symmetry, threshold boundaries, the final marginal experiment, and dilution including T=1 and zero displacement. Neyman-Pearson is the only external theorem invoked; its relevant statement and hypotheses are given above. No theorem-critical obligation remains unresolved.
