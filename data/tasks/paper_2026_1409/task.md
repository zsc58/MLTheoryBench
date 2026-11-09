# Problem

## Setup

Let L, n_u, and n_h^(l) for l = 1,...,L be positive integers, and set n_{u^(1)} = n_u and n_{u^(l)} = n_h^(l-1) for l > 1. All displayed matrices and bias vectors are finite real arrays of the compatible dimensions. All vector norms are Euclidean norms, and all matrix norms are the induced Euclidean norms.

Consider an L-layer discrete-time network. In layer l, with input v_k^(l) and state h_k^(l) in R^(n_h^(l)), define

f_k^(l) = sigma(W_f^(l) v_k^(l) + R_f^(l) h_k^(l) + b_f^(l)),

i_k^(l) = sigma(W_i^(l) v_k^(l) + R_i^(l) h_k^(l) + b_i^(l)),

h-tilde_k^(l) = tanh(W_phi^(l) v_k^(l) + b_phi^(l)),

h_{k+1}^(l) = f_k^(l) o tanh(h_k^(l)) + i_k^(l) o h-tilde_k^(l).

Here sigma is the componentwise logistic sigmoid and o denotes componentwise multiplication. The first-layer input is v_k^(1) = u_k; for l > 1, v_k^(l) = h_{k+1}^(l-1). Inputs satisfy u_k in U = [-1,1]^(n_u).

For layer l, use the compact box

U-tilde^(1) = [-2,2]^(n_u),

U-tilde^(l) = [-2,2]^(n_h^(l-1)) for l > 1.

These boxes contain the possible layer inputs whenever the layer states belong to the invariant boxes below. Let H_inv^(l) = [-2,2]^(n_h^(l)), and define

bar-sigma_f^(l) = sup over v in U-tilde^(l), h in H_inv^(l) of ||sigma(W_f^(l) v + R_f^(l) h + b_f^(l))||_infinity,

bar-phi^(l) = sup over v in U-tilde^(l) of ||tanh(W_phi^(l) v + b_phi^(l))||_infinity <= 1.

For two input sequences u^a and u^b, define their input discrepancy at horizon k by

D_k(u^a,u^b) := 0 if k=0, and
D_k(u^a,u^b) := max over 0 <= t < k of ||u_t^a-u_t^b|| for k>=1.

A system is delta-ISS on a state set with respect to an input set if there are beta in KL and gamma in K-infinity such that, for every k in the nonnegative integers, every pair of initial states in the state set, and every pair of input sequences in the input set, the corresponding trajectories satisfy

||x_k^a - x_k^b|| <= beta(||x_0^a - x_0^b||, k) + gamma(D_k(u^a,u^b)).

## Task

Prove that the product state set product over l = 1,...,L of H_inv^(l) supports the following integrated result: if

rho^(l) = bar-sigma_f^(l) + (1/4)||R_f^(l)|| + (1/4)||R_i^(l)|| bar-phi^(l) < 1

for every layer, then the deep CFN is delta-ISS with respect to U; moreover, the specialization R_f^(l) = R_i^(l) = 0 for all l is delta-ISS without any additional parameter constraint.
