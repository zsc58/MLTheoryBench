# Problem

## Setup

On a probability space \((\Omega,\mathcal F,\mathbb P)\), let \(Y\) be a random variable taking values in a finite label set \(\mathcal Y\), equipped with its discrete \(\sigma\)-algebra, and let \(X\) be a random variable taking values in a measurable space \((\mathcal X,\mathcal A)\). Let \(\Delta(\mathcal Y)\) denote the probability simplex, equipped with its Borel \(\sigma\)-algebra. Let \(s:\mathcal X\to\Delta(\mathcal Y)\) be measurable and set \(S=s(X)\).

Set \(\mathcal H_X=\sigma(X)\) and \(\mathcal H_S=\sigma(S)\). Define the conditional label laws
\[
Q=\mathbb P(Y\in\cdot\mid\mathcal H_X),\qquad
C=\mathbb P(Y\in\cdot\mid\mathcal H_S),
\]
choosing simplex-valued versions measurable with respect to their conditioning \(\sigma\)-algebras.

Let \(\ell:\Delta(\mathcal Y)\times\mathcal Y\to\mathbb R\) be a measurable loss. For \(p,q\in\Delta(\mathcal Y)\), define
\[
L(p,q)=\mathbb E_{Z\sim q}[\ell(p,Z)],\qquad
E_\ell(q)=L(q,q),\qquad
d_\ell(p,q)=L(p,q)-E_\ell(q).
\]
Assume that \(\ell\) is proper, meaning that \(L(q,q)\leq L(p,q)\) for every \(p,q\in\Delta(\mathcal Y)\). Thus \(d_\ell(p,q)\geq0\). Call \(\ell\) strictly proper if \(d_\ell(p,q)=0\) holds only when \(p=q\).

Expectations in the assertions below are interpreted as extended-real Lebesgue expectations; the value \(+\infty\) is permitted.

## Task

Prove that
\[
\mathbb E[\ell(S,Y)]
=
\mathbb E[d_\ell(S,C)]
+
\mathbb E[d_\ell(C,Q)]
+
\mathbb E[E_\ell(Q)].
\]

Further, when \(\ell\) is strictly proper, prove that
\[
\mathbb E[d_\ell(C,Q)]=0
\]
holds if and only if \(Q\) has a \(\sigma(S)\)-measurable version (equivalently, \(C=Q\) almost surely).
