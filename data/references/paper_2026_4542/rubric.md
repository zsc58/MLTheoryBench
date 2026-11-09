# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **KL optimizer and normalizer (2 points):** Derives the exponential-tilt optimizer relative to $P(x\mid y)$ and identifies the optimum with the logarithmic normalizer/continuation value.
2. **Posterior-to-PMI representation (3 points):** Uses exact posterior identification, takes the likelihood ratio, and proves the pointwise conditional-PMI identity on all defined positive-mass contexts.
3. **Gauge non-identifiability (2 points):** Exhibits the arbitrary context-only shift of reward and continuation baseline and verifies cancellation in the optimizer and posterior relation.
4. **Reversed direction and commutativity (3 points):** Sets up the swapped update, derives its analogous log-ratio, and correctly uses shared permutation-invariant values and conditional-PMI symmetry to obtain the cross-direction constraint.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental presentation choices. Penalize omission of positivity/domain qualifications when they affect validity and treat failure to establish the reversed-direction cancellation as a theorem-critical gap.
