# Problem

## Setup

Let `q in [0,1]` be a target miscoverage level and let `lambda in (0,1]`. Consider any deterministic sequence of covariate-outcome pairs `(X_t,Y_t)`, with `Y_t` in an outcome space `Y`. For each time `t` and level `a in R`, let `C_t(a;X_t)` be a prediction set satisfying the conventions

- `C_t(a;X_t) = Y` when `a <= 0`, and
- `C_t(a;X_t) = emptyset` when `a >= 1`.

For `0 < a < 1`, no probabilistic or structural assumption is imposed. Define
`M_t = 1{Y_t notin C_t(a_t;X_t)}` and initialize `a_1 in [0,1]`. Generate the untruncated adaptive sequence by

`a_{t+1} = a_t + lambda (q - M_t)`, for `t >= 1`.

## Task

Prove that for every integer `T >= 1`, the iterates satisfy `a_t in [-lambda,1+lambda]` for all `t`, and the empirical miss rate obeys

`(1/T) sum_{t=1}^T M_t = q + (a_1-a_{T+1})/(lambda T)`

and consequently

`|(1/T) sum_{t=1}^T M_t - q| <= (1+lambda)/(lambda T)`.

The guarantee must hold for every data sequence, without independence, stationarity, or any other distributional assumption.
