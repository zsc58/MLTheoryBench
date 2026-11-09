# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Bridge solvability and uniqueness (2 points).** Uses the specified conditional L2 spaces, identifies the adjoint, and verifies the compactness, orthogonality, and singular-coefficient summability needed for solvability. Proves uniqueness up to conditional next-state null sets using completeness. Justifies a measurable bridge version rather than assuming that unrelated fiberwise representatives automatically assemble measurably. A valid routine measurable-assembly argument is sufficient; the reference proof's particular iteration is not required.
2. **MNAR observed-to-full-data identification (3 points).** Uses exclusion and positivity to connect the full equation to the observable complete-case conditional equation and to the explicitly stated conditional inverse-propensity weighted residual equation. Justifies conditional integrability of the weighted residual without assuming uniform positivity or a weighted second moment. Explains why the observation law determines the bridge on behavior support without treating the propensity as known. Obtains the correct conditional one-step reward mean.
3. **Support and augmented Bellman identification (3 points).** Derives target-support coverage from the per-action domination assumption and shared controlled laws. Uses the controlled reward/next-state law and the explicit augmented transition restriction to justify conditioning additionally on prior missingness. Carries out backward induction identifying the true Bellman functions on target occupancy support. Merely asserting that the augmented process is Markov is not a substitute for the conditional reward-mean argument.
4. **Policy-value conclusion (2 points).** Correctly averages the initial augmented value at (S_1,0), establishes equality with the expected sum of true rewards, and explains why the result is determined by the behavior observation law for every target policy satisfying its own finite action-domination bounds.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award credit for merely naming overlap, completeness, Picard solvability, or dynamic programming without the corresponding derivation.

The source's primitive concentrability constants bound action-policy densities. A bound on target occupancies by the product of those constants is a derived consequence, not a separately assumed bound with the same stagewise constant.

All bridge L2 requirements are relative to the stated conditional next-state laws. Do not require an unconditional L2 bound over state-action pairs, a uniform inverse-propensity bound, or an additional global summability assumption. Conditional kernel integrals suffice for the Bellman calculation, whose resulting reward means and value functions are bounded.

Uniqueness is almost-sure uniqueness. Identification is required only on behavior support and hence on target support; arbitrary versions on unvisited pairs are not identified. Finite singular systems are permitted. The terminal next state is observed, and exclusion applies at the terminal stage as well.

An inverse-propensity identity involving an unknown propensity, without an observable-law identification argument, does not complete step 2. Likewise, adding O_{t-1} to a conditioning set by an unjustified tower-property argument does not complete step 3.
