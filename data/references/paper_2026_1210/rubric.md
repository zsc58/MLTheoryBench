# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **CDP reduction and objective (2 points).** Correctly derives the treatment-effect value objective under SUTVA and conditional ignorability, and shows that the conditional action-probability tolerance is equivalent to |E[q I{L=l}psi_l(S)]|<=P(L=l)epsilon for every stratum.
2. **Pointwise Lagrangian optimizer (3 points).** Dualizes the two-sided weighted-moment constraints and derives the scalar-multiplier sign rule I{delta_R-omega psi_l>0} on each stratum.
3. **Root selection and comparison (3 points).** Establishes monotonicity and continuity, derives a finite bracket from the bounded treatment-effect and positivity assumptions, handles the inactive case and both active boundary roots at ±P(L=l)epsilon, and proves optimality for every feasible rule using the pointwise Lagrange inequality.
4. **Global assembly (2 points).** Combines strata into the explicit perturbed sign rule and verifies feasibility and the global value inequality.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. The boundary root in an active case is scaled by P(L=l), matching the public conditional-probability tolerance. A claimed root without continuity and finite bracketing earns only partial credit for Step 3; naming duality without deriving the pointwise optimizer earns only partial credit for Step 2.
