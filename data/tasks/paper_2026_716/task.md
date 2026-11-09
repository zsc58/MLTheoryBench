# Problem

## Setup

Let `V` be the vertex set of a finite connected simple undirected graph with edge set `E`. Each edge `(i,j)` has a fixed symmetric positive base weight `A^(0)_ij` and a fixed feature vector `phi_ij` in `R^d`, with `phi_ij=phi_ji`. There are no self-loops. For `theta` in `R^d`, define

`A_ij(theta)=A^(0)_ij exp(theta^T phi_ij)` for `(i,j) in E`,

and set `A_ij(theta)=0` for nonedges, including `i=j`. Define

`D_ii(theta)=sum_{j in V} A_ij(theta)`,

and the random-walk transition matrix

`P_theta=D_theta^(-1)A_theta`.

Let `Theta subset R^d` be the parameter set, and assume that distinct parameters in `Theta` give distinct matrices `P_theta`. Parameter derivatives below mean the coordinate derivatives of the displayed smooth formulas on `R^d`, evaluated at `theta in Theta`.

Fix a nonempty proper subset `A_y subset V` and let `S_y=V\A_y`. For any nonempty index set `B`, let `1_B` be its all-ones column vector. The discrete-time walk with transition matrix `P_theta` starts at a fixed `q in S_y` and stops on its first visit to `A_y`; call this time `T_y`. Put

`M=P_theta[S_y,S_y]`, `R=P_theta[S_y,A_y]1_{A_y}`,

and assume `rho(M)<1` at the parameter under consideration. Let `e_q` be the coordinate vector of `q` in `R^{S_y}`, and let `I` be the identity on that space. For each coordinate `a in {1,...,d}`, write `M_a=partial_a M` and `R_a=partial_a R`.

The graph, base weights, features, class set, and starting vertex are held fixed under parameter differentiation; the argument `z` is also held fixed when differentiating a generating function.

## Task

Prove the following integrated theorem. With `Z=(I-M)^(-1)`, for every `q in S_y` and every integer `t>=1`,

1. `p_theta(t | q):=Pr_theta(T_y=t | X_0=q)=e_q^T M^(t-1)R`;
2. for every finite complex `z` with `|z|rho(M)<1`,

   `G_q(z):=sum_{t>=1}z^t p_theta(t | q)=z e_q^T(I-zM)^(-1)R`;

3. `E_theta[T_y | q]=e_q^T Z1_{S_y}` and

   `Var_theta(T_y | q)=e_q^T(2Z-I)Z1_{S_y}-(e_q^T Z1_{S_y})^2`;

4. the coordinate sensitivities are

   `partial_a p_theta(t | q)=e_q^T[(partial_a M^(t-1))R+M^(t-1)R_a]`,

   where

   `partial_a M^(t-1)=sum_{r=0}^{t-2}M^rM_aM^(t-2-r)`

   with the empty sum equal to zero for `t=1`, and

   `partial_a G_q(z)=z e_q^T[zW(z)M_aW(z)R+W(z)R_a]`,

   `W(z)=(I-zM)^(-1)`;

   moreover, with `partial_a Z=ZM_aZ`,

   `partial_a E_theta[T_y|q]=e_q^T(partial_a Z)1_{S_y}`,

   `partial_a E_theta[T_y^2|q]=e_q^T[2((partial_a Z)Z+Z(partial_a Z))-partial_a Z]1_{S_y}`,

   and

   `partial_a Var_theta(T_y|q)=partial_a E_theta[T_y^2|q]-2 E_theta[T_y|q] partial_a E_theta[T_y|q]`.

Derive also, for every edge `(i,j)`, the kernel identity

`partial_a P_ij(theta)=P_ij(theta)[phi_ij,a-sum_{k:(i,k) in E}P_ik(theta)phi_ik,a]`,

with zero derivative for nonedges, and use it to specify `M_a,R_a`.
