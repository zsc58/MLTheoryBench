# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Correctly identifies the mixture posterior, oracle target marginal, and exact two-stage sampler, including the live schedule factor, second-stage coordinate gate, common initialization, and independent estimator experiment. Justifies that posterior averaging generates the stated mixture marginal, or supplies a mathematically equivalent derivation.
2. **(3 points)** Establishes the characteristic two-jump decomposition under the oracle law and obtains the cubic-step/rate contribution. Any auxiliary law used for oracle-to-auxiliary KL must dominate all possible oracle transitions, including transitions after a coordinate has changed again. Derives the oracle interval comparison and its logarithmic factor rather than asserting them.
3. **(3 points)** Derives a valid location-corrected-to-auxiliary comparison using scalar Poisson-divergence bounds and the explicitly given posterior derivative bound, covering both phases and inactive coordinate gates. Establishes the estimation comparison with the correct common-history likelihood formula and the source normalization E_θK(θ)=2(ε_Est^{LC})^2, where ε_Est^{LC} is nonnegative.
4. **(2 points)** Uses an admissible floor choice, including the large-L_k^p case, and correctly combines uniform interval bounds, the KL chain rule, endpoint data processing, Pinsker, and the triangle inequality. Obtains the stated explicit logarithmic rate with an additive ε_Est^{LC}, and handles zero-rate intervals and the singleton alphabet without undefined divisions or logarithms.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, a particular auxiliary construction, or its exact floor choice if the proposed alternative proves the requested inequality.

A proof that merely names uniformization, change of measure, or concentration without deriving the required estimates does not earn the corresponding core-step credit. Propagate a missing support argument, truncation estimate, or KL estimate to the final-rate step when the conclusion is consequently unsupported.

Do not accept flooring only the posterior while leaving a possibly zero second-stage gate outside the floor as a support-dominating auxiliary construction. A small probability of the offending paths does not make their infinite KL contribution finite. Do not assume that the auxiliary process has total rate at most DM_k merely because the actual samplers do.

The task's posterior comes from the mixture experiment. It must not be identified without proof with the terminal transition kernel of the averaged CTMC. The derivative supremum directly supplies the required time variation. Do not require, or grant credit for an unsupported use of, L_k^p≤DM_k or the CTMC backward equation for this posterior.

For the reference floor, min{1,max{(τ_kDM_k)^2,τ_kL_k^p}} is admissible. An uncapped expression requires a separately justified treatment of values above 1; the step-size assumption alone does not exclude them. Other valid case splits or constructions are acceptable.

The final discretization estimate requires two directed comparisons with a common auxiliary law, followed by a TV triangle inequality; KL itself has no triangle inequality. The two square-root terms must be combined with a valid numerical inequality. Estimation uses expectation of KL before the final square root via Jensen, and no estimator-dependent oracle initial law is permitted.

The public task explicitly requires ε_Est^{LC}≥0. Thus sqrt(E_θK(θ)/2)=ε_Est^{LC} follows from its normalization. A solver may use this directly without a separate sign argument; a negative choice of ε_Est^{LC} does not satisfy the repaired task.

There is no private GT quality warning and no unresolved reference-proof obligation.
