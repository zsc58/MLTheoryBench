# Problem

## Setup

For each n>=2, let d=d_n be a positive integer, let rho=rho_n and eta=eta_n satisfy -1<rho,eta<1, and let S_n denote the permutations of [n]. Let A and B~ be symmetric n x n matrices with zero diagonal. For each i<j, the pairs (A_ij,B~_ij) are independent centered Gaussian vectors with covariance [[1,rho],[rho,1]]. Let X and Y~ be n x d matrices; the pairs (X_{ik},Y~_{ik}) are independent centered Gaussian vectors with covariance [[1,eta],[eta,1]], independently over i,k and independently of the edge variables.

Independently of these arrays, a hidden permutation pi* is uniform on S_n. The observations are A, X and the permuted copies B and Y, defined by B_{pi*(i),pi*(j)}=B~_{ij} for i<j and Y_{pi*(i),k}=Y~_{ik} for every i,k. The matrices B and Y, but not B~ and Y~, are observed. An estimator is any measurable map (A,B,X,Y)->S_n. Exact recovery means P(hat pi=pi*) -> 1. A MAP estimator maximizes the posterior probability under the uniform prior; use any fixed measurable rule to select among maximizers.

All asymptotic statements are as n->infinity; omega(.) has its usual meaning.

## Task

Prove the following integrated theorem.

1. If d=omega(log n) and, for some fixed epsilon>0 and all sufficiently large n,

   rho^2 n/(1-rho^2) + eta^2 d/(1-eta^2) >= 4(1+epsilon) log n,

   then the MAP estimator exactly recovers pi* with probability 1-o(1).

2. If d=omega((log n)^2) and

   rho^2 n/(1-rho^2) + eta^2 d/(1-eta^2) <= 4 log n - log log n - omega(1),

   then every estimator has exact-recovery probability o(1).
