# Problem

## Setup

Let \(d\geq1\), let \(T\subset\mathbb R^d\) be nonempty and compact, and let \(G\in\mathbb R^{d\times d}\) be symmetric positive definite. For any nonempty compact \(S\subset\mathbb R^d\), define its Gaussian width by
\[
w(S)=\mathbb E\,\sup_{v\in S}\langle g,v\rangle,
\qquad g\sim\mathcal N(0,I_d).
\]
For a positive-definite matrix \(A\), define the corresponding weighted width
\[
w_A(T):=w(A^{1/2}T),
\]
where \(A^{1/2}\) is the positive-definite square root.

## Task

Prove that
\[
w_G(T)\,w_{G^{-1}}(T)\geq w(T)^2.
\]
Show also that the constant one is sharp by exhibiting a family of positive-definite matrices for which equality holds.
