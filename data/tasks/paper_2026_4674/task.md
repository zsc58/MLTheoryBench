# Problem

## Setup

Let $n,d$ be positive integers and let $b$ be an integer with $1\leq b\leq n$. Let $f_1,\ldots,f_n:\mathbb R^d\to\mathbb R$ be analytic in a neighborhood of a point $z^\star$. Assume
\[
\nabla f_i(z^\star)=0\quad\text{and}\quad\nabla^2 f_i(z^\star)\succ0\qquad(i=1,\ldots,n).
\]
At each iteration choose independently a uniformly random subset $S_t\subset\{1,\ldots,n\}$ of fixed size $b$ (sampling is without replacement inside a batch), define
\[
\widehat L_S(z)=\frac1b\sum_{i\in S}f_i(z),
\]
and run
\[
z_{t+1}=z_t-\alpha\nabla\widehat L_{S_t}(z_t),\qquad t=0,1,\ldots .
\]
For each batch let $H_S=\nabla^2\widehat L_S(z^\star)$, and suppose
\[
0<\alpha<\min_{|S|=b}\frac{2}{\lambda_{\max}(H_S)}.
\]

## Task

Prove that there exists $\rho>0$ such that, for every deterministic initialization satisfying $\|z_0-z^\star\|_2<\rho$, the resulting nonlinear SGD iterates satisfy, for every even integer $k\ge2$,
\[
\rho^{-k}\,\mathbb E\!\left[\|z_t-z^\star\|_2^k\right]\xrightarrow[t\to\infty]{}0,
\]
where the expectation is over the independently sampled batches.
