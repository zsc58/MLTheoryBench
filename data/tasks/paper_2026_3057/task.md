# Problem

## Setup

Let v: R^n x [0,1) -> R^n be a pretrained flow field and let h: R^n -> R^k be an inference-time inequality map. Write J_h for its Jacobian and define ReLU(u)_i = max(u_i, 0) componentwise. Fix c > 0. For p = 2, consider, for 0 <= t < 1,

    dot{x} = v(x,t) - J_h(x)^T lambda - c J_h(x)^T(h(x)+s),
    dot{s} = c[-s + ReLU(-h(x)-lambda/c)],
    dot{lambda} = (h(x)+s)/(1-t)^2,

with x_0 sampled from N(0,I_n), lambda_0 = 0, and s_0 >= 0 componentwise. Assume a solution (x_t,s_t,lambda_t) exists on [0,1). The assertions below are pathwise for every realized solution satisfying the assumptions.

Assume the following conditions along this solution.

(B1) h is C^2, v is C^1 on R^n x [0,1), and there are finite constants L and B such that

    sup_{0 <= t < 1} ||J_h(x_t)||_2 <= L,
    sup_{0 <= t < 1} ||v(x_t,t)|| <= B.

(B2) There are constants 0 < a_min <= a_max < infinity such that

    a_min I_k <= J_h(x_t)J_h(x_t)^T <= a_max I_k

for every 0 <= t < 1.

(B3) The solution exists on [0,1), and the sets {x_t : 0 <= t < 1} and {s_t : 0 <= t < 1} are contained in compact sets.

Fix A_* in R^(k x k) with A_* positive definite. Let E_k be the finite set of diagonal matrices E = diag(e_1,...,e_k) with e_i in {0,1}. For E in E_k define

    P(A_*) = [[I_k, -I_k/2], [-I_k/2, A_*+I_k/2]],
    D_E(A_*) = [[-I_k, I_k-E], [I_k-E, E-A_*-I_k]].

Define the positive structural constants

    kappa_0(A_*) = (1/2) min_{E in E_k} lambda_min(-D_E(A_*)),
    Lambda(A_*) = lambda_max(P(A_*)).

These constants depend only on A_* (with its dimension), and are positive for A_* positive definite. Define

    rho = (sqrt(5)/2) sup_{0 <= t < 1}
          ||J_h(x_t)J_h(x_t)^T - A_*||_2,
    alpha = (kappa_0(A_*) - rho)/Lambda(A_*).

Assume rho < kappa_0(A_*), so alpha > 0. If h is affine, choose A_* = J_h J_h^T; then rho = 0.

## Task

Prove that

    ||ReLU(h(x_t))|| -> 0 as t -> 1-,

and, more precisely,

    ||ReLU(h(x_t))|| = O((1-t)^alpha),
    (1-t)||lambda_t|| = O((1-t)^alpha).
