# Problem

## Setup

Let d be a positive integer. Throughout, the norm and inner product are Euclidean. Let F:R^d to R^d satisfy, for some 0<mu<=L,
\[
\langle F(u)-F(v),u-v\rangle\geq \mu\|u-v\|^2,
\qquad
\|F(u)-F(v)\|\leq L\|u-v\|,
\]
for all u,v in R^d. Assume F has a zero x*, which is then unique. For a fixed initial point x_0 in R^d, consider
\[
x_{k+1}=x_k-\beta_k(F(x_k)+\eta_k),
\qquad
\beta_k=\frac{\beta}{k+K_0},
\]
where beta>0, K_0>0, and k ranges over the nonnegative integers.

Consider separately the following two noise models.

1. **Finite-moment independent noise.** The R^d-valued vectors eta_k are independent. For fixed 1<p<2 and finite sigma>0, they satisfy
\[
\mathbb E\eta_k=0,\qquad
\mathbb E\|\eta_k\|^p\leq\sigma^p,\qquad
\mathbb E\|\eta_k\|^2=\infty
\]
for every k>=0.

2. **Long-range-dependent noise.** The R^d-valued vectors eta_k form a zero-mean, weakly stationary process. Write
\[
\gamma(h)=\mathbb E\langle\eta_{t+h},\eta_t\rangle,
\qquad t,h\in\{0,1,2,\ldots\},
\]
where weak stationarity makes this quantity independent of t. Assume
\[
\sum_{h=0}^{\infty}|\gamma(h)|=\infty,
\qquad
|\gamma(h)|\leq\sigma^2(1+h)^{-\delta}\quad(h\geq0),
\]
for fixed finite sigma>0 and 0<delta<1.

## Task

Prove the following two statements, giving explicit admissible finite thresholds and prefactors.

- **Independent-noise model.** There is a positive threshold C4 depending only on mu,L,p such that, for every beta>C4, a positive threshold C5 depending only on mu,L,beta can be chosen with the following property: for every fixed K0>=C5, there is a finite nonnegative C6 depending only on mu,L,beta,p,sigma,K0 and ||x_0-x*|| such that
\[
\mathbb E\|x_k-x^*\|^p\leq\frac{C_6}{(k+K_0)^{p-1}}
\qquad\text{for every integer }k\geq0.
\]

- **Long-range-dependent model.** There is a positive threshold C7 depending only on mu,L,delta such that, for every beta>C7, a positive threshold C8 depending only on mu,L,beta can be chosen with the following property: for every fixed K0>=C8, there is a finite nonnegative C9 depending only on mu,L,beta,delta,sigma,K0 and ||x_0-x*|| such that
\[
\mathbb E\|x_k-x^*\|^2\leq\frac{C_9}{(k+K_0)^\delta}
\qquad\text{for every integer }k\geq0.
\]

The choices must be uniform over operators, initial points, dimensions, and noise laws with the same listed parameter values. In particular, no constant may depend on k; C4 and C7 may not depend on beta or K0; and C5 and C8 may not depend on K0.
