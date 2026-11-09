# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct core step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Descent and stochastic conditioning:** Uses the correct normalization and update. Conditions after the score update but before the fresh gradient minibatch, so the preconditioner is measurable and the gradient is conditionally unbiased. Establishes a valid Robbins–Siegmund inequality for a nonnegative shift of the objective, verifies summability from beta<alpha-1/2, and obtains objective convergence, weighted-gradient summability, and squared-step summability.

- **3 points — Adaptive Fisher spectral control:** Controls products of differentiated-retraction transports using their second-order near-isometry and squared-step summability. Uses the one-step centered-operator recursion with the pre-score filtration, rather than incorrectly treating future-transported summands as martingale differences. Proves that the centered residual vanishes and that the normalized Fisher approximation is bounded above. For the local result, also establishes a strictly positive lower spectral bound using positivity of the Fisher operator at the limit and a justified local lower-bound argument. Global positive definiteness of the Fisher operator is not available as an assumption.

- **3 points — Local rate:** Derives a valid local chart recursion and handles the adaptive noise with the stated higher moments. Establishes contraction in a justified norm; the fixed Hessian norm is one valid choice. Does not infer baseline-norm contraction from positive spectra alone. Uses only the gradient remainder justified by the assumptions, namely o(||Delta||), unless a stronger remainder is independently proved. Closes the adaptive stochastic-convolution estimate and the nonlinear/geometric remainder estimate, obtaining the exact max rate for every delta>0 and the alpha>2/3 specialization. The reference proof supplies a complete truncation/blocking/summation-by-parts route, but another valid derivation is acceptable.

- **2 points — Global conclusions and convex case:** Derives the minimum-gradient little-o rate from weighted summability and a tail-block argument. In the geodesically strictly convex case, justifies convergence of the objective gap to zero and then convergence of the iterates to the unique minimizer, using the compact iterate set and continuity or another valid argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's decomposition, coordinates, block lengths, or incidental notation.

The following are not valid completed steps: applying Robbins–Siegmund directly to an objective difference whose nonnegativity is unproved; moving the updated preconditioner outside a conditional expectation taken before the score draw without further justification; reversing the Fisher normalization; assuming global Fisher conditioning; assuming a Lipschitz Hessian; or asserting contraction in the baseline norm merely because both factors are positive definite.

A theorem-critical omission of spectral control or the adaptive stochastic rate is a major gap. A fixed-coefficient stochastic-convolution theorem cannot be applied to future-dependent random product weights solely because their norms satisfy a contraction bound. A solver must verify the relevant hypotheses or derive a suitable estimate. Merely naming martingale concentration or a specialized stochastic-approximation method does not close this obligation.

The reference proof repairs the source's quadratic Taylor-remainder claim by absorbing an o(||Delta||) drift. Do not demand the unsupported quadratic estimate as a grading requirement. Retraction Taylor remainders may be handled by integral formulas or equivalent uniform bounds. Logarithmic exponents may be reparameterized because the result is required for every positive delta.

There is no unresolved reference-proof obligation and no private ground-truth quality warning.
