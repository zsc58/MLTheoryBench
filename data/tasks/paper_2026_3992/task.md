# Problem

## Setup

Let $(\mathcal X,\mathcal A)$ and $(\mathcal Y,\mathcal B)$ be measurable spaces, and let $\mu$ be a reference measure on $\mathcal Y$. Fix training data $D_{\rm tr}$ and a source predictive density $p_s(y\mid x,D_{\rm tr})$ with respect to $\mu$. For a data stream $(X_i,Y_i)_{i\ge1}$, define
\[
\mathcal F_t=\sigma(D_{\rm tr},X_1,Y_1,\ldots,X_t,Y_t),\qquad \mathcal F_0=\sigma(D_{\rm tr}).
\]
Assume the predictive null $H_0^{\rm pred}$: conditional on $(\mathcal F_{i-1},X_i)$, the variable $Y_i$ has density $p_s(\cdot\mid X_i,D_{\rm tr})$ for every $i$. The inputs may be deterministic, stochastic, or selected using the past.

Fix in advance a measurable weight $w:\mathcal Y\to[0,\infty)$. Assume that for every input value that can occur,
\[
0<Z_w(x):=\int_{\mathcal Y}w(y)p_s(y\mid x,D_{\rm tr})\,d\mu(y)<\infty.
\]
Define
\[
q_w(y\mid x,D_{\rm tr})=\frac{w(y)p_s(y\mid x,D_{\rm tr})}{Z_w(x)},\qquad e_i=\frac{w(Y_i)}{Z_w(X_i)},
\]
where the ratio agrees with $q_w/p_s$ wherever $p_s>0$. Let $M_0=1$ and $M_t=\prod_{i=1}^t e_i$.

## Task

Prove that under $H_0^{\rm pred}$, for every $i$,
\[
\mathbb E[e_i\mid\mathcal F_{i-1},X_i]=1\quad\text{a.s.},
\]
and that $(M_t)_{t\ge0}$ is a nonnegative martingale with respect to $(\mathcal F_t)$. Consequently, for every $\alpha\in(0,1)$, the stopping time
\[
\tau^*=\inf\{t\ge1:M_t>1/\alpha\}
\]
satisfies
\[
\mathbb P_{H_0^{\rm pred}}(\tau^*<\infty)\le\alpha.
\]
