# Problem

## Setup

Consider a fixed directed graph with a finite neighborhood N(m) for each node m. For a fixed time t and node m, let x_r in R^{d_c}, for r in N(m) union {m}, denote the incoming state of node r. For each r in N(m), let W_mr be a fixed matrix mapping R^{d_c} to R^{d_s}, and let e_mr(t) be a differentiable real-valued scalar score that may depend on x_m and x_r (and on fixed quantities), but not on any other state input. Define attention coefficients by the softmax rule

alpha_mr(t) = exp(e_mr(t)) / sum_{k in N(m)} exp(e_mk(t)),   r in N(m).

Let sigma act componentwise and be differentiable. Define

s_m(t) = sum_{r in N(m)} alpha_mr(t) W_mr x_r,
(tilde h_t^m)_s = sigma(s_m(t)).

For n in N(m) with n != m, define the temporal Jacobian block

J_mn(t) = partial (tilde h_t^m)_s / partial x_n,

where the other state inputs are held fixed.

Use delta_rn for the Kronecker delta, and interpret a vector times a row vector as their outer product.

## Task

Prove that, for every n in N(m) with n != m,

J_mn(t) = diag(sigma'(s_m(t))) [ alpha_mn(t) W_mn + sum_{r in N(m)} W_mr x_r alpha_mr(t) (delta_rn - alpha_mn(t)) partial e_mn(t) / partial x_n ].

Thus the Jacobian block is the sum of a direct attention-weighted message influence and an indirect state-dependent softmax-competition influence, both modulated by the activation derivative.
