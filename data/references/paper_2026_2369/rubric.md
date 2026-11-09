# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derive the stationary weak-generator identity with a consistent gradient convention, including the integration-by-parts cancellation and the required regularity and boundary justifications.
- **2 points:** Differentiate the observed semigroup correlation, convert the Koopman gradient to the conditional-transition-score expectation, and obtain the mobility correlation identity at every fitted lag.
- **2 points:** Derive the residual as the projected generator mismatch and correctly state the fitted-lag nullspace or equivalence-class interpretation.
- **3 points:** Use the dictionary residual matrix and positive Gram matrix to bound the projected generator defect, use the explicitly defined future representation and closure-defect quantities, explicitly verify the common-domain/product-rule conditions for the semigroup comparison, and complete the Duhamel, contractivity, and Cauchy-Schwarz argument for the finite-horizon correlation bound.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not award credit for merely naming conditional scores, projection, closure, Duhamel, or contractivity without deriving the corresponding identities and inequalities. The fitted residual dictionary must be distinguished from the continuously evolved target functions used in the Duhamel argument. A valid proof must either verify the stated common-core and cross-generator regularity condition or provide an equivalent rigorous variation-of-constants justification.
