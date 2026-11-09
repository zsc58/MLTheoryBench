# Problem

## Setup

For each pair of positive integers `(n,d)` in a sequence, let `Sigma=Sigma_{n,d}` be a deterministic real symmetric positive semidefinite `d x d` matrix with uniformly bounded operator norm, and let

`X=Z Sigma^(1/2) in R^(n x d)`.

The entries of `Z` are independent, centered, have variance one, and have uniformly bounded `(4+epsilon)` moments for some fixed `epsilon>0`. Consider the proportional regime `n,d -> infinity` with `n/d -> alpha` for a fixed `alpha in (0,infinity)`, and fix `lambda>0` independent of the dimensions.

For each coordinate `k`, define its masked ridge predictor by

`ahat_k = argmin_{a in R^d: a_k=0} { n^(-1)||X_{:k}-Xa||_2^2 + lambda||a||_2^2 }`,

and let `Ahat=[ahat_1,...,ahat_d]`. Put

`S=X^T X/n`, `Q=(S+lambda I_d)^(-1)`, and `Lambda=[diag(Q)]^(-1)`,

where `diag(Q)` is the diagonal matrix formed from the diagonal entries of `Q`. For `z in C^+={z in C: Im z>0}`, define

`G(z)=(Lambda^(1/2) Q Lambda^(1/2)-zI_d)^(-1)`.

Let `mtilde` be the unique positive solution of

`mtilde=(lambda+n^(-1)Tr[ Sigma(mtilde Sigma+I_d)^(-1)])^(-1)`,

and define the deterministic diagonal matrix `Lambdabar` by

`Lambdabar_{kk}=lambda/[(mtilde Sigma+I_d)^(-1)]_{kk}`.

All these quantities may depend on `(n,d)`. The Stieltjes transform convention is `s_mu(z)=integral (t-z)^(-1) mu(dt)` for a measure on the real line.

## Task

Prove that, for every `z in C^+`, the equation

`chi(z)=n^(-1)Tr{ Sigma[-lambda I_d-(1-chi(z))^(-1)Sigma+Lambdabar/z]^(-1) }`

has exactly one solution satisfying `Im chi(z)>=0` and `chi(z)!=1`, with the displayed inverse well-defined. For this solution, prove that

`Gcal(z)=[Lambdabar^(1/2)((1-chi(z))^(-1)Sigma+lambda I_d)^(-1)Lambdabar^(1/2)-zI_d]^(-1)`

is well-defined and, for every fixed `z in C^+`,

`d^(-1)Tr G(z)-d^(-1)Tr Gcal(z) -> 0`

in probability as `n,d -> infinity`.

Consequently, characterize the empirical spectral measures

`mu_{n,d}=d^(-1)sum_{j=1}^d delta_{lambda_j(Lambda^(1/2)Q Lambda^(1/2))}`

by the dimension-dependent deterministic Stieltjes transforms `s_{n,d}(z)=d^(-1)Tr Gcal(z)`. In particular, show that along any subsequence on which these deterministic transforms converge pointwise on `C^+`, their limit is the Stieltjes transform of a probability measure and `mu_{n,d}` converges weakly to that measure in probability.
