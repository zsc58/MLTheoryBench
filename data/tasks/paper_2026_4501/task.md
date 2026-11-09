# Problem

## Setup

Let \(n,m,M\) be positive integers with \(1\le m\le n\) and \(M\ge2\), and let \(\Omega\) be a uniformly random subset of \(\{1,\ldots,n\}\) of size \(m\). Let \(A=P_\Omega\in\mathbb R^{m\times n}\) be the corresponding coordinate-selection matrix. The realized matrix \(A\) is known when performing posterior inference.

Consider the Bayesian inverse model
\[
Y=AX+\varepsilon,
\qquad \varepsilon\sim N(0,\sigma^2I_m),
\]
with \(\sigma,\tau>0\). The prior distribution of \(X\) is the isotropic Gaussian mixture
\[
\pi=\sum_{j=1}^M w_j\,N(\mu_j,\tau^2I_n),
\qquad w_j>0,\quad \sum_jw_j=1,
\]
where the means and weights are fixed and \(|\mu_{j,i}|\le1\) for every \(i,j\). In this Bayesian model, \(X\), \(\varepsilon\), and \(\Omega\) are independent. Assume the prior weights have bounded ratios: \(1/C\le w_i/w_j\le C\) for all \(i,j\), for some \(C\ge1\).

For the data-generating experiment, fix a distinguished true component \(j_0\in\{1,\ldots,M\}\) and generate
\[
X^*=\mu_{j_0}+\xi,\quad \xi\sim N(0,\tau^2I_n),\qquad
Y^*=AX^*+\varepsilon,
\]
where \(\xi,\varepsilon\), and \(\Omega\) are mutually independent. Assume every competitor is separated from the true mean by
\[
\frac1n\|\mu_j-\mu_{j_0}\|_2^2\ge\Delta>0\qquad(j\ne j_0).
\]
Set \(\Sigma=\sigma^2I_m+\tau^2AA^T\), define the measurement scores
\[
q_j(y)=\tfrac12\|\Sigma^{-1/2}(y-A\mu_j)\|_2^2,
\]
and let \(q_{(1)}(y)\le q_{(2)}(y)\) be the two smallest scores. Define
\[
g(y)=\frac{q_{(2)}(y)-q_{(1)}(y)}{m}.
\]
In the Bayesian mixture model, \(J\) denotes the component label, with prior probabilities \(w_j\) and \(X\mid J=j\sim N(\mu_j,\tau^2I_n)\). Throughout, \(\pi(\cdot\mid y)\) and \(\Pr(J\ne j_0\mid y)\) mean the Bayesian posterior distribution and probability conditional on \(Y=y\) and on the realized \(A\), not conditional on the true label \(j_0\). Use the posterior defined by Bayes' rule with the Gaussian likelihood for every \(y\in\mathbb R^m\).

For probability measures \(P,Q\) on \(\mathbb R^n\), use the total-variation distance
\[
\|P-Q\|_{\mathrm{TV}}=\sup_{B\in\mathcal B(\mathbb R^n)}|P(B)-Q(B)|,
\]
where \(\mathcal B(\mathbb R^n)\) is the collection of Borel sets.

## Task

Prove the following integrated theorem. With probability at least
\[
1-2(M-1)\exp(-m\Delta^2/32)
 -2(M-1)\exp\left(-\frac{m\Delta^2}{512(\sigma^2+\tau^2)}\right),
\]
over the random set \(\Omega\) and the Gaussian noises in the data-generating experiment, the observed data \(Y^*=y\) have a unique score minimizer \(j_0\) and satisfy
\[
g(y)\ge \bar\delta:=\frac{\Delta}{8(\sigma^2+\tau^2)}.
\]
Moreover, for every realized \(A\) and every observation \(y\) with this gap and minimizer \(j_0\), writing
\[
V=\tau^2I_n-\tau^4A^T\Sigma^{-1}A,
\qquad
m_{j_0}(y)=\mu_{j_0}+\tau^2A^T\Sigma^{-1}(y-A\mu_{j_0}),
\]
the posterior obeys
\[
\Pr(J\ne j_0\mid y)\le CM e^{-m\bar\delta},
\qquad
\|\pi(\cdot\mid y)-N(m_{j_0}(y),V)\|_{\mathrm{TV}}
\le CM e^{-m\bar\delta}.
\]
