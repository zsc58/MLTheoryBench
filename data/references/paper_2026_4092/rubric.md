# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes that valid subtree clusterings are either the node singleton or unique unions of child clusterings, with additive scores and cardinalities. Treats distinct selected node sets as distinct candidates even when their scores coincide.
- **2 points:** Derives the structural lower and upper outside-count bounds. Shows that every actual outside clustering has a count within these bounds and that, for such an existing outside clustering, interval membership is exactly the cardinality feasibility test. Establishes that empty intervals exclude feasible completions. Does not require or assert that every intermediate count is attainable.
- **4 points:** Proves safe M-fold dominance using M distinct already retained candidates and a fixed actual outside clustering. Establishes that feasibility and score are preserved and that the argument composes through bottom-up candidate generation and subsequent pruning without losing the required multiplicity. A valid truncated score-threshold invariant, a complete alternative induction, or another rigorous multiplicity-preserving argument earns full credit.
- **2 points:** Uses the root interval {0} to prove the exact output cardinality min(M,|F|), feasibility, and score ranking. Handles ties by non-strict score comparisons and arbitrary choice among tied alternatives, and includes the empty and fewer-than-M cases.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular threshold-count invariant. Award no credit for merely naming dynamic programming, dominance pruning, or an exchange argument without establishing the necessary feasibility, score, distinctness, and preservation claims.

The completion interval is a conservative numerical interval. In a non-binary tree its nonemptiness need not imply that an actual completion exists. An argument relying essentially on the contrary assertion has a substantive gap. Do not penalize a proof for correctly rejecting that assertion from the source or the earlier reference proof.

At a non-root node, more than M retained intervals may contain the same count: a later candidate can be retained because some other count is not yet M-covered. Exact per-count retained cardinality is not required and is generally false.

A single replacement of an omitted candidate by an equally good or better candidate does not by itself prove a top-M statement. The proof must preserve distinct alternatives and address subsequent pruning. Tie-breaking does not create strict numerical inequalities, and recovery of an independently prescribed global tie order is not a task requirement.

Pruning applies to leaves as well as internal nodes. The one-node tree and infeasible count ranges are included. Binary branching, balanced trees, nonnegative quality scores, or existence of feasible clusterings must not be imposed as additional hypotheses.
