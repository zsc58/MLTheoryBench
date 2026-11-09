# Problem

## Setup

Let m,n,d be positive integers, and let kappa in (0,1). Work conditional on fixed design matrices X_j in R^{n x d}, j=1,...,m, and fixed task parameters theta_j^star in R^d. For task j, observe
\[
y_j=X_j\theta_j^\star+\xi_j,
\]
and define Sigma_j=X_j^T X_j/n. Assume ||Sigma_j||_op<=1. Conditional on the complete collection of design matrices, all noise coordinates xi_{ji} are independent, centered, and unit-scale sub-Gaussian: for every real t,
\[
\mathbb E[\exp(t\xi_{ji})\mid X_1,\ldots,X_m]\le \exp(t^2/2).
\]
All probability statements below are conditional on the design. For positive semidefinite A, write ||v||_A=(v^T A v)^{1/2}.

There is a fixed nonempty inlier set S contained in {1,...,m}, a fixed centroid theta^star in R^d, and finite nonnegative epsilon,delta such that
\[
|S^c|/m\le\epsilon,\qquad \max_{j\in S}\|\theta_j^\star-\theta^\star\|_2\le\delta,
\]
while parameters of tasks in S^c are arbitrary and S,epsilon,delta are unknown to the estimator. Put s=|S|, N_S=ns, and
\[
\widehat\Sigma_S=s^{-1}\sum_{j\in S}\Sigma_j.
\]
Let B in [1,infinity] be a balancedness bound. When B is finite, require
\[
\Sigma_j\preceq B\widehat\Sigma_S\quad (j=1,\ldots,m).
\]
The convention B=infinity is used when no finite such bound exists; in that case no matrix inequality involving an infinite scalar is imposed. No individual lower-eigenvalue assumption is imposed.

Define f_j(theta)=||y_j-X_j theta||_2^2/(2n). Given lambda>0, let (theta_hat_1,...,theta_hat_m,beta_hat) be any minimizer of
\[
\frac1m\sum_{j=1}^m\bigl[f_j(\theta_j)+\lambda\|\theta_j-\beta\|_{\Sigma_j}\bigr]
\]
over (R^d)^{m+1}. Define E_j^in=||theta_hat_j-theta_j^star||_{Sigma_j}^2.

## Task

Let z=log(16m/kappa) and choose lambda=q sqrt(dz/n) for a sufficiently large universal constant q. Prove that there are universal constants C>0 and c>0 such that, with probability at least 1-kappa, simultaneously:

1. Every task, including arbitrary outliers, satisfies
\[
E_j^{\rm in}\le Cq^2\frac d n z,\qquad j=1,\ldots,m.
\]
2. If B<=c min{1/epsilon,m}, with the convention 1/0=infinity, then every inlier additionally satisfies
\[
E_j^{\rm in}\le C\left[\frac{Bd}{mn}+\min\left\{B\delta^2,q^2\frac d n\right\}+q^2B^2\epsilon^2\frac d n\right]z,\qquad j\in S.
\]
The constants are universal, and the conclusion is independent of any lower bound on the individual task covariances.
