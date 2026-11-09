# Problem

## Setup

Fix an input \(x\) in a \(K\)-class classification problem. Let
\[
a(x)\in\mathbb R_{>0}^K,\qquad
w(x)\in\left\{v\in\mathbb R_{>0}^K:\sum_{j=1}^K v_j=1\right\},\qquad
s(x)\in\mathbb R_{>0}^K.
\]
Let \(e_j\) denote the \(j\)-th standard basis vector. Consider the hierarchical model
\[
H\sim\operatorname{Cat}(w(x)),\qquad
P\mid(H=j,x)\sim\operatorname{Dir}(a(x)+s_j(x)e_j),\qquad
Y\mid(P,x)\sim\operatorname{Cat}(P).
\]
Define the induced label-probability vector \(q(x)\in\mathbb R^K\) by
\[
q_r(x)=\Pr(Y=r\mid x).
\]
Set
\[
Z(x)=\sum_{i=1}^K a_i(x),\qquad
u(x)=\frac{a(x)}{Z(x)},\qquad
g(x)=w(x),
\]
and define
\[
c(x)=\sum_{j=1}^K\frac{Z(x)w_j(x)}{Z(x)+s_j(x)},
\qquad
d_r(x)=\frac{s_r(x)}{Z(x)+s_r(x)}.
\]
Here \(\odot\) denotes coordinate-wise multiplication.

## Task

Prove the exact decomposition
\[
q(x)=c(x)\,u(x)+d(x)\odot g(x).
\]
Equivalently, prove that for every class \(r\),
\[
\Pr(Y=r\mid x)
=c(x)\frac{a_r(x)}{Z(x)}
+\frac{s_r(x)}{Z(x)+s_r(x)}w_r(x).
\]
