# Problem

## Setup

Let S and A be Polish spaces equipped with their Borel sigma-fields. Write P(E) for the probability measures on a space E. Let mu in P(A), let P(ds'|s,a) be a measurable transition probability kernel, and let c:S x A -> R be measurable with |c(s,a)|<=C_c<infinity. Fix gamma in (0,1) and tau>0.

For probability measures r and nu, define KL(r||nu)=int log(dr/dnu)dr when r is absolutely continuous with respect to nu, and define it to be +infinity otherwise. Use the extended integral convention 0 log 0=0.

An admissible policy pi is a measurable probability kernel with a jointly measurable density p_pi(a|s) relative to mu for which there is a finite M_pi such that

`exp(-M_pi)<=p_pi(a|s)<=exp(M_pi)`

for every s and mu-almost every a. Densities and their logarithms are taken in jointly measurable versions satisfying these bounds.

For bounded measurable V:S->R, define

`Q_V(s,a)=c(s,a)+gamma int V(s')P(ds'|s,a)`,

`(T^pi V)(s)=int Q_V(s,a)pi(da|s)+tau KL(pi(.|s)||mu)`,

and

`(T V)(s)=inf_{r in P(A), r<<mu}[int Q_V(s,a)r(da)+tau KL(r||mu)]`.

Let V_tau^pi be the bounded fixed point of T^pi, let Q_tau^pi=Q_{V_tau^pi}, and let V_tau^* be the bounded fixed point of T, attained by an admissible optimal policy. For rho in P(S), define

`V_tau^pi(rho)=int V_tau^pi(s)rho(ds)` and `V_tau^*(rho)=int V_tau^*(s)rho(ds)`.

Let d be a positive integer and let phi:S x A->R^d be measurable with ||phi(s,a)||_2<=1. Fix beta in P(S x A). Define

`G_beta=int phi(s,a)phi(s,a)^T beta(ds,da)` and `lambda_beta=lambda_min(G_beta)>0`.

Assume exact realizability: for every admissible pi there exists theta_pi in R^d such that

`Q_tau^pi(s,a)=<theta_pi,phi(s,a)>`

for every (s,a).

For each pi, define the state-action transition kernel

`K_pi((s,a),ds',da')=P(ds'|s,a)pi(da'|s')`

and the probability measure

`d_beta^pi=(1-gamma)sum_{j=0}^infinity gamma^j beta K_pi^j`,

where beta K_pi^0=beta and beta K_pi^j is the distribution after j transitions from beta.

For theta in R^d, define

`q_theta(s,a)=<theta,phi(s,a)>`,

`v_theta^pi(s)=int[q_theta(s,a)+tau log p_pi(a|s)]pi(da|s)`,

`delta_{theta,pi}(s,a)=q_theta(s,a)-c(s,a)-gamma int v_theta^pi(s')P(ds'|s,a)`,

`MSBE(theta,pi)=1/2 int delta_{theta,pi}(s,a)^2 d_beta^pi(ds,da)`,

and

`g(theta,pi)=int delta_{theta,pi}(s,a)phi(s,a)d_beta^pi(ds,da)`.

Starting from an admissible pi^0 and theta^0 in R^d, use exact integrals to perform, for n=0,1,2,...,

`theta^{n+1}=theta^n-h g(theta^n,pi^n)`

and, separately at every state s,

`pi^{n+1}(.|s)=argmin_{r in P(A), r<<mu}{int[q_{theta^{n+1}}(s,a)+tau log p_{pi^n}(a|s)]r(da)+(1/lambda)KL(r||pi^n(.|s))}`.

Set

`Gamma=(1-sqrt(gamma))(1-gamma)lambda_beta`

and

`h_bar=(1/2)min{Gamma/[3(1+gamma)^2],(Gamma^2-16gamma^2)/[Gamma(24gamma^2+3(1+gamma)^2)]}`.

Assume lambda>0, 0<tau lambda<1, and 32gamma^2/Gamma^2<1. Choose 0<h<=h_bar.

## Task

Prove that there is a finite constant R, depending only on gamma, tau, lambda_beta, C_c, and the initialization, but not on h, lambda, or n, such that

`sup_{n>=0}[||theta^n||_2+sup_s KL(pi^n(.|s)||mu)]<=R`.

Furthermore, prove that there is a finite constant C, with the same allowed dependence and additionally allowed to depend on lambda, but not on h, rho, or n, such that simultaneously for every rho in P(S) and every integer n>=1,

`min_{0<=k<n}[V_tau^{pi^k}(rho)-V_tau^*(rho)]<=C(1/sqrt(nh)+lambda/h)`.
