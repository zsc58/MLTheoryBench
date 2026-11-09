# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the nonempty compact, positive-definite setup and the width properties actually used. Gaussian suprema and expectations must be well-defined; any division by a width must account for singleton sets or otherwise justify positivity. Homogeneity or translation invariance should be justified when used, but an unused property need not be discussed.
- **5 points:** Establishes a complete valid sharp width comparison sufficient for the target. On the reference route, simultaneously diagonalizes the commuting square-root operators, applies weighted AM-GM to their eigenvalues, justifies squaring the coordinatewise positive ordering, verifies Gaussian increment domination, applies Sudakov–Fernique with its relevant hypotheses, bounds the comparison supremum using the same-Gaussian endpoint sum with the correct coefficients, and explicitly optimizes the resulting scalar bound. A correct direct reciprocal-midpoint argument earns the same credit without proving the full interpolation theorem. Merely naming a comparison theorem without the necessary increment and coefficient calculations does not close this step.
- **2 points:** Correctly obtains the target product inequality from the established comparison. On the interpolation route, specializes to G and its inverse at the midpoint, verifies the matrix-power identity giving the identity metric, and squares a nonnegative inequality. An alternative proof can earn these points through an equivalent valid final deduction.
- **1 point:** Exhibits equality for a family of positive-definite matrices, such as G=lambda I with lambda>0, and establishes optimality of the universal constant using an admissible set with positive width. Equality only for a singleton does not establish sharpness.

# Evaluator Notes

Accept any complete valid alternative proof; do not require the general interpolation theorem or incidental reference-proof presentation choices. Allocate comparison and final-deduction credit by mathematical content rather than by whether a solution separates them into distinct sections.

Sudakov–Fernique is an admissible standard-independent theorem. A solver may invoke it without reproving the theorem, but must establish the relevant centered-Gaussian increment comparison and justify the compact-index application, explicitly or through a valid standard formulation.

For the reference route, covariance-level AM-GM followed by independent endpoint processes does not automatically give the claimed linear endpoint-width coefficients. If a covariance is cA+eB with c,e>=0, the corresponding independent endpoint process has coefficients sqrt(c) and sqrt(e). Subadditivity then gives those square-root coefficients, not c and e. Treat an unrepaired use of the latter implication as a theorem-critical gap, not a harmless notation error. A different correctly justified independent-process argument is not excluded.

No symmetry, convexity, or origin-containment assumption on T is available. Singleton cases and zero widths must not be excluded from the theorem; routine omissions of these cases may be readily repairable when the substantive proof is otherwise correct. No incomplete private-reference step is designated as a completed scoring obligation.
