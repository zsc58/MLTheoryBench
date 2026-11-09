# Problem

## Setup

Let $n,d$ be positive integers, let $\mathcal D$ be a data distribution, and let

$$
f(x)=\mathbb E_{\xi\sim\mathcal D}[F(x;\xi)],\qquad x\in\mathbb R^d,
$$

where $f:\mathbb R^d\to\mathbb R$ is differentiable, bounded below by a finite constant $f_*$, and $L$-smooth for a fixed $L>0$:

$$
\|\nabla f(x)-\nabla f(y)\|\le L\|x-y\|\qquad\text{for every }x,y\in\mathbb R^d.
$$

There are $n$ workers with homogeneous data distributions. For worker $i$, let $g_i(x,\xi)\in\mathbb R^d$ be a measurable stochastic-gradient map. Assume there are fixed finite constants $\sigma^2\ge0$ and $G>0$, independent of the worker and evaluation point, such that for every $i\in\{1,\ldots,n\}$ and every $x\in\mathbb R^d$,

$$
\mathbb E_{\xi\sim\mathcal D}[g_i(x,\xi)]=\nabla f(x),
$$

$$
\mathbb E_{\xi\sim\mathcal D}\|g_i(x,\xi)-\nabla f(x)\|^2\le\sigma^2,
\qquad
\mathbb E_{\xi\sim\mathcal D}\|g_i(x,\xi)\|^2\le G^2.
$$

Worker $i$ requires a positive integer time $\tau_i$ for one stochastic-gradient step. Set $\tau=\operatorname{lcm}(\tau_1,\ldots,\tau_n)$, fix a positive integer $M$, and let the communication time $\zeta$ be a nonnegative integer multiple of $\tau$. Define

$$
T_i=\frac{M\tau}{\tau_i},\qquad
O_i=\frac{\zeta}{\tau_i},\qquad
H_i=T_i+O_i.
$$

In round $r$, worker $i$ starts at $x_i^r$ and forms the trajectory

$$
\theta_{i,0}^r=x_i^r,
\qquad
\theta_{i,t+1}^r=\theta_{i,t}^r-\eta\,g_i(\theta_{i,t}^r,\xi_{i,t}^r),
\quad 0\le t<H_i,
$$

where $\eta>0$ is constant. Every sample $\xi_{i,t}^r$ has distribution $\mathcal D$. Put

$$
y_i^r=\theta_{i,T_i}^r,
\qquad
z_i^r=\theta_{i,H_i}^r,
\qquad
\bar y^r=\frac1n\sum_{i=1}^n y_i^r.
$$

Fix $K\in\{1,\ldots,d\}$. At the beginning of each round, a subset $S_r\subseteq\{1,\ldots,d\}$ is sampled uniformly from all subsets of cardinality $K$, and all workers use this same subset. Let $P_{S_r}:\mathbb R^d\to\mathbb R^d$ keep the coordinates in $S_r$ and set the other coordinates to zero. All stochastic samples and masks, across workers, steps, and rounds, are mutually independent.

After the first $T_i$ steps, communication of $P_{S_r}(\bar y^r)$ proceeds concurrently with the remaining $O_i$ steps, and the next round starts from

$$
x_i^{r+1}=z_i^r+P_{S_r}(\bar y^r-y_i^r). \tag{1}
$$

Use the notation

$$
\bar x^r=\frac1n\sum_{i=1}^n x_i^r,
\qquad
\bar H=\frac1n\sum_{i=1}^nH_i,
\qquad
H_{\max}=\max_iH_i,
$$

$$
S_T=\sum_{i=1}^nT_i^2,
\qquad
S_O=\sum_{i=1}^nO_i^2,
\qquad
\Phi_H=\sum_{i=1}^n\sum_{t=0}^{H_i-1}t^2.
$$

Let $p=K/d$ and $q=1-p$. For arbitrary $a,b>0$, define

$$
\rho=q(1+a)(1+b),
\qquad
C_T=q(1+b)(1+a^{-1}),
\qquad
C_O=1+q/b.
$$

## Task

Assume common initialization $x_i^0=x^0$ for every worker, where $x^0\in\mathbb R^d$ is fixed. Suppose

$$
0<\eta\le\frac{1}{8LH_{\max}}
\qquad\text{and}\qquad
\rho<1.
$$

Prove that for every integer $R\ge1$,

$$
\frac1R\sum_{r=0}^{R-1}\mathbb E\|\nabla f(\bar x^r)\|^2
\le
\frac{4(f(x^0)-f_*)}{\eta\bar H R}
+\frac{4L\eta\sigma^2}{n}
+\frac{6L^2\eta^2G^2\Phi_H}{n\bar H}
+\frac{6L^2\eta^2G^2H_{\max}}{n\bar H}
\frac{C_TS_T+C_OS_O}{1-\rho}.
$$

The expectation is over all stochastic-gradient samples and random coordinate masks.
