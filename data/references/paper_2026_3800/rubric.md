# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the defined natural-only and augmented matrices \(\Sigma_0\) and \(\Sigma_U\), their reported-coordinate forms \(S\Sigma_0S^T\) and \(S\Sigma_US^T\), and the population GLS interpretation. A direct matrix proof starting from the definitions in the task satisfies this item. Deriving the GLS estimators and their error-covariance identities is valid supporting work, but is not an additional requirement for full credit.
- **3 points:** Establishes covariance non-deterioration. The reference route performs the block inverse/Schur-complement calculation to show \(H^TW^{-1}H=S^TW_{yy}^{-1}S+MT^{-1}M^T\), establishes the relevant positive definiteness and positive semidefiniteness, and uses inverse Loewner order. Award the same credit for another complete valid comparison argument.
- **3 points:** In the scalar-direction case, correctly uses \(\tau\), \(\tilde u\), and \(x\), and derives the exact gain quotient by a rank-one inverse identity or equivalent decisive algebra.
- **2 points:** Correctly connects the covariance difference to the target-weighted trace risk, proves the strictly positive denominator and nonnegative gain, and explicitly limits the conclusion to covariance risk under the given population GLS assumptions rather than bias-inclusive MSE or finite-sample test loss.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, a particular named matrix identity, or a separate derivation of covariance formulas already supplied as definitions. Allocate points by the mathematical obligations established, rather than by literal reproduction of the reference route.

The single-direction domain is \(u^TDu=1\) for a fixed symmetric positive-definite \(D\). Do not require \(D=I\), assume the frozen oracle is scale invariant, or impose independence or zero-mean residuals. The normalization need not appear in the inversion algebra beyond specifying the candidate domain.

The conclusion is non-strict: \(Q=0\), singular \(Q\), a zero adjusted direction, and rank-deficient information updates are permitted. A proof must not divide by a quantity that can vanish, but need not give separate cases when its argument already covers them.

Deduct for treating the claim as a finite-sample or bias-inclusive MSE guarantee, using an inverse without establishing or invoking its required hypotheses, or merely naming Schur complements/Woodbury without supplying the decisive identity or argument. Do not deduct merely for failing to restate assumptions already given in the task when their use is mathematically valid.
