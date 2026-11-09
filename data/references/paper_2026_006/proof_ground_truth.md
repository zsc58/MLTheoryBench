# Reference Proof

## Proof Structure

First reduce the transformed spectral representation to a diagonal sign similarity and compare every principal minor. Next differentiate the finite normalized likelihood to obtain the score as a centered trace map. Finally identify the zero-score space as the inverse image of the constant vectors, use the scale direction to compute the rank of the restricted map, and apply rank-nullity and the codomain dimension bound. The final local conclusion concerns infinitesimal, zero-score directions.

## Complete Proof

For the invariance statement, use Q Lambda Q^T = Lambda:

M = (D U Q)(c Lambda)(D U Q)^T
  = c D U Q Lambda Q^T U^T D
  = c D U Lambda U^T D
  = c D L D.

The matrix M is symmetric positive semidefinite because c>0 and DLD is a congruence of L. For A in X_k, let D_A be the principal submatrix of D. Then

 det(M_A) = c^k det(D_A L_A D_A)
           = c^k det(D_A)^2 det(L_A)
           = c^k det(L_A),

because every diagonal entry of D_A is plus or minus one. Summing over all A in X_k gives Z_k(M) = c^k Z_k(L)>0. Therefore M is in the k-DPP domain and

 P_M^k(A) = det(M_A)/Z_k(M) = det(L_A)/Z_k(L) = P_L^k(A)

for every A. This simultaneously establishes invariance under common positive eigenvalue scaling, diagonal sign similarity, and every orthogonal change of basis Q commuting with Lambda. The eigenspace change Q alone leaves the reconstructed kernel unchanged.

Now assume L is positive definite. Every principal submatrix L_A is then positive definite. For H in Sym(N), positive definiteness persists for all sufficiently small t, so the directional score is well-defined. All the probabilities appearing in the logarithms are positive. The log likelihood is

 log P^k_{L+tH}(A) = log det((L+tH)_A) - log Z_k(L+tH).

For positive-definite A and symmetric B, the standard log-determinant derivative is

 d/dt log det(A+tB) at t=0 = tr(A^{-1}B).

Applying this to L_A and H_A gives

 d/dt log det((L+tH)_A) at t=0 = tr(L_A^{-1} H_A).

Since the normalizer is a finite sum of positive differentiable terms,

 d/dt log Z_k(L+tH) at t=0
 = [sum_{B in X_k} det(L_B) tr(L_B^{-1} H_B)] / Z_k(L)
 = sum_{B in X_k} P_L^k(B) tr(L_B^{-1} H_B)
 = E_{B ~ P_L^k}[tr(L_B^{-1} H_B)].

Consequently,

 S_H(A;L) = tr(L_A^{-1} H_A)
            - E_{B ~ P_L^k}[tr(L_B^{-1} H_B)].

Thus S_H(A;L)=0 for every A exactly when the values tr(L_A^{-1}H_A) are all equal to one common constant (their expectation).

Define the linear map Phi: Sym(N) -> R^{X_k} by

 Phi(H) = (tr(L_A^{-1}H_A))_{A in X_k},

and let 1 denote the all-ones vector. The preceding equivalence says that the zero-score space is

 V_L = Phi^{-1}(R 1).

In particular, V_L is a vector subspace. Let m = N(N+1)/2. The matrix direction H=L satisfies Phi(L)=k 1, since L_A^{-1}L_A is the k by k identity. Because k>=1, Phi restricted to V_L has image exactly R 1 and rank one. Its kernel is ker(Phi), so finite-dimensional rank-nullity applied to this restriction yields

 dim(V_L) = dim(ker Phi) + 1
          = m - rank(Phi) + 1.

Because Phi has one coordinate for each k-subset, rank(Phi) <= |X_k| = binom(N,k). Therefore

 dim(V_L) >= N(N+1)/2 - binom(N,k) + 1.

Finally, H=L is the tangent direction to the positive scaling curve (1+t)L, so span{L} is contained in V_L. This span has dimension one because L is positive definite and hence nonzero. If binom(N,k) < N(N+1)/2, the displayed lower bound is strictly larger than one. Hence V_L contains directions outside span{L}, proving the asserted additional infinitesimal non-identifiability.

This last conclusion concerns first derivatives of the law at L. It neither requires nor asserts that each zero-score direction is tangent to an exact constant-law curve, or that L+tH has the same law for nonzero t.
