# Problem

## Setup

Let the state space be a torus or R^d, with decay, periodicity, or boundary conditions sufficient for every integration by parts below. Let p be a strictly positive smooth probability density and let s = grad log p, where gradients are column vectors. For a smooth d x d matrix mobility M, set D_M = (M+M^T)/2, assume D_M is positive semidefinite, and define

F_M = M s + div M,
L_M f = F_M dot grad f + D_M : Hess f,

where (div M)_i = sum_j partial_j M_ij. Assume the observed and learned diffusions with mobilities M_obs and M_theta are well-defined Markov diffusions, both preserve p, and all displayed generator, semigroup, differentiation, and integrability operations are justified.

Let K_t^obs and K_t^theta be their Markov semigroups. Fix a finite set of fitted lags T_fit contained in (0,infinity). For every t in T_fit, assume the observed transition kernel has a positive continuously differentiable density p_t^obs(x_t | x_0), and define

s_{t|0}(x_t | x_0) = grad_{x_0} log p_t^obs(x_t | x_0).

All expectations E_p below are with respect to the stationary observed lagged pair (X_0^obs,X_t^obs), whose one-time law is p.

For the finite-horizon comparison below, impose the following explicit cross-generator domain condition. For every target alpha, the family {K_s^obs phi_alpha: 0 <= s <= T} lies in a common invariant generator core for L_{M_obs} and L_{M_theta} in L2(p), and the map s -> L_{M_theta}K_s^obs phi_alpha is Bochner integrable on [0,T]. The two semigroup generator equations and the product rule for s -> K_{t-s}^theta K_s^obs phi_alpha are valid on this core. Equivalently, for every t in [0,T], that comparison path is L2(p)-absolutely continuous with the generator derivative obtained by applying the two generators on the common core. This condition is a domain regularity assumption, not a conclusion of the theorem.

Let phi_1,...,phi_m and v_1,...,v_q be smooth scalar observables in L2(p), with all required operations well-defined. Define, for t in T_fit,

C_obs,alpha beta(t) = E_p[phi_alpha(X_t^obs) v_beta(X_0^obs)],

A_{alpha beta,t}[H] = -E_p[phi_alpha(X_t^obs) s_{t|0}(X_t|X_0)^T H(X_0^obs) grad v_beta(X_0^obs)].

Here grad v_beta is a column vector, so the displayed expression is scalar. Define

R_theta,alpha beta(t) = A_{alpha beta,t}[M_theta] - d C_obs,alpha beta(t)/dt.

Let N_A be the set of smooth matrix perturbations H for which M_obs+H is an admissible mobility and A_{alpha beta,t}[H]=0 for every selected alpha,beta and every t in T_fit. Let V = span{v_1,...,v_q}, let P_V be the L2(p)-orthogonal projection onto V, and let G_V be the Gram matrix (G_V)_{beta gamma}=<v_beta,v_gamma>_p. Assume its smallest eigenvalue lambda_V is positive.

Let U=(u_1,...,u_r) be a finite smooth scalar future dictionary. Each u_j is one of the selected fitted-lag evolved target functions K_{tau_j}^obs phi_{alpha_j}, with tau_j in T_fit. Define the dictionary residual matrix

mathsf R_theta,j beta = <(L_{M_theta}-L_{M_obs})u_j,v_beta>_p.

Assume ||mathsf R_theta||_F <= epsilon. Let P_U be the L2(p)-orthogonal projection onto span{u_1,...,u_r}.

Fix a horizon T>0. For each target alpha define the explicitly source-independent closure quantities

A_{U,alpha}(T) = sup_{0<=s<=T} inf { ||c||_2 : P_U K_s^obs phi_alpha = sum_{j=1}^r c_j u_j },

zeta_{U,V,alpha}^theta(T) = sup_{0<=s<=T} ||(Delta L - P_V Delta L P_U)K_s^obs phi_alpha||_{L2(p)},

where Delta L=L_{M_theta}-L_{M_obs}. Assume these quantities are finite.

## Task

Prove that, for every selected alpha,beta and every t in T_fit,

d C_obs,alpha beta(t)/dt = A_{alpha beta,t}[M_obs]
= -E_p[phi_alpha(X_t^obs) s_{t|0}(X_t|X_0)^T M_obs(X_0^obs) grad v_beta(X_0^obs)],

and

R_theta,alpha beta(t) = <Delta L K_t^obs phi_alpha,v_beta>_p.

Consequently, zero fitted residuals identify only the projected generator action on the selected evolved target functions. In particular, an admissible perturbation in N_A is observationally indistinguishable at the selected fitted lags.

Finally, for 0<=t<=T, with

C_theta,alpha beta(t)=E_p[phi_alpha(X_t^theta)v_beta(X_0^theta)],

prove

|C_theta,alpha beta(t)-C_obs,alpha beta(t)| <= t ||v_beta||_{L2(p)} [ A_{U,alpha}(T) lambda_V^{-1/2} epsilon + zeta_{U,V,alpha}^theta(T) ].
