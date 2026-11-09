# Problem

## Setup

Let `A` be a directed graph shift on `C^N` that is diagonalizable as `A = U Lambda U^{-1}`. Order the eigenpairs so that every real eigenvalue has a real eigenvector, while every nonreal eigenvalue occurs with its conjugate: if index `bar n` is paired with `n`, then `lambda_bar n = conjugate(lambda_n)` and `u_bar n = conjugate(u_n)`. Thus, for every real vector `v`, its graph Fourier coordinates `v_hat = U^{-1}v` satisfy `v_hat_bar n = conjugate(v_hat_n)` on conjugate pairs and are real on real-eigenvalue indices.

For a finite-second-moment random vector `V` in `C^N`, write `mu_V = E[V]` and define its covariance by

`H_V = E[(V - mu_V)(V - mu_V)^H]`.

Call `V` directed graph wide-sense stationary (DGWSS) when `mu_V = 0` and

`H_V = U D_V U^H`

for some diagonal matrix `D_V` (whose diagonal entries are the directed graph power spectral values).

Construct a random diagonal matrix `R` as follows. On each real-eigenvalue index, set `R_nn` to an independent Rademacher sign. For one representative `n` of each nonreal conjugate pair, draw independent `Psi_n` uniformly on `[-pi, pi]` and set `R_nn = exp(i Psi_n)` and `R_bar n,bar n = exp(-i Psi_n)`. All signs and representative phases are mutually independent. For an observed real vector `m`, define its surrogate random vector by `Z_m = U R U^{-1} m`. For a DGWSS real random vector `X`, use an independent draw of `R` and define `Z_X = U R U^{-1} X`.

## Task

Prove the following integrated theorem.

1. If `X` is DGWSS, then `Z_X` is DGWSS and has exactly the same covariance matrix: `H_{Z_X} = H_X`.
2. For every observed real vector `m`, `Z_m` is real almost surely and is DGWSS; in fact,

`H_{Z_m} = U diag(|(U^{-1}m)_1|^2, ..., |(U^{-1}m)_N|^2) U^H`.
