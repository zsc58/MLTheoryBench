# Problem

## Setup

Fix integers K>=2 and r>=1, and constants 0<xi<1/2, 0<zeta<1, nu>=0, x_max>=0, and B>0. Let observations have feature vectors x in R^r and one of two sensitive groups s in {1,2}. The feature distribution in group s is a probability distribution P_s supported on {x: ||x||_2<=x_max}.

Use the fixed coordinate representation

vartheta(Theta)=(pi_1,...,pi_{K-1},mu_1,...,mu_K,vech(Sigma_1),...,vech(Sigma_K)) in R^d,

where vech lists the upper-triangular entries of a symmetric matrix and

d=(K-1)+Kr+K r(r+1)/2.

Consider a K-component Gaussian mixture with parameters Theta=(pi_k,mu_k,Sigma_k)_{k=1}^K and r-dimensional Gaussian density

f(x;Theta)=sum_{k=1}^K pi_k N(x;mu_k,Sigma_k),

where pi_k>0, sum_k pi_k=1, and Sigma_k is positive definite. Define the soft responsibility

psi_k(x;Theta)=pi_k N(x;mu_k,Sigma_k) / [sum_{ell=1}^K pi_ell N(x;mu_ell,Sigma_ell)].

Let Phi_{xi,zeta,nu} be the regular class of parameters satisfying, for every k, xi<pi_k<1-xi, ||mu_k||_2<=nu, and all eigenvalues of Sigma_k lie strictly between zeta and zeta^{-1}. Assume also that ||vartheta(Theta)||_2<=B.

For independent samples, with each group sample consisting of n_s>=1 iid draws with replacement from P_s, let X_1^(s),...,X_{n_s}^(s) denote the observations. Assume the two group samples are mutually independent. Let n'=min{n_1,n_2}, and define

Delta(Theta)=max_{1<=k<=K} | E_{P_1} psi_k(X;Theta)-E_{P_2} psi_k(X;Theta) |,

hatDelta(Theta)=max_{1<=k<=K} | n_1^{-1} sum_i psi_k(X_i^(1);Theta)-n_2^{-1} sum_j psi_k(X_j^(2);Theta) |.

Constants may depend on xi,zeta,nu,x_max,K,r,B, but not on n_1,n_2 or delta.

## Task

Prove that there is a constant C=C(xi,zeta,nu,x_max,K,r,B) such that, for every 0<delta<1, with probability at least 1-delta over the two group samples,

sup_{Theta in Phi_{xi,zeta,nu}} |hatDelta(Theta)-Delta(Theta)| <= 4 C sqrt(d/n') + 8 sqrt(2 log(8/delta)/n').

The probability statement is simultaneous over all parameters in the regular class and uses the population gap Delta defined above.
