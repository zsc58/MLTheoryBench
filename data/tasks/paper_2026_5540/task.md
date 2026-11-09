# Problem

## Setup

Let `m >= 1` and `k >= 2`. For one centered neighborhood, let `X_c in R^(k x m)` and define its covariance

`Sigma = (k-1)^(-1) X_c^T X_c`.

Assume an orthogonal eigendecomposition

`Sigma = W diag(v) W^T`,

where `W in R^(m x m)`, `W^T W = WW^T = I_m`, and `v=(v_1,...,v_m)^T` (the eigenvalues may be listed in nonincreasing order). Let `w_l` denote column `l` of `W`. Define the elementwise-square matrix `Q in R^(m x m)` by `Q_{r l}=W_{r l}^2`, and define `R` to have one column `w_a \odot w_b` for every pair `1 <= a < b <= m`. Set

`H = [Q | R]`.

The local quadratic shape-operator approximation and mean-curvature score are

`S = - H H^T Sigma`,  `kappa = |tr(S)|`.

Finally define

`C = W^T Q`,

and let `1_m` be the all-ones vector in `R^m`; `C^(odot 2)` denotes the entrywise square of `C`.

## Task

Prove the exact identity

`kappa = | 1/2 v^T ( (C^(odot 2)) 1_m ) + 1/2 1_m^T v |`.

Thus the estimator can be evaluated from the eigenvalues and `C` without explicitly carrying out the direct high-order feature-matrix contraction through `H`.
