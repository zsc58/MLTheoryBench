# Problem

## Setup

Let `Theta` be a model space and `(Z, Sigma)` a measurable data space. Let `ell: Theta x Z -> R` be a loss that is bounded below: there exists `b in R` such that `ell(theta,z) >= b` for every `theta in Theta` and `z in Z`.

A sealed audit distribution `Q` is a probability measure on `(Z, Sigma)`, fixed externally and independently of the training procedure's choices. The training procedure cannot select or alter `Q`. Any audit information it receives must be explicitly released by an external audit provider; it has no other audit access. No particular release rule is assumed, and model states may depend on information already released. The distribution remains unchanged throughout a trajectory.

For every `theta in Theta`, assume that `z -> ell(theta,z)` is `Sigma`-measurable and that

`integral_Z |ell(theta,z)| Q(dz) < infinity`.

Define the real-valued population audit loss

`L(theta) = E_{z~Q}[ell(theta,z)]`.

For an audit panel `A_n=(z_1,...,z_n)`, where `n >= 1` is an integer and each `z_i in Z`, define

`hat L_n(theta) = (1/n) sum_{i=1}^n ell(theta,z_i)`.

The same panel is used throughout a trajectory and cannot be altered by the training procedure.

An admissible trajectory of horizon `T` is any finite sequence `theta_0,...,theta_T` of elements of `Theta`, where `T` is a nonnegative integer; its intermediate states may be selected adaptively. The claims below apply to every such sequence, including every sequence arising under the audit-access convention above. Define signed, unclipped progress for `1 <= t <= T` by

`p_t = L(theta_{t-1}) - L(theta_t)`,    `hat p_t = hat L_n(theta_{t-1}) - hat L_n(theta_t)`.

For real rewards `q_1,...,q_T` and the population loss `L`, define the false-positive excess

`Gamma_T(q,L) = sum_{t=1}^T q_t - [L(theta_0)-L(theta_T)]`.

For a class `F` contained in `Theta`, define the uniform audit deviation

`d_n(F) = sup_{theta in F} |hat L_n(theta)-L(theta)|`.

This supremum is taken in `[0,+infinity]`, with `d_n(empty set)=0`. For a real number `Delta`, a panel realizes deviation `Delta` on `F` when `d_n(F) <= Delta`.

## Task

Prove the following integrated theorem for every admissible finite trajectory and every horizon `T`.

1. **Exact audit accounting.**
`sum_{t=1}^T p_t = L(theta_0)-L(theta_T)`, so `Gamma_T(p,L)=0`. Moreover, whenever a real number `L_min` satisfies `L(theta_T) >= L_min`,
`sum_{t=1}^T p_t <= L(theta_0)-L_min`.

2. **Finite-panel guarantee.** If every `theta_t`, `0 <= t <= T`, lies in `F` and the panel satisfies `d_n(F) <= Delta`, then
`sum_{t=1}^T hat p_t <= sum_{t=1}^T p_t + 2 Delta = L(theta_0)-L(theta_T)+2 Delta`.
Equivalently, `Gamma_T(hat p,L) <= 2 Delta`. The bound must hold independently of the horizon length and of how intermediate states are chosen adaptively.
