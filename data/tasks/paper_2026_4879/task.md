# Problem

## Setup

Let `n>=1` and let `x in R^n` be nonzero. Write `S={i:x_i!=0}` and `k=|S|`. Define the normalized magnitude distribution on `S` by
`pi_i=|x_i|/||x||_1`.

All logarithms are base 2, and `0 log_2 0` is defined as `0`. Define Shannon entropy and Shannon effective number of nonzeros by
`H(x)=-sum_{i in S} pi_i log_2 pi_i`, `ENZ(x)=2^{H(x)}`.

Let `u` be the uniform distribution on `S`, `u_i=1/k`. For strictly positive probability distributions `p` and `q` on `S`, define
`D_KL(p||q)=sum_{i in S} p_i log_2(p_i/q_i)`.
For `alpha>0`, `alpha!=1`, define
`R_alpha(x)=(1/(1-alpha))log_2(sum_{i in S} pi_i^alpha)`,
`ENZ^R_alpha(x)=2^{R_alpha(x)}`, and, for strictly positive probability distributions `p` and `q` on `S`,
`D_alpha(p||q)=(1/(alpha-1))log_2(sum_{i in S} p_i^alpha q_i^{1-alpha})`.

## Task

Prove the following integrated theorem. For every nonzero `x`,
`H(x)=log_2 k-D_KL(pi||u)` and
`ENZ(x)=k 2^{-D_KL(pi||u)}<=k`, with equality if and only if all nonzero magnitudes `|x_i|` are equal. Moreover, for every `alpha>0`, `alpha!=1`,
`R_alpha(x)=log_2 k-D_alpha(pi||u)` and
`ENZ^R_alpha(x)=k 2^{-D_alpha(pi||u)}<=k`.

Show also that these quantities are invariant under nonzero rescaling of `x`, that `R_alpha(x)` converges to `H(x)` as `alpha->1`, and that `R_alpha(x)` converges to `log_2 k` (equivalently `ENZ^R_alpha(x)` converges to `k`) as `alpha` decreases to `0`.
