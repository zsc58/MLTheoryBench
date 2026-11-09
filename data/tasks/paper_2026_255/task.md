# Problem

## Setup

Let $T\ge1$, $L>0$, and $D>0$. Let $K\subseteq\mathbb R^n$ be nonempty, closed, convex, and have diameter at most $D$. At round $t$, the learner chooses $w_t\in K$ before observing a differentiable convex loss $f_t:\mathbb R^n\to\mathbb R$ whose gradient is $L$-Lipschitz, and incurs $f_t(w_t)$.

For $u\in K$, define
$R_T(u)=\sum_{t=1}^T(f_t(w_t)-f_t(u))$ and
$Q_T(u)=\sum_{t=1}^T\|\nabla f_t(u)\|^2$.
Choose $w^\star\in\arg\min_{u\in K}\sum_t f_t(u)$ and write
$Q_T^\star=Q_T(w^\star)$ and
$S_T^\star=\sum_t(f_t(w^\star)-\inf_{z\in\mathbb R^n}f_t(z))$, allowing $S_T^\star=+\infty$.
Projected gradient descent uses $w_{t+1}=\Pi_K(w_t-\eta\nabla f_t(w_t))$.

## Task

Prove the following integrated theorem.

1. $Q_T^\star\le2LS_T^\star$, and for fixed positive $L,D$ there are one-dimensional instances with $T\to\infty$ and $Q_T^\star/(LS_T^\star)\to0$.

2. With $\eta=\min\{D/\sqrt{2Q_T^\star},1/(2L)\}$, interpreting the first term as $+\infty$ when $Q_T^\star=0$,
$R_T(w^\star)\le\max\{2LD^2,D\sqrt{2Q_T^\star}\}$.

3. For every deterministic online algorithm, every $T\ge1$, and every $D,M>0$, there are a one-dimensional closed convex set of diameter $D$ and linear losses with gradient norm $M$ such that
$Q_T^\star=M^2T$ and $R_T(w^\star)\ge(D/4)\sqrt{Q_T^\star}$.
