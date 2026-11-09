# Problem

## Statistical experiment and sampling map

Consider sequences with n\to\infty, d=d_n\to\infty, and \gamma_n=d/n\to\gamma\in(0,\infty). Let \Sigma=\Sigma_n\succeq0 be deterministic real d\times d matrices with \sup_n\|\Sigma_n\|_{\mathrm{op}}<\infty and convergent empirical spectral distributions. Let \mu=\mu_n\in\mathbb R^d be deterministic.

For independent z_1,\ldots,z_n\sim N(0,I_d), observe y_i=\mu+\Sigma^{1/2}z_i and set
\[
\widehat\Sigma=\frac1n\sum_{i=1}^n(y_i-\mu)(y_i-\mu)^T.
\]
Use \mu as the denoiser location; no conditioning on the empirical mean is intended. All expectations, covariances, and variances below are over these observations only. The vectors \bar x=\bar x_n and v=v_n are deterministic, fixed independently of the observations, and have uniformly bounded Euclidean norms.

For \sigma>0 define
\[
D_{\widehat\Sigma}(x;\sigma)=\mu+(\widehat\Sigma+\sigma^2I)^{-1}\widehat\Sigma(x-\mu).
\]
For T>0 and 0\le\sigma\le T define
\[
\widehat x(x_T,\sigma)=\mu+(\widehat\Sigma+\sigma^2I)^{1/2}(\widehat\Sigma+T^2I)^{-1/2}(x_T-\mu).
\]
Take x_T=\mu+T\bar x. The terminal object in this problem is the infinite-initial-noise limit, taken at each fixed dimension before the limit n\to\infty:
\[
X_\infty:=\lim_{T\to\infty}\widehat x(\mu+T\bar x,0)=\mu+\widehat\Sigma^{1/2}\bar x.
\]
All square roots are the positive semidefinite square roots. Singular population and empirical covariances are permitted.

## Deterministic quantities

Write \tau(B)=d^{-1}\operatorname{Tr}B. For \lambda>0 let \kappa(\lambda)>0 solve
\[
\kappa(\lambda)-\lambda
=\gamma_n\kappa(\lambda)\tau\!\left[\Sigma(\Sigma+\kappa(\lambda)I)^{-1}\right].
\]
Thus the aspect ratio in this finite-dimensional equation is \gamma_n=d/n, not its limit \gamma. Dependence of \kappa and all subsequent quantities on n is suppressed.

For a,b>0 define
\[
\operatorname{df}_1(a)=\operatorname{Tr}[\Sigma(\Sigma+aI)^{-1}],\qquad
\operatorname{df}_2(a)=\operatorname{Tr}[\Sigma^2(\Sigma+aI)^{-2}],
\]
\[
\operatorname{df}_2(a,b)=\operatorname{Tr}[\Sigma^2(\Sigma+aI)^{-1}(\Sigma+bI)^{-1}].
\]
For u,w>0 put
\[
K_n(u,w)=\Sigma(\Sigma+\kappa(u^2)I)^{-1}(\Sigma+\kappa(w^2)I)^{-1},
\]
\[
H_n(u,w)=
\frac{\kappa(u^2)\kappa(w^2)}{n-\operatorname{df}_2(\kappa(u^2),\kappa(w^2))}
[v^TK_n(u,w)v][\bar x^TK_n(u,w)\bar x],
\qquad
V_n=\frac4{\pi^2}\int_0^\infty\!\int_0^\infty H_n(u,w)\,du\,dw.
\]
Integrals over positive arguments are improper integrals; no value of \kappa(0) is required.

## Alignment and integration hypotheses

The negligible weighted-alignment condition for the variance claim is the following quantitative condition. Define
\[
J_n(u,w)=
\frac{\kappa(u^2)\kappa(w^2)}{n-\operatorname{df}_2(\kappa(u^2),\kappa(w^2))}
[v^TK_n(u,w)\bar x]^2.
\]
Along indices with V_n>0, assume
\[
\frac{\int_0^\infty\!\int_0^\infty J_n(u,w)\,du\,dw}{V_n}\longrightarrow0.
\]

The variance statement is made under integral uniformity at its retained scale. To specify this hypothesis, let
\[
Z_n(u)=v^T\bigl[D_{\widehat\Sigma}(\mu+\bar x;u)-\mu\bigr],
\qquad C_n(u,w)=\operatorname{Cov}(Z_n(u),Z_n(w)).
\]
On the subsequence V_n>0, each of the two families of functions
\[
\left\{C_n/V_n\right\}_n,\qquad \left\{H_n/V_n\right\}_n
\]
is assumed uniformly integrable and tight on (0,\infty)^2 with Lebesgue measure. Explicitly, for either family f_n these conditions mean
\[
\sup_n\int_{(0,\infty)^2}|f_n|<\infty,
\quad
\lim_{M\to\infty}\sup_n\int_{\{|f_n|>M\}}|f_n|=0,
\]
\[
\lim_{R\to\infty}\sup_n
\int_{(0,\infty)^2\setminus[R^{-1},R]^2}|f_n|=0.
\]
The alignment and integration hypotheses are vacuous on indices with V_n=0. They do not assert any formula for C_n.

## Claims to prove

First, establish the expectation equivalent
\[
\mathbb E X_\infty\ \approx\
\mu+\frac2\pi\int_0^\infty
\Sigma(\Sigma+\kappa(u^2)I)^{-1}\bar x\,du.
\]
Here the vector symbol \approx means that, for every deterministic sequence a_n with uniformly bounded Euclidean norm, the scalar obtained by multiplying the difference of the two sides by a_n^T converges to zero.

Show also that the deterministic map on the right shrinks each population eigenspace at least as much as the population map \mu+\Sigma^{1/2}\bar x: its coefficient at an eigenvalue s is between 0 and \sqrt s. At s=0 both coefficients are zero, and at each positive eigenvalue the deterministic finite-dimensional coefficient is strictly less than \sqrt s. No uniformly positive limiting gap is asserted.

Finally, prove the leading variance equivalent
\[
\operatorname{Var}(v^TX_\infty)\ \approx\
\frac4{\pi^2}\int_0^\infty\!\int_0^\infty
\frac{\kappa(u^2)\kappa(w^2)}{n-\operatorname{df}_2(\kappa(u^2),\kappa(w^2))}
\Big[v^T\Sigma(\Sigma+\kappa(u^2)I)^{-1}(\Sigma+\kappa(w^2)I)^{-1}v\Big]
\Big[\bar x^T\Sigma(\Sigma+\kappa(u^2)I)^{-1}(\Sigma+\kappa(w^2)I)^{-1}\bar x\Big]du\,dw.
\]
For this scalar claim, \approx means \operatorname{Var}(v^TX_\infty)/V_n\to1 along indices with V_n>0. On indices with V_n=0, prove that the variance is exactly zero. Include well-definedness and finiteness of the displayed deterministic quantities and improper integrals.
