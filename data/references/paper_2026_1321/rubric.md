# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Establishes a valid optimality characterization for the discrete transport matrix, such as finite transportation LP duality and complementary slackness with correctly signed dual constraints, or an equivalent characterization sufficient for the subsequent discrete argument. Checks or correctly uses its applicability to the finite feasible transportation problem.
2. **3 points:** In the discrete case, constructs a correctly signed max-affine convex potential, proves active target atoms satisfy subgradient inequalities at each source row, and proves the normalized barycentric value t_i also satisfies such an inequality. An equivalent direct proof of cyclic monotonicity of the indexed barycentric relation earns the same credit. Repeated source locations must not be excluded or silently assumed to have identical row barycenters.
3. **3 points:** In the semi-discrete case, rewrites the cell inequalities as dominance of affine pieces of a convex max-affine potential and proves every selected active target satisfies the subgradient inequality at every x in R^d, including ties. An equivalent direct proof using the cell inequalities earns the same credit. Almost-everywhere inclusion alone does not establish the full-domain graph conclusion.
4. **2 points:** Derives the exact cyclic inequality specified in the task and applies it correctly to both relations. If summing subgradient inequalities toward succeeding rather than preceding points, explicitly reverses the cyclic ordering or otherwise justifies the required target-shift convention.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solution that merely names optimal transport duality or convexity without establishing the relevant inclusions or an equivalent direct cyclic inequality has not completed the corresponding core step.

No invocation of semi-discrete duality, Brenier's theorem, or a pushforward identity is required: the semi-discrete graph argument follows from the stipulated pointwise active-target selection. The optimizer's existence is stipulated, not an additional conclusion to prove. Do not require a separate inner-product/squared-cost equivalence discussion from a proof that directly establishes the displayed inner-product inequality.

Tie resolution may choose any active target subject to the stated measurability. Do not require uniqueness of active cells, distinct target points, or differentiability of a convex potential. Do not award full credit for replacing the pointwise semi-discrete target by an almost-everywhere statement.
