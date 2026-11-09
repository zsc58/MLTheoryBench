# Problem

## Setup

Fix integers \(d,q,s\ge1\). All norms are Euclidean; on a product of Euclidean spaces, use the Euclidean norm after concatenating the coordinates. Let
\[
F:(\mathbb R^d)^q\to\mathbb R^d,
\qquad
G:(\mathbb R^d)^s\to\mathbb R^{d\times d}
\]
with \(G(Y)=\operatorname{diag}(G_1(Y),\ldots,G_d(Y))\) and nonnegative diagonal entries. For \(t\in\mathbb Z\), let \(x_t,\zeta_t,\eta_t\) be \(\mathbb R^d\)-valued random vectors satisfying
\[
x_t=F(x_{t-q},\ldots,x_{t-1})+\zeta_t,
\qquad
\zeta_t=G(\zeta_{t-s},\ldots,\zeta_{t-1})\eta_t.
\]
Vector inequalities, including \(\eta_t\le y\), are interpreted componentwise. The innovations \((\eta_t)\) are iid, independent of the past observations and residuals, have a continuous joint CDF \(P\), satisfy \(\mathbb E\eta_1=0\), and obey \(\operatorname{Var}(\eta_{1,i})\le C\) for every coordinate, for some finite constant \(C\).

For each integer \(T>q+s\), from observations \(x_1,\ldots,x_T\), let
\[
\widehat F:(\mathbb R^d)^q\to\mathbb R^d,
\qquad
\widehat G:(\mathbb R^d)^s\to\mathbb R^{d\times d}
\]
be fitted functions based on these observations, with
\(\widehat G(Y)=\operatorname{diag}(\widehat G_1(Y),\ldots,\widehat G_d(Y))\).
Dependence of the fitted functions on \(T\) is suppressed in the notation. Define
\[
\widehat\zeta_t=x_t-\widehat F(x_{t-q},\ldots,x_{t-1}),
\qquad t=q+1,\ldots,T.
\]
Assume that, for each \(T>q+s\) and \(t=q+s+1,\ldots,T\), the matrix
\(\widehat G(\widehat\zeta_{t-s},\ldots,\widehat\zeta_{t-1})\)
is nonsingular almost surely, and define
\[
\widehat\eta_t=\widehat G(\widehat\zeta_{t-s},\ldots,\widehat\zeta_{t-1})^{-1}\widehat\zeta_t,
\qquad t=q+s+1,\ldots,T.
\]
The fitted residual vectors, normalized residual vectors, and the two estimator-error suprema in the following display are assumed measurable. Assume, as \(T\to\infty\),
\[
\sup_{X\in(\mathbb R^d)^q}\|\widehat F(X)-F(X)\|\xrightarrow{p}0,
\qquad
\max_{1\le i\le d}\sup_{Y\in(\mathbb R^d)^s}|\widehat G_i(Y)-G_i(Y)|\xrightarrow{p}0.
\]
Each \(G_i\) is continuously differentiable with
\[
\sup_{Y\in(\mathbb R^d)^s}\|\nabla G_i(Y)\|<\infty,
\qquad
\inf_{Y\in(\mathbb R^d)^s}|G_i(Y)|\ge c
\]
for a constant \(c>0\) common to all coordinates. The dimensions, lag lengths, functions \(F,G\), and constants \(C,c\) are fixed as \(T\to\infty\).

For \(m=T-q-s\), define the joint empirical CDF
\[
\widehat P_T(y)=\frac1m\sum_{t=q+s+1}^{T}{\bf1}\{\widehat\eta_t\le y\},
\qquad y\in\mathbb R^d.
\]

## Task

Prove that
\[
\sup_{y\in\mathbb R^d}\big|\widehat P_T(y)-P(y)\big|\xrightarrow{p}0
\qquad\text{as }T\to\infty.
\]
