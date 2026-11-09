# Scoring Guide

- 0: No correct idea or relevant valid method.
- 1-2: Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- 3-7: Some correct core steps or conclusions, but important steps are missing.
- 8-9: Complete and essentially correct, with only readily repairable errors or omitted cases.
- 10: Fully correct.

# Core Steps

1. Existence, minimum-norm projections, alpha-target closure, and target invariance (2 points). Correctly uses the projected-range assumptions, the well-definedness convention for the displayed optimizers, defines the minimum-norm representatives, establishes the active alpha targets from the residual-aware source conditions, and shows that Psi is well defined.
2. Exact residual-aware bias identity (3 points). Derives the three-term identity with correctly typed orthogonality, including both residual-debiasing inner products and the inactive-coordinate cases; merely naming orthogonality is insufficient.
3. Learner guarantees (2 points). A valid solution may either derive a learner guarantee from fully verified optimization geometry and the stated empirical-process assumptions, or correctly recognize that the direct strong-error and product-rate conditions are independently assumed and use them in the final theorem. Unsupported claims that arbitrary measurable restricted classes automatically yield unrestricted Tikhonov rates do not receive credit for this step.
4. Product-rate remainder and inference (3 points). Uses iid observations, cross-fitting with fold-size weights or balanced folds, conditional second-moment control, the bias identity, the two product-rate conditions, the CLT, and the empirical variance argument to obtain asymptotic linearity, normality, and variance consistency.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require incidental presentation choices. Treat omission of either residual direction, failure to use minimum-norm representatives, failure to handle misspecification, failure to state or use conditional residual realizability, failure to define measurable attained nuisance optimizers, or replacing the bias and remainder arguments by an assertion of a named method as a theorem-critical gap.
