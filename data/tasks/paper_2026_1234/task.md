# Problem

## Setup

Let `0 < alpha_0, gamma, alpha < 1`. Let `D_tr` be a training sample and let `pi(d theta | D_tr)` be a posterior probability measure on parameters `theta`. For every covariate `x` and parameter `theta`, let `F_theta(. | x)` be a conditional CDF, with generalized inverse
\[
F^{-1}(p\mid x)=\inf\{y:F(y\mid x)\ge p\}.
\]
Define
\[
a_\theta(x)=F_\theta^{-1}(\alpha_0/2\mid x),\qquad
b_\theta(x)=F_\theta^{-1}(1-\alpha_0/2\mid x).
\]
Let `c_L(x)` be the `gamma/2` posterior quantile of the random variable `a_theta(x)`, and let `c_U(x)` be the `1-gamma/2` posterior quantile of `b_theta(x)`, where posterior quantiles use the same generalized-inverse convention. Retain
\[
R(x)=\{\theta:a_\theta(x)\ge c_L(x),\ b_\theta(x)\le c_U(x)\},
\]
and set the trimmed envelope `L(x)=c_L(x)`, `U(x)=c_U(x)`.

Let `(X_i,Y_i)`, `i=1,...,m`, be a calibration split, and let `(X_{m+1},Y_{m+1})` be a test point. Together with `D_tr`, these observations are exchangeable; the envelope is fitted using `D_tr` only. Define calibration scores
\[
r_i=\max\{L(X_i)-Y_i,\ Y_i-U(X_i)\}.
\]
Set `k=ceil((m+1)(1-alpha))` and let `hat t` be the `k`th order statistic of the calibration scores (with `hat t=+infinity` when `k>m`). Define
\[
\mathcal C(x)=\{y:\max\{L(x)-y,\ y-U(x)\}\le\hat t\}.
\]

## Task

Prove the following integrated theorem:

1. For every fixed `x`, the posterior-predictive probability of the trimmed envelope satisfies
\[
\int F_\theta([L(x),U(x)]\mid x)\,\pi(d\theta\mid D_{tr})\ge(1-\gamma)(1-\alpha_0).
\]
2. The conformalized set has finite-sample distribution-free marginal coverage
\[
\Pr\{Y_{m+1}\in\mathcal C(X_{m+1})\}\ge1-\alpha.
\]
