# Problem

## Setup

Fix integers `K>=1` and `H>=1`. For each `n`, let

`(U_i,X_i,Y_i(0),Y_i(1)), i=1,...,n`

be iid draws from one population distribution that does not change with `n`, where `U_i in [0,H]` is a continuous arrival time, `X_i` is a covariate, and `Y_i(0),Y_i(1)` are real-valued potential outcomes. Independently across units and independently of all other variables conditional on the covariates, assign unit `i` to a priority queue `G_i in {1,...,K}` with

`P(G_i=k | X_i=x)=rho_k(x)`,

where `rho` is a measurable vector of queue-assignment probabilities. Queue `1` has highest priority.

For each `n`, let `B_{1,n},...,B_{H,n}` be deterministic nonnegative integer service budgets. At the allocation at the end of period `t`, the eligible waiting units are exactly those with `U_i<=t` that have not previously been served. Service is work-conserving: exactly the smaller of `B_{t,n}` and the number of eligible waiting units is served. Higher-priority queues are exhausted before lower-priority queues receive service, and service within each queue is first-in-first-out. Let `D_i` indicate that unit `i` has been served by period `H`, and observe `Y_i=Y_i(D_i)`.

Assume:

1. `U independent of X` and `U independent of (Y(0),Y(1)) given X`. Arrival ties have probability zero.
2. With `p_k=E[rho_k(X)]`, the vector `p` is fixed as `n` varies. The numbers `K,H`, the functions `rho_k`, and the distribution of `U` are also fixed.
3. For some `beta in (0,1)`,

   `max_{1<=t<=H} | n^{-1} sum_{s=1}^t B_{s,n} - beta P(U<=t) | -> 0`.
4. Writing `e_n(x)=P(D_i=1 | X_i=x)`, there are `gamma>0` and `n_0` such that

   `gamma <= e_n(X) <= 1-gamma` almost surely for every `n>=n_0`.
5. `E[Y(0)^2+Y(1)^2]<infinity`.

Write `v_+=max(v,0)`. Define `c_0=0`, `c_k=sum_{j=1}^k p_j`, and

`a_k = {[(beta-c_{k-1})_+-(beta-c_k)_+]/p_k, if p_k>0; 0, if p_k=0}`.

Set

`e_infty(x)=sum_{k=1}^K a_k rho_k(x)`.

Let

`mu_z(x)=E[Y(z)|X=x]`, `sigma_z^2(x)=Var(Y(z)|X=x)`, and `tau=E[Y(1)-Y(0)]`.

Let `P_X` denote the marginal covariate distribution, with `||f||_{L2(P_X)}^2=integral |f(x)|^2 dP_X(x)`. Using an auxiliary training sample `T`, independent of all experimental variables above, construct jointly measurable, `T`-measurable fitted regressions `hat mu_0,hat mu_1` taking values in `L2(P_X)` almost surely and satisfying

`||hat mu_z-mu_z||_{L2(P_X)}=o_P(1)`, for `z=0,1`.

The training sample and fitted regressions may depend on `n`; their indices are suppressed.

For `n>=n_0`, consider the doubly robust estimator

`hat tau_n = n^{-1} sum_{i=1}^n [hat mu_1(X_i)-hat mu_0(X_i) + D_i{Y_i-hat mu_1(X_i)}/e_n(X_i) -(1-D_i){Y_i-hat mu_0(X_i)}/{1-e_n(X_i)}]`.

## Task

Prove that

`n Var(hat tau_n | T) ->_P E[sigma_1^2(X)/e_infty(X)+sigma_0^2(X)/(1-e_infty(X))] + Var(mu_1(X)-mu_0(X))`.

Here the conditional variance is taken over experimental sampling and queue randomization with the training sample held fixed, and convergence in probability is with respect to the training sample.

Thus, although the queue produces dependent treatment assignments, the leading variance equals the usual iid semiparametric efficiency bound for the average treatment effect with propensity `e_infty`.
