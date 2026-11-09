# Problem

## Setup

Let \(B\geq 1\) be an integer. Consider a finite directed acyclic computational graph with a distinguished terminal output node \(o\). For each node \(v\), let \(E_v\) be its state space and \(P_v\) its parameter space, both finite-dimensional real inner-product spaces. Parameters are local to their respective nodes.

Fix the minibatch inputs and the parameter values. Input nodes have prescribed values \(x_v^b\) for \(b=1,\ldots,B\) and have parameter space \(\{0\}\). At every noninput node, differentiable maps compute
\[
x_v^b=f_v\bigl(\theta_v,(x_u^b)_{u\to v}\bigr).
\]
Let \(\ell^b=\ell(x_o^b)\) be a differentiable scalar loss. Using the inner products to represent derivatives as gradients, define
\[
g_v^b=\frac{\partial\ell^b}{\partial x_v^b},\qquad
h_v^b=\frac{\partial\ell^b}{\partial\theta_v}.
\]
For an edge \(v\to w\), let \(A_{vw}^b:E_w\to E_v\) be the adjoint of the derivative of \(f_w\) with respect to its \(x_v\) argument, evaluated at the fixed forward values. Let \(A_v^b:E_v\to P_v\) be the adjoint of the derivative of \(f_v\) with respect to \(\theta_v\); at input nodes this is the zero map. The exact reverse pass is seeded by \(g_o^b=\nabla\ell(x_o^b)\) and satisfies
\[
g_v^b=\sum_{v\to w}A_{vw}^b g_w^b\quad(v\ne o),\qquad
h_v^b=A_v^b g_v^b\quad\text{for every }v.
\]

On a common probability space, let \(\widetilde A_{vw}^b:E_w\to E_v\) and \(\widetilde A_v^b:E_v\to P_v\) be measurable random linear maps. Define the randomized reverse pass by
\[
\widetilde g_o^b=g_o^b,\qquad
\widetilde g_v^b=\sum_{v\to w}\widetilde A_{vw}^b\widetilde g_w^b\quad(v\ne o),\qquad
\widetilde h_v^b=\widetilde A_v^b\widetilde g_v^b.
\]
All expectations below are over this backward-pass randomization, with the minibatch, parameters, and exact forward quantities held fixed.

Assume each randomized map has finite expected operator norm. For every edge \(v\to w\) and sample \(b\), assume
\[
\mathbb E\|\widetilde A_{vw}^b\widetilde g_w^b\|^2<\infty.
\]
For every node \(v\) and sample \(b\), assume
\[
\mathbb E\|\widetilde A_v^b\widetilde g_v^b\|<\infty.
\]
The vector norms and operator norms are induced by the specified inner products.

For every edge \(v\to w\), define
\[
\mathcal D_{v,w}
=\sigma\!\left(
\{\widetilde g_u^c:v\to u,\ 1\leq c\leq B\},
\{\widetilde A_{vu}^c:v\to u,\ u\ne w,\ 1\leq c\leq B\}
\right).
\]
Assume, almost surely, for every edge and sample,
\[
\mathbb E[\widetilde A_{vw}^b\mid\mathcal D_{v,w}]=A_{vw}^b,
\]
and, for every node and sample,
\[
\mathbb E[\widetilde A_v^b\mid\sigma(\widetilde g_v^b)]=A_v^b.
\]
Conditional expectations of linear maps are taken coordinatewise.

Define the minibatch means
\[
g_v=\frac1B\sum_{b=1}^B g_v^b,\qquad
h_v=\frac1B\sum_{b=1}^B h_v^b,\qquad
\widetilde g_v=\frac1B\sum_{b=1}^B\widetilde g_v^b,\qquad
\widetilde h_v=\frac1B\sum_{b=1}^B\widetilde h_v^b.
\]

## Task

Prove that, for every node \(v\) and sample \(b\),
\[
\mathbb E[\widetilde g_v^b]=g_v^b,\qquad
\mathbb E[\widetilde h_v^b]=h_v^b,
\]
and consequently
\[
\mathbb E[\widetilde g_v]=g_v,\qquad
\mathbb E[\widetilde h_v]=h_v.
\]

Show the samplewise mean-square identity
\[
\mathbb E\|\widetilde g_v^b-g_v^b\|^2
=\sum_{v\to w}\mathbb E\|(\widetilde A_{vw}^b-A_{vw}^b)\widetilde g_w^b\|^2
+\mathbb E\left\|\sum_{v\to w}A_{vw}^b(\widetilde g_w^b-g_w^b)\right\|^2.
\]
Consequently, the minibatch average of its left-hand side equals the minibatch average of its right-hand side.

Also establish the following identity for the minibatch means:
\[
\mathbb E\|\widetilde g_v-g_v\|^2
=\sum_{v\to w}\mathbb E\left\|
\frac1B\sum_{b=1}^B(\widetilde A_{vw}^b-A_{vw}^b)\widetilde g_w^b
\right\|^2
+\mathbb E\left\|
\frac1B\sum_{b=1}^B\sum_{v\to w}A_{vw}^b(\widetilde g_w^b-g_w^b)
\right\|^2.
\]
