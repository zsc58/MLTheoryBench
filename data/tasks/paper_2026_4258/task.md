# Problem

## Setup

Let D_n=(z_1,...,z_n), with z_i=(x_i,y_i), be training observations. The parameter vartheta lies in an open subset of a finite-dimensional Euclidean space. Vector norms are Euclidean and matrix norms are the induced operator norms. All random objects and probability expressions below are assumed measurable.

Define

L_n(vartheta)=n^{-1} sum_{i=1}^n ell(z_i,vartheta),

hat vartheta=argmin_vartheta L_n(vartheta),

g_i=gradient_vartheta ell(z_i,hat vartheta),

H_i=Hessian_vartheta ell(z_i,hat vartheta),

H=n^{-1} sum_i H_i,    H_F=n^{-1} sum_i g_i g_i^T.

Assume the empirical minimizer is unique and sum_i g_i=0. In a neighborhood N of hat vartheta, the score map vartheta -> gradient_vartheta ell(z_i,vartheta) is twice continuously differentiable for almost every observation, and the per-observation Hessians are locally Lipschitz. Assume H is invertible and, as n -> infinity,

||H^{-1}||=O_p(1),    n^{-1} sum_i ||g_i||^2=O_p(1).

Let A be a nonempty compact interval contained in (0,infinity). For each fixed alpha>0, resampling weights are drawn conditionally on D_n according to Dirichlet(alpha,...,alpha), independently of the training data. Let j be the length-n all-ones vector, tilde w=nw-j, and G=[g_1,...,g_n], with gradients as columns. Define the influence perturbation

Delta vartheta_w=-H^{-1}G tilde w/n.

For each fixed alpha in A, assume the weighted minimizer

hat vartheta_w=argmin_vartheta sum_i w_i ell(z_i,vartheta)

exists in N and satisfies

||hat vartheta_w-hat vartheta||=O_p(n^{-1/2}),

||sum_i w_i H_i-H||=O_p(n^{-1/2}).

These rate statements refer to the training and resampling randomness as n -> infinity; they do not assert uniform rates over alpha.

## Predictive Intervals and Validation

Let 0<tau<1. To specify the predictive distribution, let R(x,u,e) be a given measurable real-valued prediction rule, where u is a parameter vector, and let nu be a given probability law for an auxiliary variable e. The rule and law may depend on D_n, but are fixed before observing validation data and do not depend on alpha. Assume the rule is defined on the parameter values used below. Conditional on D_n, draw e with law nu independently of w and define

F_alpha(x,t)=Pr{R(x,hat vartheta+Delta vartheta_w,e)<=t | D_n}.

For 0<p<1, define

q_p(x;alpha)=inf{t in R: F_alpha(x,t)>=p},

I_{1-tau}(x;alpha)=[q_{tau/2}(x;alpha),q_{1-tau/2}(x;alpha)].

Assume the interval endpoints are measurable in x and alpha.

Let P be the population law of a fresh pair (X,Y), with Y real-valued. The validation pairs (X_k,Y_k), k=1,...,m, are independent draws from P and are independent of D_n. A fresh test pair also has law P and is independent of the training and validation data. Define population and validation coverage by

C(alpha)=integral 1{y in I_{1-tau}(x;alpha)} P(dx,dy),

C_hat_m(alpha)=m^{-1} sum_{k=1}^m 1{Y_k in I_{1-tau}(X_k;alpha)}.

Thus C is population coverage for the trained predictive construction and may depend on D_n. For the validation limit, n is held fixed while m -> infinity. Assume, almost surely with respect to D_n, that C is continuous and strictly monotone on A and that there is a unique alpha_tau in A satisfying C(alpha_tau)=1-tau. Assume also

sup_{alpha in A}|C_hat_m(alpha)-C(alpha)| ->p 0

as m -> infinity. Choose any measurable selector

alpha_hat_m in argmin_{alpha in A}|C_hat_m(alpha)-(1-tau)|.

## Task

Prove that, for each fixed alpha in A, as n -> infinity,

||n Var(Delta vartheta_w | D_n)-alpha^{-1}H^{-1}H_FH^{-1}|| ->p 0.

The matrices on the right are the empirical matrices at sample size n; convergence to fixed matrices is not assumed. Identify the alpha=1 case as the Bayesian-bootstrap covariance scaling. For the additional specialization in which ell is a correctly specified negative log-likelihood and

||H_F-H|| ->p 0,

prove that at alpha=1,

||n Var(Delta vartheta_w | D_n)-H^{-1}|| ->p 0.

Also prove, as m -> infinity with n fixed, that

alpha_hat_m ->p alpha_tau,    C(alpha_hat_m) ->p 1-tau.
