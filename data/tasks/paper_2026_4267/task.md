# Problem

## Notation

All logarithms are natural. For a vector v, let supp(v) be its nonzero-coordinate set, let ||v||_0 be its size, and let ||v||_q^q=sum_j |v_j|^q for q>=1. Matrix eigenvalues refer to symmetric matrices. Write a vee b=max{a,b}.

## Upper-bound experiment and estimator

Let n,p>=2 be integers and sigma>0. Consider

Y=X beta*+sqrt(n)theta*+xi,

where beta* is in R^p, theta* is in R^n, s=||beta*||_0 satisfies 1<=s<p, and o=max{||theta*||_0,1}<n. The coordinates of xi are independent, centered, and sigma-sub-Gaussian: E exp(t xi_i)<=exp(sigma^2 t^2/2) for every real t. The noise vector xi is independent of X.

The rows of X are independent and distributed as Z_i Sigma^(1/2), where all standardized coordinates Z_ij are iid, centered, have variance one, and satisfy E exp(t Z_ij)<=exp(t^2/2) for every real t. For a fixed M>1, assume

M^(-1)<=Lambda_min(Sigma)<=Lambda_max(Sigma)<=M.

Set delta=4M^2/(4M^2+1), and fix

eta in [2M/(4M^2+1),4M/(4M^2+1)],  kappa in (delta,1).

The assertion below includes the existence of constants C_M=C_M(M)>1, C_0=C_0(M,eta,kappa)>0, and C=C(M,eta,kappa)>0. These constants are fixed independently of n,p,s,o,sigma,beta*,theta*, and the probability parameter. Assume

n>=C_0(s log p+o log n).

Define the limiting thresholds by

lambda_beta,infty=(16eta kappa/(kappa-delta))sigma sqrt(M log p/n)
 +(48eta^2kappa^2C_M/(kappa-delta)^3)sigma sqrt((s log p+o log n)/(ns))sqrt(o log n/n),

lambda_theta,infty=(12eta kappa/(kappa-delta))sigma sqrt(log n/n)
 +(64eta^2kappa^2C_M sqrt(M)/(kappa-delta)^3)sigma sqrt((s log p+o log n)/(no))sqrt(s log p/n).

For every positive integer m and lambda>0, define T_lambda^m:R^m -> R^m by

[T_lambda^m(z)]_j=z_j 1{|z_j|>=lambda},  j=1,...,m.

The superscript is the ambient dimension; this operator has no prescribed support-size cap.

Define

L(beta,theta)=(2n)^(-1)||Y-X beta-sqrt(n)theta||_2^2.

Starting from beta^0=0 and theta^0=0, at each stage-one iteration form the simultaneous updates

H_beta^{t+1}=beta^t+eta X^T(Y-X beta^t-sqrt(n)theta^t)/n,

H_theta^{t+1}=theta^t+eta(Y-X beta^t-sqrt(n)theta^t)/sqrt(n).

Update the thresholds and vectors by

lambda_beta,t+1=(kappa lambda_beta,t) vee lambda_beta,infty,
lambda_theta,t+1=(kappa lambda_theta,t) vee lambda_theta,infty,

beta^{t+1}=T_{lambda_beta,t+1}^p(H_beta^{t+1}),
theta^{t+1}=T_{lambda_theta,t+1}^n(H_theta^{t+1}).

Choose initial thresholds satisfying

lambda_beta,0>lambda_beta,infty,  lambda_theta,0>lambda_theta,infty,
sqrt(s)lambda_beta,0>||beta*||_2,  sqrt(o)lambda_theta,0>||theta*||_2,

lambda_beta,0/lambda_theta,0=lambda_beta,infty/lambda_theta,infty.

Run this stage for

T_1=max{ceil(log(lambda_beta,0/lambda_beta,infty)/log(1/kappa)),ceil(log(lambda_theta,0/lambda_theta,infty)/log(1/kappa))}

iterations and set beta_hat=beta^{T_1}, theta_hat=theta^{T_1}.

Stage two starts at (beta_hat,theta_hat), uses the same simultaneous updates and coordinatewise thresholding, but keeps the thresholds fixed at lambda_beta,infty and lambda_theta,infty. Run it for T_2=ceil(C log n) iterations and denote its outputs by (tilde beta,tilde theta).

## Upper-bound claims

Prove that the constants C_M,C_0,C can be chosen so that, with probability at least 1-O(p^-2+n^-3),

||beta_hat||_0 lesssim s,  ||theta_hat||_0 lesssim o,

||beta_hat-beta*||_2^2 lesssim sigma^2[s log p/n+o^2 log^2 n/n^2],

||theta_hat-theta*||_2^2 lesssim sigma^2[o log n/n+s^2 log^2 p/n^2].

For every fixed varrho in (0,1), prove that with probability at least 1-varrho-O(p^-2+n^-3), the second-stage outputs satisfy ||tilde beta||_0 lesssim s and ||tilde theta||_0 lesssim o, and the condition

min_{j in supp(beta*)}|beta_j*| >= [4kappa/(kappa-delta)+(kappa-delta)/(4kappa)]lambda_beta,infty

implies

||tilde beta-beta*||_2^2 lesssim sigma^2[(s+log(1/varrho))/n+(s log p+o log n)^2/n^2].

Without this condition, prove the fallback bound for the second-stage output itself:

||tilde beta-beta*||_2^2 lesssim sigma^2[s log p/n+o^2 log^2 n/n^2].

Here every constant in lesssim and O depends only on M,eta,kappa; probabilities are over the design and noise. The probability assertion is for each fixed varrho, not one event simultaneous over all varrho.

## Separate lower-bound experiment

For this claim, let n,p,s,o be integers with 1<=s<p and 9<=o<n, and let sigma>0. Assume max{s log p,o log n}<=K_0 n for a fixed constant K_0>0.

Fix a clean covariate law nu: a row has distribution Z Sigma^(1/2), where Z has iid centered, variance-one, 1-sub-Gaussian coordinates as defined above. In this lower-bound experiment replace the global spectral bounds of the upper experiment by the requirement

sup_{S subset {1,...,p}, |S|<=2s}Lambda_max(Sigma_{S,S})<=C_{2s},

where C_{2s}>0 is fixed and Sigma is a covariance matrix. The clean one-observation law P_beta is specified by x~nu and, conditional on x, y=x beta+epsilon, with epsilon~N(0,sigma^2) independent of x.

For an integer k between 0 and o, let P_{beta,k} be the class of joint laws of n observed design-response pairs for which there is an unknown set O of k indices such that the pairs outside O are iid with law P_beta. The pairs in O may have an arbitrary joint law; no restriction is imposed on their dependence on the clean pairs. Set

M(beta,o)=union_{k=0}^o P_{beta,k}.

The infimum below is over all measurable estimators hat beta:(R^p x R)^n -> R^p based on the observed pairs, with no access to beta or O.

Prove that, for every q in [1,2] and every constant 0<c_q<(8C_{2s})^(-q/2)/160,

inf_{hat beta} sup_{||beta||_0<=s} sup_{R in M(beta,o)} E_R||hat beta-beta||_q^q
>=c_q sigma^q[s(log(ep/s)/n)^(q/2)+s^(1-q/2)o^q/n^q].
