# Problem

## Setup

Let L and n_0,n_1,...,n_L be positive integers, with n_0=n_u. For each layer l=1,...,L, let h_k^(l) in R^{n_l}, let the layer-input dimension be n_{l-1}, and let

- W_f^(l), W_h~^(l) be matrices in R^{n_l x n_{l-1},
- R_f^(l), R_h~^(l) be matrices in R^{n_l x n_l}, and
- b_f^(l), b_h~^(l) be vectors in R^{n_l}.

Define
`f_k^(l)=sigma(W_f^(l)u~_k^(l)+R_f^(l)h_k^(l)+b_f^(l))`,
`h~_k^(l)=tanh(W_h~^(l)u~_k^(l)+R_h~^(l)(f_k^(l) circ h_k^(l))+b_h~^(l))`,
`h_{k+1}^(l)=(1-f_k^(l))circ h_k^(l)+f_k^(l)circ h~_k^(l)`,
where `u~_k^(1)=u_k` and `u~_k^(l)=h_{k+1}^(l-1)` for l>1. Here `circ` is componentwise multiplication, `sigma(t)=1/(1+exp(-t))`, and tanh is componentwise. Let `H_l=[-1,1]^{n_l}`, `U=[-1,1]^{n_u}`, and `V_1=U`, `V_l=H_{l-1}` for l>1.

Assume `h_0^(l) in H_l` for every l and `u_k in U` for every k. Use the infinity norm and its induced operator norm. Define
`bar_sigma_l=sigma(||[W_f^(l) R_f^(l) b_f^(l)]||_infty)` and
`bar_phi_l=tanh(||[W_h~^(l) R_h~^(l) b_h~^(l)]||_infty)`.

A function is of class `K` if it is continuous, strictly increasing, and vanishes at zero. It is in `K_infinity` if it is also unbounded. A function `psi` is in `KL` if, for each fixed positive first argument, `psi` decreases to zero in its second argument, and for each fixed second argument it is of class `K` in the first argument.

Adopt the convention that the maximum over an empty index set is 0. A discrete-time system is delta-ISS on a state set `X` with respect to an input set `V` if there exist `psi in KL` and `gamma in K_infinity` such that every pair of trajectories from `X`, driven by input sequences in `V`, satisfies
`||x_k^a-x_k^b||_infty <= psi(||x_0^a-x_0^b||_infty,k) + gamma(max_{0<=t<k}||v_t^a-v_t^b||_infty)` for every `k>=0`.

## Task

Prove that if, for every layer l,
`bar_sigma_l+bar_sigma_l^2||R_h~^(l)||_infty+(1/4)||R_f^(l)||_infty(bar_sigma_l||R_h~^(l)||_infty+bar_phi_l+1)<1`,
then every layer is delta-ISS on `H_l` with respect to `V_l`, and the full stacked MGU network is delta-ISS on `H_1 x ... x H_L` with respect to `U`, with the trajectory-difference estimate above for every pair of admissible trajectories and every time `k`.
