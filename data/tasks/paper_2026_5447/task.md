# Problem

## Setup

Let \(l\ge 1\) be an integer and let \(Y=\{-1,+1\}^l\). A constant \(d_0\ge 0\) and functions \(d_k:\{-1,+1\}^2\to\mathbb R\), for \(1\le k\le l\), are supplied; each function is specified by its four finite real table entries. Define
\[
D(v,w)=d_0+\sum_{k=1}^l d_k(v_k,w_k),
\]
and assume \(D(v,w)\ge 0\) for every \(v,w\in Y\). Define
\[
S=\sum_{v\in Y}\sum_{w\in Y}D(v,w),
\qquad C(y,y')=S-D(y',y).
\]

Let \(y\in Y\) be the observed label and \(s=(s_1,\ldots,s_l)\in\mathbb R^l\) a supplied score vector. For \(u>0\), define
\[
\Phi_0(u)=\log u,\qquad
\Phi_\tau(u)=\frac{u^{-\tau}-1}{\tau}\quad(\tau>0).
\]
For every finite real \(\tau\ge 0\), define
\[
L_\tau(y,s)=\sum_{y'\in Y} C(y,y')\,
\Phi_\tau\!\left(
\sum_{y''\in Y}\exp\!\left\{\sum_{k=1}^l(y''_k-y'_k)s_k\right\}
\right).
\]

The inputs are \(l,d_0\), the cost tables, \(y,s\), and \(\tau\). In particular, \(S\) is defined by its displayed sum and is not supplied as an oracle value. Complexity is measured in a unit-cost real-arithmetic model that also counts each exponential, logarithm, and positive-real power evaluation as one operation. Storage is counted in real scalars; no bit-complexity or numerical-precision bound is requested.

## Task

Prove that for every allowed input, \(L_\tau(y,s)\), including the computation of \(S\), can be evaluated exactly using \(O(l)\) operations and \(O(l)\) storage, without enumerating the label vectors in the displayed sums. Give explicit factorization identities in terms of label-wise finite sums and products, treating \(\tau=0\) and \(\tau>0\) separately. The supplied scores and cost entries need not satisfy any magnitude bound.
