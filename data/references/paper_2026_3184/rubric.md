# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Skeleton and separator invariants (2 points).** Uses oracle faithfulness to show that neither skeleton searches nor collider-subroutine deletions remove true adjacencies. Explains why missing edges have valid stored separators, including known gaps, and why previously stored separators remain usable.
2. **Orientation and iterative ancestry bottleneck (3 points).** Establishes the collider dependence-witness argument and its validity throughout the observational equivalence class. On true adjacencies, shows that these arrowheads and consistent background orientations preserve possibly directed paths of G. Inducts from the pre-pruning retained set to the next one, including the presence of every vertex of the needed b-possibly causal path and retention of targets. Does not assume finite-order Meek orientations.
3. **Maximal-order exact recovery (3 points).** Shows that the true parents required by a separating set survive and stay in the background-filtered candidate sets until their cardinality is tested, using either endpoint and the appropriate ordinary or known-gap pass. Proves exact skeleton recovery and both soundness and completeness of final unshielded-collider recovery. Justifies identifying the full-order Meek output with G restricted to the larger retained b-possibly ancestral set, rather than merely asserting that all induced MPDAGs have the same restricted-information interpretation.
4. **Final targeted equality and MPDAG status (2 points).** Shows that b-possibly causal paths and their backward-chord tests are unchanged when restricting to the larger closed retained set, giving exactly G[bPossAn_G(T)] after final pruning. Separately justifies that this final induced graph is an MPDAG. Covers empty targets and the stated trivial-size convention.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation, moral-graph presentation, or graph-extension argument. Standard independent d-separation, Markov-equivalence, CPDAG, and Meek-completeness results may be used with their relevant hypotheses checked. A citation to an algorithm-specific SNAP or RFCI guarantee does not by itself establish the paper-specific pruning invariant or exact-recovery argument.

The b-possible ancestors of the targets need not form a set closed under b-possible ancestry. For example, in the MPDAG a->b, a-c, b-c, the b-possible ancestors of a are {a,c}, while b is a b-possible ancestor of c. Therefore applying the closed-set restriction lemma directly to the final target-ancestor set is not a completed proof of MPDAG status. A valid hereditary Meek-closure argument is acceptable; it need not establish recovery using only the original knowledge restricted to that final set.

The procedure resets temporary orientations at each order and applies Meek closure only after the full-order run. Arguments about a different algorithm with finite-order Meek closure do not establish this task. Likewise, ordinary possibly directed paths must not be equated with b-possibly causal paths in an MPDAG.

A named algorithm without a valid ancestry/path argument earns no credit for the corresponding part of Step 2. Theorem-critical gaps in iterative retention, exact recovery, or final equality are major omissions. There are no unresolved private-reference proof obligations.
