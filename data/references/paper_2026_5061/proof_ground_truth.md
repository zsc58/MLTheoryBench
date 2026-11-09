# Reference Proof

## Proof Structure

Use the positive-definite empirical covariance of the full-column-rank design to obtain a whitening factor. Express the least-squares coefficient through that factor, then identify all five Transformer parameters and verify the forward-pass algebra exactly.

## Complete Proof

Let (1/n) A^T A = V Lambda V^T be an eigendecomposition, where V is orthogonal and Lambda is diagonal with strictly positive entries. Define L = V Lambda^(-1/2). Then

(1/n) L^T A^T A L = I_d,

and

(A^T A)^(-1) = (1/n) L L^T.

Define p = (1/n) L^T A^T y. The least-squares coefficient is therefore

beta = (A^T A)^(-1) A^T y = (1/n) L L^T A^T y = L p,

so the least-squares prediction is A beta = A L p.

Choose the Transformer parameters

W_Q = L,  W_K = L,  W_V = L,  W_FFN = I_d,  W_P = p.

Substitution into the specified linear-attention map gives

(1/n)(A L)(A L)^T(A L) I_d p
 = A L[(1/n)L^T A^T A L]p
 = A L p.

By the preceding coefficient calculation, A L p = A(A^T A)^(-1)A^T y. Thus these explicitly constructed parameters make one forward pass exactly equal to the ordinary least-squares projection.
