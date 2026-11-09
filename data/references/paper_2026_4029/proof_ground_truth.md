# Reference Proof

## Proof Structure

1. Sum the recursion to obtain an exact identity relating the empirical miss rate to the terminal and initial adaptive levels.
2. Prove by induction that every untruncated iterate remains in `[-lambda, 1+lambda]`, using the whole-space and empty-set conventions outside `[0,1]`.
3. Bound the endpoint difference in the identity and conclude the deterministic `O(1/T)` guarantee.

## Complete Proof

Write `a_t` for the adaptive level and `M_t` for the miss indicator. From
`a_{t+1}-a_t = lambda(q-M_t)`, summing from `t=1` to `T` gives

`a_{T+1}-a_1 = lambda(T q - sum_{t=1}^T M_t)`.

Rearranging and dividing by `T` yields the exact identity

`(1/T) sum_{t=1}^T M_t = q + (a_1-a_{T+1})/(lambda T)`.

It remains to bound the iterates. We prove inductively that `a_t in [-lambda,1+lambda]` for all `t`. This holds at `t=1` because `a_1 in [0,1]`. Suppose it holds at time `t`.

If `a_t <= 0`, the whole-space convention gives `M_t=0`, so
`a_{t+1}=a_t+lambda q`. Since `a_t >= -lambda` and `q in [0,1]`, this lies in `[-lambda,lambda]`, hence in `[-lambda,1+lambda]` (using `lambda <= 1`).

If `0 <= a_t <= 1`, then `M_t in {0,1}`. Consequently
`a_{t+1}=a_t+lambda(q-M_t)` lies between `a_t-lambda` and `a_t+lambda`, and therefore in `[-lambda,1+lambda]`.

If `a_t >= 1`, the empty-set convention gives `M_t=1`, so
`a_{t+1}=a_t+lambda(q-1)`. Here `a_t in [1,1+lambda]` and `q in [0,1]`, hence `a_{t+1} in [1-lambda,1+lambda]`, again contained in `[-lambda,1+lambda]`. The induction is complete.

In particular, `a_{T+1} in [-lambda,1+lambda]` while `a_1 in [0,1]`, so
`|a_1-a_{T+1}| <= 1+lambda`. Applying this to the exact identity gives

`|(1/T) sum_{t=1}^T M_t - q| <= (1+lambda)/(lambda T)`.

The argument is deterministic and uses no independence, stationarity, or other distributional property of the data sequence.
