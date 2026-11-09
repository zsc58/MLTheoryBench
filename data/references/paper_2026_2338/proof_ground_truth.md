# Reference Proof

## Proof Structure

Construct the scaling bijection between the two hypercubes. Show that, with the prescribed lengthscales, every normalized pairwise distance and therefore every kernel Gram matrix is preserved. The corresponding latent and noisy Gaussian vectors consequently have identical information gains. Finally, take the supremum over the bijection of designs.

## Complete Proof

Fix an integer D >= 1, a constant c > 0, a side length L in (0,1], and a sample size N >= 1. Let phi: X_1 -> X_L be phi(x) = Lx. Since L > 0, phi is a bijection, with inverse u -> u/L, and it maps every N-point design in X_1 bijectively to an N-point design in X_L.

Set ell_1 = c sqrt(D) and ell_L = c L sqrt(D). For any x,x' in X_1,

||phi(x) - phi(x')||_2 / ell_L
= ||Lx - Lx'||_2 / (c L sqrt(D))
= ||x - x'||_2 / (c sqrt(D))
= ||x - x'||_2 / ell_1.

Using the common isotropic stationary kernel profile,

k_{ell_L}(phi(x), phi(x'))
= kappa(||phi(x)-phi(x')||_2/ell_L)
= kappa(||x-x'||_2/ell_1)
= k_{ell_1}(x,x').

Thus, if a design in X_1 is enumerated as (x_1,...,x_N) and its image is (u_1,...,u_N) with u_i = phi(x_i), then the Gram matrices satisfy
K^{(L)}_{ij} = k_{ell_L}(u_i,u_j) = k_{ell_1}(x_i,x_j) = K^{(1)}_{ij}
for every i,j. The zero-mean GP finite-dimensional latent Gaussian vectors therefore have the same covariance matrix. Because the observation noise is independent Gaussian with the same variance sigma_epsilon^2, the corresponding observation vectors have identical Gaussian laws, and hence, by the stated information-gain formula,

IG_{X_L,k_{ell_L}}(u_1,...,u_N)
= (1/2) log det(I_N + sigma_epsilon^{-2} K^{(L)})
= (1/2) log det(I_N + sigma_epsilon^{-2} K^{(1)})
= IG_{X_1,k_{ell_1}}(x_1,...,x_N).

This equality holds for every N-point design in X_1 and its image. Because phi is a bijection on N-point designs, the two sets of attainable information-gain values are equal. Taking suprema over these corresponding design sets yields

gamma_N(X_1,k_{ell_1}) = gamma_N(X_L,k_{ell_L})
for every N >= 1, as claimed.
