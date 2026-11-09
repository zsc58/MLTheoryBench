# Problem

## Setup

Let `n>=1` and `d>=2` be integers, set `N=n^d`, and let `r>=d-1` be an integer. Draw a random tensor-train vector `omega in R^N` as follows. For each mode `j=1,...,d`, let `G^(j)` be a Gaussian TT core, with boundary indices `alpha_0=alpha_d=1` and internal indices `alpha_1,...,alpha_{d-1} in {1,...,r}`. All entries across all cores are mutually independent standard normal random variables. For `I=(i_1,...,i_d) in {1,...,n}^d`, define

`omega_I = r^{-(d-1)/2} sum_{alpha_1,...,alpha_{d-1}=1}^r prod_{j=1}^d G^(j)_{alpha_{j-1},i_j,alpha_j}`.

Let `A in R^{N times N}` be a fixed symmetric positive semidefinite matrix with `tr(A)>0`. For independent copies `omega_1,...,omega_ell` of this probe, define

`H_ell(A) = (1/ell) sum_{t=1}^ell omega_t^T A omega_t`.

For `k` independent blocks, each formed from `ell` fresh probes, write `H_ell^(b)(A)` for block `b` and let `H_{k,ell}(A)` be their median. For odd `k`, use the central order statistic; for even `k`, use any measurable selection between the two central order statistics. Assume `0<epsilon<1` and `0<delta<1`. Take positive integers `k>=7 log(1/delta)` and `ell>=88 epsilon^(-2)`, where `log` denotes the natural logarithm.

## Task

Prove that

`P( |H_{k,ell}(A)-tr(A)| > epsilon tr(A) ) <= delta`.

Consequently, show that choosing `k=ceil(7 log(1/delta))` and `ell=ceil(88 epsilon^(-2))` gives a sufficient probe count

`k ell = O(epsilon^(-2)(1+log(1/delta)))`

uniformly for `0<epsilon,delta<1`. In particular, this is `O(epsilon^(-2)log(1/delta))` as `delta` tends to zero, uniformly in `epsilon`. The constants must be independent of `n`, `d`, `r`, and `A` whenever `r>=d-1`.
