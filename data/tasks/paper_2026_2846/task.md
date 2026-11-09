# Problem

## Setup

Let d and N be positive integers and let x_1,...,x_N in R^d be a finite data set. Define
\[
\mu=N^{-1}\sum_{j=1}^N x_j,\qquad \Sigma=N^{-1}\sum_{j=1}^N(x_j-\mu)(x_j-\mu)^T,
\]
and assume Sigma is positive definite. Let L be an invertible matrix with LL^T=Sigma. Fix delta>0 and sigma>=0, let epsilon be standard Gaussian in R^d, and define
\[
p_\delta(z)=N^{-1}\sum_{j=1}^N \mathcal N(z\mid x_j,\delta^2I_d),\quad
V(z)=-E_\epsilon[\log p_\delta(z+\sigma\epsilon)],\quad g(z)=\nabla V(z).
\]
The unconstrained density proportional to exp(-V) has free energy
\[
F(\rho)=\int V(z)\rho(z)\,dz+\int\rho(z)\log\rho(z)\,dz.
\]
Let C(mu,Sigma) be the class of normalized densities rho on R^d with finite displayed integrals, mean mu, and covariance Sigma.

For each integer P>=d+1, let 1_P be the all-ones vector in R^P, write Y=(y_1,...,y_P)^T in R^{P\times d}, and define
\[
M_P=\{Y:1_P^TY=0,\ Y^TY=PI_d\}.
\]
Set V_tilde(y)=V(mu+Ly). Let U_{M_P} denote the uniform measure induced by Stiefel-Haar measure on M_P. Define the constrained P-particle Gibbs law on M_P by density proportional to
\[
\exp\{-\sum_{i=1}^P V_{\rm tilde}(y_i)\}\,dU_{M_P}(Y).
\]
For a draw from this law, map each particle to Z_i=mu+Ly_i and denote the law of Z_1 by rho_P^{(1)}.

## Task

Prove that rho_P^{(1)} converges weakly as P tends to infinity to a density rho_infty, and that rho_infty is the unique minimizer of F over C(mu,Sigma). Equivalently, show that for some symmetric matrix Lambda and vector lambda,
\[
\rho_\infty(z)=Z^{-1}\exp\{-V(z)-\lambda^Tz-\tfrac12(z-\mu)^T\Lambda(z-\mu)\},
\]
with normalization constant Z, and, for Z distributed according to rho_infty,
\[
\lambda=-E[g(Z)],\qquad
\Sigma\Lambda+\Lambda\Sigma=2\bigl(I_d-\operatorname{sym}(C)\bigr),\quad
C=E[(Z-\mu)g(Z)^T],\quad \operatorname{sym}(C)=\tfrac12(C+C^T).
\]
