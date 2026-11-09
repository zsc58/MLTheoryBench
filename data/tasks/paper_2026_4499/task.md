# Problem

## Setup

Fix current data \(\mathcal D\), and work throughout under a real-valued Gaussian-process surrogate law \(f\mid\mathcal D\) on a nonempty design space \(\mathcal X\), with mean \(m:\mathcal X\to\mathbb R\) and covariance \(C:\mathcal X^2\to\mathbb R\). Every finite collection of function values is jointly Gaussian. All probabilities, expectations, variances, and covariances below are under this current surrogate and the specified observation model, with \(\mathcal D\) held fixed.

Fix a queried pair \(a,b\in\mathcal X\) before observing its outcome \(Y\in\{+,-\}\). The unit-noise probit observation model is
\[
\Pr(Y=+\mid f)=\Phi\bigl(f(a)-f(b)\bigr),\qquad
\Pr(Y=-\mid f)=1-\Pr(Y=+\mid f),
\]
where \(\phi\) and \(\Phi\) are the standard normal density and cdf. Define
\[
\mu_d=m(a)-m(b),\quad v_d=\operatorname{Var}(f(a)-f(b)),\quad c_x=\operatorname{Cov}(f(x),f(a)-f(b)),
\]
\[
s=\sqrt{v_d+1},\qquad t=\mu_d/s.
\]
For \(y\in\{+,-\}\), let
\[
\mu_y(x)=\mathbb E[f(x)\mid Y=y]
\]
be the one-step look-ahead posterior mean under this model.

For a function \(g:\mathcal X\to\mathbb R\) having a finite attained maximum, write
\[
V(g)=\max_{x\in\mathcal X}g(x).
\]
For the knowledge-gradient assertion, assume that \(m,\mu_+,\mu_-\) each have a finite attained maximum. Define the one-step preferential knowledge gradient by
\[
\operatorname{KG}(a,b)=\mathbb E_Y\bigl[V(\mu_Y)\bigr]-V(m),
\]
where the expectation is over the predictive outcome of the fixed query.

## Task

Prove that the one-step look-ahead posterior means after the two possible preference outcomes are
\[
\mu_+(x)=m(x)+\frac{c_x}{s}\frac{\phi(t)}{\Phi(t)},\qquad
\mu_-(x)=m(x)-\frac{c_x}{s}\frac{\phi(t)}{\Phi(-t)}
\]
for every \(x\in\mathcal X\). Also prove that \(\Pr(Y=+)=\Phi(t)\), \(\Pr(Y=-)=\Phi(-t)\), and hence that
\[
\operatorname{KG}(a,b)=\Phi(t)V(\mu_+)+\Phi(-t)V(\mu_-)-V(m).
\]
