# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Simultaneous concentration and base optimism (2 points).** Uses the explicitly assumed bandit interface with the correct normalized conditional-mean rewards, allowing predictable adaptive rewards. Constructs concentration uniformly over the prefixes and empirical benchmarks actually used. Conditions transition-gap martingales on the pre-transition history. Proves optimism, including estimates based on partial epochs when needed, and establishes valid epoch-count and confidence-width bounds. Empty epochs require no undefined empirical average.

2. **Variance recursion and a valid prefix bound (2 points).** Uses finite minimax and total variation to control empirical optimistic gaps, accounts for geometric rounding, and derives the base Bellman-gap bound. Justifies removal of the additive rounding term on arbitrary restart prefixes: for example, use the full base estimate when T>=|S|/eta and the deterministic HT bound otherwise. Merely invoking a K-episode theorem with eta>=|S|/K does not establish the claimed T-episode estimate. If using aggregate local variance bounded by C, defines it through a minimum over enclosing intervals or supplies an alternative valid comparison.

3. **Restart analysis, parameter feasibility, and switch accounting (3 points).** Compares the computable statistic with regret and optimistic gaps at all stopping prefixes. Derives the geometric nontermination balance and shows that reached final parameters are unclipped in the large-K regime, or supplies another valid analysis of clipping. Proves stationary ordinary tests cannot terminate. Correctly charges completed ordinary tests to switches, includes the initial-segment offset, and handles one-episode stopping overshoot. It is not enough to call the last sub-block a switch detector or merely name a doubling argument.

4. **Block aggregation and the final simultaneous rate (3 points).** Derives the block cost, treats a reached final calibration sub-block separately as necessary, and obtains both the geometric variance aggregation and the Cauchy-Schwarz switch aggregation on one event. Partitions global regret using its common benchmark rather than asserting that distinct local benchmark values telescope. Handles K=1 and the remaining small-K regime. The inference HK=O(H^2|S|) from K<16H^2|S| is invalid; bounding HK by both complete rate branches is acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require incidental notation, a particular concentration allocation, or the exact proof organization above. Universal constant changes and equivalent logarithmic confidence factors are acceptable if their dependencies are stated correctly and they do not change the algorithm's polynomial parameter dependence.

The public task explicitly assumes the supplied bandit-module interface. A solver need not prove that assumption or reconstruct an implementation from a method name. The private audit has not verified the separate specialized implementation theorem for one-half-Tsallis FTRL with implicit exploration and doubling. This unresolved external instantiation must not be represented as a completed reference-proof step, and it must not be used to penalize a correct proof of the public conditional theorem.

A proof may use the supplied bandit inequality, but it must still verify that the feedback, normalization, information timing, and adaptive conditional-mean environment satisfy its hypotheses. Oblivious opponent policies do not by themselves make the learned bandit reward vectors oblivious.

The central restart, nontermination, and dual aggregation argument is theorem-critical. Merely naming a restart method, citing the desired base or meta theorem, or assuming the block-cost bound does not close these obligations.
