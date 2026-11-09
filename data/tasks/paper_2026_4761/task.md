# Problem

## Setup

Let `n>=1` be an integer and let `k` be an integer with `1<=k<=n`. Define the `(n,k)` hypersimplex
`Delta_k^n={u in [0,1]^n : sum_{i=1}^n u_i=k}`.
For `tau>0` and `x in R^n`, define the temperature-scaled projection
`S_tau(x)=argmin_{u in Delta_k^n} {tau ||u||_2^2-2<x,u>}`.

## Task

Prove the following integrated theorem. If
`x_1/tau >= x_2/tau >= ... >= x_n/tau`,
then the unique vector `y=S_tau(x)` satisfies
`y_1>=y_2>=...>=y_n`.
Moreover, with
`C_k={u in [0,1]^n : u_1>=u_2>=...>=u_n, sum_{i=1}^n u_i=k}`,
`y` is the unique minimizer of
`min_{u in C_k} ||u-x/tau||_2^2`,
and this minimizer can be computed using the pool-adjacent-violators (PAV) algorithm, with the displayed box and prescribed-sum constraints enforced, in `O(n log n)` time.
