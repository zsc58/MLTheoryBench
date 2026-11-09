# Problem

## Setup

There are K fixed sites and a fixed covariate dimension d, where K and d are positive integers. Site k contains n_k independent right-censored subjects, with total n=sum_{k=1}^K n_k and, as n tends to infinity, n_k/n tends to p_k>0. The sample sizes are nonrandom. Subjects are independent within and across sites, and the observations within each site are identically distributed according to a fixed site-specific law.

Subject i at site k has covariate X_{ik} in R^d, nonnegative event time T_{ik}, censoring time C_{ik}, observed time Y_{ik}=min(T_{ik},C_{ik}), event indicator delta_{ik}=1{T_{ik}<=C_{ik}}, counting process N_{ik}(t)=1{Y_{ik}<=t,delta_{ik}=1}, and at-risk process R_{ik}(t)=1{Y_{ik}>=t}. Fix tau>0. For a column vector v, write v^{\otimes2}=vv^T.

At each site assume that C_{ik} is independent of (T_{ik},X_{ik}); in particular, T_{ik} and C_{ik} are conditionally independent given X_{ik}. On [0,tau], assume the continuous-time common-coefficient additive hazard model
\[
\lambda_{ik}(t\mid X_{ik})=\lambda_{0k}(t)+\beta_0^TX_{ik},
\]
where each site has its own nonnegative locally integrable baseline hazard lambda_{0k}, but the same beta_0 in R^d. Covariates are time-independent and satisfy ||X_{ik}||<=B almost surely for a fixed finite B. For each site and every t in [0,tau], assume P(R_{1k}(t)=1 | X_{1k})>0 almost surely, and P(Y_{1k}>=tau)>0. Assume every site information matrix A_k defined below is positive definite.

Define
\[
\mu_k(t)=\frac{E[R_{1k}(t)X_{1k}]}{E[R_{1k}(t)]},
\qquad
A_k=\int_0^\tau E\!\left[R_{1k}(t)(X_{1k}-\mu_k(t))^{\otimes2}\right]dt,
\]
\[
\Sigma_k=E\!\left[\int_0^\tau (X_{1k}-\mu_k(t))^{\otimes2}dN_{1k}(t)\right],
\qquad
A_S=\sum_{k=1}^Kp_kA_k,
\qquad
\Sigma_S=\sum_{k=1}^Kp_k\Sigma_k.
\]
For each site set
\[
\bar X_k(t)=\frac{\sum_iR_{ik}(t)X_{ik}}{\sum_iR_{ik}(t)},\quad
\widehat A_k=\frac1{n_k}\sum_i\int_0^\tau R_{ik}(t)(X_{ik}-\bar X_k(t))^{\otimes2}dt,
\]
\[
D_k=\frac1{n_k}\sum_i\int_0^\tau (X_{ik}-\bar X_k(t))dN_{ik}(t),
\quad
\widehat\Sigma_k=\frac1{n_k}\sum_i\int_0^\tau (X_{ik}-\bar X_k(t))^{\otimes2}dN_{ik}(t).
\]
Set bar X_k(t)=0 when its denominator is zero.

Let p_{k,n}=n_k/n and define
\[
\widehat A_S=\sum_kp_{k,n}\widehat A_k,
\qquad
\widehat\Sigma_S=\sum_kp_{k,n}\widehat\Sigma_k.
\]
On the event that Ahat_S is invertible, define the one-round stratified estimator and its weighted sandwich by
\[
\widehat\beta_S=\widehat A_S^{-1}\left(\sum_kp_{k,n}D_k\right),
\qquad
\widehat V_S=\widehat A_S^{-1}\widehat\Sigma_S\widehat A_S^{-1}.
\]
On the complementary event, set beta_hat_S=0 and Vhat_S=0, with zero vector and zero matrix of the appropriate dimensions.

## Task

Prove that, under the stated assumptions,
\[
\sqrt n\,(\widehat\beta_S-\beta_0)\Rightarrow N\!\left(0,A_S^{-1}\Sigma_SA_S^{-1}\right),
\]
and
\[
\widehat V_S\xrightarrow{p}A_S^{-1}\Sigma_SA_S^{-1}.
\]
The normal law may be degenerate. Thus n^{-1}Vhat_S is a consistent estimator of the estimator-scale asymptotic covariance: multiplying this covariance estimate by n gives convergence in probability to the covariance matrix in the displayed limiting normal law.
