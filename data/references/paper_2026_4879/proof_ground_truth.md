# Reference Proof

## Proof Structure

Normalize the nonzero magnitudes of `x` to a probability distribution on its support. Express Shannon entropy and Renyi entropy by expanding their divergences from the uniform distribution on that support, then exponentiate. Nonnegativity of the two divergences gives the support-size bounds. Finally, take the standard limiting orders of the Renyi entropy.

## Complete Proof

Let `S=Supp(x)`, `k=|S|`, and let `u` be uniform on `S`, so `u_i=1/k` for `i in S`. Since `x != 0`, `k>=1` and `pi` is a probability distribution on `S`.

For Shannon entropy,
`D_KL(pi||u) = sum_{i in S} pi_i log_2(pi_i/u_i)`.
Substituting `u_i=1/k` and using `sum_i pi_i=1` gives
`D_KL(pi||u) = sum_i pi_i log_2 pi_i + log_2 k = log_2 k - H(x)`.
Therefore
`H(x)=log_2 k-D_KL(pi||u)`.
Exponentiating base 2 yields
`ENZ(x)=2^{H(x)}=k 2^{-D_KL(pi||u)}`.
KL nonnegativity gives `ENZ(x)<=k`. Equality holds exactly when `D_KL(pi||u)=0`, equivalently `pi=u`, which means all nonzero magnitudes `|x_i|` are equal.

For `alpha>0`, `alpha!=1`, define
`R_alpha(x)=(1/(1-alpha))log_2(sum_{i in S} pi_i^alpha)`
and
`D_alpha(pi||u)=(1/(alpha-1))log_2(sum_{i in S} pi_i^alpha u_i^{1-alpha})`.
Because `u_i=1/k`,
`sum_i pi_i^alpha u_i^{1-alpha}=k^{alpha-1}sum_i pi_i^alpha`.
Hence
`D_alpha(pi||u)=log_2 k+(1/(alpha-1))log_2(sum_i pi_i^alpha)=log_2 k-R_alpha(x)`.
Thus
`ENZ^R_alpha(x)=2^{R_alpha(x)}=k 2^{-D_alpha(pi||u)}`.
Renyi-divergence nonnegativity gives `ENZ^R_alpha(x)<=k`.

The expression `pi_i=|x_i|/||x||_1` is unchanged when `x` is multiplied by any nonzero scalar, so all these sparsity quantities are scale invariant. The continuous Renyi limit at order `alpha->1` is Shannon entropy: applying l'Hopital's rule to `log(sum_i pi_i^alpha)/(1-alpha)` gives `-sum_i pi_i log_2 pi_i=H(x)`. Since every `pi_i>0` on `S`, as `alpha downarrow 0`, `sum_i pi_i^alpha->k`, so `R_alpha(x)->log_2 k` and `ENZ^R_alpha(x)->k`.
