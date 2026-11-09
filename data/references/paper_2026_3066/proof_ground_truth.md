# Reference Proof

Condition on the source data and the calibration fold. The source standing condition is part of the ambient contract, although the validation comparison below only uses the conditional independence and bounded-loss consequences. Let the resulting sigma-field be the non-validation information. Conditional on it, every predictor in F is fixed and the validation observations are independent target-population draws.

For k=0,...,M and i=1,...,n_val, define

`ell_{k,i} = (Y_i - f_hat_k(X_i))^2`.

For each k, the variables `ell_{k,i}` are conditionally independent and have conditional mean

`R(f_hat_k) = E_{(X,Y)~P_tar}[(Y-f_hat_k(X))^2]`.

By the corrected bounded-loss assumption, `0 <= ell_{k,i} <= B_n` conditional almost surely, where `B_n` is fixed before the validation draw. Set

`a = B_n sqrt(log(2(M+1)/delta)/(2 n_val))`.

Conditional Hoeffding and a union bound give

`P(max_{0<=k<=M}|R_hat_val(f_hat_k)-R(f_hat_k)| > a | source, calibration) <= delta`.

On the simultaneous event, let `k_sel` be the index selected by validation minimization and let `k_opt` minimize the finite set of true risks. Then

`R(f_hat_sel) <= R_hat_val(f_hat_sel)+a`

`<= R_hat_val(f_hat_{k_opt})+a`

`<= R(f_hat_{k_opt})+2a`

`= min_{0<=k<=M} R(f_hat_k)+2a`.

Because `f_hat_0` belongs to the candidate set, the finite-set minimum is at most `R(f_hat_0)`, yielding the no-negative-transfer inequality. The conditional probability bound holds for the fixed non-validation realization, and integrating over that realization gives the same unconditional probability bound.
