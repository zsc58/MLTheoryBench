# Reference Proof

## Audited Contract

The law P_0, hypothesized predictor f_*, and nonzero direction h are fixed as n increases. The function f_0 is the unique population risk minimizer. The true contributions varphi_0(W_i;h,f_*) are iid because they evaluate a fixed measurable function at iid observations. Estimated contributions may share validation-sample nuisance estimates and need not be independent. Neither a CLT nor a law of large numbers is applied directly to them.

The denominator is an uncentered second moment. It equals the variance under the null because of centering, but need not equal the variance under an alternative. The statistic is defined to be zero when its empirical denominator is zero. No finite-sample almost-sure positivity assumption is imposed.

The fixed-law, fixed-predictor, fixed-direction contract is recovered from source L000012-L000027 and L000082-L000099. The source explicitly allows validation-sample nuisance estimation at L000080. This theorem does not assert a result for local alternative sequences, validation-adaptively selected predictors or directions, or optional stopping.

## Audited Standard Background

The following standard-independent results are recorded in theory_016 and are invoked by the source at L000021-L000024 and L000820-L000858.

- If U_i are iid and E|U_1| is finite, their empirical average converges in probability to E[U_1].
- If U_i are iid with mean mu and finite variance v, then sqrt(n)(E_n[U]-mu) converges in distribution to N(0,v).
- If A_n converges in distribution to A and B_n converges in probability to a constant b, then (A_n,B_n) converges in distribution to (A,b). In particular, adding an o_p(1) remainder preserves a distributional limit. No independence between A_n and B_n is required.
- A measurable map that is continuous almost surely at the limiting random vector preserves convergence in distribution. The analogous continuous-mapping statement holds for convergence in probability.
- Cauchy-Schwarz gives E|U| <= sqrt(E[U^2]) when the second moment is finite. A bounded linear functional on a real Hilbert space has a unique Riesz representer. The latter representation is already explicitly assumed in the task.
- The square of a standard normal random variable has the chi-square distribution with one degree of freedom.

## Proof Structure and Obligations

The null numerator is handled by the assumed asymptotic linearity and the iid CLT. The denominator is handled by second-moment consistency and the integrable law of large numbers. Its positive population limit makes the zero-denominator completion asymptotically immaterial and permits continuous mapping. Under a fixed alternative, first-moment consistency and the law of large numbers identify a nonzero score mean, and division by the positive limiting second moment yields linear divergence. Each obligation is derived below; no specialized external theorem or unresolved nuisance-rate derivation is needed beyond the assumptions stated in the public task.

## Complete Proof

Write
\[
\bar\varphi_n=\mathbb E_n[\widehat\varphi(h,f_*)],\qquad
D_n=\mathbb E_n[\widehat\varphi(h,f_*)^2],
\]
and put
\[
\mu_* =\mathbb E[\varphi_0(h,f_*)],\qquad
m_* =\mathbb E[\varphi_0(h,f_*)^2].
\]
The notation m_* denotes a second moment, not an alternative-side variance. Under either hypothesis considered, the applicable assumptions give 0<m_*<infinity. Therefore
\[
\mathbb E|\varphi_0(h,f_*)|\leq\sqrt{m_*}<\infty.
\]
Consequently both the true contribution and its square are integrable. No fourth moment is required.

### Step 001: Null numerator

Under H_0, f_*=f_0. Assumption 1 gives mu_0=0, and Assumption 3 gives 0<m_0<infinity. The true contributions are iid, centered, and have variance m_0. The scalar CLT therefore gives
\[
\sqrt n\,\mathbb E_n[\varphi_0(h,f_0)]\Rightarrow N(0,m_0).
\]
Assumption 4 gives the explicit comparison
\[
\sqrt n\,\bar\varphi_n
=\sqrt n\,\mathbb E_n[\varphi_0(h,f_0)]+o_p(1).
\]
Slutsky's theorem yields
\[
\sqrt n\,\bar\varphi_n\Rightarrow N(0,m_0).
\]
This reconstructs the d=1 argument of source L000825-L000828, without treating the estimated evaluations as iid.

