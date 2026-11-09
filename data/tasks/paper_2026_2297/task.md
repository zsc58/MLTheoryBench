# Problem

## Setup

Let K>=2 and T>=K be integers, let sigma>=0, and let V_T>=0 be a budget. There are K arms with unknown deterministic mean functions mu_i(t), for i in [K]={1,...,K} and t=1,...,T. Each function is non-increasing in calendar time and satisfies

\[
-V_T\leq\mu_i(t)\leq0,
\qquad
\sum_{t=1}^{T-1}\max_{i\in[K]}|\mu_i(t+1)-\mu_i(t)|\leq V_T.
\]

At time t, a policy chooses I_t using only its past selected arms and observations, and possibly independent internal randomization. It then observes

\[
Y_t=\mu_{I_t}(t)+\varepsilon_t.
\]

Conditional on the information available just after choosing I_t and before observing Y_t, the noise has mean zero and satisfies, for every real lambda,

\[
\mathbb E[\exp(\lambda\varepsilon_t)\mid\text{that information}]
\leq\exp(\sigma^2\lambda^2/2).
\]

The learner does not observe rewards of unselected arms. Define the expected regret by

\[
J_T(\pi)=\mathbb E_\pi\!\left[\sum_{t=1}^T\mu_{I_t}(t)\right],
\qquad
J_T^*=\max_{(i_1,\ldots,i_T)\in[K]^T}\sum_{t=1}^T\mu_{i_t}(t),
\qquad
R_T(\pi)=J_T^*-J_T(\pi).
\]

## Algorithms

Both algorithms below know K and sigma, use a fixed tuning parameter alpha, and first pull arm i at round i for i=1,...,K. Write

\[
N_i(t)=\sum_{s=1}^t\mathbf1\{I_s=i\},
\qquad
c(h,\delta)=\sqrt{\frac{2\sigma^2\log(2/\delta)}{h}},
\qquad
\delta_t=2t^{-\alpha}.
\]

For 1<=h<=N_i(t-1), let hat_mu_{i,h}(t) be the empirical average of arm i's last h observations strictly before round t.

**RAW-UCB.** For t>K, use

\[
I_i(t)=\min_{1\leq h\leq N_i(t-1)}
\{\widehat\mu_{i,h}(t)+c(h,\delta_t)\},
\]

and select an arm with maximal index. Use alpha>=4.

**Geometric-window implementation.** Use levels h_j=2^j for integers j>=0. For each arm, refresh level zero after every pull of that arm. For j>=1, first initialize level j at the arm's h_j-th pull and subsequently refresh it at pull counts

\[
r=h_j+\ell h_j/2,\qquad \ell=0,1,2,\ldots.
\]

At each initialization or refresh, store the average of the h_j observations ending at that pull. Retain the stored average until its next refresh. At decision time t, denote this stored average by hat_mu^{geom}_{i,j}(t); only levels with h_j<=N_i(t-1) are initialized and eligible. Use the index

\[
I_i^{\mathrm{geom}}(t)=
\min_{j:\,2^j\leq N_i(t-1)}
\{\widehat\mu^{\mathrm{geom}}_{i,j}(t)+c(2^j,\delta_t)\},
\]

and select an arm with maximal index. Use alpha>=3. In both algorithms, ties may be resolved by any fixed rule, and confidence radii are evaluated at the current round t.

## Task

Prove the following integrated theorem.

1. For every K,T,sigma,V_T satisfying the setup and

\[
V_T\geq\sigma\sqrt{K/(8T)},
\]

and for every policy, there exists an instance satisfying the setup, with variation at most V_T, such that

\[
R_T(\pi)\geq\frac{1}{16\sqrt2}
(\sigma^2V_TKT^2)^{1/3}.
\]

2. RAW-UCB and the specified geometric-window implementation, without knowing T or V_T, satisfy

\[
R_T(\pi)=\widetilde O_\alpha\!\left(
(\sigma^2V_TKT^2)^{1/3}+\sigma\sqrt{KT}+KV_T
\right).
\]

Here the notation suppresses logarithmic factors in T and constants depending only on the fixed tuning parameter alpha and on which of the two algorithms is used, not on K,T,sigma,V_T or the instance.
