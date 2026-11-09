# Problem

## Setup

Let `d_q,d_a,M,s,T` be positive integers with `d_q>=2`, and let `0<=epsilon<1`. Write `||.||_2` for the Euclidean norm on vectors and the operator norm on matrices, `||.||_*` for the nuclear norm, and `<X,Y>_F=Tr(X^T Y)` for the Frobenius inner product.

Let the action set `A` be a nonempty finite subset of `R^{d_a}`, with `||a||_2<=1` for every `a in A`. Admissible queries form `Q={q in R^{d_q}: ||q||_2<=1}`. Before the interaction, the environment fixes a matrix `Psi^* in R^{d_a x d_q}` and functions `nu:Q x A -> R`, with

`||Psi^*||_2<=1`, `|nu(q,a)|<=epsilon`,

and reward

`r(q,a)=<Psi^*,a q^T>_F+nu(q,a)`.

There are `M` experts. Before the interaction, the environment also fixes matrices `Psi_m in R^{d_a x d_q}` and functions `mu_m:Q x A -> R`. Expert `m` has recommendation law

`xi_m(a|q)=exp(<Psi_m,a q^T>_F+mu_m(q,a))/sum_{b in A}exp(<Psi_m,b q^T>_F+mu_m(q,b))`,

where

`rank(Psi_m)<=s`, `||Psi_m||_2<=sqrt(epsilon)`, and `|mu_m(q,a)|<=epsilon`.

The functions `nu` and `mu_m` are Borel measurable in `q` for each action. Their values, the environment matrices, and the experts' recommendation distributions are not supplied to the learner. The learner is supplied with `d_q,d_a,A,M,T,s`.

In round `t`, the environment selects a query `q_t in Q` before the current expert and action draws. Its choice may depend measurably on the previous interaction and may use its own randomization, but not on the current expert or action draws. The learner observes `q_t`, samples an expert `m_t` from its routing distribution, and receives one item `a_t` sampled conditionally according to `xi_{m_t}(.|q_t)`. It observes that item and the reward

`r_t=r(q_t,a_t)+eta_t`,

but does not observe any expert's full recommendation distribution or any unselected expert's recommendation. If `H_t` denotes the interaction history through round `t-1` augmented by `q_t`, the noise satisfies, for every real `u`,

`E[eta_t|H_t,m_t,a_t]=0`,

`E[exp(u eta_t)|H_t,m_t,a_t]<=exp(u^2/2)`.

For symmetric matrices `W_1,...,W_M in R^{d_q x d_q}`, collect them into `W=diag(W_1,...,W_M)` and define

`pi_W(m|q)=exp(q^T W_m q)/sum_{j=1}^M exp(q^T W_j q)`.

On the query sequence produced in the learner's actual interaction, let

`L_t(W)=-E_{m~pi_W(.|q_t)}E_{a~xi_m(.|q_t)}[r(q_t,a)]`.

For `tau>0`, define

`B_*^M(tau)={diag(W_1,...,W_M): W_m=W_m^T, ||W_m||_*<=tau for all m}`.

For an online sequence of parameters `W_t`, define its expected linearized policy regret by

`Reg_T(tau)=sup_{U in B_*^M(tau)} E[sum_{t=1}^T <grad L_t(W_t),W_t-U>_F]`.

Here each comparator `U` is a fixed matrix, not a function of the random trajectory. The expectation is over the interaction randomness, including routing, item sampling, observation noise, and any randomized query selection. Comparators are evaluated on the learner's actual query sequence, not on a separate interaction.

For `beta>0`, define

`Phi_beta(W)=sum_{lambda in eigenvalues(W)}[lambda asinh(lambda/beta)-sqrt(lambda^2+beta^2)]`,

where eigenvalues are counted with multiplicity. Its Bregman divergence is

`D_Phi(X||Y)=Phi_beta(X)-Phi_beta(Y)-<grad Phi_beta(Y),X-Y>_F`.

Consider the following online routing algorithm, with parameters `tau,beta,eta>0`. It starts from the all-zero block matrix `W_1=0`. At round `t`, it samples `m_t` from `pi_{W_t}(.|q_t)` and obtains `a_t,r_t` as described above. It forms

`hat G_{t,m}=-r_t(1[m_t=m]-pi_{W_t}(m|q_t))q_t q_t^T`,

`hat G_t=diag(hat G_{t,1},...,hat G_{t,M})`,

and updates by

`W_{t+1}=argmin_{W in B_*^M(tau)} {eta<hat G_t,W>_F+D_Phi(W||W_t)}`.

The blocks of the iterate `W_t` are denoted by `W_{t,m}`.

## Task

Prove the following integrated theorem.

1. **Structural claim.** There exist a function `C:Q -> R`, fixed symmetric matrices `W_m^* in R^{d_q x d_q}`, and functions `delta_m:Q -> R` such that, for every `q in Q` and every expert `m`,

   `E_{a~xi_m(.|q)}[r(q,a)]=C(q)+q^T W_m^*q+delta_m(q)`,

   with

   `|delta_m(q)|<=K epsilon` and `||W_m^*||_*<=rank(W_m^*)<=2s`,

   where `K` is a universal constant.

2. **Optimization claim.** Run the online routing algorithm with

   `tau=2s`, `beta=2s/d_q`, and `eta=sqrt(M log d_q/T)`.

   Under the adaptive-query and noisy-feedback model above, prove

   `Reg_T(2s)<=C_0 s sqrt(MT log d_q)`

   for a universal constant `C_0`, uniformly over all admissible fixed environments and adaptive query-selection strategies.
