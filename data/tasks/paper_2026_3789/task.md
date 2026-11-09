# Problem

## Setup

Fix an integer `d>=3`, write `[d]={1,...,d}`, and set

`rho_d=min(1/4,1/(2 sqrt(d)))`.

Constants `C_d>0` and `0<c_d<=rho_d` are to be chosen depending only on `d`, before all dimensions, parameters, planted vectors, and noise realizations below.

Let `n_1,...,n_d` be positive integers and put `N=sum_{i=1}^d n_i`. Let `x_i` be a deterministic unit vector in `R^{n_i}`. Let `W` be a real tensor of dimensions `n_1 x ... x n_d` with independent centered unit-variance entries. For finite real parameters `beta>0`, `r>0`, `L>=1`, and `Theta>=1`, set

`T = beta x_1 tensor ... tensor x_d + N^(-1/2) W`.

Use Euclidean vector norms. For vectors in all modes except `i`, write `T(v_(-i))` for the resulting contraction in mode `i`. For a tuple `U=(u_1,...,u_d)` of unit vectors, define the simultaneous alternating power map wherever its denominators are nonzero by

`(A(U))_i = T(u_(-i))/||T(u_(-i))||`.

Use the positive local chart

`u_i = alpha_i x_i + a_i`, `a_i perpendicular to x_i`, `alpha_i=sqrt(1-||a_i||^2)>0`.

Set

`delta(U)=max_i ||a_i||`,

`B_r={U in the positive local chart: delta(U)<=r/beta}`,

and, when `V` has orthogonal coordinates `b_i`,

`d_loc(U,V)=max_i ||a_i-b_i||`.

For `I_i=[d] excluding {i}` and `S subseteq I_i`, let `W_{i,S}(v_S)` be the contraction of `N^(-1/2)W` with `v_j in R^{n_j}` in modes `j in S`, with `x_j` in modes `j in I_i excluding S`, and with mode `i` left free. Define the scalar and vector maps

`eta_{i,S}(v_S)=<x_i,W_{i,S}(v_S)>`,

`H_{i,S}(v_S)=W_{i,S}(v_S)-eta_{i,S}(v_S)x_i`.

For `S subseteq[d]`, define `omega_S(v_S)` to be the full scalar contraction of `N^(-1/2)W` with `v_j` in modes `j in S` and `x_j` in all other modes. Empty-subset contractions are fixed vectors or scalars.

For a multilinear map `B` with slots indexed by a nonempty set `S`, define

`||B||_op = sup_{||v_j||<=1 for every j in S} ||B(v_S)||`,

using absolute value for scalar maps. The arguments range over the full spaces `R^{n_j}`, not only their planted-orthogonal subspaces.

Define `F_{d,N}(L,Theta)` to be the event on which, for every mode `i`, all three inequalities below hold:

`|eta_{i,empty}| + ||H_{i,empty}|| + |omega_empty| <= L`,

`max_{S subseteq I_i, |S|=1}(||eta_{i,S}||_op+||H_{i,S}||_op) + max_{S subseteq[d], |S|=1}||omega_S||_op <= L`,

`max_{S subseteq I_i, 2<=|S|<=d-1}(||eta_{i,S}||_op+||H_{i,S}||_op) + max_{S subseteq[d], 2<=|S|<=d}||omega_S||_op <= Theta`.

A maximum over an empty family is zero.

Define

`G_{r,d}(beta)=C_d L(1+r/beta)+C_d Theta r^2/beta^2`,

`b_beta=C_d L/beta`,

`kappa_aff=kappa_ctr=C_d L/beta+C_d Theta r/beta^2`.

Assume `F_{d,N}(L,Theta)` holds, together with

`r/beta<=rho_d`,

`G_{r,d}(beta)<=beta/4`,

`beta>=C_d(1+L)`,

`r/beta<=c_d`,

`kappa_aff<1`, `kappa_ctr<1`,

and

`b_beta+kappa_aff r/beta<=r/beta`.

## Task

Prove that the constants `C_d` and `c_d` can be chosen as stipulated so that, whenever these assumptions hold, the map is well-defined on `B_r` and maps `B_r` into itself. For every initial `U_0 in B_r`, define `U_{t+1}=A(U_t)` for nonnegative integers `t`, and prove

`delta(U_t) <= kappa_aff^t delta(U_0) + b_beta (1-kappa_aff^t)/(1-kappa_aff)`

for every nonnegative integer `t`.

Moreover, prove that for all `U,V in B_r`,

`d_loc(A(U),A(V))<=kappa_ctr d_loc(U,V)`.

Deduce that `A` has a unique fixed point `U_star in B_r`, with positive planted coordinates, such that

`delta(U_star)<=b_beta/(1-kappa_aff)`

and, for every initial `U_0 in B_r` and every nonnegative integer `t`,

`d_loc(U_t,U_star)<=kappa_ctr^t d_loc(U_0,U_star)`.
