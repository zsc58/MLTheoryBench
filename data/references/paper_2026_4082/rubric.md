# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives a balanced separator partition from treewidth: separator size at most t+1, both sides of size at most 2n/3, and no edge between them. Justifies the component-grouping argument and handles an empty remainder. A valid standard separator theorem may be cited with its relevant statement and hypotheses; reproducing the reference proof's direct derivation is not required.
- **4 points:** Gives a correct recursive O(t log(n+1)) embedding. For the reference construction, the child embeddings share one coordinate block; cross-side products are bounded and suppressed by separation coordinates. Separator coordinates certify all paths through the separator, including endpoint and diagonal cases under reflexive reachability. Verifies reachable and nonreachable pairs and obtains a maximum-child-dimension recurrence with O(t) additional coordinates. Accounts for empty children and a constant-size base case.
- **2 points:** Constructs the odd-to-even bounded-span DAG family, proves its pathwidth/treewidth bound with valid bag indices, and proves that independently selectable edges yield at least 2^{Omega(nt)} distinct reachability matrices. Any valid universal constant in the exponent is sufficient; the unsupported nt/4 lower bound is not required and is generally false.
- **2 points:** Correctly applies a standard low-sign-rank counting bound, addresses the positive/nonpositive score convention, and derives the Omega(t/log(n/t)) lower bound uniformly for 2≤t≤n/2. Justifies the logarithmic inversion and handles dimensions outside the counting theorem's applicable range. Either a counting theorem explicitly valid for the weak sign convention or a strict-sign conversion with its rank overhead is acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular constants, its direct separator derivation, or its use of a rank-one perturbation when an appropriately stated counting result already covers zero scores.

Disjoint recursive supports generally require the sum of child dimensions, not their maximum. A proof that uses disjoint supports cannot claim the reference recurrence without a separate valid argument. Conversely, shared supports do not make cross-side products vanish; the separation coordinates must control them.

The target uses reflexive reachability, so a complete embedding must give positive self-scores. The upper bound permits cyclic directed graphs and must not rely on acyclicity. Only the lower-bound examples are required to be DAGs.

A routine constant or terminal-index slip in an otherwise complete argument is locally repairable. Do not award full credit for an uncorrected dimension recurrence or a materially incomplete sign-verification argument. No private proof obligation remains unresolved in the repaired reference proof.
