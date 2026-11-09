# Problem

## Setup

Let $\mathcal X=\{x_1,\ldots,x_K\}$ be a finite realization set. Fix an empirical probability distribution $q$ on $\mathcal X$, with masses $q_i=q(x_i)\ge0$ and $\sum_{i=1}^K q_i=1$. Candidate models may be any probability distribution $r=(r_1,\ldots,r_K)$ on $\mathcal X$, so $r_i\ge0$ and $\sum_i r_i=1$. Fix $\beta\in\mathbb R$. Define
\[
\operatorname{softplus}(z)=\log(1+e^z),\qquad (u)_+=\max\{u,0\}.
\]
Consider the objective
\[
F_\beta(r)=-\sum_{i=1}^K q_i\,\operatorname{softplus}(\beta+\log r_i),
\]
where the summand is understood by continuity as $0$ when $r_i=0$.

## Task

Prove that every minimizer of $F_\beta$ has the form
\[
r_i=\frac{e^{-\beta}}{\tau}(q_i-\tau)_+,\qquad i=1,\ldots,K,
\]
where $\tau\in(0,\max_i q_i)$ is the unique solution of
\[
\tau=e^{-\beta}\sum_{i=1}^K(q_i-\tau)_+.
\]
Thus the optimizer is obtained by subtracting the cutoff $\tau$ from each empirical mass, truncating at zero, and renormalizing.
