# Reference Proof

## Proof Structure

The proof first converts the learner's pathwise regret bound into a comparison between its log wealth and the log wealth of the fixed witness `u_*`. It then lower-bounds every comparator log increment by its predictable quadratic edge plus a martingale difference. The uniform edge assumption supplies linear cumulative drift, while a conditional Hoeffding argument controls the martingale fluctuation. Finally, the resulting exponential tail bound yields almost-sure crossing and the expected stopping-time bound.

## Complete Proof

Fix a witness `u_*` satisfying the uniform edge condition and write

`lambda_t = <u_*, x_t>`, `mu_t = E_Q[e_t | G_{t-1}]`, and `a_t = lambda_t mu_t - lambda_t^2`.

Because `u_*` is in `C` and `||x_t||_2 <= R`, we have `|lambda_t| <= 1/2`. Also `|e_t| <= 1` and hence `|mu_t| <= 1`.

By the definition of regret,

`log W_T = -sum_{t=1}^T ell_t(u_t) = -sum_{t=1}^T ell_t(u_*) - Reg_T(u_*)`.

Thus the pathwise regret bound gives

`log W_T >= sum_{t=1}^T log(1 + lambda_t e_t) - r_T`.  (1)

For `|z| <= 1/2`, the elementary inequality `log(1+z) >= z-z^2` holds. Applying it with `z=lambda_t e_t` and using `e_t^2 <= 1` yields

`log(1 + lambda_t e_t) >= lambda_t e_t - lambda_t^2`

`= lambda_t(e_t-mu_t) + lambda_t mu_t-lambda_t^2`

`= lambda_t(e_t-mu_t) + a_t`.

Define

`S_T = sum_{t=1}^T lambda_t(e_t-mu_t)` and `A_T = sum_{t=1}^T a_t`.

Since `lambda_t` and `mu_t` are `G_{t-1}`-measurable and `E_Q[e_t-mu_t | G_{t-1}]=0`, the increments of `S_T` form a martingale-difference sequence. Combining the preceding inequality with (1) gives the key pathwise reduction

`log W_T >= S_T + A_T-r_T`.  (2)

We next lower-bound `A_T`. For `t<t_0`,

`a_t >= -|lambda_t||mu_t|-lambda_t^2 >= -1`.

For `t>=t_0`, the witness assumption gives `a_t>=kappa`. Therefore, for every `T>=t_0`,

`A_T >= -(t_0-1) + kappa(T-t_0+1)`

`= kappa T-(1+kappa)(t_0-1)`

`>= kappa T-2(t_0-1)`,  (3)

where the last inequality uses `kappa<=1`.

For completeness, we establish the required martingale tail bound. Conditionally on `G_{t-1}`, the random variable `e_t` is supported in the two-point set `{-alpha,1-alpha}`. Consequently, the conditional support interval of `lambda_t(e_t-mu_t)` has length at most `|lambda_t|<=1`, irrespective of the sign of `lambda_t`. Conditional Hoeffding's lemma therefore gives, for every `eta>0`,

`E_Q[exp(-eta lambda_t(e_t-mu_t)) | G_{t-1}] <= exp(eta^2/8)`.

Iterating conditional expectations shows

`E_Q[exp(-eta S_T)] <= exp(eta^2 T/8)`.

Markov's inequality then gives, for `s>0`,

`Q(S_T <= -s) <= exp(-eta s + eta^2 T/8)`.

Optimizing at `eta=4s/T` yields

`Q(S_T <= -s) <= exp(-2s^2/T)`.  (4)

Let `N=N_gamma(r)` and fix `T>=N`. If `sigma_gamma>T`, then in particular `W_T<1/gamma`. From (2) and (3), this implies

`S_T < log(1/gamma)+r_T-kappa T+2(t_0-1)`

`= -[kappa T-2(t_0-1)-r_T-log(1/gamma)]`.

By the definition of `N`, the expression in square brackets is at least `kappa T/2`. Applying (4) with `s=kappa T/2` gives

`Q(sigma_gamma>T) <= Q(S_T < -kappa T/2) <= exp(-kappa^2 T/2)`.

This proves the finite-time bound.

Because the right-hand side tends to zero and `{sigma_gamma=infinity}` is contained in `{sigma_gamma>T}` for every `T`, continuity of probability gives

`Q(sigma_gamma<infinity)=1`.

Finally, the tail-sum identity and the finite-time bound imply

`E_Q[sigma_gamma] = sum_{T=0}^infinity Q(sigma_gamma>T)`

`<= N + sum_{T=N}^infinity exp(-kappa^2 T/2)`

`<= N + 1/[1-exp(-kappa^2/2)]`.

For `0<kappa<=1`, `1-exp(-kappa^2/2) >= kappa^2/4`. Hence

`E_Q[sigma_gamma] <= N_gamma(r)+4/kappa^2`,

as required.
