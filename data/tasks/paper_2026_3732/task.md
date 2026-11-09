# Problem

## Setup

Consider a finite discounted Markov decision process with nonempty finite state and action sets $\mathcal S,\mathcal A$, discount factor $0<\gamma<1$, expected-reward vector $R\in\mathbb R^N$, and state-action-to-next-state transition matrix $P\in\mathbb R^{N\times|\mathcal S|}$, where $N=|\mathcal S||\mathcal A|$. All state-action-indexed objects use one consistent ordering. Let $p\ge1$ be a feature dimension, let $\Phi\in\mathbb R^{N\times p}$ have full column rank, and represent action values by $Q_\theta=\Phi\theta$ for $\theta\in\mathbb R^p$. Let $d$ be a state-action probability distribution with $d(s,a)>0$ for every pair, and set $D=\operatorname{diag}(d)$ and $G=\Phi^\top D\Phi$. Define
\[
V_\theta(s)=\max_{a\in\mathcal A}Q_\theta(s,a),\qquad \Pi_D=\Phi G^{-1}\Phi^\top D.
\]
A projected Bellman fixed point, if one exists, is a parameter $\theta^*$ satisfying
\[
\Phi\theta^*=\Pi_D(R+\gamma P V_{\theta^*}),
\qquad\text{equivalently}\qquad
G\theta^*=\Phi^\top D(R+\gamma P V_{\theta^*}).
\]
Its existence is not assumed for the endpoint comparisons.

For a deterministic policy $\pi:\mathcal S\to\mathcal A$, let $\Pi^\pi$ select its action from a state-action vector and set $B_\pi=\Phi^\top DP\Pi^\pi\Phi$. For an integer period $m\ge1$, define
\[
A_{\pi,m}=(I-\alpha G)^m+\sum_{i=0}^{m-1}(I-\alpha G)^i\alpha\gamma B_\pi,
\quad \mathcal A_m=\{A_{\pi,m}:\pi\text{ deterministic}\},
\quad \mathcal A_{\rm DLQL}=\mathcal A_1,
\]
and
\[
A_\pi^{\rm PQVI}=\gamma G^{-1}B_\pi,
\qquad \mathcal A_{\rm PQVI}=\{A_\pi^{\rm PQVI}:\pi\text{ deterministic}\}.
\]
Starting with $\bar\theta_0=\theta_0$, the deterministic algorithm performs
\[
\theta_{t+1}=\theta_t+\alpha\Phi^\top D\bigl(R+\gamma P V_{\bar\theta_t}-\Phi\theta_t\bigr).
\]
At times $t=km$, it copies the online parameter to the target; that target stays fixed throughout the following $m$ online updates. Any greedy-policy tie breaking for a frozen target is allowed. Assume $0<\alpha<2/\lambda_{\max}(G)$.

For a bounded finite matrix family $\mathcal H$, define
\[
\rho(\mathcal H)=\limsup_{k\to\infty}\ \sup_{H_1,\ldots,H_k\in\mathcal H}\|H_k\cdots H_1\|^{1/k},
\]
using a fixed matrix norm. For finite families its value is unchanged by replacing $\mathcal H$ with its convex hull.

## Task

Prove the following integrated theorem. Write $\rho_{\rm D}=\rho(\mathcal A_{\rm DLQL})$ and $\rho_{\rm P}=\rho(\mathcal A_{\rm PQVI})$. For every fixed $m$, if $\rho(\mathcal A_m)<1$, then the projected Bellman equation has a unique solution $\theta^*$, and the hard-target iterates converge to it from every initialization, with a uniform upper exponential rate arbitrarily close to $\rho(\mathcal A_m)^{1/m}$ per online step. This holds for every greedy tie breaking at period boundaries.

Moreover, the endpoint values determine the periodic regimes: if $\rho_{\rm D}<1$ (respectively $>1$), period one is uniformly stable (respectively its matrix family has JSR instability); and there exists $M$ such that for all $m\ge M$, periods are uniformly stable when $\rho_{\rm P}<1$ and their matrix families have JSR instability when $\rho_{\rm P}>1$. Consequently, under strict inequalities, the four possibilities
\[
(\rho_{\rm D}<1,\rho_{\rm P}<1),\quad
(\rho_{\rm P}<1<\rho_{\rm D}),\quad
(\rho_{\rm D}<1<\rho_{\rm P}),\quad
(\rho_{\rm D}>1,\rho_{\rm P}>1)
\]
produce respectively stable/stable, unstable/stable, stable/unstable, and unstable/unstable behavior at the period-one and sufficiently-large-period endpoints. Here JSR instability means failure of uniform worst-case convergence for arbitrary products of the indicated matrix family: arbitrarily long products have exponentially growing norms. Such products need not be realizable as greedy-policy sequences of the nonlinear algorithm, so no divergence claim about its realized trajectories follows.