### Step 002: Denominator consistency and its domain

For either the null or an alternative satisfying Assumption 6, Assumption 5 with k=2 and the law of large numbers applied to the integrable true squared contribution give
\[
D_n
=\mathbb E_n[\varphi_0(h,f_*)^2]+o_p(1)
\xrightarrow{p}m_*.
\]
Since D_n is nonnegative and m_*>0,
\[
\Pr(D_n=0)
\leq\Pr\bigl(|D_n-m_*|>m_*/2\bigr)\longrightarrow0.
\]
Thus the public convention at D_n=0 does not impose a restriction on the sampling model.

For explicit use of continuous mapping, define privately on R x [0,infinity)
\[
Q(x,y)=\begin{cases}x^2/y,&y>0,\\0,&y=0.\end{cases}
\]
This is measurable and is continuous at every point (x,y) with y>0. The definition of the public statistic gives the exact identities
\[
T_n=Q(\sqrt n\,\bar\varphi_n,D_n),\qquad
T_n/n=Q(\bar\varphi_n,D_n),
\]
including on the event D_n=0.

This is the scalar form of the second-moment argument at source L000829-L000835. Under an alternative, its integrability comes from the finite second moment at f_* explicitly required by the source lemma and power proposition, not from the condition at f_0 alone.

### Step 003: Null calibration

Under H_0, Steps 001 and 002 and Slutsky's theorem yield
\[
(\sqrt n\,\bar\varphi_n,D_n)
\Rightarrow (\sqrt{m_0}\,Z,m_0),\qquad Z\sim N(0,1).
\]
Because m_0>0, Q is continuous at every possible limiting point. Continuous mapping gives
\[
T_n\Rightarrow Q(\sqrt{m_0}\,Z,m_0)=Z^2\sim\chi^2_1.
\]
No independence of numerator and denominator is needed. This closes the scalar null target, corresponding to source L000836-L000844.

### Step 004: Fixed-alternative power

Suppose f_* differs from f_0 and the directional signal is nonzero. Assumption 2 gives
\[
\mu_* =\langle h,h^*(f_*)\rangle\ne0.
\]
The integrability established above allows the law of large numbers for the true contributions. Combining it with Assumption 5 for k=1 gives
\[
\bar\varphi_n
=\mathbb E_n[\varphi_0(h,f_*)]+o_p(1)
\xrightarrow{p}\mu_*.
\]
Step 002 gives D_n ->p m_*. Since m_*>0, continuous mapping yields
\[
\frac{T_n}{n}=Q(\bar\varphi_n,D_n)
\xrightarrow{p}\lambda:=\frac{\mu_*^2}{m_*}>0.
\]
Here lambda is a fixed positive constant because P_0, f_*, and h are fixed. For any fixed finite real c_alpha, choose n sufficiently large that n lambda/2 > c_alpha. Then
\[
\Pr(T_n>c_\alpha)
\geq\Pr(T_n/n>\lambda/2)\longrightarrow1.
\]
This also proves T_n ->p infinity. It covers alternatives with zero centered variance but nonzero mean; only the positive finite second moment appearing in the statistic is needed. This is the scalar argument of source L000845-L000858.

## Closure Audit

The sampling and domain obligations, null CLT transfer, denominator consistency, zero-denominator handling, null continuous-mapping argument, alternative mean identification, and rejection-probability limit are all closed. The needed external results are standard independent results with their relevant statements and hypotheses supplied above. No verification of application-specific nuisance rates is claimed: their required effects are precisely the public asymptotic-linearity and moment-consistency assumptions. The existing source repair changing the alternative label from H_0 to H_1 is retained. There is no unresolved ground-truth proof obligation.
