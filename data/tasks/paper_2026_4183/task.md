# Problem

## Setup

Fix positive integers L, d_x, C, d_k, and d_ff, and a finite horizon T>0. Hidden states are matrices in R^{L x d_x}. Matrix norms and inner products are Frobenius; parameter vectors use the Euclidean norm. Transposes of derivatives denote adjoints for these inner products.

Let K be a compact subset of R^{L x d_x}, let mu_X be a Borel probability measure with support contained in K, and let X_0 have law mu_X. Let Y:R^{L x d_x}->R^{L x C} be a measurable map whose rows are one-hot vectors. All expectations below are over X_0. For a vector z in R^C, define softmax(z)_j=exp(z_j)/sum_{i=1}^C exp(z_i), and apply softmax rowwise to matrices. For logits Z in R^{L x C}, define
\[
\ell(Y,Z)=\frac1L\sum_{l=1}^L\left[\log\!\left(\sum_{j=1}^C e^{Z_{lj}}\right)-Y_l^\top Z_l\right],
\qquad
\nabla_Z\ell(Y,Z)=\frac1L(\operatorname{softmax}(Z_l)-Y_l)_{l=1}^L.
\]

Identify a parameter vector u in R^m with the entries of
\[
u=(W_Q,W_K,W_V,W_O,W_1,b_1,W_2,b_2),
\]
where
\[
W_Q,W_K,W_V\in\mathbb R^{d_x\times d_k},\quad W_O\in\mathbb R^{d_k\times d_x},
\]
\[
W_1\in\mathbb R^{d_x\times d_{\rm ff}},\quad b_1\in\mathbb R^{d_{\rm ff}},\quad
W_2\in\mathbb R^{d_{\rm ff}\times d_x},\quad b_2\in\mathbb R^{d_x}.
\]
Thus m is the total number of entries in this tuple. Let Theta be a nonempty compact convex subset of this parameter space. For X in R^{L x d_x}, put Q=XW_Q, K_att=XW_K, and V=XW_V, with rows q_r and k_r for Q and K_att. Define
\[
(A_u(X))_{rs}=\begin{cases}
\displaystyle\frac{\exp(q_r^\top k_s/\sqrt{d_k})}{\sum_{j=1}^r\exp(q_r^\top k_j/\sqrt{d_k})},&s\le r,\\
0,&s>r,
\end{cases}
\qquad 1\le r,s\le L.
\]
Let sigma:R->R be a fixed smooth scalar activation applied componentwise, and let 1_L be the all-ones column vector. All matrices and biases in the following field are the components of u:
\[
F(X;u)=A_u(X)VW_O+\sigma(XW_1+\mathbf 1_Lb_1^\top)W_2+\mathbf 1_Lb_2^\top.
\]

Let zeta:[0,T]->[0,infinity) be bounded and Lipschitz. Assume F is continuously differentiable in (X,u) on a neighborhood of K x Theta, and that F, D_XF, and D_uF are uniformly bounded on K x Theta. Assume also that there are finite constants L_F and L_F^{(1)} such that, for every X,X' in K and a in Theta,
\[
\|F(X;a)-F(X';a)\|_F\le L_F\|X-X'\|_F,
\]
\[
\|D_XF(X;a)-D_XF(X';a)\|_{\rm op}\le L_F^{(1)}\|X-X'\|_F.
\]
Let G:K->R^{L x C} be the restriction of a continuously differentiable map on a neighborhood of K. Assume G is bounded and Lipschitz on K and DG is uniformly bounded there; the resulting cross-entropy is bounded.

Let U be an admissible subset of L^infinity([0,T];Theta), where controls are deterministic measurable functions of time, common to all inputs, and are identified up to equality almost everywhere. For u in U, let
\[
\dot S_t^u=\zeta(t)F(S_t^u;u_t),\qquad S_0^u=X_0,
\]
with the differential equation understood almost everywhere in time. Assume all these trajectories, for initial states in supp(mu_X), exist on [0,T] and remain in K. Define
\[
J(u)=\mathbb E\,\ell(Y(X_0),G(S_T^u)).
\]
For the first conclusion, assume u* in U is locally minimizing in a fixed topology on U for which the feasible convex perturbations specified below converge to u*. Write S_t*=S_t^{u*} and define the adjoint, separately for each initial input, by
\[
-\dot P_t=\zeta(t)D_XF(S_t^*;u_t^*)^\top P_t,
\qquad
P_T=DG(S_T^*)^\top\frac1L(\operatorname{softmax}(G(S_T^*))-Y(X_0)).
\]

## Task

Prove that for every v in U such that u^alpha=u*+alpha(v-u*) belongs to U for all sufficiently small alpha>=0,
\[
\int_0^T\mathbb E\left[\zeta(t)\left\langle P_t,D_uF(S_t^*;u_t^*)[v_t-u_t^*]\right\rangle_F\right]dt\ge0.
\]

If, in addition, U=L^infinity([0,T];Theta), arbitrary needle replacements by any a in Theta are admissible, and u* is locally minimizing in the strong L1([0,T];R^m) topology, define
\[
\overline H(t,a)=\mathbb E\left[\zeta(t)\left\langle P_t,F(S_t^*;a)\right\rangle_F\right].
\]
Prove that there is a Lebesgue null set N subset [0,T] such that, for every t outside N and every a in Theta,
\[
\overline H(t,u_t^*)\le\overline H(t,a).
\]
Under these additional assumptions, at almost every time for which u_t* is an interior point of Theta in R^m and zeta(t)>0, prove
\[
\mathbb E\left[D_uF(S_t^*;u_t^*)^\top P_t\right]=0.
\]
