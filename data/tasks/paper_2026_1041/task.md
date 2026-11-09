# Problem

## Setup

Let inputs lie in R^d. Fix an integer M >= 1, weights w_m >= 0 with sum_m w_m = 1, and activation functions h_m: R -> R. For each width H, draw iid hidden-parameter pairs (a_j,u_j), where a_j ~ N(0,sigma_a^2) and u_j ~ N(0,sigma_u^2 I_d), with a_j independent of u_j and the pairs independent across j. Draw independent output-weight blocks v_j^(m) ~ N(0,sigma_v^2/H), independent over j,m and of the hidden parameters. Let b ~ N(0,sigma_b^2) be independent of all these variables. Define

f_H(x) = b + sum_{m=1}^M sqrt(w_m) sum_{j=1}^H v_j^(m) h_m(a_j + u_j^T x).

For a pair of inputs, let (Z(x), Z(x')) denote the centered Gaussian pair induced by one hidden unit, with Cov(Z(x), Z(x')) = sigma_a^2 + sigma_u^2 x^T x'. Assume that, for every m and x, E[h_m(Z(x))^2] < infinity (for example, each h_m has polynomial growth). Set

K_m(x,x') = E[h_m(Z(x)) h_m(Z(x'))],
K(x,x') = sigma_b^2 + sigma_v^2 sum_{m=1}^M w_m K_m(x,x').

## Task

Prove that, as H tends to infinity, the random functions f_H converge in finite-dimensional distributions to a centered Gaussian process with covariance kernel K: for every n and every x_1,...,x_n in R^d,

(f_H(x_1),...,f_H(x_n)) converges in distribution to N_n(0, [K(x_r,x_s)]_{r,s=1}^n).
