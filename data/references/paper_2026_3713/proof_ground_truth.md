# Reference Proof

## Proof Structure

We verify that the paired randomizer preserves real-valued signals, has unit-modulus diagonal entries, and has zero-mean entries. We also verify finite second moments. For a zero-mean DGWSS random input, independence permits a conditional covariance calculation, and the diagonal spectral covariance is unchanged by this randomizer. For a fixed observed real signal, the surrogate has zero mean; we compute every entry of its randomized spectral covariance, including the conjugate-pair case.

## Complete Proof

Write `r_n = R_nn`. Every `r_n` has modulus one. A Rademacher sign has mean zero, and for `q = 1, 2, -1, -2`, a uniform phase satisfies

`E[exp(i q Psi)] = (1/(2 pi)) integral_{-pi}^{pi} exp(i q t) dt = 0`.

In particular, `E[R] = 0` entrywise.

Let `||B||_op` denote the matrix norm induced by the Euclidean vector norm. For every vector `v` and every realization of `R`,

`||U R U^{-1}v||_2 <= ||U||_op ||U^{-1}||_op ||v||_2`,

because `R` preserves the Euclidean norm in the spectral coordinates. Therefore the surrogate of a finite-second-moment input has finite second moments. This also applies to every fixed observed vector.

The construction preserves real-valuedness. Indeed, if `a = U^{-1}v` for a real vector `v`, then `a` is real on real-eigenvalue indices and has conjugate coordinates on paired indices. Consequently `b = R a` has the same properties. In the expansion `U b`, a real-eigenvalue contribution is real, and the contribution from a conjugate pair is

`u_n b_n + conjugate(u_n) conjugate(b_n) = 2 Re(u_n b_n)`.

Thus `U R U^{-1}v` is real. This argument applies to each real realization of a random input as well.

Now let `X` be DGWSS and let `R` be independent of `X`. By definition, `E[X] = 0` and `X` has finite second moments. Put `a_X = U^{-1}X`. Then `E[a_X] = 0`, and

`D_X = E[a_X a_X^H] = U^{-1}H_X U^{-H}`

is diagonal, with `H_X = U D_X U^H`.

Independence gives

`E[Z_X] = U E[R] E[a_X] = 0`.

Thus its covariance equals its second moment. For `Z_X = U R a_X`,

`H_{Z_X} = U E[R a_X a_X^H R^H] U^H`.

Conditioning on `R` and using independence yields

`H_{Z_X} = U E_R[R D_X R^H] U^H`.

Both `R` and `D_X` are diagonal, and every diagonal entry of `R` has modulus one. Hence

`R D_X R^H = D_X`

for every realization of `R`. Therefore

`H_{Z_X} = U D_X U^H = H_X`.

Together with zero mean and finite second moments, this proves that `Z_X` is DGWSS. The preceding conjugacy argument also shows that it is real almost surely.

Next fix an observed real vector `m` and put `a = U^{-1}m`. For `Z_m = U R a`,

`E[Z_m] = U E[R] a = 0`.

Consequently its covariance equals its second moment, and its spectral covariance is

`U^{-1}H_{Z_m}U^{-H} = E[R a a^H R^H]`.

The `(n,k)` entry equals

`E[r_n conjugate(r_k)] a_n conjugate(a_k)`.

For `n = k`, the multiplier is one. For distinct real-eigenvalue indices, the independent Rademacher signs give expectation zero. For indices belonging to distinct nonreal conjugate pairs, the entries depend on independent representative phases and each entry has mean zero, so the expectation again vanishes. Mixed sign/phase cases also factor into zero-mean expectations by independence.

If `k` is the conjugate partner of `n`, then `r_n conjugate(r_k)` is either `exp(2 i Psi)` or `exp(-2 i Psi)`. Both have expectation zero by the uniform-phase calculation above. These cases exhaust all distinct indices. Thus

`E[r_n conjugate(r_k)] = 1` when `n = k`, and `0` otherwise.

Consequently,

`E[R a a^H R^H] = diag(|a_1|^2, ..., |a_N|^2)`,

so

`H_{Z_m} = U diag(|(U^{-1}m)_1|^2, ..., |(U^{-1}m)_N|^2) U^H`.

The surrogate is real almost surely by the conjugacy argument, has zero mean and finite second moments, and has diagonal spectral covariance. It is therefore DGWSS. Both required claims follow.

The argument also covers the zero observed vector, zero spectral powers, repeated eigenvalues in the fixed paired eigenbasis, and the cases with no real indices or no nonreal pairs. No invertibility of the graph shift, orthogonality of `U`, positive spectral powers, or realization-wise energy preservation is required.
