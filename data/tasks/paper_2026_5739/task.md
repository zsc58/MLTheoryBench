# Problem

## Setup

Fix an integer `K >= 2`. Let

`Delta^(K-1) = {q in R^K : q_i >= 0 for all i, sum_i q_i = 1}`

and let `Delta^(K-1,o)` denote its interior, where every coordinate is strictly positive. Define the barycenter

`u = (1/K, ..., 1/K)`.

For `q in Delta^(K-1,o)`, define

`g(q) = (product_{i=1}^K q_i)^(1/K)`

and the centered log-ratio map

`[Psi(q)]_i = log(q_i / g(q)),   i = 1, ..., K`.

For `lambda in [0,1)`, define the shrinkage map

`S_lambda(p) = (1-lambda)p + lambda u = u + (1-lambda)(p-u)`.

In the statement below, `O((1-lambda)^2)` is componentwise as `lambda` approaches `1` from below; equivalently, each coordinate is bounded in absolute value by a constant times `(1-lambda)^2` for all sufficiently large `lambda`.

## Task

Prove that for every fixed `p in Delta^(K-1,o)`,

`Psi(S_lambda(p)) = K(1-lambda)(p-u) + O((1-lambda)^2)`

as `lambda` approaches `1` from below.
