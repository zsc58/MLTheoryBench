# Problem

## Setup

Let $A$ be a finite nonempty action set and $(X,(Y(a))_{a\in A})$ a counterfactual random system with law $P$, where $X$ takes values in a measurable feature space $\mathcal X$ and the outcomes take values in $\mathcal Y$. Let $u:A\times\mathcal Y\to\mathbb R$ be bounded. Fix a finite real number
\[
u_{\max}\ge\max_{a\in A}\sup_{y\in\mathcal Y}u(a,y)
\]
and fix $\alpha\in(0,1)$. Assume regular conditional laws given $X$ exist and all displayed sets and functions are measurable.

For a nonrandomized action-indexed prediction-set system $C$, with $C(x,a)\subseteq\mathcal Y$, define
\[
\nu_C(x)=\max_{a\in A}\inf_{y\in C(x,a)}u(a,y),
\]
where the infimum over an empty set is $u_{\max}$. Let $\pi_C:\mathcal X\to A$ be a measurable maximizing action. Policy-coupled feasibility means
\[
P\{Y(\pi_C(X))\in C(X,\pi_C(X))\}\ge1-\alpha.
\]
Universal feasibility means
\[
P\{Y(\pi(X))\in C(X,\pi(X))\}\ge1-\alpha
\quad\text{for every measurable deterministic }\pi:\mathcal X\to A.
\]
The associated optimization problem maximizes $E[\nu_C(X)]$ over systems satisfying the relevant constraint.

For $r\in[0,1)$, define
\[
\operatorname{Quantile}^{+}_{r}[Z]=\sup\{z\in\mathbb R:P(Z\le z)\le r\},
\]
and set $\operatorname{Quantile}^{+}_{1}[Z]=u_{\max}$. For $t\in[0,1]$, define
\[
\gamma(x,t,a)=\operatorname{Quantile}^{+}_{1-t}[u(a,Y(a))\mid X=x],\qquad
\theta(x,t)=\max_{a\in A}\gamma(x,t,a),
\]
and, for $\beta\ge0$,
\[
g(x,\beta)\in\arg\max_{s\in[0,1]}\{\theta(x,s)+\beta s\}.
\]
Assume that for every $\beta\ge0$ this maximizer is unique for $P_X$-almost every $x$.

## Task

Prove that there exists $\beta^*\ge0$ with
\[
E[g(X,\beta^*)]=1-\alpha.
\]
Writing $t^*(x)=g(x,\beta^*)$, prove that
\[
C^*(x,a)=\{y\in\mathcal Y:u(a,y)\ge\gamma(x,t^*(x),a)\}
\]
is population-optimal among all universally feasible systems and also among all policy-coupled-feasible systems, attaining the same maximal value in both problems.
