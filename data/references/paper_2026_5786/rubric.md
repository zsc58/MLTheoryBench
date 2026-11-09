# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Proves that singleton-intervention changes produce a graph whose transitive closure is exactly TC(G). This must establish both locality-based absence of false reachability and representation of every true edge or reachability relation; merely asserting detectability is insufficient. The locality argument also justifies the acyclicity needed for the topological traversal.
- **4 points:** Establishes the conditional edge test in both directions. For a true edge, the proof must show that intervening on the other current parents eliminates every alternative path and invokes unique-child detectability. For a non-edge, it must show that all paths are blocked and invoke conditional locality.
- **1 point:** Maintains or otherwise justifies the state needed by every deletion query, namely that the current graph contains G and is contained in TC(G), and concludes that the returned graph is exactly G after all candidate edges are processed.
- **2 points:** Correctly counts O(n^2) intervention distributions, including both distributions potentially needed for each conditional comparison, and proves that every intervention set has cardinality at most n-1. Handles n<=1 by the stipulated query-free return; for n>=2, singletons satisfy the bound and conditional target sets exclude the candidate head.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's induction or incidental processing order. Award a later step when its needed conclusion has been independently established, even if an earlier attempted derivation was flawed. A proof that merely names faithfulness, locality, or a pruning method without verifying the relevant residual paths has a theorem-critical gap.

The hard intervention on each vertex is fixed across target sets. The public task already assumes conditional locality, so solvers need not separately derive it from structural equations. The target is exact recovery from exact distributional comparisons, not a finite-sample guarantee or a mean-change result.

A conditional comparison may need P^B and P^(B union {x}); counting two distributions per candidate edge is sufficient. A smaller count is acceptable if reuse or availability of the baseline distributions is justified. The observational distribution is not a hard intervention. The n<=1 case uses no intervention at all, so its cardinality requirement is vacuous. Omitting only this readily repairable case is not a failure of the central identification argument, but it is an omission for full credit.
