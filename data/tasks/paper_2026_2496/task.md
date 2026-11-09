# Problem

## Setup

Fix an integer dimension d>=1 and horizon T>=1. Let Y_1,...,Y_T be independent Rademacher signs. A dyadic predictable process consists of functions X_t:{-1,1}^{t-1}->R^d, with X_t evaluated on (Y_1,...,Y_{t-1}). Thus X_t is chosen before Y_t; over the finite sign tree its covariates are bounded. Define
\[
S_t=\sum_{i=1}^tY_iX_i,\qquad V_t=\sum_{i=1}^tX_iX_i^\top,\qquad R_t=S_t^\top V_t^\dagger S_t,
\]
where V_t^\dagger is the Moore-Penrose pseudoinverse. In particular, R_t=0 when V_t=0. Let
\[
R_d(T)=\sup_X\mathbb E[R_T],
\]
where the supremum is over all such dyadic predictable processes and the expectation is over the signs.

For the regret assertion below, consider the sequential square-loss game in which, on each round, the environment reveals x_t in R^d, the learner then predicts a real number \(\widehat y_t\), and the environment subsequently reveals y_t in [-1,1]. Strategies may be adaptive or randomized. Define
\[
\operatorname{Reg}(T)=\sum_{t=1}^T(\widehat y_t-y_t)^2-
\inf_{\theta\in\mathbb R^d}\sum_{t=1}^T(\langle\theta,x_t\rangle-y_t)^2.
\]

## Task

Prove the following sharp dimension dichotomy. In dimension d=1, there are absolute constants a,b>0 such that, for all T>=10,
\[
a\log T\le R_1(T)\le b\log T.
\]
More explicitly, for every 0<c<=1/4 and every scalar dyadic predictable process,
\[
\mathbb E e^{cR_T}\le T e^{c/(1-2c)},\qquad
\mathbb E R_T\le\frac{\log T}{c}+\frac1{1-2c},
\]
and some such process satisfies \(\mathbb E R_T\ge a\log T\) for T>=10.

In every dimension d>=2, for every T>=1 and epsilon in (0,1), prove
\[
R_d(T)\ge(1-\varepsilon^2)T,
\]
while always \(R_d(T)\le T\). Moreover, prove that for these d,T,epsilon there is one environment, independent of the learner's predictions, with \(\|x_t\|\le1\) and \(y_t\in\{-1,1\}\), for which every learner has
\[
\mathbb E[\operatorname{Reg}(T)]\ge(1-\varepsilon^2)T.
\]
The expectation is over the environment and any learner randomization. Consequently no regret bound sublinear in T and uniform over both covariate scale and all comparators in R^d holds in dimensions d>=2.
