# Reference Proof

## Proof Structure

1. Check that the stated measurable and integrable objects support the expectations used below.
2. Unroll the pathwise contractivity recursion from zero initial discrepancy to obtain a terminal bound by the certificate.
3. Transfer this predictor discrepancy to a pointwise loss difference, then average over the shared randomness and use the neighboring-dataset supremum to obtain the stability bound.
4. Use an independent replace-one sample and exchangeability to convert the expected population-to-empirical risk gap into an average neighboring loss difference, and apply the stability bound. Handle unchanged replacements separately.

## Source-local Correction

The source proof of the stability-to-generalization lemma contains incorrect intermediate equalities at L000408 and L000410. In particular, L000410 reverses the sign of the correct replace-one identity. The proof below uses the direct exchange of the original and replacement examples, as already done in the previous reference proof. The absolute stability hypothesis controls the resulting difference, so the source statement and the final conclusion require no change. This local source repair is recorded under theory_009.

## Complete Proof

The measurable learner, discrepancy and coefficient maps make each coupled discrepancy and each fixed-pair certificate measurable: they are compositions and finite sums and products of measurable functions. The measurability of the dataset-level supremum is a separate public assumption, not a consequence asserted from fixed-pair measurability. Its integrability gives E_S gamma_T(S)=L E_S C_T(S)<infinity.

The public loss assumptions imply that the terminal population risk and each terminal training loss are integrable under (S,U). Indeed, |R(h_T(S,U))| is at most the integral of |ell(h_T(S,U),z)| against P. These same assumptions permit the independent-test-sample and exchangeability calculations below by Fubini's theorem. At a fixed neighboring pair, integrability of the loss difference over U will also follow directly from its integrable certificate bound; separate integrability of the two fixed-dataset losses over U is not needed.

Fix a neighboring pair S~S' and a realization of U. In this paragraph all coefficients are evaluated at (S,S';U). Define C_0=0 and, for t>=1,

C_t = sum_{j=0}^{t-1} (prod_{k=j+1}^{t-1} a_k)b_j.

Since D_0=0 and D_{t+1}<=a_t D_t+b_t, induction gives D_t<=C_t for every t. The base case is immediate. If D_t<=C_t, nonnegativity of a_t and the definition of C_{t+1} give

D_{t+1} <= a_t C_t+b_t = C_{t+1}.

For t=0 the last equality reads C_1=b_0; for later t it follows by separating the final summand. Thus D_T<=C_T(S,S';U) pathwise.

By loss domination, for every example z,

|ell(h_T(S,U),z)-ell(h_T(S',U),z)| <= L D_T <= L C_T(S,S';U).

The fixed-pair certificate is integrable over U. Taking expectation and using |E X|<=E|X|, followed by the supremum over z, gives

sup_z |E_U[ell(h_T(S,U),z)-ell(h_T(S',U),z)]|
<= L E_U[C_T(S,S';U)]
<= L sup_{S''~S} E_U[C_T(S,S'';U)]
= gamma_T(S).

This proves the asserted stability inequality for every neighboring pair. The neighbor supremum remains outside the expectation throughout.

For expected generalization, fix an index i. Let z_i' have law P independently of (S,U), and let S^(i) be S with its ith coordinate replaced by z_i'. Independence and the stated integrability imply

E_{S,U}[R(h_T(S,U))-Rhat_S(h_T(S,U))]
= (1/n) sum_i E_{S,z_i',U}[ell(h_T(S,U),z_i')-ell(h_T(S,U),z_i)].

Swapping z_i and z_i' preserves their joint law with all other sample coordinates and U. Under this swap, (S,z_i') becomes (S^(i),z_i). Consequently,

E_{S,z_i',U}[ell(h_T(S,U),z_i')]
= E_{S,z_i',U}[ell(h_T(S^(i),U),z_i)],

and hence

E_{S,U}[R(h_T(S,U))-Rhat_S(h_T(S,U))]
= (1/n) sum_i E_{S,z_i',U}[ell(h_T(S^(i),U),z_i)-ell(h_T(S,U),z_i)].

For fixed S and z_i', if S^(i) differs from S, it is a neighbor. The stability inequality anchored at S bounds the absolute value of the U-averaged difference in the last display by gamma_T(S). If z_i'=z_i, then S^(i)=S, and the coupled loss difference is exactly zero, also at most gamma_T(S). This argument is pointwise in the sample and replacement and requires no claim that a replacement differs almost surely.

Averaging over S and z_i', then over i, proves

E_{S,U}[R(h_T(S,U))-Rhat_S(h_T(S,U))] <= E_S[gamma_T(S)].

All arguments hold for n=1 and T=1. If there are no neighbors, the first assertion is vacuous and the certificate is zero by convention; every replacement is unchanged, so the same argument gives zero expected gap. No contraction restriction a_t<1, metric axiom, interpolation condition or adaptedness hypothesis is used.

## Obligation Closure

- Measurability and expectation interchanges: justified by the explicit public regularity assumptions, composition, finite sums and products, and Fubini's theorem for the integrable loss variables.
- Terminal discrepancy control: proved by the displayed finite induction.
- Uniform loss stability: proved by pointwise domination, integration of the fixed-pair certificate, and the dataset-level supremum.
- Expected generalization: proved by the explicit independent replacement and correct exchangeability identity, including unchanged replacements.

There are no unresolved proof obligations and no unclosed external dependency.
