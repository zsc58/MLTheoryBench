# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the simultaneous confidence event for every sample size and uses it to prove PairTest returns the better arm with probability at least \(1-\delta\). Justifies application to adaptively selected input pairs using the fresh conditional observation model.
- **2 points:** Derives the inverse-gap expected stopping-time bound for one pair, including the \(\log(1/\delta)+\log(1/\gamma)+1\) dependence, a valid boundary inversion, and an integrable stopping-time tail. Establishes almost-sure termination; a bound only on the confidence event is insufficient for the expectation claim.
- **2 points:** Proves Knockout's dominant-arm correctness by tracking that arm and using the round-confidence union bound. Proves its unconditional expected cost with a valid integer-rounding or equivalent geometric count argument, including the zero-cost singleton case. Does not assume every candidate set has a dominant arm.
- **3 points:** Establishes the sibling-block decomposition, identifies the unique winner-entry block when the starting arm is not the winner, and proves capture and preservation. The capture argument includes the merge at the entry level, not only the block tournament and strictly later merges. Covers a winning starting arm and empty blocks, and obtains total failure probability at most \(\varepsilon\) with the specified \(\beta_h,\eta_h\). This is the characteristic tree-tournament bottleneck.
- **1 point:** Completes the unconditional expected-comparison calculation, including the capacity-weighted confidence sum, merge costs, and conversion from padded size M to N. Handles arbitrary fixed bracket placements and non-power-of-two N without treating formal byes as stochastic arms.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Deduct for treating any paper-specific intermediate conclusion as an assumption or for omitting either the correctness or linear-in-N expected-cost conclusion.

The bound \(K_r\le m/2^r\) is false for arbitrary m: for m=3, round 2 has one test. Accept ceiling-respecting bounds, such as \(K_r\le m/2^r+1\) with the rounding contribution controlled, or \(K_r\le2m/2^r\) for active rounds. Do not penalize a valid proof for retaining these rounding terms.

Tests with adaptive inputs are controlled by conditioning on their pre-call histories and using fresh samples. Unconditional independence of their errors is neither available nor required. The expected tournament-cost bound must apply even to sets containing cycles and no dominant arm. No particular numerical threshold constant or reference-proof notation is required.
