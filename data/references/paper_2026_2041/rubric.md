# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Uses the conditional population energy-score objective and correct specification. Applies strict propriety on its finite-first-moment domain and explains why the integrated nonnegative conditional excess risk is zero for every population minimizer, yielding conditional-law recovery almost everywhere. A correctly stated standard strict-propriety theorem may be cited; its proof need not be reproduced.
- **4 points:** Uses both structural and generator independence to factor the conditional noisy laws, cancels the nowhere-zero noise characteristic function, and invokes uniqueness of characteristic functions to recover the de-noised conditional law. A single full-column-rank matrix must work almost everywhere; taking tilde A=A is sufficient. Subtraction must reuse the added generator draw. Merely naming deconvolution, or subtracting noise from equality of marginal laws, is insufficient.
- **2 points:** Shows that the full-column-rank transformation has a measurable inverse on its image, or uses its continuous linear left inverse, and hence gives equal confounder sigma-algebras. Establishes equality of the outcome regressions in the two coordinate systems with the stated fixed-treatment version convention.
- **1 point:** Uses the structural intervention semantics or a correctly applied adjustment formula, with absolute integrability, to integrate the regression against the marginal confounder law and conclude the formula for every stipulated treatment value.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Missing arguments should affect the corresponding recovery or transform-recovery points; award adjustment points when that conclusion is independently established.

The score's first-moment conditions are conditional; do not require an additional unconditional first moment of W or a uniform moment bound. Do not require a Lebesgue density for AU or Z when d>k. The conditional-law equality in part 1 is almost everywhere, while part 2 uses the explicitly specified structural-model versions for each fixed treatment value. Equality of observational conditional expectations almost surely, or positivity of a treatment density, alone does not settle arbitrary versions on null treatment slices. Do not reward an argument that incorrectly asserts otherwise.

The recovered generator signal need not equal the original latent signal samplewise. The conclusion is distributional. No proof of the separate bounded-completeness theorem, no bounded-posterior assumption, and no claim that tilde A differs from A is required. The outer expectation in the adjustment formula is with respect to the marginal law of Z, not P(Z|X=x).
