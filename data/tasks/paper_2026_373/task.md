# Problem

## Setup

Let (X, d) be a complete separable metric space with its Borel sigma-algebra, and let P2(X) be the Borel probability measures on X with finite second moment, equipped with the 2-Wasserstein metric W2. For alpha and beta in P2(X), W2(alpha, beta) is the infimum, over all couplings gamma of alpha and beta, of (integral d(x,y)^2 dgamma(x,y))^(1/2).

For each parameter theta, let K_theta be a Markov transition kernel on X. Its transfer operator T_theta maps a measure nu in P2(X) to the measure defined by

integral f(y) dT_theta(nu)(y) = integral [integral f(y) K_theta(x,dy)] dnu(x)

for every bounded measurable f. Assume T_theta maps P2(X) into itself and is a contraction in W2: there is kappa_theta in [0,1) such that

W2(T_theta(alpha), T_theta(beta)) <= kappa_theta W2(alpha, beta)

for all alpha, beta in P2(X). Assume it has an invariant law pi_theta in P2(X), meaning T_theta(pi_theta) = pi_theta.

Let rho in P2(X) be a data distribution, let Z_1,...,Z_n be iid with law rho, and let rho_n = (1/n) sum_{i=1}^n delta_{Z_i} be the empirical measure. Define

r_n(theta) = W2(T_theta(rho_n), rho_n),

s_n = W2(rho, rho_n).

## Task

Prove that, for every n >= 1, every parameter theta satisfying the setup, and every sample realization,

W2(pi_theta, rho) <= r_n(theta)/(1-kappa_theta) + s_n.
