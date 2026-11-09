# Problem

## Setup

Let \(D_{\mathrm{tr}}\) be a training sample of size \(m\). Let \(D_{\mathrm{cal}}=\{(X_j,Y_j)\}_{j=1}^n\) and \((X_{n+1},Y_{n+1})\) be iid calibration and test pairs from the same fixed distribution of a covariate \(X\) and a real-valued response \(Y\), jointly independent of \(D_{\mathrm{tr}}\). Write \(P_X\) for the covariate law and \(F(y\mid x)\) for the true conditional CDF of \(Y\) given \(X=x\).

Fit a measurable conditional CDF estimator \(\widehat F(y\mid x)\) using only \(D_{\mathrm{tr}}\). Here measurability is in the training data, covariate, and response argument, and for each realized training sample and covariate, \(\widehat F(\cdot\mid x)\) is a CDF on \(\mathbb R\). Define
\[
\widehat Q(u\mid x)=\inf\{y\in\mathbb R:\widehat F(y\mid x)\ge u\},\qquad u\in[0,1],
\]
with the infimum taken in the extended real line and \(\inf\varnothing=+\infty\). In particular, \(\widehat Q(0\mid x)=-\infty\). Intervals with infinite endpoints are interpreted as sets of real responses satisfying the displayed endpoint inequalities.

Fix \(\alpha\in(0,1)\). Choose a starting point \(z\) that is fixed or measurable with respect to \(D_{\mathrm{tr}}\) and the test covariate \(X_{n+1}\) only. Form calibration PIT values
\[
U_j=\widehat F(Y_j\mid X_j),\quad U_{(1)}\le\cdots\le U_{(n)}.
\]
For each such \(z\), set
\[
L(z)=\lfloor z(n+1)\rfloor+1,\qquad
H(z)=\lceil (z+1-\alpha)(n+1)\rceil,
\]
and assume these indices lie in \(\{1,\ldots,n\}\) with \(L(z)\le H(z)\). Define
\[
\widehat C(x)=\big[\widehat Q(U_{(L(z))}\mid x),\widehat Q(U_{(H(z))}\mid x)\big],
\]
using the starting point selected for that test covariate.

Assume that, as \(m\to\infty\), for \(P_X\)-almost every \(x\),
\[
\sup_y\left|\widehat F(y\mid x)-F(y\mid x)\right|=o_P(1),
\]
and that for \(P_X\)-almost every \(x\), the conditional law of \(Y\mid X=x\) is continuous and \(F(\cdot\mid x)\) is strictly increasing on its support.

In the statement below, \(\Pr_{\mathrm{cal,test}}(\cdot\mid D_{\mathrm{tr}},X_{n+1}=x)\) denotes probability over the calibration sample and the test response, conditional on the realized training data and on \(X_{n+1}=x\); it does not condition on the realized calibration sample.

## Task

Prove that, as both \(m\) and \(n\) tend to infinity, for \(P_X\)-almost every covariate value \(x\),
\[
\Pr_{\mathrm{cal,test}}\!\left\{Y_{n+1}\in\widehat C(X_{n+1})\mid D_{\mathrm{tr}},X_{n+1}=x\right\}
=1-\alpha+o_P(1),
\]
where the \(o_P(1)\) is with respect to the training-sample randomness.
