# Problem

## Setup

Use the Euclidean norm on R^d. For a positive integer d and a vector mu in R^d with ||mu||=7 sqrt(d), let pi_tar=N(mu,I_d). Its score is grad log pi_tar(x)=-(x-mu).

For a globally Lipschitz vector field hat{s}:R^d->R^d and an initial probability law rho, let X be the solution, for t>=0, of

dX_t=hat{s}(X_t)dt+sqrt(2)dB_t,   X_0~rho,

where B is standard d-dimensional Brownian motion independent of X_0. Write L(X_t) for the law of X_t. For probability measures P,Q on R^d, define

TV(P,Q)=sup_{A Borel}|P(A)-Q(A)|.

For a finite real p>=1, define the target score error by

(E_{X~pi_tar}||hat{s}(X)-grad log pi_tar(X)||^p)^(1/p).

## Task

Prove that there exist universal constants c,C,L>0, a universal integer d_*>=1, and a choice of deterministic vector fields hat{s}_{d,mu} for every integer d>=d_* and every mu with ||mu||=7 sqrt(d), satisfying all the following properties.

1. Each field is globally Lipschitz with constant at most L.

2. For the diffusion driven by hat{s}_{d,mu} and initialized with X_0~N(0,I_d), every 0<=T<=exp(c d/2) satisfies

   TV(L(X_T),pi_tar)>=1-C exp(-c d).

3. For every fixed finite real p>=1, there are constants C_p,c_p>0 and an integer d_0(p)>=d_*, depending only on p, such that for every d>=d_0(p) and every mu with ||mu||=7 sqrt(d),

   (E_{X~pi_tar}||hat{s}_{d,mu}(X)-grad log pi_tar(X)||^p)^(1/p)<=C_p exp(-c_p d).

The same family of fields must satisfy these conclusions for all the stated p and T; the fields may depend on d and mu, but not on p or T.
