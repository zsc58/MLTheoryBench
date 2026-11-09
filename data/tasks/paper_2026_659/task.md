# Problem

## Setup

Fix integers d >= 1 and D_out >= 1. Let X be a common domain for the raw input channels, let Gamma_{D_out} be the all-ones tensor in R^{D_out}, and let sigma: R^{D_out} -> R^{D_out} be a fixed componentwise nonlinearity. An input is Z = (Z_1,...,Z_d) with Z_k in X. For U = (U_1,...,U_d) with each U_k in R^{D_out} and a = (a_1,...,a_d) in R^d, define

U odot_t a = sum_{k=1}^d U_k a_k.

A tensor-affine node has output

sigma(U odot_t a + b Gamma_{D_out})

for scalar weights a_k and scalar bias b. For a node pre-activation q'_j(Z, theta_j), call it input-separable if there are parameter blocks theta_{jk} and maps q'_{jk}: X x Theta_{jk} -> R^{D_out} such that

q'_j(Z, theta_j) = sum_{k=1}^d q'_{jk}(Z_k, theta_{jk}) + b_j Gamma_{D_out}.

Its associated output is sigma(q'_j). Given an input-separable node, define the scalar-reweighted construction

q_tilde_j(Z, theta_j, gamma_j) = sum_{k=1}^d gamma_{jk} q'_{jk}(Z_k, theta_{jk}) + b_j Gamma_{D_out},

with output f_tilde_j = sigma(q_tilde_j). The blocks theta_{jk} are frozen, while the scalars gamma_{jk} are trainable. A collection of nodes has homogeneous inputs if all nodes receive the same channel tensors; otherwise its inputs are inhomogeneous.

## Task

Prove the following integrated claim for every scalar-reweighted node. Define Z_tilde_{jk} = q'_{jk}(Z_k, theta_{jk}). Then f_tilde_j is exactly a tensor-affine node with channel inputs (Z_tilde_{j1},...,Z_tilde_{jd}), scalar weights (gamma_{j1},...,gamma_{jd}), and bias b_j. Across a collection of such nodes these processed inputs may be node-specific, so the representation may be inhomogeneous. Consequently, every property or training result valid for tensor-affine nodes under inhomogeneous inputs transfers to these nodes; specifically, with the channelwise functions frozen, transferred training uses one trainable scalar per input-channel contribution.
