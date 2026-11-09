# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Derives conditional super-uniformity of the empirical rank p-values from the failure-side dominance assumption, with a valid order-statistic threshold argument or equivalent method. Handles ties and the full range of u. Justifies using thresholds determined by the reference pool, for example through countably valued approximations or a simultaneous rational-threshold conditional-law argument.
- **3 points:** Proves that predictable nonincreasing betting functions with integral at most one have conditional expectation at most one under the calibrated p-values, using a valid layer-cake, finite-support, monotonicity, or equivalent argument. Consequently establishes the product supermartingale property.
- **2 points:** Applies Ville's inequality, or an equivalent valid maximal or stopped-process argument, to obtain P(D=1 | F=0)<=alpha. Correctly relates finite-horizon release to a bounding crossing or supremum event; does not rely on an infinite supremum being attained.
- **1 point:** Maintains the enlarged conditioning by the reference pool and past history, verifies evaluation measurability, adaptedness, integrability, and initialization, and connects all definitions to the integrated target without adding assumptions. Concise valid justifications suffice.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Rank calibration and the predictable betting expectation bound must be proved rather than replaced by the name of a specialized method. Ville's inequality is an allowed standard-independent result: a correct statement or unambiguous invocation with its hypotheses verified suffices, and its derivation is not required. A valid direct bounded-stopping argument is equally acceptable.

The p-values have finite support, so pointwise predictability of f_t at the possible p-values suffices for evaluation measurability. Do not require additional joint measurability, continuity, strict positivity, score independence, or exchangeability assumptions. Conditional-law proofs and countably valued threshold proofs are both acceptable; do not insist on a particular dyadic approximation.

Finite-time threshold attainment implies that the infinite supremum is at least the threshold, but the reverse implication is not generally valid. An unnecessary mistaken equality is a readily repairable local error when replacing it by containment leaves the argument complete.

Propagate a missing p-value validity result to the betting and safety steps only when those conclusions are not independently justified.
