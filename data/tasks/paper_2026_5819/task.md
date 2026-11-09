# Problem

## Setup

Let \(\Sigma\) be a finite alphabet of size \(m\), let \(n\ge1\) be an integer, and let \(K\) be an integer with \(3\le K\le m\). Consider distributions \(\pi,\mu\) on \(\Sigma^n\) such that every next-token conditional at a positive-probability prefix, for either distribution, has support size at most \(K\).

The distributions are unknown and are accessed only through their two prefix oracles. For \(\rho\in\{\pi,\mu\}\), a call at a prefix \(x_{1:i}\), \(0\le i<n\), having positive probability under \(\rho\), returns a random probability vector \(\widehat p(\cdot\mid x_{1:i})\) on \(\Sigma\). Writing
\[
p_\rho(a\mid x_{1:i})=\Pr_\rho(X_{i+1}=a\mid X_{1:i}=x_{1:i}),
\]
the response satisfies
\[
\mathbb E[\widehat p(a\mid x_{1:i})]=p_\rho(a\mid x_{1:i}),\qquad
\sum_{a:p_\rho(a\mid x_{1:i})>0}
\frac{\operatorname{Var}(\widehat p(a\mid x_{1:i}))}{p_\rho(a\mid x_{1:i})}
\le\sigma^2.
\]
Here \(0\le\sigma^2\le K\) is a given upper bound, and the expectation and variance are over the oracle response. Every call, including a repeated call at the same prefix, uses fresh independent randomness: conditional on the selected oracle and prefix, its response has that oracle's fixed response law and uses randomness independent of the preceding interaction and the algorithm's internal randomness. At a zero-probability prefix, the oracle may return a null symbol or use an arbitrary probability-vector extension; the displayed moment requirements apply only at positive-probability prefixes.

An algorithm may adaptively query either oracle and use internal randomness. Its query cost is the total number of calls to both oracles, with a query bound meaning a worst-case bound on this number. Guarantees must hold uniformly over the distributions and oracle response laws satisfying these conditions.

For \(\epsilon,\delta\in(0,1)\), the estimation requirement is to output \(\widehat d\) satisfying
\[
\Pr\bigl(|\widehat d-\operatorname{TV}(\pi,\mu)|\le\epsilon\bigr)\ge1-\delta,
\qquad
\operatorname{TV}(\pi,\mu)=\tfrac12\sum_{x\in\Sigma^n}|\pi(x)-\mu(x)|.
\]
The probability includes both oracle and algorithm randomness.

## Task

Prove that there are universal positive constants such that, for \(\epsilon\in(0,1/8)\) and \(n\ge c\log(1/\epsilon)\) with a sufficiently large universal \(c\), the following statements hold:

1. For every \(\delta\in(0,1)\), there is an algorithm satisfying the estimation requirement and using
\[
O\!\left((n+n^2\sigma^2)\epsilon^{-2}\log^2(1/\epsilon)\log(1/\delta)\right)
\]
queries.

2. Every algorithm that satisfies the estimation requirement with success probability at least \(2/3\) uniformly over the admissible distributions and oracle laws requires
\[
\Omega\!\left(\frac{n(1\vee\sigma^2)}{\epsilon^2\log K}\right)
\]
queries in the worst case over that class, where \(1\vee\sigma^2=\max\{1,\sigma^2\}\).

All constants in these bounds are independent of \(m,K,n,\sigma^2,\epsilon,\delta\).
