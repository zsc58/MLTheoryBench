# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points: Localized optimality and exact score decomposition.** Establish feasibility of the true factors and the basic inequality with penalty differences in the order true minus estimated. Decompose the reconstruction difference into the UD, D, and VD error terms, or give a valid equivalent argument. Optimization is over the localized feasible set.

2. **3 points: Localization and factor perturbation.** Use localization and Weyl to obtain full estimated rank. Justify sorting and simultaneous sign alignment without compromising the fixed-vector Gaussian calculations. Derive the factor bounds by the stated target gaps and matrix perturbation estimates, obtaining each UD and VD error bounded by a universal multiple of eta_r times reconstruction error, and the singular-value error bounded by reconstruction error. Merely invoking a paper-specific supplementary factor lemma is not a derivation. A correctly stated independently standard perturbation theorem with verified hypotheses, followed by the necessary weighted summation, is acceptable.

3. **2 points: Score events, clean-support decomposition, and curvature.** Establish simultaneous Gaussian score bounds with the required probability, controlling the dependence of the fitted right factor on the noise by localization rather than assuming independence. Use decomposability over CLEAN source-coordinate supports to obtain the effective complexity r(r_u+r_v+1)+s_u+s_v. Apply restricted curvature and the mixed-norm localization bound, retaining the explicit initializer remainder before absorption. The initializer bounds are standing assumptions, not a success event on which Gaussian concentration can be conditioned without justification.

4. **2 points: Noisy-source approximation.** Derive both gap and tail contributions to the off-support mass. The support counts and cutoffs refer to clean source bases, while the mass being bounded uses noisy source bases. Obtain a bound of the form M_u+M_v <= constant times d_1* epsilon_src^2, or an equivalent bound whose square root is at most constant times sqrt(d_1*) epsilon_src. Retain the source singular-value and tau denominators until their fixed-universal status justifies absorption. Handle empty gap or tail blocks, including full truncations, without invoking an undefined boundary eigengap.

5. **1 point: Quadratic solution and final rate.** Solve the quadratic inequality with square-root dependence on its constant term, absorb R_1,n sqrt(log(p)/n) using the stated assumption, and conclude both terms of the probability-1-delta Frobenius bound with the declared constant dependencies.

# Evaluator Notes

Accept a complete valid alternative proof and do not require the reference proof's incidental presentation choices or particular universal numerical constants. The standard perturbation and Gaussian concentration results may be invoked in precise forms with their hypotheses checked. The nonstandard supplementary citation is not a substitute for an unresolved proof step; the reference proof now closes the needed factor result directly.

The source-local algebraic corrections are recorded in provenance: the elementary quadratic consequence uses a square root, the intermediate tail coefficient retains 1/sqrt(tau), and substitution of an upper bound is an inequality. These do not change the target theorem. A solution correctly using these forms receives full credit. Do not require a Lasso construction or the optional Lasso sample-size condition, and do not assess the excluded minimax branch.
