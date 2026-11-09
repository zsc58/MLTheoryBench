# Problem

## Setup

Fix a dimension \(d\), an integer \(m\ge 2\), and work conditionally on an arbitrary fixed history; all expectations below refer to this conditional law. Let \(g\in\mathbb R^d\), and let the numerator group \(A\) produce an integrable estimator \(\widehat g_A\) satisfying

\[
\mathbb E[\widehat g_A]=g.
\]

The same group also produces random vectors \(X^A_1,\ldots,X^A_m\in[0,\infty)^d\). Their denominator-statistic marginals are i.i.d., although \(\widehat g_A\) may depend arbitrarily on them. Independently of the entire group \(A\), a denominator group \(B\) produces i.i.d. vectors \(X_1,\ldots,X_m\) with the same denominator-statistic law. Write, for \(k=1,\ldots,d\),

\[
\mu_k=\mathbb E[X_{1,k}],\qquad
\sigma_k^2=\operatorname{Var}(X_{1,k}),\qquad
\bar X_k=\frac1m\sum_{j=1}^m X_{j,k},
\]

and assume \(\max_k\mathbb E|X_{1,k}-\mu_k|^4<\infty\). Coordinates of any one \(X_j\) need not be independent. Define

\[
\widehat V_k=\frac{1}{m(m-1)}
\sum_{j=1}^m (X_{j,k}-\bar X_k)^2.
\]

Fix \(\lambda>0\) and let

\[
T_a(x)=(x+\lambda)^{-a}.
\]

Consider either of the following regimes:

- the diagonal inverse regime, where \(a=1\) and \(Q=I_d\); or
- the aligned inverse-root regime, where \(a\in(0,1]\) and \(Q\) is a fixed orthogonal population-aligned basis in which all denominator perturbations used here are diagonal.

Set

\[
H=Q\operatorname{diag}(T_a(\mu_k))_{k=1}^dQ^\top,
\]

\[
\widehat H_B
=Q\operatorname{diag}(T_a(\bar X_k))_{k=1}^dQ^\top,
\]

and define the theoretical, unclipped corrected estimator

\[
\widetilde H_B
=Q\operatorname{diag}\left(
T_a(\bar X_k)-\frac12T_a''(\bar X_k)\widehat V_k
\right)_{k=1}^dQ^\top.
\]

Define \(\widehat H_A\) analogously to \(\widehat H_B\), using the denominator statistics from group \(A\). In the aligned regime, \(Q\) is fixed rather than estimated from the random averaged denominator matrix.

## Task

Prove the following integrated bias-reduction theorem.

First, the same-group estimator admits the exact decomposition

\[
\mathbb E[\widehat H_A\widehat g_A]-Hg
=
\operatorname{Cov}(\widehat H_A,\widehat g_A)
+(\mathbb E[\widehat H_A]-H)g,
\]

where

\[
\operatorname{Cov}(\widehat H_A,\widehat g_A)
:=\mathbb E[\widehat H_A\widehat g_A]
-
\mathbb E[\widehat H_A]\,\mathbb E[\widehat g_A].
\]

For the independent denominator group, cross-fitting removes this coupling term exactly. Moreover, as \(m\to\infty\),

\[
\mathbb E[\widehat H_B]-H
=
\frac{1}{2m}Q\operatorname{diag}
\big(T_a''(\mu_k)\sigma_k^2\big)_{k=1}^dQ^\top
+O(m^{-3/2})
\]

in operator norm, whereas

\[
\|\mathbb E[\widetilde H_B]-H\|_{\mathrm{op}}
=O(m^{-3/2}).
\]

Consequently,

\[
\mathbb E[\widehat H_B\widehat g_A]-Hg
=
\frac{1}{2m}Q\operatorname{diag}
\big(T_a''(\mu_k)\sigma_k^2\big)_{k=1}^dQ^\top g
+O(m^{-3/2})\|g\|,
\]

while

\[
\|\mathbb E[\widetilde H_B\widehat g_A]-Hg\|
=O(m^{-3/2})\|g\|.
\]

The constants implicit in the asymptotic notation may depend on the fixed dimension, \(a\), \(\lambda\), and the moment bounds, but not on \(m\).
