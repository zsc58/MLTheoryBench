# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Shallow Gram reduction and strict-positivity criterion (2 points).** Derives the expected feature-Gram representation for the shallow covariance and an appropriate tangent decomposition. Uses the actual bias scale, either through the ridge argument u^T x+gamma v with standard Gaussian v or through a bias variable of variance gamma^2. Shows that a zero quadratic form yields the relevant feature identity using integrability and Gaussian full support. The limiting kernels are supplied by the setup; proving their existence again is not independently required, but any recursive formula used must be justified.

2. **Linear independence for both activation classes (3 points).** Establishes independence of the operator-differentiated ridge features for smooth non-polynomial activations and for biased RePU activations. The reference route uses standard-polynomial induction in the smooth case and distinct biased hyperplanes in the RePU case. A proof using these methods must actually close the one-location case and the induction or jump calculation. If joint monomial nondegeneracy is used later, establish the stronger shallow statement allowing several distinct monomial marks at each location; positivity for only one mark at each location does not by itself establish that statement.

3. **Propagation through depth and covariance positivity (3 points).** Establishes nondegeneracy at every depth and the conclusion for general operator marks. In the reference route, the Gaussian jet vector has joint full support, not necessarily independent coordinates. The differentiated activation expression is polynomial in positive-order jet coordinates with coefficients depending on the value coordinates. Comparing its linear jet coefficients and then varying individual value coordinates closes the argument, including zeroth-order marks. Do not accept dropping other locations' zeroth-order terms after setting their variables to zero unless their remaining constants are handled. No assumption sigma(0)=0 is available. A nonzero final coefficient vector must produce a nonzero expanded jet coefficient array by the evaluated operator coefficient condition.

4. **Tangent-kernel remainder and final conclusion (2 points).** Derives a valid positive-semidefinite remainder beyond the covariance, using the tangent recursion, independently coupled feature representations, or an equivalent finite-gradient-block limiting argument. Products of expectations must be represented using independent copies when required. If cross-output tangent terms are eliminated, use the sequential-limit induction rather than asserting that distinct hidden coordinates have disjoint lower-layer parameters. Concludes strict positivity by adding the positive-semidefinite remainder to the positive-definite covariance.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its named algebraic framework, or its particular representation of the tangent remainder. In particular, a correct direct argument may replace the source's sigma-polynomial presentation, and a correct finite-gradient-block argument may replace recursive feature regrouping.

Credit both activation regimes and every stated depth. The case m=0 and zeroth-order terms in mixed operators are part of the claim. RePU has integer degree q>=m+1; parameter gradients are evaluated almost surely at Gaussian initialization, and exceptional zero preactivations do not require an additional global differentiability assumption. Growth is required through m+1, not through every derivative introduced in a smooth algebraic argument.

Theorem-critical omissions remain major even when the architecture is plausible. A citation to the source's specialized independence or depth-propagation result is not a substitute for proving the needed statement. The reference proof contains no unresolved theorem-critical obligation.
