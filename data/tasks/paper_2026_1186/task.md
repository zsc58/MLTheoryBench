# Problem

## Setup

Let `(X,dx)` be a measurable space with reference measure `dx`, and let `k` be a positive integer. Let `p_1,...,p_k:X->(0,infinity)` be measurable probability density functions, each integrating to one. Their values are finite and strictly positive at every point. For an order `r` in `R union {-infinity,+infinity}`, define the pointwise generalized mean by

- `M_{k,r}(x)=(k^{-1}sum_{i=1}^k p_i(x)^r)^{1/r}` for finite `r!=0`;
- `M_{k,0}(x)=(prod_{i=1}^k p_i(x))^{1/k}`;
- `M_{k,-infinity}(x)=min_i p_i(x)` and `M_{k,+infinity}(x)=max_i p_i(x)`.

Set `Z_{k,r}=integral_X M_{k,r}(x) dx` and, whenever `0<Z_{k,r}<infinity`, define the normalized aggregate density `p^circ_{k,r}(x)=M_{k,r}(x)/Z_{k,r}`.

## Task

Prove the following integrated characterization.

1. For every positive integer `k`, every collection of density functions satisfying the setup, every `x in X`, and every `r in [0,1]`, the normalizer is positive and finite (indeed `0<Z_{k,r}<=1`) and
`log p^circ_{k,r}(x) >= k^{-1}sum_{i=1}^k log p_i(x)`.

2. For every order `r` outside `[0,1]` (including `r=-infinity` and `r=+infinity`), there exist two distinct probability density functions satisfying the setup on a common reference-measure space and a point `x` at which the normalized aggregate is defined and
`log p^circ_{2,r}(x) < (1/2)(log p_1(x)+log p_2(x))`.
