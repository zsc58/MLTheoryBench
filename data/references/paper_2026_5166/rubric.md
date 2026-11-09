# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly differentiates the energy and the prescribed surrogate, proves strict negative surrogate curvature, and derives the first component's finite mean and strictly positive precision by completing the quadratic. Establishes the associated Gaussian's variance as the reciprocal precision, either directly or using correctly stated elementary Gaussian facts.
- **3 points:** Computes the pointwise limiting energy with r and m fixed, derives its stationarity equation, and obtains the explicit secondary location through the positive inverse of v exp(v), equivalently the principal Lambert-W branch. Establishes uniqueness and finiteness. Derives the second component using the full slope and the selected ordinary-or-fallback precision, proving positivity in both branches and covering zero full curvature without evaluating an undefined Newton quotient.
- **4 points:** Derives the normalized exponential-energy weights and their strict energy ordering, including equal-energy weights. Derives the mixture mean and second moment or variance, including the between-component contribution. Establishes finite strictly positive mixture variance and reciprocal precision, and verifies that the final Gaussian has the mixture's first two raw moments. The argument must remain valid for coincident component means and for either unimodal or bimodal energies.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental notation or presentation choices. An explicitly defined inverse equivalent to the positive principal Lambert-W branch is acceptable; leaving the secondary location only as an unsolved equation does not fulfill the explicit-expression requirement.

The public construction specifies which approximation is required. A different curvature regularization, a different secondary point, or weights modified by component normalization factors are not equivalent answers merely because they also produce positive precision.

A solution that omits the nonpositive-curvature branch, uses the unreplaced curvature in the second mean after selecting the fallback, merely names Lambert W without deriving the limiting stationarity equation, or asserts positive mixture variance without establishing valid positive component precisions has a theorem-critical gap. The component precisions must be selected before their associated means are evaluated.

Do not require the secondary point or its corrected mean to be an exact stationary point of the original energy. Do not require a small-a assumption, a test for the existence of two modes, equality with the moments of the original normalized exponential, or a quantitative posterior-approximation bound. None is part of the public claim.

Energy ordering determines which weight is greater, not that the greater weight is arbitrarily close to one. If limiting dominance is discussed, a diverging energy gap justifies the corresponding weight limit. Do not require, or credit as established without additional justification, convergence of mixture means or variances along arbitrary changing-parameter sequences merely from a weight tending to zero or one.

All theorem-critical reference-proof obligations are closed; no scoring step relies on an undisclosed specialized result.
