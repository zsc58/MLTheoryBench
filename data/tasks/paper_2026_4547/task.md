# Problem

## Setup

Let `n>=1` and `T>=1` be integers. Let `Z` be a measurable example space, let `P` be a probability distribution on `Z`, and let `F` be a measurable space of predictors. Let `ell:F x Z -> R` be a measurable loss. Draw a training set `S=(z_1,...,z_n)` iid from `P`; write `S~S'` when two datasets in `Z^n` differ in exactly one coordinate. Let `U` be shared algorithmic randomness, independent of the data, and let `h_t:Z^n x U -> F`, `t=0,...,T`, be measurable learner maps, where the second factor denotes the measurable state space of the randomness.

Let `rho:F x F -> [0,infinity)` be a measurable, finite-valued nonnegative discrepancy. For neighboring datasets define
`D_t(S,S';U)=rho(h_t(S,U),h_t(S',U))`.
Assume there is a finite constant `L>0` such that for every `h,g in F` and `z in Z`,
`|ell(h,z)-ell(g,z)| <= L rho(h,g)`.

For `t=0,...,T-1`, let `a_t(S,S';U)` and `b_t(S,S';U)` be measurable, finite-valued nonnegative coefficient functions. These coefficients may depend on the ordered dataset pair and the shared randomness. The pair of coefficient processes is a trajectory contractivity profile if, for every neighboring `S~S'` and every realization of `U`,
`D_{t+1}(S,S';U) <= a_t(S,S';U) D_t(S,S';U)+b_t(S,S';U)`.
Assume the chosen coefficients form such a profile. Assume also that the shared initialization is data-independent and that
`D_0(S,S';U)=0`
for every neighboring pair and every realization of `U`.

For a neighboring pair define
`C_T(S,S';U)=sum_{t=0}^{T-1}(prod_{k=t+1}^{T-1}a_k(S,S';U))b_t(S,S';U)`,
with empty products equal to one. Define
`C_T(S)=sup_{S'~S} E_U[C_T(S,S';U)]` and `gamma_T(S)=L C_T(S)`.
The supremum is taken in `[0,infinity]`, with the supremum of the empty set equal to zero. Assume
`E_U[C_T(S,S';U)]<infinity`
for every fixed neighboring pair. Assume that `S -> C_T(S)` is measurable and that
`E_{S~P^n}[C_T(S)]<infinity`.

For every `h in F`, assume `integral_Z |ell(h,z)| P(dz)<infinity`, and define
`R(h)=integral_Z ell(h,z) P(dz)` and
`Rhat_S(h)=n^{-1}sum_{i=1}^n ell(h,z_i)`.
Assume the terminal test and training losses satisfy the explicit integrability conditions
`E_{S,U}[integral_Z |ell(h_T(S,U),z)| P(dz)]<infinity`
and, for each `i=1,...,n`,
`E_{S,U}[|ell(h_T(S,U),z_i)|]<infinity`.

## Task

Prove the following integrated theorem: under the assumptions above, for every dataset `S` and every neighbor `S'~S`,
`sup_{z in Z} |E_U[ell(h_T(S,U),z)-ell(h_T(S',U),z)]| <= gamma_T(S)`,
and the randomized learner satisfies
`E_{S,U}[R(h_T(S,U))-Rhat_S(h_T(S,U))] <= E_S[gamma_T(S)]`.
This must hold for every integer horizon `T>=1` and sample size `n>=1`.
