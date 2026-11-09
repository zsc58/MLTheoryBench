# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes simultaneous pushforward invariance of the stated f-divergence, including both the integral and singular parts (or an equivalent fully justified argument). Handles potentially infinite values correctly. If using a nonnegative-generator reduction, invokes a supporting slope under the finite-valued interior hypothesis and accounts for the singular part of the affine correction.
- **3 points:** Uses target invariance, divergence invariance, and variational-family stability to prove minimizer-set stability and then uses uniqueness to deduce that the minimizer is invariant under every group element.
- **2 points:** Shows that statistic compatibility makes the induced maps on statistic values well-defined, with domain stability ensuring that their values lie in Y_0, and correctly uses the defined common fixed set.
- **2 points:** Applies invariance of the target and unique minimizer to prove that both statistic values lie in the fixed set, with all domain conditions respected.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A theorem-critical omission in pushforward invariance, uniqueness-based invariance, or the final fixed-set conclusion is a major gap.

The generator is finite-valued on (0,infinity), with its value at zero defined by the right limit. The dominating measure is sigma-finite, and zero times infinity is zero. Standard supporting-slope and pushforward-integration results may be used with their hypotheses respected. A solver need not separately reprove independence of the dominating measure or nonnegativity of the divergence when treating the stated f-divergence definition as given. Direct change of variables is acceptable when the integrals are justified; the particular affine normalization is not mandatory.

Do not impose finite divergence, strict convexity, differentiability, mutual absolute continuity, singleton fixed set, or parameter-level uniqueness. The minimum may be +infinity; the argument must not subtract infinite objective values. The claim is membership of both statistic values in the fixed set, not equality of those values in general.
