# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly formulate the alpha-ball candidate family within each cluster and recognize the greedy procedure as selecting a largest-covered currently-uncovered set.
2. **3 points:** Establish the coverage invariant and finite termination, using an unmatched point's reflexive self-match to show that every nonterminal iteration removes at least one point.
3. **2 points:** Derive the exact similarity and categorical-attribute guardrails for every assignment from membership in the selected representative's alpha-ball, and lift the argument over the partition.
4. **3 points:** Define the partition-constrained optimum and apply the classical greedy set-cover approximation theorem to obtain |R_k|≤(1+ln|C_k|)OPT_k for every cluster.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The termination argument must not assume that a maximizer chosen from all of C_k is itself unmatched; it is enough to use any unmatched point's reflexive self-match.
