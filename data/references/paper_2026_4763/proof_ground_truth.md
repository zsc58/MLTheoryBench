# Reference Proof

## Proof Structure

1. Show that any Bayes-optimal preprocess-then-linear pair must satisfy the exact conditional-mean factorization `g(X_0,Z) beta = m_t(X_0,Z)` almost surely.
2. Use nonsingularity of `Cov(m_t)` to prove that `beta` is invertible, then derive the complete family of such factorizations.
3. Apply the anchoring equation `B_t beta = I_d` to collapse that family to the unique pair and identify its preprocessor with `h_t`.

## Complete Proof

Let `m=m_t(X_0,Z)=E[X_t|X_0,Z]`. For any measurable `g` and matrix `beta`, conditional expectation gives

`E[||X_t-g beta||_2^2] = E[||X_t-m||_2^2] + E[||m-g beta||_2^2]`,

because `E[X_t-m|X_0,Z]=0`. Hence a pair is Bayes-optimal (attains the Bayes risk) if and only if `g beta=m` almost surely.

Suppose therefore that `g beta=m` almost surely. Since `Cov(m)` is invertible, `beta` cannot be singular: if `beta u=0` for some nonzero vector `u`, then `m u=g beta u=0` almost surely, which contradicts positive variance in every nonzero direction implied by invertibility of `Cov(m)` (the variables are centered). Thus `beta` is invertible. Consequently `g=m beta^{-1}` almost surely.

The matrix `B_t` is invertible by assumption, so `B_t beta` is invertible. Since `(B_t beta)^{-1}B_t=beta^{-1}`, we obtain the equivalent representation

`g=m (B_t beta)^{-1} B_t` almost surely.

Conversely, if `B_t beta` is invertible and `g=m (B_t beta)^{-1}B_t`, then

`g beta = m (B_t beta)^{-1} B_t beta = m`,

so the pair is Bayes-optimal. This establishes the full coordinate family needed here.

Now impose the anchoring condition `B_t beta=I_d`. Left-multiplication by `B_t^{-1}` yields uniquely `beta=B_t^{-1}`. Substitution into the representation gives `g=m B_t` almost surely. Because `B_t` is deterministic, linearity of conditional expectation gives

`m B_t=E[X_t|X_0,Z]B_t=E[X_t B_t|X_0,Z]=h_t(X_0,Z)`.

Therefore every anchored Bayes-optimal pair equals `(h_t,B_t^{-1})` almost surely. Finally, this pair is indeed Bayes-optimal, since `h_t B_t^{-1}=m B_t B_t^{-1}=m`. Hence it is the unique anchored Bayes-optimal preprocess-then-linear factorization.
