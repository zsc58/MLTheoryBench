# Problem

## Setup

Fix positive integers n, k, and d, data points x_1, ..., x_n in R^d, and a nonempty compact set K contained in (R^d)^k. A centroid tuple is mu = (mu_1, ..., mu_k) in K. For sigma > 0 define the softmax responsibilities

r_ij(sigma; mu) = exp(-||x_i - mu_j||^2 / (2 sigma^2)) / sum_{l=1}^k exp(-||x_i - mu_l||^2 / (2 sigma^2)).

Define the soft weighted-distortion objective and the hard nearest-centroid distortion by

L_sigma(mu) = sum_{i=1}^n sum_{j=1}^k r_ij(sigma; mu) ||x_i - mu_j||^2,

J(mu) = sum_{i=1}^n min_{1 <= j <= k} ||x_i - mu_j||^2.

For a family F_sigma on K, say that F_sigma Gamma-converges to F as sigma tends to zero if (i) for every sigma_m -> 0 and mu_m -> mu in K, liminf_m F_{sigma_m}(mu_m) >= F(mu), and (ii) for every mu in K and every sigma_m -> 0, there exists mu_m -> mu in K with limsup_m F_{sigma_m}(mu_m) <= F(mu).

## Task

Prove that L_sigma Gamma-converges to J on K as sigma tends to zero. Moreover, if sigma_m -> 0 and mu_m is a minimizer of L_{sigma_m} on K for each m, then every accumulation point of (mu_m) is a minimizer of J on K.
