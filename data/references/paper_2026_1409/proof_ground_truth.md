# Reference Proof

## Proof Structure

1. Establish forward invariance of the hidden-state boxes.
2. Derive the single-layer incremental estimate using the sigmoid and tanh Lipschitz bounds, retaining recurrent-gate sensitivities.
3. Stack the estimates through depth as a lower-triangular comparison recursion and use Schur stability.
4. Set recurrent gate matrices to zero for the DGN.

## Complete Proof

All vector norms below are Euclidean norms and all matrix norms are the induced Euclidean norms. For k>=0, define

D_k := 0 if k=0, and
D_k := max_{0 <= t < k} ||u_t^a-u_t^b|| if k>=1.

The same convention is used for layer-input discrepancies. For each layer, the layer-input domain is the compact box specified in the task. The first-layer input is in U, and every deeper-layer input is a preceding hidden state, so these domains contain all layer inputs for trajectories in the product invariant set.

Suppress the layer index. Write

f_k = sigma(W_f v_k + R_f h_k + b_f),
i_k = sigma(W_i v_k + R_i h_k + b_i),

htilde_k = tanh(W_phi v_k + b_phi),

h_{k+1} = f_k o tanh(h_k) + i_k o htilde_k.

Because sigmoid values lie in (0,1) and tanh values lie in (-1,1), every component of h_{k+1} has absolute value strictly below two. Induction proves that [-2,2]^(n_h) is forward invariant for every admissible layer input. Applying this layer by layer at each time step proves that the product of the layer boxes is forward invariant for the stacked network.

For two trajectories, put Delta h_k = h_k^a - h_k^b and Delta v_k = v_k^a - v_k^b. Add and subtract the cross terms f_k^a o tanh(h_k^b) and i_k^a o htilde_k^b. The sigmoid is 1/4-Lipschitz componentwise, tanh is 1-Lipschitz, ||tanh(h)||_infinity <= 1, and ||htilde_k||_infinity <= bar_phi. Therefore,

||Delta h_{k+1}|| <= rho ||Delta h_k|| + Gamma ||Delta v_k||,

where

rho = bar_sigma_f + (1/4)||R_f|| + (1/4)||R_i|| bar_phi,

Gamma = ||W_phi|| + (1/4)||W_f|| + (1/4)||W_i|| bar_phi.

Here the gate-difference estimates use ||x o y||_2 <= ||x||_infinity ||y||_2, and the definitions of bar_sigma_f and bar_phi provide the required uniform bounds. If rho < 1, iteration gives, for every k>=0,

||Delta h_k|| <= rho^k ||Delta h_0|| + Gamma/(1-rho) D_k.

For k=0 this is the initial-state inequality because D_0=0; for k>=1 it follows by bounding the geometric convolution by D_k. Since sigmoid values are strictly positive and the layer dimensions are positive, bar_sigma_f is in (0,1), so rho is positive whenever the contraction condition holds. Thus beta(s,k)=rho^k s is a class-KL function on the discrete time domain. If Gamma=0, replace the linear input coefficient by Gamma/(1-rho)+epsilon for any epsilon>0; otherwise the displayed linear gain is already class-K-infinity. Thus the single-layer estimate has valid delta-ISS comparison functions.

For the stacked network, let d_l(k)=||Delta h_k^(l)|| and let d(k)=(d_1(k),...,d_L(k))^T. Put Gamma_l equal to the layerwise Gamma. The layer estimate gives

d_1(k+1) <= rho_1 d_1(k) + Gamma_1 ||Delta u_k||,

and, for l>1,

d_l(k+1) <= rho_l d_l(k) + Gamma_l d_{l-1}(k+1).

Define a nonnegative lower-triangular matrix A and nonnegative vector B recursively by

A_{1,1}=rho_1, B_1=Gamma_1,

A_{l,l}=rho_l, A_{l,j}=Gamma_l A_{l-1,j} for j<l, and B_l=Gamma_l B_{l-1} for l>1.

Substitution through the preceding layers then yields, componentwise,

d(k+1) <= A d(k) + B ||Delta u_k||.

The diagonal entries of A are rho_l. Hence A is Schur stable when every rho_l<1. Unrolling the recursion gives, for every k>=0,

d(k) <= A^k d(0) + sum_{t=0}^{k-1} A^(k-1-t) B ||Delta u_t||,

where the sum is zero when k=0. A standard finite-dimensional Schur-matrix power estimate gives constants C>=1 and q in (0,1) such that ||A^k||<=C q^k. Since A is nonnegative and Schur stable, the input sum is bounded by ||(I-A)^(-1)B|| D_k, with the k=0 case again equal to zero. The Euclidean norm of the stacked state difference equals the Euclidean norm of d(k), because d_l(k) is the Euclidean norm of the l-th block. Therefore,

||Delta h_k|| <= C q^k ||Delta h_0|| + ||(I-A)^(-1)B|| D_k.

The first coefficient defines a class-KL function. If the second coefficient vanishes, add epsilon s to the input gain; otherwise it is already a class-K-infinity gain. This proves delta-ISS of the deep CFN on the product invariant set with respect to U, including k=0.

For the DGN, R_f^(l)=R_i^(l)=0 gives rho_l=bar_sigma_f^(l). Each bar_sigma_f^(l) is strictly below one because it is the supremum of a continuous sigmoid expression over a compact finite-valued domain. Thus every layer satisfies the contraction condition, regardless of the remaining finite parameters. The deep comparison argument therefore proves delta-ISS of the DGN without any additional parameter constraint.
