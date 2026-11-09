# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Admissible reduction and setup (2 points).** Fixes the selection rule, support point, and refinement before constructing the process. Uses the distinct selected prices correctly and verifies the structural model, finite-second-moment heterogeneity and shocks, independence assumptions, independent uniform query randomization, and an integrable causal parameter. The witnessing process must satisfy local exogeneity for every index, including nonselected indices. Correctly identifies its conditional causal target.

2. **Query-identity failure (2 points).** Handles the case in which some common outcome configuration distinguishes the two query indices. Realizes that configuration using a suitable constant parameter solving the two selected-price equations, or another valid construction. Produces measurable distinct predictors with equal minimal risk by perturbing in query-price-orthogonal directions. A zero parameter is sufficient only if it actually realizes a distinguishing configuration; it is not generally sufficient for an arbitrary rule.

3. **Outcome-information failure (4 points).** In the complementary case, establishes that the common outcome function varies in at least one coordinate. Constructs and verifies a centered finite-support shock law and appropriate structural mean, rather than asserting that suitable probabilities exist. Produces a measurable positive-probability refinement event and derives a nonzero query-shock moment. For the reference construction, checks the three-point probabilities, centering, and the nonzero leading selected-coordinate coefficient with control of the remaining same-coordinate contribution. Correctly uses linear independence to prevent cancellation by the other price-vector direction; it must not assume that all other-query contributions are higher order. Concludes genuine failure of population minimization, either through a justified conditional-risk argument with an admissible measurable improvement or by directly exhibiting a predictor with strictly smaller risk.

4. **Uniform conclusion and quantifiers (2 points).** Covers the alternative coordinate and explains why the two query cases exhaust every pointwise nonconstant refinement. Concludes that for every fixed qualifying refinement there exists a witnessing process satisfying all setup assumptions and all-index local exogeneity. Does not confuse nonconstancy on the full specified domain with nonconstancy almost surely under a previously fixed distribution.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's three-point law, numerical remainder bound, identical shock distributions, or particular perturbation when another construction closes the same obligations. Substantial credit for the event-moment step requires an actual admissible construction and a derived nonzero moment, not an unsupported appeal to choosing probabilities or a named method. Merely stating a conditional first-order condition without establishing its failure and the population-risk consequence leaves an important obligation open.

Zero-variance shocks are allowed. No demand-slope sign, price-sign restriction, or positive lower bound on the selected price separation is required beyond distinctness at the fixed support point. For K=2 the unselected outcome vector is empty. The theorem concerns population identification, not empirical estimation or consistency; do not require assumptions or conclusions from a separate consistency result.
