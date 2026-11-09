# Reference Proof

## Proof Structure

1. Compute the one-step watermarked green probability by aggregating the Dirichlet mass on the green list and evaluating the logit-shift transform.
2. Derive the null Gaussian limit from independent Bernoulli green indicators.
3. Convert mutual-information decay to geometric alpha-mixing and apply the stationary mixing CLT under the alternative.
4. Insert the two limits into the detector threshold, distinguishing the normal power surrogate from its fixed-parameter asymptotic justification.

## Complete Proof

Let m=|V| and g=\gamma m. Since \gamma\in(0,1) and g is an integer, 1\leq g<m. For a fixed green list G, write Y=\sum_{v\in G}\sigma_v. Under the uniform Dirichlet law, aggregation gives Y\sim\operatorname{Beta}(g,m-g), with \mathbb EY=\gamma. If the unwatermarked green mass is y, adding \delta to every green logit multiplies its total mass by e^\delta, hence the conditional green probability is f(y)=e^\delta y/[1+(e^\delta-1)y]. Therefore \gamma'=\mathbb E f(Y). The beta integral for this expectation is Euler's integral for {}_2F_1 with parameters 1,g+1,m+1 and argument -(e^\delta-1); its condition m+1>g+1>0 holds. It gives
\[
\gamma'=e^\delta\gamma\,{}_2F_1(1,g+1;m+1;-(e^\delta-1)).
\]
Also f'(y)=e^\delta/[1+(e^\delta-1)y]^2\leq e^\delta on [0,1]. Since \operatorname{Var}(Y)=g(m-g)/[m^2(m+1)]=O(m^{-1}), Cauchy-Schwarz yields |\mathbb E f(Y)-f(\gamma)|=O(m^{-1/2}), and thus
\[
\gamma'=\frac{e^\delta\gamma}{1+\gamma(e^\delta-1)}+O(m^{-1/2}).
\]
Here the constants may depend on the fixed \gamma and \delta. Moreover, f(y)-y=(e^\delta-1)y(1-y)/[1+(e^\delta-1)y]>0 for 0<y<1. The beta law is supported in (0,1), so \gamma'>\gamma; also \gamma'<1.

Under the null, condition on the entire token sequence. The green lists remain independent uniform g-subsets of V, so the conditional joint law of the indicators is the product of Bernoulli(\gamma) laws, independent of the conditioned token values. Averaging establishes that I_i are i.i.d. Bernoulli(\gamma). Hence S_n has mean n\gamma, variance n\gamma(1-\gamma), and (S_n-n\gamma)/\sqrt{n\gamma(1-\gamma)}\Rightarrow N(0,1). The stated normal-quantile rejection rule consequently has asymptotic null level \alpha.

For the alternative, let \mathcal F_{-\infty}^{j}=\sigma(I_i:i\leq j) and \mathcal F_{j+k}^{\infty}=\sigma(I_i:i\geq j+k). The assumed information bound is uniform in j. The standard inequality 2\alpha(\mathcal U,\mathcal V)\leq I(\mathcal U;\mathcal V)^{1/2} implies that the strong-mixing coefficient satisfies \alpha(k)\leq\sqrt C\rho^{k/2}/2. The relevant standard stationary strong-mixing CLT states: if a strictly stationary centered sequence (X_i) has \mathbb E|X_1|^{2+\eta}<\infty for some \eta>0, \sum_{k\geq1}\alpha(k)^{\eta/(2+\eta)}<\infty, and a positive limiting variance \tau^2=\lim_{n\to\infty}n^{-1}\operatorname{Var}(\sum_{i=1}^nX_i), then n^{-1/2}\sum_{i=1}^nX_i\Rightarrow N(0,\tau^2). Apply this with X_i=I_i-\gamma' and \eta=1. Stationarity is assumed, |X_i|\leq1 supplies the third moment, geometric decay makes \sum_k\alpha(k)^{1/3} finite, and the assumed long-run variance is \sigma^2>0. Consequently,
\[
\sqrt n(S_n/n-\gamma')\Rightarrow N(0,\sigma^2).
\]
Writing \sigma^2=c\gamma'(1-\gamma') defines c>0.

Under the alternative, the rejection event is
\[
\frac{S_n-n\gamma'}{\sqrt n\,\sigma}>
\frac{z_{1-\alpha}\sqrt{\gamma(1-\gamma)}-\sqrt n(\gamma'-\gamma)}{\sigma}.
\]
Replacing the standardized count by its limiting standard normal law gives the stated normal surrogate
\[
\Pr_\delta(\mathrm{reject})\approx\Phi\!\left(\frac{\sqrt n(\gamma'-\gamma)-z_{1-\alpha}\sqrt{\gamma(1-\gamma)}}{\sqrt{c\gamma'(1-\gamma')}}\right).
\]
A CLT alone does not establish a nontrivial Gaussian tail approximation uniformly at this moving threshold. For fixed m, \gamma, \delta, \alpha, and alternative law, however, \gamma'>\gamma makes the displayed threshold tend to -\infty. The standardized counts are tight by the CLT, so actual power tends to one; the normal surrogate also tends to one. Their absolute difference is therefore o(1). No finite-sample identity, error rate, or uniform approximation over varying parameters is claimed.
