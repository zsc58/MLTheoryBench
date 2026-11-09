# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Objective and estimator setup (2 points).** Correctly uses the defined profiled population and empirical objectives, the estimator's membership in U_N, and global optimality of u*. In particular, the fitted population gap is nonnegative. These facts may be used directly in the comparisons; repeating all model definitions is unnecessary.
2. **Vanishing objective gap (2 points).** Uses r_N->0, omega_N->p0, and delta_N^alg->p0 to conclude that the nonnegative population objective gap vanishes in probability. No independence of the three errors is required. Uniform convergence is an assumption, not something the solver must derive from compactness.
3. **Oracle objective-gap inequality (3 points).** Derives Delta_N<=r_N+2 omega_N+delta_N^alg by decomposing the gap into sieve bias and within-sieve error, comparing population and empirical suprema, and using algorithmic suboptimality. Accept an equivalent direct comparison or contradiction argument establishing the same control.
4. **Separation-to-law convergence (3 points).** For each epsilon>0, uses the positive population separation margin to show that an epsilon-away fitted law forces a positive objective gap, whose probability vanishes. Handles an empty separation set explicitly or by a valid convention. Concludes bounded-Lipschitz convergence to P* and then to P0 when the task's stipulated equality P*=P0 holds.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that only names an M-estimation or separation argument without establishing the objective comparison and the event implication is incomplete.

Do not require a proof of a constant absolute envelope, population integrability from compactness, a Glivenko-Cantelli theorem, or latent maximizer attainment. The first two proposed deductions are not valid from a variance floor and compactness alone; integrability is explicit in the task, and growing-sieve uniform convergence is assumed. The reference proof's preliminary measurability and attainment discussion is supplementary, not an additional target or a prerequisite for full credit on a correct direct consistency proof.

Do not require a proof that mere membership of P0 in the model family makes it a maximizer of the profiled, KL-penalized objective. The specialization explicitly stipulates P*=P0. Do not confuse observable-law uniqueness with parameter uniqueness or require convergence of hat u_N to a particular parameter.
