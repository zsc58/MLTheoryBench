# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the Gaussian conditional-covariance equation and the stated hyperbola with unit-norm conditions. Uses the Gaussian control law in A and the Gaussian population law in B.
- **3 points:** Proves all displayed scores are deconfounding under both model formulations. Justifies identification, required integrability, and the change-of-measure or conditional-regression steps. In B, explicitly connects population conditional independence to adjustment using the control regression; does not assume that the control law is Gaussian.
- **3 points:** Derives the correctly normalized Gaussian smoothing representation of overlap in each model and proves nondecrease, with strictness in every stated strict regime. Supplies a valid differentiation/integration argument or a valid alternative, including justification of its analytic operations and treatment of correlation endpoints. Establishes the higher-derivative implication rather than merely asserting strictness. Handles threshold and ReLU links without assuming they satisfy the smooth classes.
- **2 points:** Optimizes treatment-direction correlation over the specified unit-vector family, proving the prognostic minimizers for nonzero rho and the feasible rho=0 projection segment. Establishes exactness only when strict monotonicity applies.

# Evaluator Notes

Accept any valid alternative proof. The elementary argument using (alpha^T gamma)(beta^T gamma)=rho and |alpha^T gamma|<=1 is sufficient for optimizer geometry; differentiation of hyperbola branches is not required.

In model A, if c=E[h(Z)], the objective is E[S_u(Z)^2]/c^2. In model B it is (1-pi)/pi^2 times E[S_u(Z)^2/(1-S_u(Z))], where pi=P(T=1). These formulas must not be conflated. A harmless omission of a positive constant in an inequality-only argument is different from an incorrect asserted equality or an incorrect model-B functional.

A citation to the inherited density-ratio proposition is not, by itself, a replacement for its needed content. Its relevant push-forward identity can be established directly by testing against bounded functions of the representation. Likewise, merely naming Gaussian differentiation, a specialized Gaussian integral, or a strictness method does not close the corresponding proof obligation.

For the smooth strict regime, the recurrence J_j'=2u J_(j+1) need only be justified for j<=K-1. Jensen gives J_K>=E[h^(K)(Z)]^2, so differentiability of J_K is unnecessary. Do not demand an extra derivative of h.

Strict increase is a comparison between different values of |beta^T gamma|. It does not require positive derivative at zero and does not distinguish different coefficients with the same correlation magnitude. Endpoint arguments must include |beta^T gamma|=1.

All global minimization claims are restricted to the family in the task, not all representations or all deconfounding scores. In dimension two, only segment projections compatible with a unit vector and the available orthogonal complement are relevant.

Do not require an exact optimizer claim in the non-strict class, where constant links are allowed and the objective may be flat. Do not require proving that the displayed family contains every possible deconfounding score for a particular choice of links.
