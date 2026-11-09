# Problem

## Setup

Let \(X\) and \(U\) be finite nonempty sets, and let \(s:U\to X\) assign each action its source state. For each \(x\in X\), let
\[
 U_x=s^{-1}(\{x\}),
\]
and assume \(U_x\) is nonempty. Fix transition probabilities \(p(y\mid u)\geq0\) satisfying \(\sum_{y\in X}p(y\mid u)=1\) for every \(u\in U\), and fix \(0\leq\gamma<1\). A reward is a vector \(r\in\mathbb R^U\). Equip \(\mathbb R^U\) and \(\mathbb R^X\) with their usual Euclidean topologies, subsets with the relative topology, and products with the product topology.

A deterministic stationary policy \(\pi\) selects one action \(\pi(x)\in U_x\) at each state. Let \(P_\pi(x,y)=p(y\mid\pi(x))\) be its state-transition matrix and \(r_\pi(x)=r(\pi(x))\) its selected-reward vector. Define \(v_{\pi,r}\) by
\[
 v_{\pi,r}=r_\pi+\gamma P_\pi v_{\pi,r},
\]
and let \(v_r^*\) be the componentwise maximum of \(v_{\pi,r}\) over all deterministic stationary policies. For an action \(u\), define
\[
 \operatorname{adv}_{\pi,r}(u)=r(u)+\gamma\sum_y p(y\mid u)v_{\pi,r}(y)-v_{\pi,r}(s(u)).
\]

For a state function \(\delta:X\to\mathbb R\), define
\[
 (\ell_\delta r)(u)=r(u)+\gamma\sum_y p(y\mid u)\delta(y)-\delta(s(u)).
\]
These transformations form a faithful additive action of \(\mathbb R^X\) on \(\mathbb R^U\). Call \(r\) normal when \(v_r^*\equiv0\), and write \(N\) for the set of normal rewards.

## Task

Prove that every orbit of \(r\mapsto\ell_\delta r\) contains exactly one normal reward. Moreover,
\[
 N=\{r\in\mathbb R^U:\max_{u\in U_x}r(u)=0\text{ for every }x\in X\},
\]
and
\[
 r\longmapsto\bigl(P(r),v_r^*\bigr),\qquad P(r):=\ell_{v_r^*}r,
\]
is a homeomorphism from \(\mathbb R^U\) onto \(N\times\mathbb R^X\), with inverse \((n,\delta)\mapsto\ell_{-\delta}n\). Under this identification the additive action is free and transitive on each fiber over \(N\), so reward space is a principal bundle over \(N\) with state-value fibers.
