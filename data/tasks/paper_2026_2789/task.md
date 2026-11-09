# Problem

## Setup

For each positive integer `n`, let `v_1,...,v_n` be real values and let costs satisfy `0<w_min<=w_i<=w_max` for fixed constants `w_min,w_max`; also assume `|v_i|<=V_max` for a fixed finite `V_max`. Fix `C>0` and `0<rho<1`, set `W_n=nC` and `K_n=ceil(n rho)`, and assume the constraints below are feasible.

Define
`P_n^01 = max { sum_i v_i z_i : z_i in {0,1}, sum_i w_i z_i <= W_n, sum_i z_i >= K_n }`
and the linear relaxation
`P_n^LP = max { sum_i v_i x_i : 0<=x_i<=1, sum_i w_i x_i <= W_n, sum_i x_i >= K_n }`.

For multipliers `lambda_n,nu_n>=0`, put `s_{n,i}=v_i-lambda_n w_i+nu_n` and define the binary threshold allocation `g_{n,i}=1` when `s_{n,i}>=0` and `g_{n,i}=0` otherwise. Assume this allocation satisfies both constraints. If the pairs for a given `n` are modeled as random with a common marginal law `Q_n` for a value-cost pair `(V,W)`, assume `Q_n{(v,w):v-lambda w+nu=0}=0` for every dual-optimal multiplier pair `(lambda,nu)` of `P_n^LP`.

## Task

Prove the integrated theorem that, for every `n`,
`0 <= P_n^LP-P_n^01 <= 2V_max`,
so that
`0 <= P_n^LP/n-P_n^01/n <= 2V_max/n -> 0`.
Moreover, if a sequence `r_n` satisfies `r_n/n -> 0` and the feasible threshold allocations satisfy
`sum_i v_i g_{n,i} >= P_n^LP-r_n`, prove
`0 <= P_n^01/n - (1/n)sum_i v_i g_{n,i} -> 0`.
