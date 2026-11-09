# Problem

## Setup

Let $(\mathcal X,\mathcal F)$ be a measurable space and let $\mu$ and $\nu$ be probability measures with $\nu\ll\mu$. Write
\[
r=\frac{d\nu}{d\mu},\qquad \lambda=Zr,
\]
where $Z>0$ is unknown and can be queried through the nonnegative oracle value $\lambda(x)$; equivalently $Z=\int \lambda\,d\mu$. We observe iid samples $X_1,\ldots,X_n\sim\mu$ and oracle evaluations $\lambda(X_i)$. For $M>0$ define
\[
\operatorname{Cov}_M(\nu\|\mu)=\nu\{x:r(x)\ge M\},\qquad
\operatorname{ICov}_M(\nu\|\mu)=\int_0^M\operatorname{Cov}_t(\nu\|\mu)\,dt.
\]

Fix $0<\epsilon\le\tfrac12$ and $0<\delta<\tfrac13$.

## Task

Prove the following integrated-coverage characterization.

1. **Achievability.** For every $M>0$ satisfying
\[
\operatorname{ICov}_M(\nu\|\mu)\le \frac{\epsilon M}{4},
\]
there is an estimator based on iid proposal samples and oracle evaluations such that
\[
\Pr\big[(1-\epsilon)Z\le\widehat Z\le(1+\epsilon)Z\big]\ge1-\delta
\]
whenever $n\ge C M\log(1/\delta)/\epsilon$, for a universal constant $C$.

2. **Converse.** For every nonatomic proposal measure $\mu$ and every $0<\epsilon\le\tfrac12$, there is a family of target instances and a threshold $M>0$ with $\operatorname{ICov}_M(\nu\|\mu)\le\epsilon M$ such that every estimator attaining the same multiplicative guarantee with success probability at least $2/3$ requires $n\ge cM/\epsilon$ samples, for a universal constant $c>0$.
