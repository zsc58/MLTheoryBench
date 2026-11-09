# Problem

## Setup

Let $K\geq1$ be an integer and define
\[
\Delta_K=\left\{x\in[0,1]^K:\sum_{k=1}^K x_k=1\right\}.
\]
Let $\pi\in\Delta_K$. For an inverse temperature $\beta>0$, define
\[
(\pi_\beta)_k=\frac{\pi_k^\beta}{\sum_{j=1}^K\pi_j^\beta},
\qquad k=1,\ldots,K,
\]
with $0^\beta=0$.

For vectors $x,y\in\mathbb R^K$, write $x\prec y$ when
\[
\sum_{k=1}^K\phi(x_k)\leq\sum_{k=1}^K\phi(y_k)
\]
for every convex function $\phi:\mathbb R\to\mathbb R$.
A functional $U:\Delta_K\to\mathbb R$ is called symmetric Schur-concave if it is invariant under coordinate permutations and, for $x,y\in\Delta_K$, $x\prec y$ implies $U(x)\geq U(y)$.
Define Shannon entropy by
\[
H(x)=-\sum_{k=1}^K x_k\log x_k,\qquad x\in\Delta_K,
\]
with the convention $0\log0=0$.

## Task

Prove that for every $0<\beta_1<\beta_2$,
\[
\pi_{\beta_1}\prec\pi_{\beta_2}.
\]
Consequently, every symmetric Schur-concave uncertainty or dispersion functional is nonincreasing with inverse temperature:
\[
U(\pi_{\beta_1})\geq U(\pi_{\beta_2}).
\]
In particular,
\[
H(\pi_{\beta_1})\geq H(\pi_{\beta_2}).
\]
