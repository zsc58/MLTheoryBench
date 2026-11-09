# Problem

## Setup

Let \((\mathcal X,\mathcal H)\) and \((\mathcal Y,\mathcal G)\) be measurable spaces. Let \((\Omega,\mathcal F,P)\) be a probability space and let
\(X:\Omega\to\mathcal X\), \(Y:\Omega\to\mathcal Y\) be measurable, with
\(\mathcal F=\sigma(X,Y)\). Write \(P_X,P_Y\) for the laws of \(X,Y\) under \(P\). Let \(\mu\) and \(\nu\) be probability measures on \((\mathcal X,\mathcal H)\) and \((\mathcal Y,\mathcal G)\) satisfying \(\mu\ll P_X\) and \(\nu\ll P_Y\), with densities
\[
h=\frac{d\mu}{dP_X},\qquad g=\frac{d\nu}{dP_Y}.
\]
Let \(a:\mathcal X\to[0,\infty)\) and \(b:\mathcal Y\to[0,\infty)\) be fixed measurable functions. A probability measure \(Q\) on \((\Omega,\mathcal F)\) is called a factorized joint shift (FJS) law relative to \(P\) with factors \(a,b\) if \(Q\ll P\) and
\[
\frac{dQ}{dP}=a(X)b(Y)
\quad P\text{-a.s.}
\]
Write \(Q_X,Q_Y\) for the laws of \(X,Y\) under \(Q\).

Conditional expectations of nonnegative random variables are understood in the extended nonnegative sense, allowing the value \(+\infty\). Products of nonnegative quantities use the convention \(0\cdot\infty=0\).

## Task

Prove the following characterization: there exists an FJS law \(Q\) relative to \(P\) with the specified factors \(a,b\) and marginals \(Q_X=\mu\), \(Q_Y=\nu\) if and only if
\[
h(X)=a(X)\,\mathbb E_P[b(Y)\mid\sigma(X)],
\qquad
 g(Y)=b(Y)\,\mathbb E_P[a(X)\mid\sigma(Y)]
\quad P\text{-a.s.}
\]
In the converse direction, show that these equations make \(a(X)b(Y)\) a probability density and that the resulting law has the prescribed two marginals.
