# Problem

## Setup

Let `M` be a positive integer and let `A={1,...,M}` be a finite active frontier. Arm `i` has unknown true mean `mu_i`; let `mu^*=max_i mu_i`, assume the maximizer `m_opt` is unique, and define `Delta_i=mu^*-mu_i`.

Let `F_t = sigma(I_1,Y_1,...,I_t,Y_t)` with `F_0` trivial. At round `t`, the algorithm selects `I_t` measurably with respect to `F_{t-1}`, observes `Y_t`, and may stop at a finite stopping time `tau` with respect to `(F_t)`. The pulls are the rounds `1,...,tau`; define `N_i=sum_{t=1}^tau 1{I_t=i}` and `N=sum_i N_i`. Its output `hat_m` is `F_tau`-measurable.

For every selected arm and past filtration, the conditional observation mean differs from its true mean by at most `L`, where `L>=0`. More explicitly, if `xi_t=Y_t-E[Y_t | F_{t-1}, I_t]`, then the centered noise is conditionally `sigma^2`-sub-Gaussian: for every real `lambda`,

`E[exp(lambda xi_t) | F_{t-1}, I_t] <= exp(lambda^2 sigma^2/2)`.

The algorithm is uniformly `(epsilon,delta)`-PAC: in every admissible environment it outputs `hat_m` with `mu_{hat_m} >= mu^*-epsilon` with probability at least `1-delta`. The scale satisfies `sigma>=0`.

Fix `0<delta<1/4`, `epsilon>0`, and a hard instance satisfying `Delta_i>epsilon` and `Delta_i+epsilon>2L` for every `i != m_opt`.

## Task

Prove that every uniformly `(epsilon,delta)`-PAC algorithm has an admissible instance `P` for which

`E_P[N] >= 2 sigma^2 log(1/(4 delta)) sum_{i != m_opt} 1/(Delta_i+epsilon-2L)^2`.

Consequently, in the small-confidence regime `delta<=1/16` (and, more generally, asymptotically as `delta` tends to zero), the worst-case expected sample complexity is at least of order

`sum_{i != m_opt} sigma^2 log(1/delta)/(Delta_i+epsilon-2L)^2`.

For the full range `0<delta<1/4`, retain the exact factor `log(1/(4 delta))` in the displayed lower bound above.
