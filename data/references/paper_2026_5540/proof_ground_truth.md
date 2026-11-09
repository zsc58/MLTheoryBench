# Reference Proof

## Proof Structure

1. Expand the two blocks of the feature matrix and collapse the pairwise Hadamard-product Gram matrix using the pairwise-sum identity and orthogonality of `W`.
2. Insert the resulting identity into the trace estimator.
3. Use cyclicity and the spectral decomposition of `Sigma` to express the remaining contraction through `C` and its entrywise-square row sums.

## Complete Proof

Write `Q = W^(2)` and `R = W^(times)`, so that `H = [Q | R]`. Hence

`HH^T = QQ^T + RR^T`.

For rows `r,t`, set `x_l = W_{rl}W_{tl}`. Since the columns of `R` are `w_a \odot w_b` for `a<b`,

`(RR^T)_{rt} = sum_{a<b} x_a x_b`.

The elementary identity

`2 sum_{a<b} x_a x_b = (sum_l x_l)^2 - sum_l x_l^2`

therefore gives

`(RR^T)_{rt} = 1/2 ((WW^T)_{rt})^2 - 1/2 (QQ^T)_{rt}`.

Because `W` is orthogonal, `WW^T = I_m`, and the entrywise square of `I_m` is again `I_m`. Thus

`RR^T = 1/2 I_m - 1/2 QQ^T`,

so

`HH^T = 1/2 QQ^T + 1/2 I_m`.                                             (1)

By definition, `S = -HH^T Sigma` and `kappa = |tr(S)|`; the minus sign disappears under the absolute value. Using (1), linearity of trace, and cyclicity,

`kappa = | 1/2 tr(QQ^T Sigma) + 1/2 tr(Sigma) |`

`= | 1/2 tr(Q^T Sigma Q) + 1/2 tr(Sigma) |`.

Now `Sigma = W diag(v) W^T`, so `tr(Sigma) = sum_s v_s`. With `C = W^T Q`,

`Q^T Sigma Q = Q^T W diag(v) W^T Q = C^T diag(v) C`.

Therefore

`tr(Q^T Sigma Q) = tr(C^T diag(v) C)`

`= sum_s v_s sum_l C_{sl}^2`

`= v^T ( (C^(odot 2)) 1_m )`.

Substitution yields

`kappa = | 1/2 v^T ( (C^(odot 2)) 1_m ) + 1/2 1_m^T v |`.

This is exactly the desired closed form. It evaluates the estimator from `v` and `C`, eliminating the direct feature-matrix contraction through all columns of `H`.
