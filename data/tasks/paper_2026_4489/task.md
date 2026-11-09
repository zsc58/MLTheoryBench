# Problem

## Setup

Fix one arm. Its successive pulls are independent copies (X_t,Y_t,F_t) of a fixed joint law (X,Y,F), where X has distribution D and Y,F belong to [0,1] almost surely. The target is theta=E[Y]. The proxy F_t is always observed, whereas Y_t is observed only if that pull is audited.

A policy is a fixed measurable function pi of the current context and proxy. After observing (X_t,F_t), draw A_t with Bernoulli probability pi(X_t,F_t), using fresh randomization independent of the outcomes and of other pulls. In particular, conditional on the current observables and the past observed history, A_t is independent of Y_t. Policies must satisfy, almost surely,
\[
\pi_{\min}\leq\pi(X,F)\leq1,
\qquad E[\pi(X,F)]=\rho,
\qquad 0<\pi_{\min}\leq\rho\leq1.
\]
All expectations refer to the fixed arm's joint law and, where applicable, the audit randomization. Let g be a measurable version of
\[
g(x,f)=E[(Y-F)^2\mid X=x,F=f].
\]

For each integer n>=1, use the inverse-propensity residual estimator
\[
\widehat\theta_n=\frac1n\sum_{t=1}^n
\left[F_t+\frac{A_t}{\pi(X_t,F_t)}(Y_t-F_t)\right].
\]
The weighted residual term is taken to be zero when A_t=0, so the estimator uses only observed data. Let V(pi) be the variance of one summand, equivalently the asymptotic variance coefficient lim_{n to infinity} n Var(theta-hat_n). Define the audit-induced variance component by
\[
B(\pi)=V(\pi)-\operatorname{Var}(Y).
\]

## Task

Prove that among all feasible policies, an optimizer can be chosen with
\[
\pi^*(x,f)=\max\{\pi_{\min},\min\{1,c\sqrt{g(x,f)}\}\}
\quad\text{on }\{g>0\},
\]
for a suitable c in [0,infinity], where c=infinity means full auditing on the positive-g stratum. Its values on {g=0} may be chosen measurably in [pi_min,1] to complete the budget E[pi*]=rho. Changing these values while preserving their total audit budget does not affect V. The assertion includes endpoint budgets and the case g=0 almost surely.

Also prove that uniform auditing need not be optimal and can have an arbitrarily larger audit-induced variance component. Precisely, for every fixed 0<pi_min<rho<1 and every L>0, there is a joint law satisfying the setup, with g(X,F) not almost surely constant, for which an optimal policy satisfies
\[
0<B(\pi^*)
\quad\text{and}\quad
B(\pi\equiv\rho)>L\,B(\pi^*).
\]
