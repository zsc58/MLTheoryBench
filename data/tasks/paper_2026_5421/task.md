# Problem

## Setup

Let `d` be a positive integer, and let `X,Y` be nonempty convex compact subsets of `R^d`. Let `phi:X -> Y` be a smooth bijection. For each round `t=1,...,T`, suppose the differentiable loss has the form

`f_t(x)=c_t(phi(x))`,

where `c_t:Y -> R` is convex.

All vector norms are Euclidean. Bounds on derivatives use the induced operator norms, including the corresponding multilinear operator norm for higher derivatives. Derivatives on the compact domains are understood in ambient Euclidean coordinates through local extensions with the stated regularity. Derivatives of `phi^{-1}` are those of the local inverse of `phi`. Write `J_phi` for the Jacobian of `phi`.

Define the external regret by

`Reg_T=sum_{t=1}^T f_t(x_t)-min_{x in X}sum_{t=1}^T f_t(x)`.

Assume there is a twice continuously differentiable, strictly convex function `Psi:Y -> R` such that, for every `x in X`,

`[nabla^2 Psi(phi(x))]^{-1}=J_phi(x)J_phi(x)^T`.

For `u,v in Y`, write

`D_Psi(u||v)=Psi(u)-Psi(v)-<nabla Psi(v),u-v>`.

Suppose that finite constants `L>1`, `M>0`, and `B>0` satisfy all of the following:

- `phi` is `L`-Lipschitz, and the first and second derivatives of `phi^{-1}` are bounded in operator norm by `L`.
- `Psi` is 1-strongly convex and smooth, meaning that its gradient is Lipschitz on `Y`; its first and third derivatives exist and are bounded by `L`.
- For every fixed `u in Y`, the function `v -> D_Psi(u||v)` is `L`-Lipschitz on `Y` in Euclidean norm.
- `||nabla f_t(x)||_2 <= M` for every `t` and `x in X`, and `sup_{u,v in Y}D_Psi(u||v)<=B`.

At round `t`, the learner selects `x_t` using only information available before that round and then receives the exact gradient `nabla f_t(x_t)`. The losses may be chosen adversarially after the current decision, subject to the assumptions above. The map `phi` is not supplied to the learner.

Starting from any initial point `x_1 in X`, projected gradient descent uses a fixed positive step size `eta` and the update

`x_{t+1}=Pi_X(x_t-eta nabla f_t(x_t))`,

where `Pi_X(v)=argmin_{x in X}||x-v||_2^2` is Euclidean projection onto `X`.

## Task

Prove that there are constants `k>0`, `C<infinity`, and `T_0>=1`, depending only on `L,M,B`, such that for every integer `T>=T_0`, every loss sequence satisfying the setup, and every initial point `x_1 in X`, the algorithm with

`eta=k T^{-1/2}`

satisfies

`Reg_T<=C sqrt(T)`.
