# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Define the true sliding-memory state and reset substitute experiment correctly; establish the conditional-law Markov representation, cost equivalence, and policy information restrictions. Justify the discounted value characterization for both models, including the relevant reward regularity and measurable approximate or exact selectors. Do not require proving a sufficient condition for weak-Feller regularity: true augmented-state regularity is an explicit hypothesis.
2. **3 points:** Prove contraction of the common next-block observation/realized-action mixture under full total variation. Bound the immediate block-cost and continuation-law errors with justified constants and derive the value bound using a comparison covered by the stationary-policy stability supremum. Distinguish fixed conditional initialization from a generated random window.
3. **3 points:** Transfer an optimal substitute policy only through the substitute state, obtain the factor-two performance-loss bound, and prove convergence of the discounted error sum when each fixed-q error tends to zero as M increases. Keep the initialization expectation in the generated version and control it with the generated-initialization stability supremum.
4. **2 points:** Derive the expected Bayesian numerator and normalization estimates under the true observation law, prove or justify the correctly normalized Dobrushin contraction, and iterate by conditional expectation. Establish the K-update result and geometric decay for generated M-block windows without claiming a uniform conditional estimate for every fixed window.

# Evaluator Notes

Accept any complete valid alternative proof under the repaired assumptions. Require the explicit quantitative bounds and a genuine Bayesian contraction derivation. Naming filtering stability, Bellman comparison, Young continuity, or a specialized stationary-optimality citation does not close the corresponding obligation.

The source uses full total variation, whose maximum is two. Consequently its overlap coefficient has the factor one half in the pairwise-kernel formula. Accept another convention only when all definitions and bounds are consistently translated.

The reference now derives the needed discounted optimality without the specialized external stationary-optimality citation. Exact stationary minimizer existence need not be proved for the value comparison when measurable stationary approximate selectors suffice. The policy-loss claim is conditional on an optimal stationary substitute policy, as stated.

A true-state-dependent optimal policy cannot simply be applied as a substitute-state policy. A history-based implementation requires a precise admissibility argument and must still justify coverage by the stationary-policy error supremum. The reference avoids this transfer by selecting a stationary true policy from the continuous Bellman-error expression. Do not accept an iteration that silently replaces the public stationary-policy supremum with a nonstationary-policy supremum.

The standing old-prior domination requirement covers every stationary true policy at the initialization under consideration; it is not a rule for excluding a comparison policy from the supremum.

The general-observation sufficient condition previously used for sliding-memory weak-Feller regularity is not a required solver claim and is not valid under state-only continuity of the observation density. The direct weak-Feller assumption is part of the public contract. Propagate a dependency failure only to conclusions that actually rely on it.
