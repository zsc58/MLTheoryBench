# Problem

## Setup

Let `M` be a nonnegative integer and let `n_val` be a positive integer. Let

`F = {f_hat_0, f_hat_1, ..., f_hat_M}`

be a finite collection of predictors for a target distribution on pairs `(X,Y)`. The predictor `f_hat_0` is a target-only predictor; the other predictors may be obtained from source data and a calibration fold.

The source data, when present, satisfy the standing source condition: source covariates `x_i^(src)` are independent draws from a continuous density supported on `[0,1]^p` and bounded below by a positive constant, and source responses have the form `y_i^(src)=f^(src)(x_i^(src))+epsilon_i^(src)`, where the errors are independent, mean-zero, sub-Gaussian, and have uniformly bounded second moments. This inherited source condition is part of the ambient contract, although the validation comparison below uses only the conditional validation-sampling consequences.

Target data are randomly split into disjoint calibration and validation folds. Conditional on the source data and calibration fold, the validation observations

`(X_1,Y_1), ..., (X_{n_val},Y_{n_val})`

are independent draws from the target population and are independent of the fixed predictors in `F`.

For a fixed predictor `f`, define its target risk by

`R(f) = E_{(X,Y)~P_tar}[(Y-f(X))^2]`.

When a predictor is random before conditioning, this denotes the corresponding conditional target risk after the predictor has been fixed by conditioning on the non-validation data.

Define the validation risk

`R_hat_val(f) = (1/n_val) sum_{i=1}^{n_val} (Y_i - f(X_i))^2`.

Assume there is a finite nonnegative constant `B_n`, fixed before the validation draw conditional on the source and calibration data, such that for every `k=0,...,M`,

`(Y - f_hat_k(X))^2 <= B_n`

conditional almost surely for an independent target-population draw `(X,Y)`. Equivalently, every validation loss is conditionally almost surely in `[0,B_n]`.

Let `f_hat_sel` be any predictor in `F` minimizing `R_hat_val` (ties arbitrary), and let `delta in (0,1)`.

## Task

Prove that, with probability at least `1-delta` (conditional on the source and calibration data, and hence also unconditionally),

`R(f_hat_sel) <= min_{0<=k<=M} R(f_hat_k) + 2 B_n sqrt(log(2(M+1)/delta)/(2 n_val)).`

In particular, prove the no-negative-transfer guarantee

`R(f_hat_sel) <= R(f_hat_0) + 2 B_n sqrt(log(2(M+1)/delta)/(2 n_val)).`
