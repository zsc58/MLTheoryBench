# Problem

## Setup

Let $G=(S\cup X,E)$ be a finite directed acyclic graph, where $S$ and $X$ are disjoint. It has a unique source $s_0\in S$ and a unique sink $s_{\mathrm{sink}}\in S$, distinct from $s_0$. The incoming neighbors of $s_{\mathrm{sink}}$ are exactly the terminal states $X$. A terminal state $x\in X$ has only the outgoing edge $x\to s_{\mathrm{sink}}$; this final transition is deterministic.

A forward policy $p_F(s,\cdot)$ is a probability distribution on the children of each nonterminal state $s\in S\setminus\{s_{\mathrm{sink}}\}$. A backward policy $p_B(v,\cdot)$ is a probability distribution on the parents of each $v\in(S\cup X)\setminus\{s_0,s_{\mathrm{sink}}\}$.

For $x\in X$, let $\mathcal T_x$ be the set of complete trajectories
\[
 \tau=(s_0,s_1,\ldots,s_n=x,s_{\mathrm{sink}}).
\]
The auxiliary final transition is omitted from both policy products: define
\[
 p_F(\tau)=\prod_{i=0}^{n-1}p_F(s_i,s_{i+1}),
 \qquad
 p_B(\tau\mid x)=\prod_{i=0}^{n-1}p_B(s_{i+1},s_i).
\]
Thus the backward product describes transitions starting at $x$, not at $s_{\mathrm{sink}}$.

Fix a canonical forward policy $p_F^g$ and a constant $Z_g>0$. Write
\[
 p_{\mathrm{top}}^g(x)=\sum_{\tau\in\mathcal T_x}p_F^g(\tau),
 \qquad \widehat R_g(x)=Z_g p_{\mathrm{top}}^g(x).
\]
Fix a reward function $R:X\to(0,\infty)$ and parameters $\alpha>0$, $\beta>0$. Define
\[
 O=\mathrm{OA}(\alpha,g)=\{x\in X:\widehat R_g(x)\ge\alpha R(x)\},
 \qquad U=\mathrm{UA}(\alpha,g)=X\setminus O.
\]

Let $p_F^\nabla$ and $p_B^\nabla$ be exploration forward and backward policies, and let $Z_\nabla$ be a finite nonnegative real constant. For a trajectory $\tau\in\mathcal T_x$, define the exploration loss
\[
 \ell(\tau)=
 \left[
 \log\left(
 \frac{Z_\nabla p_F^\nabla(\tau)}{R(x)^\beta p_B^\nabla(\tau\mid x)}
 +\mathbf 1\{x\in O\}
 \right)
 \right]^2.
\]
Assume that for every $x\in X$ and every $\tau\in\mathcal T_x$, the denominator and the logarithm argument in this expression are strictly positive, and $\ell(\tau)=0$. Assume $U\ne\varnothing$. Define the exploration terminal marginal by
\[
 p_{\mathrm{top}}^\nabla(x)=\sum_{\tau\in\mathcal T_x}p_F^\nabla(\tau).
\]

## Task

Prove that the exploration GFlowNet samples terminal states according to the reward tempered by $\beta$ and restricted to the under-allocated set:
\[
 p_{\mathrm{top}}^\nabla(x)=
 \frac{R(x)^\beta\,\mathbf 1\{x\in U\}}
 {\sum_{y\in U}R(y)^\beta}
 \quad\text{for every }x\in X,
\]
and that $Z_\nabla=\sum_{y\in U}R(y)^\beta$.
