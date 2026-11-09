# Problem

## Setup

Let `m,n,r` be positive integers with `r <= min(m,n)`, and let `C_S,tau` be finite nonnegative real constants. Let `A0` in `R^(m x r)` and `B0` in `R^(n x r)` have orthonormal columns. A random matrix `X` has the representation

`X = A0 S0 B0^T + E`,

where `S0` is an `r x r` random matrix and `E` is an `m x n` random matrix. Assume that

- `E[S0 S0^T]` and `E[S0^T S0]` are positive definite;
- `E||S0||_F^2 <= r C_S^2`;
- `E[E | S0]=0` and `E||E||_2^2 <= tau^2`.

Here matrix norms `||.||_F` and `||.||_2` are the Frobenius and spectral norms, respectively; vector norms are Euclidean.

Fix matrices `A` in `R^(m x r)` and `B` in `R^(n x r)` with orthonormal columns. Define the encoded core `C=A^T X B`, its vectorization `c=vec(C)` in `R^d`, where `d=r^2`, and let `p_C` be the law of `c`. The map `vec` stacks the columns of a matrix, and `mat` is its inverse. Let `q=N(0,I_d)`. Define

`delta_A = ||sin Theta(A,A0)||_2`,  `delta_B = ||sin Theta(B,B0)||_2`,

where the quantities are the largest sines of the principal angles between the respective column spaces.

For independent `c` distributed as `p_C` and `z` distributed as `q`, set `Y_t=(1-t)c+tz`. Let `rho_t` be the Lebesgue density of `Y_t`, and let `v(x,t)` be a Borel version of the marginal velocity `E[z-c | Y_t=x]`. Thus `rho_0` is the density of `p_C`, `rho_1` is the density of `q`, and the density path satisfies the continuity equation for `v`.

Fix a Borel learned velocity field `vhat:R^d x [0,1] -> R^d`. Let `Phi_t` denote its ODE flow, initialized by `Phi_0(x)=x`, so trajectories satisfy `d Phi_t(x)/dt = vhat(Phi_t(x),t)` almost everywhere in time. Let `rhohat_t` be the Lebesgue density of `Phi_t(c)` for `c` distributed as `p_C`. In particular, `rhohat_0=rho_0` and

`partial_t rhohat_t + div(rhohat_t vhat)=0`.

Assume that finite constants `epsilon,L_v,C1,L,C2 > 0` satisfy

`integral_0^1 integral_R^d ||v(x,t)-vhat(x,t)||^2 rho_t(x) dx dt <= epsilon^2`,

and that, for every `t` in `[0,1]`:

- both velocity fields are spatially `L_v`-Lipschitz;
- the densities are positive and differentiable in space, with `rho_t(x), rhohat_t(x) <= C1 exp(-||x||^2/2)` for every `x`;
- `||grad log rho_t(x)||, ||grad log rhohat_t(x)|| <= L(1+||x||)` for every `x`;
- `integral_R^d (1+||x||)^2 rho_t(x)^3/rhohat_t(x)^2 dx <= C2`.

Define the generated core law `p_hatC` as the law of `Phi_1^(-1)(z)` for `z` distributed as `q`. If `chat` has law `p_hatC`, define the generated matrix by `Xhat=A mat(chat) B^T`, with law `p_hatX`. Let `p_X` denote the law of `X`. Finally set

`C_F = 4 C1 (2pi)^(d/2) L sqrt(C2)`.

Here `W_2` between matrix laws uses the Frobenius norm as its ground metric.

## Task

Prove that

`W_2(p_hatX,p_X) <= sqrt(r) C_S (delta_A+delta_B) + exp(L_v) sqrt(2 C_F epsilon) + sqrt(min(m,n)) tau`.
