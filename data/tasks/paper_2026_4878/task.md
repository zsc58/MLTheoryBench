# Problem

## Setup

Let `K>=2` and `T>=1` be integers, and write `[K]={1,...,K}`. A stochastic bandit instance is a tuple `nu=(P_1,...,P_K)` of probability distributions supported on `[0,1]`. Arm `j` has mean `mu_j=E_{X~P_j}[X]`. Each arm has an i.i.d. reward stream, and these streams are mutually independent. At round `t`, the learner chooses an arm `A_t` and observes only the next unused reward `R_t` from that arm's stream. Define

`Reg_T = T max_j mu_j - sum_{t=1}^T mu_{A_t}`.

Write `V` for the class of all such instances and `V_Ber` for the subclass with `P_j=Ber(mu_j)` for every arm. Expectations `E_nu` include reward randomness and the learner's randomness. A learner's decision and update maps are fixed independently of the unknown instance.

A learner has a read-only random seed `U`, sampled before interaction, independent of the instance and of its reward streams. All algorithmic randomness may be included in `U`. A learner with `W` bits of persistent memory has a finite state space `M` with `|M|<=2^W`, a fixed initial state `M_0`, and a state `M_t in M` after every round. Apart from the seed and the public current time, all information retained between rounds is encoded in this state. Computation within a round is unrestricted. State updates are measurable maps of the form

`M_t = phi_t(M_{t-1},U,A_t,R_t)`.

A `B`-batch protocol, where `1<=B<=T` is an integer, partitions the horizon into integer boundaries

`0=t_0<t_1<...<t_B=T`.

For `b<B`, an adaptive-grid learner chooses

`t_b = psi_b(t_{b-1},M_{t_{b-1}},U)`.

For every round `t` in batch `b`, its action is specified by a measurable map

`A_t = rho_{b,t}(t_{b-1},M_{t_{b-1}},U)`.

Thus the complete action sequence of a batch is committed at its start. Rewards may update the state during a batch but cannot change later actions in that batch. In a static-grid protocol, the full grid is fixed before interaction: it may depend on `U` but not on observations.

Use `log` for the natural logarithm and `log_2` for the base-2 logarithm.

## Task

Prove the following integrated theorem.

There exist universal constants `c,gamma_0,C_1,C_2,C_3>0` such that:

1. **Converse.** For every constant `C>=1`, every even integer `K>=2`, and every integer `T>=1`, any adaptive-grid `B`-batch learner with integer memory budget `W>=1` satisfying

   `sup_{nu in V_Ber} E_nu[Reg_T] <= C sqrt(KT) log T log K`

   and

   `T >= c C^6 K log^6 T log^6 K`

   must satisfy

   `B >= (gamma_0 K - (1/2)log_2(2K))/W`.

   In particular, `B=Omega(K/W)` for sufficiently large `K`.

2. **Achievability.** For every integer `K>=2`, every block size `S in {1,...,K}`, and every integer `T>=cK`, there exists a static-grid learner using at most `C_1 S log T` persistent bits and at most `C_2 (K/S)(log log T)^2` batches such that

   `sup_{nu in V} E_nu[Reg_T] <= C_3 sqrt(KT log T)(log log T)^2`.

Together these statements establish the memory-adaptivity tradeoff up to logarithmic factors.
