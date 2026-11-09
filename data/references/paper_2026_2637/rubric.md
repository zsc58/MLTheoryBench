# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Represents threshold losses by score-ordered partial sums, with the public rank equal to the number of scores strictly below a threshold. Correctly establishes the uniform leave-one-out perturbation and the interior crossing/low-sum-block consequence. It must handle the bumped sample-size correction, the formal endpoint, a potentially missing leave-one-out score rank, and non-monotone threshold losses.
- **4 points:** Proves logarithmic expected rank displacement. This requires excluding bad endpoint and low-score events, using conditional independence of concomitants and the positive drift assumption, and deriving an O(log n) longest low-sum-block bound rather than merely invoking rank stability.
- **3 points:** Correctly transfers stability to expected test risk using exchangeability, the 2K/N averaged loss comparison, bumped feasibility on the nonempty event, and an exponentially small empty-feasible contribution.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that assumes the rank-stability bound, the low-sum block property, or the risk comparison without deriving the required nonstandard content cannot receive full credit. Equivalent rank conventions are acceptable when used consistently and when their relation to the task's K is justified.
