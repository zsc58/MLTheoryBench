# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines the within-color averaging and replication maps, identifies the reduced box, and correctly verifies preservation of color sums and box bounds.
- **3 points:** Proves the objective inequality for the color average using convexity, differentiability, equal objective gradients on color-constant points, and the zero inner product from preserved color sums.
- **3 points:** Proves feasibility preservation by applying the same argument to each aggregated constraint, using equality of right-hand sides and constraint values within each constraint color to recover every individual inequality. Verifies that a reduced feasible point lifts to an original feasible point.
- **2 points:** Establishes both optimality directions (projection of every original optimum and lifting of every reduced optimum) and proves convexity of the reduced objective and constraints by affine restriction. The optimality comparison must use the already-established feasibility and objective inequalities; if equality of the original and averaged objective at an original optimum is used, it follows from those inequalities together with original optimality.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The equal-gradient argument and the aggregated-constraint step must be derived, not merely named. A missing direction of the optimum correspondence or an unsupported feasibility implication is theorem-critical.

The supporting-hyperplane inequality and preservation of convexity under affine composition may be used as standard convexity facts when their hypotheses and domains are respected. An auxiliary affine-slice minimization must remain within the box; the task does not assume convexity or even a function definition outside that box. Do not demand interior points, strict bounds, strict convexity, constraint qualifications, or existence of an optimum.

Equality of objective values at an original optimum is justified because its averaged lift is feasible and cannot have either a larger value (by averaging) or a smaller value (by original optimality). A proof may instead establish the optimum implications directly with inequalities. If all the necessary feasibility and objective inequalities are present, omitting an explicit sentence explaining this immediate equality is at most a minor presentation omission, not a missing optimality direction.

Do not require a bijection between the full optimal sets or require every original optimum to be color-constant. Singleton colors and coincident lower and upper bounds are permitted. Empty feasible sets make the conditional optimum assertions vacuous, and absent inequality constraints require no aggregation step. A proof whose general argument already covers these cases need not enumerate them separately.
