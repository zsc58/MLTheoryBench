# Problem

## Setup

Let $S$ and $A$ be finite nonempty sets, let $P(\cdot\mid s,a)$ be transition probabilities, let rewards satisfy $r(s,a)\in[0,1]$, and let $\gamma\in[0,1)$. A stationary policy $\pi$ assigns $\pi(\cdot\mid s)\in\Delta(A)$ at each state. Let $V^\pi,Q^\pi$ be its discounted value and action-value functions, and let $V^*,Q^*$ be optimal. Write $\Pi^*$ for the set of optimal policies.

For each state let $A_s^*=\arg\max_a Q^*(s,a)$. Assume $\widetilde S=\{s:A_s^*\ne A\}$ is nonempty. For $s\in\widetilde S$ define
\[
\Delta_s=V^*(s)-\max_{a\notin A_s^*}Q^*(s,a),\qquad \Delta=\min_{s\in\widetilde S}\Delta_s>0.
\]
Let $S_{=1}=\{s:|A_s^*|=1\}$ and $S_{>1}=\{s:|A_s^*|>1\}$.

Let $\psi:\mathbb R\to\mathbb R\cup\{+\infty\}$ be proper, closed and convex, with $[0,1]\subseteq\operatorname{dom}\psi$. Assume that $\psi$ is differentiable and strictly convex on $\operatorname{int}(\operatorname{dom}\psi)$, and that $|\psi'(x_n)|\to\infty$ whenever a sequence $x_n\in\operatorname{int}(\operatorname{dom}\psi)$ approaches a boundary point of $\operatorname{dom}\psi$. Assume
\[
\psi'(0+)>-\infty,\qquad \psi'(1-)=+\infty.
\]
Set $h(p)=\sum_a\psi(p(a))$ and let $D_h$ be its Bregman divergence. For $\eta>0$, initialize $\pi_0$ with all coordinates in $\operatorname{int}(\operatorname{dom}\psi)$ and define
\[
\pi_{k+1}(\cdot\mid s)=\arg\max_{p\in\Delta(A)}\{\eta\langle p,Q^{\pi_k}(s,\cdot)\rangle-D_h(p\|\pi_k(\cdot\mid s))\}.
\]

Define $\chi(x)=\psi'(1-x)$ for $x\in(0,1]$; thus $\chi$ is continuous and strictly decreasing from $+\infty$ to $\psi'(0+)$, with inverse $\chi^{-1}:[\psi'(0+),\infty)\to(0,1]$.

## Task

Prove the integrated theorem: $\pi_k$ converges to some $\pi_\infty\in\Pi^*$; suboptimal actions have limiting probability zero; the unique optimal action at a state in $S_{=1}$ has limiting probability one; and every optimal coordinate at a state in $S_{>1}$ has limiting value in $\operatorname{int}(\operatorname{dom}\psi)$. Moreover:

1. If $S_{=1}=\varnothing$, there is finite $T_{\rm ter}$ such that $\pi_k=\pi_{T_{\rm ter}}\in\Pi^*$ for all $k\ge T_{\rm ter}$.
2. If $S_{=1}\ne\varnothing$, finite termination is impossible. Writing $\Delta_{=1}=\min_{s\in S_{=1}}\Delta_s$, prove that for every $\sigma\in(0,\Delta/2)$ there are finite constants $C_1,C_2,K$ such that for all $k\ge K$,
\[
\Delta\,\chi^{-1}(k\eta(\Delta_{=1}+2\sigma)+C_2)
\le \|V^*-V^{\pi_k}\|_\infty
\le (1-\gamma)^{-2}\chi^{-1}(k\eta(\Delta_{=1}-2\sigma)+C_1),
\]
with inverse arguments in $[\psi'(0+),\infty)$.
