# Problem

## Setup

Let \(\mathcal S\) and \(\mathcal A\) be finite nonempty state and action sets. Let \(r:\mathcal S\times\mathcal A\to\mathbb R\) satisfy \(|r(s,a)|\le R<\infty\), and let \(P(\cdot\mid s,a)\) be a probability distribution on \(\mathcal S\). A stationary policy assigns an action probability distribution \(\pi(\cdot\mid s)\) to each state. Define
\[
P^\pi(s,s')=\sum_a\pi(a\mid s)P(s'\mid s,a),\qquad
r^\pi(s)=\sum_a\pi(a\mid s)r(s,a).
\]
Restrict policies to
\[
\Pi_+=\{\pi:\pi(a\mid s)>0\text{ for every }s,a\}.
\]
Fix an initial probability distribution \(\mu\) with full support, represented as a column vector.

For \(\pi\in\Pi_+\), let
\[
P_*^\pi=\lim_{n\to\infty}\frac1n\sum_{t=0}^{n-1}(P^\pi)^t.
\]
Let \(\mathcal R^\pi\) be the union of the closed recurrent communicating classes of \(P^\pi\), and let \(\mathcal T^\pi=\mathcal S\setminus\mathcal R^\pi\) be its transient states. Define the \(\mathcal S\times\mathcal S\) matrix
\[
\bar T^\pi(s,s')=
\begin{cases}
P^\pi(s,s'),&s,s'\in\mathcal T^\pi,\\
0,&\text{otherwise},
\end{cases}
\]
and the row vectors
\[
d_\mu^\pi=\mu^\top P_*^\pi,\qquad
\delta_\mu^\pi=\mu^\top(I-\bar T^\pi)^{-1}.
\]

Define the state average reward by
\[
J^\pi(s)=\liminf_{H\to\infty}\frac1H
\mathbb E_\pi\!\left[\sum_{t=0}^{H-1}r(s_t,a_t)\,\middle|\,s_0=s\right],
\qquad J_\mu^\pi=\sum_s\mu(s)J^\pi(s),
\]
where trajectories use \(a_t\sim\pi(\cdot\mid s_t)\) and \(s_{t+1}\sim P(\cdot\mid s_t,a_t)\). Let \(V^\pi\) be the normalized relative-value vector specified by
\[
J^\pi+V^\pi=r^\pi+P^\pi V^\pi,\qquad P_*^\pi V^\pi=0.
\]
Define
\[
K^\pi(s,a)=\sum_{s'}P(s'\mid s,a)J^\pi(s'),\qquad
Q^\pi(s,a)=r(s,a)+\sum_{s'}P(s'\mid s,a)V^\pi(s')-K^\pi(s,a).
\]

## Task

Prove that for every \(\pi,\pi'\in\Pi_+\),
\[
J_\mu^\pi-J_\mu^{\pi'}
=\sum_{s\in\mathcal R^\pi}d_\mu^\pi(s)\sum_a
\bigl(\pi(a\mid s)-\pi'(a\mid s)\bigr)Q^{\pi'}(s,a)
+\sum_{s\in\mathcal T^\pi}\delta_\mu^\pi(s)\sum_a
\bigl(\pi(a\mid s)-\pi'(a\mid s)\bigr)K^{\pi'}(s,a).
\]
Moreover, for every differentiable parameterization \(\theta\mapsto\pi_\theta\in\Pi_+\) on a finite-dimensional differentiable parameter manifold, prove
\[
\nabla_\theta J_\mu^{\pi_\theta}
=\sum_{s\in\mathcal R^{\pi_\theta}}d_\mu^{\pi_\theta}(s)\sum_a
\nabla_\theta\pi_\theta(a\mid s)Q^{\pi_\theta}(s,a)
+\sum_{s\in\mathcal T^{\pi_\theta}}\delta_\mu^{\pi_\theta}(s)\sum_a
\nabla_\theta\pi_\theta(a\mid s)K^{\pi_\theta}(s,a).
\]
Here parameter gradients are taken in any local coordinates, including the usual coordinates when the parameter domain is open in Euclidean space. Empty sums are zero.
