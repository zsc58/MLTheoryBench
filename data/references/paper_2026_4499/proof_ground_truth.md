# Reference Proof

## Proof Structure

Work conditionally on the fixed current data under the stipulated Gaussian surrogate. Represent the probit comparison by an equivalent Gaussian-noise observation model, establish its predictive probabilities and joint moments with any function evaluation, derive Gaussian regression and the two truncated first moments, and substitute into the defining knowledge-gradient expectation. Exactness is relative to this current surrogate; it does not assert that the posterior from historical preference observations was exactly Gaussian.

## Complete Proof

### Step 001: Observation model and predictive probabilities

Fix the queried pair \(a,b\). All probabilities and expectations below use the current surrogate law, with the current data held fixed. Let
\[
d=f(a)-f(b),\quad \mu_d=m(a)-m(b),\quad v_d=\operatorname{Var}(d),\quad c_x=\operatorname{Cov}(f(x),d),
\]
and set \(s=\sqrt{v_d+1}\) and \(t=\mu_d/s\). Finite-dimensional Gaussianity implies that these moments are finite. In particular, \(s\geq1\) and \(t\) is finite.

On an enlarged probability space introduce \(\varepsilon\sim N(0,1)\), independent of the entire surrogate, and put \(Z=d+\varepsilon\). Define \(\widetilde Y=+\) when \(Z\geq0\) and \(\widetilde Y=-\) otherwise. Conditional on \(f\),
\[
\Pr(\widetilde Y=+\mid f)=\Pr(\varepsilon\geq-d\mid f)=\Phi(d).
\]
Thus \((f,\widetilde Y)\) has the same joint law as \((f,Y)\). We may compute all the desired conditional means using this realization; equality of the original and auxiliary events on an already fixed probability space is not required.

For each \(x\), \((f(x),Z)\) is jointly Gaussian, with means \((m(x),\mu_d)\), \(\operatorname{Var}(Z)=s^2\), and \(\operatorname{Cov}(f(x),Z)=c_x\). Consequently,
\[
\Pr(Y=+)=\Pr(Z\geq0)=\Phi(t),\qquad
\Pr(Y=-)=\Pr(Z<0)=\Phi(-t).
\]
Both probabilities are strictly positive because \(t\) is finite, and \(\Pr(Z=0)=0\).

### Step 002: Regression and truncated first moments

For a fixed \(x\), define the Gaussian residual
\[
R_x=f(x)-m(x)-\frac{c_x}{s^2}(Z-\mu_d).
\]
It has mean zero and covariance zero with \(Z\). Jointly Gaussian variables with zero covariance are independent: their joint Gaussian characteristic function factors into the two marginal characteristic functions. This statement also covers a deterministic residual. Therefore
\[
\mathbb E[f(x)\mid Z]=m(x)+\frac{c_x}{s^2}(Z-\mu_d).
\]
No nonsingularity assumption on the covariance of \((f(x),Z)\) is needed; only \(s^2>0\), already verified, is used.

Let \(U=(Z-\mu_d)/s\), so \(U\sim N(0,1)\). Since \(\phi'(u)=-u\phi(u)\) and \(\phi\) vanishes at both infinities,
\[
\int_{-t}^{\infty}u\phi(u)\,du=\phi(t),\qquad
\int_{-\infty}^{-t}u\phi(u)\,du=-\phi(t).
\]
Dividing by the respective event probabilities gives
\[
\mathbb E[Z-\mu_d\mid Z\geq0]=s\frac{\phi(t)}{\Phi(t)},\qquad
\mathbb E[Z-\mu_d\mid Z<0]=-s\frac{\phi(t)}{\Phi(-t)}.
\]
These calculations directly establish the needed truncated-Gaussian mean identity; no unproved ESN moment formula is required.

### Step 003: Both posterior means

The conditioning events are functions of \(Z\), so the conditional-expectation tower property and Step 002 yield
\[
\begin{aligned}
\mu_+(x)
&=\mathbb E[f(x)\mid Y=+]\\
&=m(x)+\frac{c_x}{s^2}\mathbb E[Z-\mu_d\mid Z\geq0]\\
&=m(x)+\frac{c_x}{s}\frac{\phi(t)}{\Phi(t)},
\end{aligned}
\]
and
\[
\begin{aligned}
\mu_-(x)
&=\mathbb E[f(x)\mid Y=-]\\
&=m(x)+\frac{c_x}{s^2}\mathbb E[Z-\mu_d\mid Z<0]\\
&=m(x)-\frac{c_x}{s}\frac{\phi(t)}{\Phi(-t)}.
\end{aligned}
\]
Each conditional mean exists because a Gaussian evaluation is integrable and each outcome has positive probability. The argument holds for every \(x\in\mathcal X\).

### Step 004: Domain and degenerate cases

Neither the mean formulas nor the outcome probabilities require any spatial maximum to exist. For the KG assertion, the public task separately assumes that \(m,\mu_+,\mu_-\) have finite attained maxima. Hence their three \(V\)-values are real, and \(V(\mu_Y)\) is a measurable, integrable random variable taking only two values. No measurability of an optimizer selection is needed.

If \(v_d=0\), then \(d=\mu_d\) almost surely, so \(c_x=0\) for every \(x\). Both updated means equal \(m\), and the KG value, when defined, is zero. This includes \(a=b\), when also \(\mu_d=t=0\) and both outcome probabilities equal \(1/2\). If \(f(x)\) is deterministic or merely has \(c_x=0\), its updated mean remains \(m(x)\). Thus zero variances and singular finite-dimensional Gaussian laws introduce no omitted case.

### Step 005: Knowledge gradient

By the defining predictive expectation and the two possible outcomes,
\[
\begin{aligned}
\operatorname{KG}(a,b)
&=\mathbb E_Y[V(\mu_Y)]-V(m)\\
&=\Pr(Y=+)V(\mu_+)+\Pr(Y=-)V(\mu_-)-V(m)\\
&=\Phi(t)V(\mu_+)+\Phi(-t)V(\mu_-)-V(m).
\end{aligned}
\]
This is the claimed exact expression. The outcome expectation and conditional means have been evaluated analytically; the spatial maxima appearing in \(V\) remain part of the expression and are not asserted to have analytic maximizers.

## Obligation Closure

All theorem-critical obligations are closed in Steps 001–005. The source's extended-skew-normal route is an alternative justification of the same truncated mean, not an unresolved dependency of this proof.
