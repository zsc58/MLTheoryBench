# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly states or derives the KL/Gibbs normalized weights for both marginal and joint ideals, with appropriate positive finite normalizers. A derivation may use the entropy identity and truncated exponential competitors. A cited standard Gibbs variational result is acceptable when its relevant statement is supplied and its hypotheses are verified; merely citing the paper's general variational theorem does not close this step.
- **3 points:** Forms the marginal density ratio with the correct normalizer orientation, calibrates a positive constant threshold, and proves exact equivalence with the stated conditional loss-difference cutoff, including ties.
- **3 points:** Rewrites the joint ratio using the expert-tilted posterior and uses Jensen's inequality to derive the expected loss-difference bound and pointwise inclusion. Verifies that the tilted kernel and the finite-label expectations are well-defined.
- **2 points:** Clearly identifies the two calibrated thresholds and concludes both parts for every fixed gamma>0 and every real cutoff c, P_x-almost surely. Establishes or correctly explains why the ideal input marginals are equivalent to P_x, so arbitrary versions of the Radon–Nikodym ratios do not affect the conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular truncation argument when an applicable standard variational result is correctly used. A proof that merely names KL duality, exponential tilting, or Jensen without carrying out the ratio identities and threshold implications is incomplete.

The correct thresholds in the reference notation are tau_m=(Z_m^e/Z_m^h)exp(c/gamma) and tau_j=(Z_j^e/Z_j^h)exp(c/gamma). Equivalent notation or another valid calibration is acceptable. Do not require a common threshold for the two ideals.

The public c is a loss-difference cutoff, not an additional positive calling cost in a risk objective. The public problem asks only for its two explicit inequalities and does not ask for an optimal-risk claim. Do not require a solver to discuss or reproduce the private source's calling-cost sign correction. Do not penalize a solver for using the correct normalizer orientation instead of the source proof's inverted orientation.

The reference proof closes all theorem-critical obligations; no unresolved private dependency is being treated as a completed scoring step.
