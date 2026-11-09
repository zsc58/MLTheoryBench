# Reference Proof

## Proof Structure and Obligations

The proof uses only finite real arithmetic and the definition of a supremum. Its obligations are:

1. Verify that the population losses, empirical losses, signed rewards, and finite reward sums are real-valued, with one fixed population loss and one fixed empirical loss throughout the trajectory.
2. Establish telescoping for any real-valued potential and every nonnegative finite horizon.
3. Deduce the population identity, zero excess, and the conditional terminal lower-bound budget.
4. Apply the same identity to empirical progress.
5. Obtain the two endpoint deviation inequalities from the stated uniform bound.
6. Combine those inequalities and verify the horizon, adaptivity, and degenerate cases.

All six obligations are derived below. No external result, concentration statement, or paper-specific unproved dependency is needed.

## Complete Proof

### step_001: Well-defined quantities

Fix a nonnegative integer `T` and an admissible sequence `theta_0,...,theta_T`. For every state, measurability and the assumption `integral_Z |ell(theta,z)| Q(dz) < infinity` ensure that `L(theta)` is a finite real number. Because `n` is a positive integer and every `ell(theta,z_i)` is real, `hat L_n(theta)` is also a finite real number. Thus both signed progress sequences and all their finite sums are real-valued.

The same distribution and the same panel are used at all times. Consequently `L` and `hat L_n` are each a single function on the model space. The proof fixes an arbitrary realized state sequence; it does not need a probability distribution on trajectories or independence between a trajectory and released audit information. The ambient lower bound on the loss is a supplied source assumption; no numerical value of that bound is needed to establish the two requested conclusions.

### step_002: Finite telescoping

For any function `V: Theta -> R`, define `d_t(V)=V(theta_{t-1})-V(theta_t)` for `1 <= t <= T`.

If `T=0`, the sum is empty and equals zero. Since `theta_T=theta_0`, this is also `V(theta_0)-V(theta_T)`.

If `T>=1`, expanding gives

`sum_{t=1}^T d_t(V) = [V(theta_0)-V(theta_1)] + ... + [V(theta_{T-1})-V(theta_T)]`.

Every intermediate value `V(theta_t)`, `1 <= t < T`, occurs once with each sign and cancels. Therefore, in both cases,

`sum_{t=1}^T d_t(V) = V(theta_0)-V(theta_T)`.

### step_003: Population accounting and the terminal budget

Taking `V=L` proves

`sum_{t=1}^T p_t = L(theta_0)-L(theta_T)`.

By the definition of the false-positive excess,

`Gamma_T(p,L) = sum_t p_t - [L(theta_0)-L(theta_T)] = 0`.

If a real number `L_min` satisfies `L(theta_T) >= L_min`, then `-L(theta_T) <= -L_min`. Hence

`sum_t p_t = L(theta_0)-L(theta_T) <= L(theta_0)-L_min`.

This uses only the stated terminal inequality; it does not require a new lower-bound assumption on all trajectory states.

### step_004: Empirical accounting

Applying step_002 with `V=hat L_n` gives

`sum_{t=1}^T hat p_t = hat L_n(theta_0)-hat L_n(theta_T)`.

### step_005: Uniform deviation at the endpoints

Suppose now that `theta_t in F` for every `0 <= t <= T` and `d_n(F) <= Delta`, where `Delta` is real. In particular, `theta_0` and `theta_T` belong to `F`.

The supremum definition gives

`|hat L_n(theta_0)-L(theta_0)| <= d_n(F) <= Delta`

and

`|hat L_n(theta_T)-L(theta_T)| <= d_n(F) <= Delta`.

The first inequality implies

`hat L_n(theta_0) <= L(theta_0)+Delta`.

The second implies

`hat L_n(theta_T) >= L(theta_T)-Delta`.

The deviation hypothesis also ensures that `d_n(F)` is finite. Since it is nonnegative, that hypothesis implies `Delta >= 0`.

### step_006: Finite-panel guarantee and quantifiers

Combining steps_004 and _005 yields

`sum_t hat p_t = hat L_n(theta_0)-hat L_n(theta_T)`

`<= (L(theta_0)+Delta) - (L(theta_T)-Delta)`

`= L(theta_0)-L(theta_T)+2 Delta`

`= sum_t p_t + 2 Delta`,

where the last equality is step_003. Subtracting the population endpoint improvement gives

`Gamma_T(hat p,L) <= 2 Delta`.

For `T=0`, the same argument applies, and the empirical excess is zero; the required inequality follows from `Delta >= 0`. For `Delta=0`, the derivation remains valid without division or a strict-positivity requirement. If `F` is empty, there is no trajectory with `theta_0 in F`, so the finite-panel implication has no instance. If `d_n(F)=+infinity`, no real `Delta` satisfies its premise. A negative `Delta` likewise cannot satisfy the deviation premise. If `Theta` is empty, there are no admissible trajectories, even at horizon zero, and the universal assertions are vacuous.

The proof is valid for each finite state sequence and uses the deviation hypothesis only at states already covered by the same class `F`. Thus, for any fixed panel and class satisfying that hypothesis, it establishes the claimed inequalities for every horizon and every trajectory in that class simultaneously. Adaptive selection does not add a term to the bound. No i.i.d. sampling assumption, probability of the deviation condition, measurability of a random supremum, or restriction on class cardinality is asserted or needed.
