# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes that attaining Bayes risk is equivalent to the almost-sure factorization `g(X_0,Z) beta=m_t(X_0,Z)`, using the conditional-mean squared-error decomposition or an equivalent valid argument.
- **3 points:** Uses the anchoring condition `B_t beta=I_d` and the assumed invertibility of `B_t` to obtain uniquely `beta=B_t^{-1}`. A direct argument suffices; a preliminary characterization of all Bayes-optimal factorizations is optional.
- **3 points:** Combines conditional-mean recovery with the fixed decoder to obtain `g=m_t B_t` almost surely, and correctly identifies this with `h_t=E[X_tB_t|X_0,Z]` by linearity of conditional expectation.
- **2 points:** Verifies that `(h_t,B_t^{-1})` satisfies the anchoring condition and attains Bayes risk, and concludes uniqueness among all anchored pairs, up to almost-sure equality of the preprocessor.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its optional characterization of unanchored pairs. In particular, a proof may impose anchoring first, deduce `beta=B_t^{-1}`, and then identify `g` directly from Bayes optimality. Such a proof deserves full credit without using the covariance assumption or deriving `g=m_t(B_t beta)^{-1}B_t` for general decoders.

If a solver chooses to establish the general unanchored characterization, evaluate that argument for correctness, but do not require it or its converse for the stated anchored theorem. Existence of the claimed anchored pair must be justified, either explicitly by substitution or by an equivalent argument already establishing its anchoring and Bayes optimality. Do not confuse this existence obligation with the optional converse for all unanchored factorizations.

The squared-error decomposition may be established for finite-risk predictions, which suffices for Bayes-optimal candidates, or as an identity of extended nonnegative risks. Do not require square-integrability of every measurable candidate preprocessor. Uniqueness concerns the decoder matrix and almost-sure equality of the preprocessor evaluated at `(X_0,Z)`, not equality at every possible input.
