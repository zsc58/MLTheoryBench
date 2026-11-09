# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Analytic polynomial approximation and error control (2 points).** Establishes a finite polynomial approximation of the analytic class with quantitative uniform error, degree, and number-of-terms bounds sufficient for the claimed rate. In the reference route, this includes normalized tensor Legendre coefficients, coefficient summability, and the exponential tail on the weighted-degree index set. The public task does not grant the truncation theorem as an assumption. An unexplained invocation of the specialized truncation result is not a completed derivation. A valid alternative analytic approximation argument receives full credit.

2. **Polynomial ReLU realization (3 points).** Quantitatively constructs the required powers, polynomial features, and coordinate products. Verifies multiplication domains, internal error propagation, and width and depth. In the reference route, blockwise polynomial realization and a shared-feature construction produce the two complementary balances. A standard bounded-domain multiplication theorem may be used with its relevant statement and verified hypotheses. Naming a paper-specific construction without its quantitative justification does not close this step. Exact constant and affine cases, low coordinate degrees, and the one-dimensional product must be handled wherever they affect the proof.

3. **Weighted summation architecture (2 points).** Implements the complete weighted sum with controlled architecture and error. In the reference route, signed identity channels transport inputs or shared features and the accumulated scalar; affine additions are exact. The final partial block is handled, and coefficient summability controls total approximation error. Clipping is neither required nor part of the source's sequential accumulation argument. A different correct summation architecture is acceptable.

4. **Width-depth optimization (2 points).** Derives sufficient intermediate width-depth-error estimates and performs the parameter rescalings explicitly. Checks the lower width constraint and the upper logarithmic constraint, integer rounding, the separate kappa=0 case allowing alpha=0, and the kappa=d logarithmic depth factor. Preserves the stated constant dependencies: architecture constants cannot acquire dependence on kappa or alpha merely through logarithmic absorption; thresholds may depend on fixed regime parameters.

5. **Final assembly (1 point).** Obtains the stated piecewise tau, verifies the endpoints and dimension-one case, selects the stronger applicable estimate on overlaps, and combines analytic and network errors. Establishes uniformity over the analytic class and all stated width, depth, and error bounds.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental basis, architecture, presentation, or numerical constants. The two construction estimates in the reference proof are conclusions to be justified, not additional public assumptions. The reference proof now supplies their derivations and the analytic truncation derivation; there are no disclosed unresolved reference-proof obligations.

A source citation alone does not establish a theorem-critical specialized construction. Conversely, a solver need not reproduce an independently standard multiplication theorem after stating it accurately and checking its hypotheses. Award credit for correctly closed obligations rather than for matching named source lemmas.

Propagate a missing analytic approximation or optimization dependency only when the final bound is unsupported; theorem-critical quantitative gaps remain major. A cosmetic typo or an omitted routine case warrants only a small deduction if the correct repair is immediate and does not alter the claimed regime or architecture. Do not accept a proof that actually loses the rate at d=1, uses a nondecaying multiplication-error bound, silently assumes alpha>0 when kappa=0, or introduces prohibited constant dependencies.
