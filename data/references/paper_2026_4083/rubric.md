# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **1 point — Protocol and comparator.** Establishes simplex admissibility, conditional mean-zero noise, and the proper-loss comparator hat p_n. Handles initialization and defines any terminal analysis draw. Respects the distinction between fresh conditional randomization and unconditional independence.

2. **2 points — Smooth-loss guarantee.** Uses the actual outcome-wise smoothness assumption to compare noisy predictions with FTL. Proves the logarithmic FTL bound, for example through the Bayes-risk telescoping identity, and proves a sufficient noise second-moment estimate. A direct uniform-ball covariance calculation is fully acceptable and yields a stronger moment bound than required. Includes boundary distributions and the first round.

3. **3 points — General-loss stability.** Gives the shifted-prediction decomposition and bounded-function TV inequality, establishes a valid neighboring-law geometric estimate, and sums it with exceptional-round and count-harmonic control. The proof must apply to the actual sampler on boundary faces. Simply deleting zero coordinates and calling the resulting law uniform is not valid. A conditional-radius mixture argument, or a complete alternative treatment, earns full credit. If using exact ellipsoid volumes, the proof must compute a section rather than an orthogonal projection. Equivalent shell arguments not requiring an exact volume formula are also acceptable.

4. **2 points — BTPL control.** Derives the affine-outcome BTL inequality and bounds the perturbation increments through a valid coupling, obtaining O(n sqrt(d) rho). Uses an operator-norm rotation estimate or another valid bound. Explains that the coupled pathwise inequality transfers to the original sampler in expected additive loss, not as a pathwise assertion for arbitrary independent noise realizations.

5. **1 point — Information timing and adaptive transfer.** Justifies the claimed non-anticipating-adversary guarantee. One valid route proves a deterministic inequality for the sum of conditional expected losses on every outcome path and then applies conditional expectation. Conditioning on the complete adaptive outcome sequence and treating the noise as unchanged is not valid.

6. **1 point — Rates and simultaneous quantifiers.** Substitutes rho=d^{3/4}/sqrt(n) into both regimes, obtains the requested dimension and horizon dependence with universal constants, and keeps the guarantees per fixed loss in expectation for the same loss-independent algorithm.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, exact constants, exact covariance formula, or specific geometric parametrization.

The public smoothness definition is outcome-wise. The weaker-looking expected-loss inequality used inside the reference proof is a derived consequence, not the assumption defining the class.

Treat omission of either regret regime, an unsupported invocation of the geometric bottleneck, failure to handle the sampler's boundary-supported laws, invalid coupling transfer, or an unjustified adaptive-adversary extension as a substantive proof gap. Merely naming a specialized prior FTL result or a paper-specific geometric lemma does not close its application unless the relevant statement and hypotheses are supplied or the required conclusion is derived.

Do not require or reward the source's incorrect projection-volume formula, its claim that all unit directions have equal displacement under a fixed rotation, or its unqualified pathwise BTPL assertion for independently drawn noises. The repaired reference proof contains complete derivations of the needed statements; no unresolved GT obligation is being treated as a completed rubric step.
