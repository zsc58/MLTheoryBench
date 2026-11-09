# Problem

## Setup

Let n and p be positive integers with p<n. Let Y in R^n and let X in R^{n x p} have full column rank. The observation model is

Y | beta,u,tau_y ~ N(X beta+u,tau_y^(-1)I_n),

where beta in R^p and tau_y>0. Denote its density in Y by f(Y|beta,u,tau_y).

Let W=(w_ij) be the adjacency matrix of a connected undirected graph on n vertices. Define d_i=sum_{j=1}^n w_ij, D=diag(d_1,...,d_n), and R=D-W. Thus R is symmetric positive semidefinite, has rank n-1, and has nullspace spanned by the all-ones vector 1. Set

E={v in R^n:1^T v=0}.

Equip E with the inherited Euclidean inner product, and let du denote its induced (n-1)-dimensional Lebesgue measure. For tau_u>0, let pi_tau_u be the normalized density on E proportional to

exp[-(tau_u/2)u^T R u].

Define

P_X^perp=I_n-X(X^T X)^(-1)X^T,

A=tau_y P_X^perp+tau_u R.

Assume v^T A v>0 for every nonzero v in E. Let Pi_E be the orthogonal projection onto E, and define the operator A_E:E to E by A_E v=Pi_E A v for v in E.

Use Lebesgue measure d beta as the flat-prior measure for beta, and define the integrated likelihood-prior function

g(Y,u|tau_y,tau_u)=pi_tau_u(u) integral_{R^p} f(Y|beta,u,tau_y) d beta.

Here g is not required to be a probability density normalized over Y and u. Define

L(tau_y,tau_u;Y)=log integral_E g(Y,u|tau_y,tau_u) du.

For mu in E and a positive definite self-adjoint covariance operator Sigma:E to E, write N_E(mu,Sigma) for the Gaussian distribution on E with that mean and covariance. Let Q be the family of all these distributions. For q in Q, also writing q for its density with respect to du, define

ELBO(q,tau_y,tau_u)=E_q[log g(Y,u|tau_y,tau_u)]-E_q[log q(u)].

## Task

For every Y and every fixed pair tau_y,tau_u>0 satisfying the setup, prove that the conditional posterior of u, after integrating beta, is the well-defined distribution N_E(mu_*,Sigma_*), where

b_E=Pi_E(tau_y P_X^perp Y),

mu_*=A_E^(-1)b_E,

Sigma_*=A_E^(-1).

Moreover, prove that

sup_{q in Q} ELBO(q,tau_y,tau_u)=L(tau_y,tau_u;Y),

so the Gaussian variational family admits an approximation with zero posterior approximation error.
