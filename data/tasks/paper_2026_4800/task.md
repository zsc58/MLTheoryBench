# Problem

## Setup

Let \(d,L\in\mathbb N\) with \(L\ge1\). For each feature coordinate \(i\in\{1,\ldots,d\}\) and layer \(k\in\{1,\ldots,L\}\), let \(u_i^{(k)}(t)\) be the parameters of an \(L\)-layer diagonal linear network, and define its effective coordinate weight by
\[
w_i(t)=\prod_{k=1}^L u_i^{(k)}(t).
\]
Assume balanced positive initialization:
\[
u_i^{(1)}(0)=\cdots=u_i^{(L)}(0)>0\quad\text{for every }i.
\]
The parameters follow continuous-time gradient flow for the loss \(\ell(w)\), with the solution existing for all \(t\ge0\), all layer coordinates remaining positive, and \(w(t)^TS_b w(t)\ne0\) for all \(t\). Here \(S_w,S_b\in\mathbb R^{d\times d}\) are fixed symmetric matrices, and
\[
\ell(w)=\frac{w^TS_w w}{w^TS_b w}
\]
for nonzero \(w\) with nonzero denominator. The objective is evaluated through the effective weights, so
\[
\frac{d}{dt}u_i^{(k)}(t)=-\frac{\partial}{\partial u_i^{(k)}}\ell(w(t)).
\]
For positive vectors, define \(\|w\|_{2/L}^{2/L}:=\sum_{i=1}^d w_i^{2/L}\).

## Task

Prove that along this gradient-flow trajectory,
\[
\|w(t)\|_{2/L}^{2/L}=\|w(0)\|_{2/L}^{2/L}\qquad\text{for every }t\ge0.
\]
Equivalently, prove that \(\sum_{i=1}^d w_i(t)^{2/L}\) is exactly conserved by the dynamics.
