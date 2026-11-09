# Reference Proof

## Contract and Proof Obligations

The dictionary, its population operators, the positive regularization parameter, the number of retained eigenvalues, and the fold count are fixed. The fold size is the common value \(N_f=N/F\). The population eigenvalues are those of the regularized covariance-gradient RKHS operator defined in the task, not of a degree-normalized Markov operator.

The concentration inequality is a primitive assumption. No external concentration theorem, independence between estimates, spectral-projector theorem, or approximation-consistency theorem is needed. The obligations are to control all eigenvalue errors, transfer that control to risks, handle the margin boundary and empirical ties, and take the fixed-parameter limit.

## Complete Proof

Write \(\mathcal D=\{\theta_1,\ldots,\theta_M\}\). All scores are measurable finite sums of real-valued estimates. Since the dictionary is finite and nonempty, an empirical minimizer exists; a fixed ordering supplies a measurable tie rule if needed. The result holds for every measurable minimizer allowed by the task.

If \(M=1\), the selector necessarily equals \(\theta^*\), so both conclusions hold. Assume henceforth that there are competitors.

For \(t>0\), define
\[
E_t=\bigcap_{\theta\in\mathcal D}\bigcap_{f=1}^F\bigcap_{j=1}^r
\left\{\left|\widehat\mu_j^{(f)}(\theta)-\mu_j^\infty(\theta)\right|<t\right\}.
\]
For every \(0<s<t\), if \(E_t\) fails then at least one of these errors is greater than \(s\). The assumed concentration bound and the union bound therefore give
\[
\mathbb P(E_t^c)
\le \sum_{\theta,f,j}\mathbb P\left(\left|\widehat\mu_j^{(f)}(\theta)-\mu_j^\infty(\theta)\right|>s\right)
\le 2MFr\exp(-cN_f s^2).
\]
Letting \(s\uparrow t\) in this numerical upper bound yields
\[
\mathbb P(E_t^c)\le 2MFr\exp(-cN_f t^2).
\]
This also handles possible atoms at the threshold. No independence is used.

On \(E_t\), for every \(\theta\in\mathcal D\),
\[
\left|\widehat R_N(\theta)-R(\theta)\right|
\le \frac1F\sum_{f=1}^F\sum_{j=1}^r
\left|\widehat\mu_j^{(f)}(\theta)-\mu_j^\infty(\theta)\right|
<rt.
\]
Consequently, for every \(\theta\ne\theta^*\),
\[
\widehat R_N(\theta)-\widehat R_N(\theta^*)
>R(\theta)-R(\theta^*)-2rt
\ge\Delta-2rt.
\]
Choose \(t=\Delta/(2r)\). The strict inequality gives
\(\widehat R_N(\theta)>\widehat R_N(\theta^*)\) for every competitor, including competitors whose population risk difference is exactly \(\Delta\). Thus \(\theta^*\) is the unique empirical minimizer on \(E_t\), and every allowed selector equals it there. Hence
\[
\mathbb P(\widehat\theta_N\ne\theta^*)
\le \mathbb P(E_{\Delta/(2r)}^c)
\le 2MFr\exp\left(-\frac{cN_f\Delta^2}{4r^2}\right).
\]
The argument applies whenever the assumed tails hold, so in particular for all sufficiently large admissible sample sizes.

Because \(M,F,r,c,\Delta\) are fixed, \(c,\Delta>0\), and \(N_f\to\infty\), this upper bound tends to zero. On the finite dictionary with its discrete topology, this is exactly convergence in probability of \(\widehat\theta_N\) to \(\theta^*\).

## Constant and Source Audit

The factor \(F\) is retained explicitly. For fixed \(F\), one may write the prefactor as \(C_FMr\), with \(C_F=2F\), but one may not replace the numerical value \(2MFr\) by \(2Mr\) while keeping the same exponent constant without another argument. The source's strict-margin endpoint is repaired by the strict event above rather than by reducing the exponent. All proof obligations for this conditional selection theorem are closed.
