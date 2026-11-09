# Reference Proof

## Proof Structure

Use a positive-semidefinite Gram certificate whose diagonal entries are one and whose entries on the cycle edges are a common negative number. Nonnegativity of the Frobenius inner product of two positive-semidefinite matrices then converts that certificate into an upper bound on the cycle-edge sum. Alternating one-dimensional vectors give the even-cycle certificate, while planar vectors give the odd-cycle certificate.

## Complete Proof

Fix an integer k >= 4 and let X be in C(C_k). Let the cycle edges be (i,i+1), with indices modulo k, and write S = sum_{i=1}^k X_{i,i+1}. Since X is symmetric, has diagonal one, and vanishes on non-edges, it suffices to construct a positive-semidefinite matrix Q with diagonal one and with Q_{i,i+1} = -alpha on every cycle edge, where alpha > 0. The standard PSD inner-product fact gives <X,Q>_F = Tr(XQ) >= 0: its hypotheses hold because X and Q are real symmetric PSD matrices of the same size. Expanding the inner product, all off-diagonal terms outside the cycle vanish because the corresponding entries of X are zero, so

0 <= <X,Q>_F = k - 2 alpha S.

Therefore S/k <= 1/(2 alpha).

For any vectors u_1,...,u_k, their Gram matrix Q satisfies a^T Q a = ||sum_i a_i u_i||^2 >= 0 for every a in R^k. Thus it is PSD, and unit vectors give unit diagonal.

If k is even, take unit vectors u_i = (-1)^i in R (with any consistent parity indexing). Consecutive vectors, including the wrap-around pair, have inner product -1. Their Gram matrix Q is positive semidefinite, has unit diagonal, and has alpha = 1 > 0. Hence

m_{C_k}(X) = S/k <= 1/2.

If k is odd, then k >= 5. Set theta = (k-1) pi/k and assign to vertex i the vector u_i = (cos((i-1) theta), sin((i-1) theta)) in R^2, for i = 1,...,k. Consecutive inner products equal cos(theta) = -cos(pi/k). For the wrap-around pair, the angle difference is (k-1)theta = (k-2)pi + pi/k; since k-2 is odd, its cosine is also -cos(pi/k). Thus the Gram matrix is positive semidefinite with unit diagonal and alpha = cos(pi/k) > 0, and

m_{C_k}(X) <= 1/(2 cos(pi/k)).

These inequalities hold for every X in C(C_k). If t exceeds the applicable bound, no such X can satisfy m_{C_k}(X) >= t, so the threshold-feasible set F_t(C_k) is empty.
