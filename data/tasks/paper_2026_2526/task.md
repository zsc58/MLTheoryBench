# Problem

## Setup

Let $d\ge1$ be an integer, let $L>0$, and let $F(x)=\mathbb E_z[f(x,z)]$ for $x\in\mathbb R^d$. Throughout, $\|\cdot\|$ is the Euclidean norm. Assume that $F$ is differentiable, $L$-smooth,
\[
\|\nabla F(x)-\nabla F(y)\|\le L\|x-y\|,
\]
and is bounded below by a finite value $F^*$. The stochastic gradient is unbiased and has a uniformly bounded p-th moment: for some $p\in(1,2]$ and $\sigma>0$,
\[
\mathbb E_z[\nabla f(x,z)]=\nabla F(x),\qquad
\mathbb E_z\|\nabla f(x,z)\|^p\le\sigma^p
\quad\text{for every }x.
\]
Let $x_1\in\mathbb R^d$ and write $\Delta_1=F(x_1)-F^*$. At iteration $t$, draw an independent batch $z_{t,1},\ldots,z_{t,n}$, iid from the law of $z$, with batches independent across iterations. For parameters $\alpha>0$ and $\beta>0$, define
\[
\widehat g_t=\frac1n\sum_{k=1}^n c_{t,k}\nabla f(x_t,z_{t,k}),\qquad
c_{t,k}=\min\left\{1,\frac{\alpha k^{1/\beta}}{\|\nabla f(x_t,z_{t,k})\|}\right\},
\]
where the ratio is interpreted as $+\infty$ when the denominator is zero. Update
\[
x_{t+1}=x_t-\eta_t\widehat g_t.
\]

Fix any integer horizon $T\ge1$, batch size $n\ge1$, and step sizes satisfying $0<\eta_t<1/L$. Set $\alpha=\sigma$ and $\beta=p$.

## Task

Prove that the iterates satisfy
\[
\frac{\sum_{t=1}^T\eta_t\,\mathbb E\|\nabla F(x_t)\|^2}{\sum_{t=1}^T\eta_t}
\le
\frac{2\Delta_1}{\sum_{t=1}^T\eta_t}
+8\sigma^2 n^{-2(p-1)/p}.
\]
