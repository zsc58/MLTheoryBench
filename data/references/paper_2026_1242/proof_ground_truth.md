# Reference Proof

## Proof Structure

We show both directions. First, matrices of the form `alpha I_C + beta 11^T` commute with every permutation matrix. Conversely, commutation with permutations implies invariance of matrix entries under simultaneous relabeling of row and column indices; transpositions then force one common diagonal value and one common off-diagonal value. Rewriting those two values gives the claimed form and coordinate update.

## Complete Proof

Let `P_pi` be the permutation matrix associated with `pi`. Suppose first that `M = alpha I_C + beta 11^T`. Every permutation matrix commutes with `I_C`. Moreover, `P_pi 1 = 1` and `1^T P_pi = 1^T`, so `P_pi 11^T = 11^T P_pi`. Hence `P_pi M = M P_pi` for every `pi`.

Conversely, assume `M P_pi = P_pi M` for every permutation `pi`. Since `P_pi^{-1}=P_pi^T`, multiplying the commutation relation by `P_pi^{-1}` gives `P_pi M P_pi^{-1}=M`. In entries, this says

`M_{i,j} = M_{pi(i),pi(j)}`

for every `i,j` and every permutation `pi`. In particular, using transpositions (which generate the symmetric group), any ordered pair `(i,i)` can be sent to any other diagonal pair `(k,k)`, so all diagonal entries equal a common value `d`. Likewise, any ordered pair `(i,j)` with `i != j` can be sent to any other ordered pair `(k,l)` with `k != l`, so all off-diagonal entries equal a common value `o` (the assertion is vacuous when `C=1`). Therefore, for `C >= 2`,

`M = (d-o) I_C + o 11^T`.

Setting `alpha=d-o` and `beta=o` yields the required representation. For `C=1`, the same representation holds by taking, for example, `alpha=M_{1,1}` and `beta=0`.

Finally, for any `h in R^C`, the `c`-th coordinate of the coupled update is

`(M h)_c = alpha h_c + beta sum_{j=1}^C h_j`.

Thus the coupling is exactly a local self-term plus a global pooled interaction, and the two characterizations are equivalent.
