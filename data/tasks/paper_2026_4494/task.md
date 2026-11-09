# Problem

## Setup

Let `m, K, C` be positive integers. For class indices `c in {1,...,C}`, component indices `k in {1,...,K}`, and feature indices `j in {1,...,m}`, fix real coefficients `alpha_{c,k}` and real exponents `beta_{c,k,j}`. For `x in R_{>0}^m`, define component scores
`z_{c,k}(x) = alpha_{c,k} product_{j=1}^m x_j^{beta_{c,k,j}}`
and class scores `z_c(x) = sum_{k=1}^K z_{c,k}(x)`. Define softmax probabilities
`p_c(x) = exp(z_c(x)) / sum_{r=1}^C exp(z_r(x))`.

For every `x in R_{>0}^m`, define
`G_{c,j}(x) = partial z_c(x) / partial log x_j`.
On the subset where `z_c(x)>0`, define
`E_{c,j}(x) = partial log z_c(x) / partial log x_j`.
Derivatives with respect to `log x_j` hold all other input coordinates fixed. For class indices c and c', let `M_{c,c'}(x) = z_c(x)-z_{c'}(x)`. Let `b in R_{>0}^m` be a fixed baseline. Logarithms of components or scores are used only when their arguments are positive.

In the local expansions below, `||delta||` denotes the Euclidean norm. Each O-term is for fixed dimensions, coefficients, exponents, indices, and expansion point; its constant may depend on those fixed quantities.

## Task

Prove the following statements on their specified domains.

1. For every positive input x,
`G_{c,j}(x) = sum_k beta_{c,k,j} z_{c,k}(x)`.
When `z_c(x)>0`, also prove
`E_{c,j}(x) = sum_k (z_{c,k}(x)/z_c(x)) beta_{c,k,j}`
and `G_{c,j}(x) = z_c(x) E_{c,j}(x)`.

2. If only coordinate j is replaced by `q x_j`, with `q>0`, and the resulting input is x', then
`z_c(x') = sum_k q^{beta_{c,k,j}} z_{c,k}(x)`.
In particular, for `q=1+epsilon`, prove
`z_c(x') = z_c(x) + epsilon G_{c,j}(x) + O(epsilon^2)`
as `epsilon -> 0`.

3. For every positive input x, the margin and probability sensitivities are
`partial M_{c,c'}(x)/partial log x_j = G_{c,j}(x)-G_{c',j}(x)`
and
`partial p_c(x)/partial log x_j = p_c(x)[G_{c,j}(x)-sum_r p_r(x)G_{r,j}(x)]`.
When `z_c(x)>0` and `z_{c'}(x)>0`, also prove
`partial M_{c,c'}(x)/partial log x_j = z_c(x)E_{c,j}(x)-z_{c'}(x)E_{c',j}(x)`.

4. For each component positive at x and b, prove
`log z_{c,k}(x) = log z_{c,k}(b) + sum_j beta_{c,k,j} log(x_j/b_j)`.
If `K=1` and the whole score is positive at x and b, the same identity holds with z_c in place of z_{c,1}.

With `delta_j=log(x_j/b_j)`, prove that, for every positive-coordinate baseline b,
`z_c(x) = z_c(b) + sum_j G_{c,j}(b) delta_j + O(||delta||^2)`
and
`p_c(x) = p_c(b) + sum_j p_c(b)[G_{c,j}(b)-sum_r p_r(b)G_{r,j}(b)] delta_j + O(||delta||^2)`
as `delta -> 0`.
If additionally `z_c(b)>0`, prove
`log z_c(x) = log z_c(b) + sum_j E_{c,j}(b) delta_j + O(||delta||^2)`
as `delta -> 0` with `z_c(x)>0`.
