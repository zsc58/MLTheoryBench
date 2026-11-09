# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **3 points:** Correctly expands partition synergy into entropy terms and uses the factorized maximum-entropy intervention to derive conditional total correlation (or an equivalent expected KL-divergence representation), with the relevant distributions identified.
2. **2 points:** Establishes nonnegativity from KL divergence and the upper bound by nonnegativity of the block mutual informations.
3. **3 points:** Proves the exact one-block hierarchical refinement identity by expanding the refined and unrefined partition definitions and cancelling terms.
4. **2 points:** Iterates refinements to the singleton partition and uses nonnegative increments to prove finest-partition maximality for every source and target subset.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The conditional-total-correlation/KL step is theorem-critical; merely naming it without deriving the entropy identity does not earn that step's full credit.
