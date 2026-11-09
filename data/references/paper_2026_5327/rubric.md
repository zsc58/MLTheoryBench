# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly derives the polyhedral KKT characterization without assuming uniqueness of multipliers or equivalence between activity and positive multipliers, and obtains the affine formula $g(z)=P_Iz+c_I$, including for rank-deficient $A_I$.
- **3 points:** Constructs a finite polyhedral cover or equivalent active-set decomposition, refines it into finitely many affine cells off a finite union of measure-zero boundaries, and verifies that the cells cover every nonexceptional input.
- **2 points:** Handles differentiability correctly, including possible differentiability on cell boundaries, and proves that the derivative equals the linear part of an adjacent full-dimensional affine cell. Award only partial credit if the argument establishes the formula merely away from the exceptional set.
- **2 points:** Proves that the Jacobian is an orthogonal projector, derives its spectrum in $\{0,1\}$, and establishes tangency/normal-gradient suppression for the associated active constraints.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require a particular choice of active representation or polyhedral refinement. Redundant constraints can make active sets and KKT multipliers nonunique; a proof that relies materially on their uniqueness has a major gap unless it separately imposes and justifies a nondegenerate representation. Propagate an omitted cell-boundary argument only to claims about all differentiability points, not to correctly established almost-everywhere conclusions.
