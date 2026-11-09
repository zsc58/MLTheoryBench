# Problem

## Setup

Fix integers P >= 1, H >= 1, C >= 1, and N >= 1. Let training samples be (x_n, y_n) with x_n in R^P and y_n in {1,...,C}. The trainable parameters are U, V, and T. The matrix U has shape 2P by P and is constrained to the fixed sparse pattern
F = {(2p-1,p),(2p,p): p = 1,...,P}; entries outside F are fixed at zero, and each row therefore has at most one trainable entry. Matrices V and T have shapes 2P by H and H by C.

For x in R^P define
lambda_i(x) = sum_p U_{i,p} x_p,
g_h(x) = min_{1 <= i <= 2P} (lambda_i(x) + V_{i,h}),
z_d(x) = max_{1 <= h <= H} (g_h(x) + T_{h,d}),
and p_d(x) = exp(z_d(x)) / sum_{r=1}^C exp(z_r(x)).

For sample n let ell_n = -log p_{y_n}(x_n), and define the training objective J = max_{1 <= n <= N} ell_n.

The optimization variables are the free entries of U in F together with all entries of V and T. Let ∂^C J denote the Clarke subdifferential of J with respect to these trainable coordinates: it is the closed convex hull of all limits of ordinary gradients at points where J is differentiable, as those points tend to the current parameter value. In this task, a valid nonsmooth subgradient means an element of ∂^C J.

## Task

Prove that, for every choice of parameters and every training set as above, there exists a valid nonsmooth subgradient G = (G0,G1,G2) of J such that each parameter layer has at most C nonzero entries:
|supp(G0)| <= C,  |supp(G1)| <= C,  and |supp(G2)| <= C.
The bound is one possible contribution per output class, so coincident contributions may make the support smaller.
