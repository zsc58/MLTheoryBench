# Problem

## Setup

Let X = R^m with its Euclidean metric, and let Z = R^d and Theta = R^p, where m,d,p are positive integers. The latent prior pi_Z and the parameter prior pi_Theta are nondegenerate Gaussian laws. The notation pi_Z(z) also denotes the density of the latent prior. Conditional on (z,theta), the observable has Gaussian density p_theta(x|z) with mean mu_theta(z) and covariance Sigma_theta(z). There is a constant lambda>0 such that Sigma_theta(z)>=lambda I_m for every z,theta, in the positive-semidefinite order. The mean and covariance maps are jointly measurable and continuous in (z,theta).

Let U=R^p times (0,infinity), with its Euclidean topology and Borel sigma-algebra. For u=(a_u,s_u) in U, let q_u=N(a_u,s_u^2 I_p). For every Borel set A in X, define the induced observable law
P_u(A) = integral over z and theta of P_theta(A|z) pi_Z(dz) q_u(dtheta),
where P_theta(A|z)=integral_A p_theta(x|z) dx.

For x in X and u in U, define the profiled criterion
m(x;u) = sup over z in Z of { E_{theta~q_u}[log p_theta(x|z)] + log pi_Z(z) }.
The inner expectation may take the value minus infinity. Assume that m(x;u) is a finite real number for every x,u.

Let P0 be a Borel probability law on X and let X_1,X_2,... be iid observations from P0. Assume that
integral |m(x;u)| P0(dx) < infinity
for every u in U. Define the population and empirical objectives by
J(u) = E_{X~P0}[m(X;u)] - KL(q_u||pi_Theta),
J_N(u) = (1/N) sum_{i=1}^N m(X_i;u) - KL(q_u||pi_Theta),
where KL(q_u||pi_Theta) is the integral of log(dq_u/dpi_Theta) against q_u.

For probability laws P and Q on X, define the bounded-Lipschitz distance by
d_BL(P,Q) = sup_f |integral f d(P-Q)|,
where the supremum is over all functions f with sup_x |f(x)|<=1 and |f(x)-f(y)|<=||x-y|| for all x,y.

Let U_1 subseteq U_2 subseteq ... subseteq U be nonempty compact sieves whose union is dense in U. Suppose J has a maximizer u* in U and every maximizer induces the same law P*=P_{u*}. Let the fitted parameter hat u_N be measurable and belong to U_N almost surely.

Define
omega_N = sup over u in U_N |J_N(u)-J(u)|,
delta_N^alg = sup over u in U_N J_N(u) - J_N(hat u_N),
r_N = J(u*) - sup over u in U_N J(u).
Assume omega_N is measurable, allowing the value +infinity. Assume
omega_N ->p 0, delta_N^alg ->p 0, and r_N -> 0
as N tends to infinity. Convergence in probability is with respect to the observations and any randomness used to produce hat u_N.

Assume also the population separation condition: for every epsilon>0,
Delta(epsilon) = inf { J(u*)-J(u) : u in U, d_BL(P_u,P*)>=epsilon } > 0,
with the convention inf(empty)=+infinity.

## Task

Prove that d_BL(P_{hat u_N},P*) ->p 0. In the correctly specified case stipulated by P*=P0, conclude that d_BL(P_{hat u_N},P0) ->p 0.
