# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points: Concentration and contract.** Establish the simultaneous restricted covariance, block, and coordinate-noise bounds with failure probability O(p^-2+n^-3), and the fixed true-support score bound with additional failure probability at most varrho. Verify conditioning on X using independence of noise and design. A valid statement and application of standard covariance or quadratic-form concentration is acceptable; merely naming a concentration result is not.

2. **3 points: First-stage dynamics.** Derive the correct simultaneous update expansions, including the scalar factor 1-eta in the theta self term. Establish the induction base, sparsity control, both error invariants, feasibility of the coupled threshold inequalities, and preservation along the common-ratio schedule. Obtain both first-stage statistical rates. Account for integer support sizes and threshold ties, either explicitly or by an equivalent sound argument. Hard thresholding is coordinatewise in dimensions p and n, not a top-budget projection.

3. **2 points: Second-stage refinement and fallback.** Show that fixed-threshold continuation preserves sparsity and the first-stage beta rate without beta-min. Under beta-min, derive a genuine contraction inequality with the true-support score term and the contamination remainder, and show that a sufficiently large constant times log n iterations absorbs the transient uniformly in signal magnitudes and varrho. It is not necessary to prove exact support recovery, nor is beta-min by itself a justification for asserting that every true coordinate is retained immediately.

4. **3 points: Minimax lower bound.** Prove both components and justify a sufficient numerical constant to obtain every positive c_q<(8C_{2s})^(-q/2)/160. For the uncontaminated component, supply an applicable independent lower-bound statement with a sufficient constant or derive it by finite testing. For the contamination component, verify the sparse alternatives, KL/TV bound, equal-mixture coupling, and transfer to at most o contaminated pairs. Handle all 1<=s<p, including odd s and p<3s/2, and the identical-clean-law case if the lower covariance is singular. A prior average over admissible fixed-subset laws suffices; do not require its mixture to belong to a single fixed-subset class.

# Evaluator Notes

Accept any complete valid alternative proof. The reference proof derives the uncontaminated constant using blockwise Fano and binary testing and handles contamination truncation using clipped loss, but neither route is mandatory. Naming a method without deriving or explicitly invoking a sufficiently precise independent result does not close an obligation.

Keep the upper and lower experiments distinct. The upper theorem does not establish robustness to arbitrary contaminated covariates. The lower model has Gaussian conditional errors; Gaussian covariates are not required. Lower-bound estimators observe only the design-response sample and do not receive the unknown coefficient or outlier set.

Zero response contamination in the upper experiment is represented by o=1. The upper coefficient support is nonempty. Initialization must exceed the positive limiting thresholds as well as dominate the coefficient norms. All implicit upper-bound constants depend only on M,eta,kappa, and the support-score event is calibrated separately for each varrho.

The source's noninteger-support shorthand and its even-s shifted-support lower-bound example are locally repaired in the reference proof. Do not demand those invalid literal constructions, and do not penalize a solver for replacing them with equivalent valid bookkeeping or alternatives. There are no unresolved reference-proof obligations.
