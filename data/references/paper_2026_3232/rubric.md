# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly defines the free-observation continuation values and derives the first-step recursions for optimal loss and Thompson-sampling loss, including the first-round mistake term. An operational infimum over policies is sufficient; an equality between that infimum and an expectation of posterior optimal values requires justification if used.
- **3 points:** Proves the continuation-loss comparison through a valid free-observation/deletion coupling. Handles the case where the free arm equals the initial arm, identifies the deleted action when the free arm is never used or is used only at the final simulated step, and derives the exact loss comparison before averaging. The disagreement probability may depend on the continuation policy, so its uniform lower bound must be established before taking the infimum over that policy. Independent randomization may be handled by fixing and averaging the policy seed.
- **3 points:** Proves the uniform disagreement bound. For the swap proof, restricts the exchangeability split to distinct best-arm indices, handles score ties by the prescribed index order, proves that swapping entire unobserved arm vectors preserves probability and the transcript, and shows that the image of the exceptional set lies in the disagreement event outside the already-counted event. It is enough that the recomputed deletion index belongs to the unchanged observed-arm set; its value need not be unchanged.
- **2 points:** Completes induction uniformly over admissible posteriors. Establishes the zero-horizon case and the conditional continuation comparison after a free observation, uses almost-sure admissibility of updated posteriors, and obtains the factor-two conclusion for every finite integer horizon. The argument must apply to countably many arms and must not assume that an optimal policy or minimizing arm exists.

# Evaluator Notes

Accept any complete valid alternative proof; the displayed route and notation are not mandatory. Treat an unproved deletion-coupling inequality or disagreement estimate as a theorem-critical gap. For a swap argument, merely asserting measure preservation without accounting for the adaptively chosen observed-arm set, or merely showing that an image lies in the disagreement event without establishing the required disjointness, does not close that gap. Do not penalize omission of redundant special-case discussions when the argument already covers them. All finite-horizon losses are bounded, so countable weighted sums of such losses need no additional moment assumptions.
