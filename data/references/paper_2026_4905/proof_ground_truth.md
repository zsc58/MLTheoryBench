# Reference Proof

## Theorem-Critical Obligations

1. Establish that the surrogate and estimator expectations are well-defined, and verify the surrogate's mean under each applicable true-label case.
2. Identify the selected-label conditional mean and justify indicator weighting with fixed nuisance values.
3. Derive the IPS expectation and conclude unbiasedness under correct propensities.
4. Derive the DR expectation and prove both the correct-propensity and correct-imputation branches.

## Ambient Contract and Standard Background

The proof is pointwise in the fixed predictor, loss, and estimated functions. They are constants with respect to the annotation and observability draws, not same-sample fitted random variables declared fixed after observing those draws. The population and all latent preferences are fixed. All probabilities and expectations below use this experiment.

The standard conditioning result associated with theory_010 is: if \(Z\) is integrable and \(\mathcal G\) is a sigma-field, then \(\mathbb E[\mathbb E[Z\mid\mathcal G]]=\mathbb E[Z]\). This follows by taking the whole probability space in the defining integral property of conditional expectation. Its relevant indicator consequence is derived explicitly below, so no specialized external theorem or unproved paper-specific result is needed.

## Complete Proof

### Surrogate Values, Finiteness, and Conditional Means

Write
\[
a_i=\ell(\hat r_\theta(x_i),0),\qquad b_i=\ell(\hat r_\theta(x_i),1),\qquad d=1-\rho_{01}-\rho_{10}>0.
\]
With exact noise rates, the determinant of the defining two-equation system is \(d\). Its solution is
\[
s_i(1):=\widetilde\ell(\hat r_\theta(x_i),1)
=\frac{(1-\rho_{10})b_i-\rho_{01}a_i}{d},
\]
\[
s_i(0):=\widetilde\ell(\hat r_\theta(x_i),0)
=\frac{(1-\rho_{01})a_i-\rho_{10}b_i}{d}.
\]
Both values are finite. The population is finite and nonempty, each \(\hat p_i\) is a fixed positive finite number, and each imputation is a fixed finite number. Consequently every estimator summand has finitely many finite possible values. All expectations and conditional expectations used here are therefore integrable. No uniform bound away from zero beyond these pointwise positive denominators is needed.

For a unit whose fixed preference is \(r_i^*=1\), the channel probabilities and the defining equations give
\[
\mathbb E[\widetilde\ell_i\mid x_i]
=(1-\rho_{01})s_i(1)+\rho_{01}s_i(0)=b_i.
\]
For a unit whose fixed preference is \(r_i^*=0\), they give
\[
\mathbb E[\widetilde\ell_i\mid x_i]
=\rho_{10}s_i(1)+(1-\rho_{10})s_i(0)=a_i.
\]
These are case distinctions on fixed labels; they do not condition on an absent class. Equivalently, either identity follows immediately from the corresponding defining surrogate equation, without explicitly inverting the system.

Because each unit's observability is independent of its annotation noise conditional on its fixed \((x_i,r_i^*)\), selection does not change that unit's annotation channel. Since \(p_i>0\), the quantity
\[
m_i:=\mathbb E[\widetilde\ell_i\mid x_i,o_i=1]
\]
is well-defined and satisfies
\[
m_i=\ell(\hat r_\theta(x_i),r_i^*).
\]

### Indicator Weighting and IPS

For any two fixed finite numbers \(z(0),z(1)\), summation over the binary label gives
\[
\begin{aligned}
\mathbb E[o_i z(r_i)]
&=\sum_{t\in\{0,1\}}z(t)\Pr(o_i=1,r_i=t\mid x_i)\\
&=p_i\sum_{t\in\{0,1\}}z(t)\Pr(r_i=t\mid x_i,o_i=1)\\
&=p_i\mathbb E[z(r_i)\mid x_i,o_i=1].
\end{aligned}
\]
This identity does not require conditioning on \(o_i=0\), so it also holds when \(p_i=1\). Applied to the surrogate and using the fixed denominator, it yields
\[
\mathbb E\left[\frac{o_i}{\hat p_i}\widetilde\ell_i\right]
=\frac{p_i}{\hat p_i}m_i
=\frac{p_i}{\hat p_i}\ell(\hat r_\theta(x_i),r_i^*).
\]
Linearity of a finite sum therefore gives
\[
\mathbb E[L_{\mathrm{IPS}}^*]-L_{\mathrm{ideal}}
=\frac1n\sum_{i=1}^n\left(\frac{p_i}{\hat p_i}-1\right)\ell(\hat r_\theta(x_i),r_i^*).
\]
If \(\hat p_i=p_i\) for every unit, every summand vanishes, proving the IPS claim.

### DR and Both Robustness Branches

Abbreviate \(\varepsilon_i=\hat\varepsilon_i\). These values and the denominators are fixed. The indicator identity, or its application to the fixed function \(s_i(t)-\varepsilon_i\), gives
\[
\begin{aligned}
\mathbb E\left[\varepsilon_i+\frac{o_i}{\hat p_i}(\widetilde\ell_i-\varepsilon_i)\right]
&=\varepsilon_i+\frac{p_i}{\hat p_i}(m_i-\varepsilon_i)\\
&=m_i+\left(1-\frac{p_i}{\hat p_i}\right)(\varepsilon_i-m_i).
\end{aligned}
\]
Consequently,
\[
\mathbb E[L_{\mathrm{DR}}^*]-L_{\mathrm{ideal}}
=\frac1n\sum_{i=1}^n\left(1-\frac{p_i}{\hat p_i}\right)(\varepsilon_i-m_i).
\]
If \(\hat p_i=p_i\) for all units, the first factor in each summand is zero, regardless of the fixed imputation values. This proves the correct-propensity branch.

If instead \(\varepsilon_i=m_i=\mathbb E[\widetilde\ell_i\mid x_i,o_i=1]\) for all units, the second factor in each summand is zero, regardless of the fixed positive propensity estimates. This proves the correct-imputation branch. Thus under either condition \(\mathbb E[L_{\mathrm{DR}}^*]=L_{\mathrm{ideal}}\).

## Closure and Scope

All four theorem-critical obligations have been explicitly derived. The argument permits zero noise rates, zero losses or imputations, \(p_i=1\), a population of one unit, a population containing only one preference class, and an empty realized observed set. It uses no cross-unit independence and no sign restriction on surrogate or imputed losses. It does not claim unbiasedness for models or nuisances adaptively fitted to the evaluation draws, nor does it establish noise-rate identification, variance reduction, or unbiasedness of a learned optimizer. The source's prior-work attribution supplies no unresolved dependency because the relevant calculations are reproduced here in full.
