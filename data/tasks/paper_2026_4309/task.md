# Problem

## Setup

Let \(d\) be a positive integer, and write \(|\cdot|\) for the Euclidean norm. For probability measures \(\rho,\sigma\) on \(\mathbb R\) with finite first moments, define
\[
W_1(\rho,\sigma)=\inf_{\gamma\in\Pi(\rho,\sigma)}\int_{\mathbb R^2}|s-t|\,d\gamma(s,t),
\]
where \(\Pi(\rho,\sigma)\) is the set of probability measures with marginals \(\rho\) and \(\sigma\).

For any probability measure \(\rho\) on \(\mathbb R^d\) with finite first moment and any unit vector \(v\), write \(R^v(x)=v\cdot x\) and \(\rho^v=(R^v)_\#\rho\), the law of \(v\cdot X\) when \(X\) has law \(\rho\). For two such measures \(\mu,\nu\), define
\[
d_{\mathrm{MaxDSW}}(\mu,\nu)=\max_{(v_1,\ldots,v_d)\ \mathrm{orthonormal}}\sum_{i=1}^d W_1(\mu^{v_i},\nu^{v_i}).
\]
Let \(\mu\) be a probability measure on \(\mathbb R^d\) with finite first moment. For each positive integer \(n\), let \(X_1,\ldots,X_n\) be i.i.d. with law \(\mu\), and let \(\hat\mu_n=n^{-1}\sum_{j=1}^n\delta_{X_j}\). Define
\[
\psi_\mu(z)=\mu\{x:|x|>z\},\qquad z\ge0,
\]
and
\[
\ell(t)=1+\max\{0,\log t\},\qquad t>0,
\]
where \(\log\) denotes the natural logarithm. Expectations below are over the i.i.d. sample.

## Task

Prove the following integrated theorem, with constants uniform over \(d\), \(n\), and all measures satisfying the stated tail bound.

If, for some \(\beta>2\) and \(C_0>0\),
\[
\psi_\mu(z)\le C_0(1+z)^{-\beta}\qquad(z\ge0),
\]
then there is a constant \(\kappa>0\), depending only on \(C_0,\beta\), such that, for every positive integer \(n\),
\[
\mathbb E\,d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)\le \kappa d^{3/2}n^{-(\beta-1)/(2\beta-1)}.
\]
If, for some \(C_0,\delta>0\),
\[
\psi_\mu(z)\le C_0e^{-\delta z}\qquad(z\ge0),
\]
then there is a constant \(\kappa>0\), depending only on \(C_0,\delta\), such that, for every positive integer \(n\),
\[
\mathbb E\,d_{\mathrm{MaxDSW}}(\hat\mu_n,\mu)\le \kappa d^{3/2}\ell(n)n^{-1/2}.
\]
Consequently, after enlarging the constant in each regime if necessary, prove that for every \(\varepsilon>0\) the expected error is at most \(\varepsilon\) whenever the positive integer sample size satisfies
\[
n\ge\left(\frac{\kappa d^{3/2}}{\varepsilon}\right)^{(2\beta-1)/(\beta-1)}
\]
in the polynomial-tail regime, or
\[
n\ge\left(\frac{\kappa d^{3/2}\ell(d/\varepsilon)}{\varepsilon}\right)^2
\]
in the exponential-tail regime. These constants have the same allowed dependencies as in the corresponding rate bounds and do not depend on \(\varepsilon\).
