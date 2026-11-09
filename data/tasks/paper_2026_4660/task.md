# Problem

## Setup

Let d be a positive integer, let M be a condition manifold, and let tilde c be an off-manifold condition (tilde c not in M). Let x_0 be sampled from a prior p_0. A conditional flow on t in [0,1] is defined by

 d psi_t(x_0)/dt = v_t(psi_t(x_0), tilde c),    psi_0(x_0) = x_0,

where v_t maps states in R^d and conditions to R^d. Write x_hat_1 = psi_1(x_0). Assume the vector field uses smooth activations and differentiable time embeddings, with uniformly bounded derivatives on a compact domain containing the normalized trajectories; consequently, the velocity along this trajectory belongs to H^1([0,1]; R^d). Define the endpoint-relative constant velocity u = x_hat_1 - x_0 and the local transport-energy excess

 E_local = integral_0^1 ||v_t(psi_t(x_0), tilde c) - u||_2^2 dt.

Suppose E_local >= Delta_local for some Delta_local > 0.

## Task

Prove that the integrated squared acceleration (trajectory curvature energy)

 kappa = integral_0^1 || d/dt v_t(psi_t(x_0), tilde c) ||_2^2 dt

satisfies

 kappa >= pi^2 Delta_local > 0.

Thus every realized off-manifold trajectory with positive endpoint-relative transport-energy excess has quantitatively nonzero integrated curvature.
