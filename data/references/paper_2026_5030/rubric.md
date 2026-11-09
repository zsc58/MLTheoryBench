# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly proves that separation for every positive threshold implies injectivity by applying it to the distance between any distinct pair.
- **3 points:** For the converse, constructs C_delta, handles the empty-set case, proves compactness when nonempty, and notes the denominator is bounded away from zero.
- **3 points:** Shows the distance ratio is continuous and strictly positive on C_delta using continuity and injectivity, then obtains a strictly positive minimum by compactness.
- **2 points:** Chooses epsilon below that minimum and derives strict separation for the arbitrary delta, completing the equivalence.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The compactness/minimum argument is the characteristic bottleneck; merely naming compactness without verifying compactness, continuity, and positivity is insufficient.

Source-audit clarification: the minimum argument applies only when C_delta is nonempty. Empty pair sets, including thresholds exceeding the diameter, give vacuous separation and must not be assigned a minimizing pair. The reference proof already includes this local case split; the point allocations are unchanged. For an alternative proof, award corresponding credit without requiring the particular set or ratio notation, provided the argument covers every positive threshold and establishes the required uniformity over eligible pairs.
