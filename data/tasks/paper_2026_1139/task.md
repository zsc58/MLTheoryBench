# Problem

## Setup

Let \((\mathcal X,\mathcal A)\) be a measurable input space and let \(\mathfrak G\) be the measurable space of labeled finite-graph representatives. Let
\[
(X_1,Y_1),\ldots,(X_{n+1},Y_{n+1})
\]
be exchangeable random elements of \(\mathcal X\times\mathfrak G\), where \(n\ge1\) and \(\alpha\in(0,1)\). Exchangeability means that the joint law is invariant under every permutation of the \(n+1\) indices.

Fix, independently of the calibration sample \((X_i,Y_i)_{i=1}^n\), measurable functions
\[
s:\mathcal X\times\mathfrak G\to\mathbb R,\qquad
\omega:\mathcal X\to\Omega,\qquad
\psi:\Omega\to\mathbb R,
\]
where \(\Omega\) is measurable. For \(i=1,\ldots,n\), define calibration residuals
\[
R_i=s(X_i,Y_i)-\psi(\omega(X_i)).
\]
Set \(k=\lceil(n+1)(1-\alpha)\rceil\), append \(+\infty\) to the \(n\) calibration residuals, and let \(\widehat q\) be the \(k\)-th order statistic of \(R_1,\ldots,R_n,+\infty\). For any input \(x\), define
\[
\Gamma(x)=\{y\in\mathfrak G:\ s(x,y)\le \psi(\omega(x))+\widehat q\}.
\]

## Task

Prove that the resulting input-adaptive graph-valued prediction set has finite-sample marginal coverage:
\[
\mathbb P\bigl\{Y_{n+1}\in\Gamma(X_{n+1})\bigr\}\ge 1-\alpha.
\]
