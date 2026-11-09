# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the supplied SCM/query/Kolmogorov framework and establishes the conditional counting bound, including its probability guarantee uniform in c, and the constant-observation complexity relation, or an equivalent direct conditional argument. Repeating the supplied definitions is not required.
- **3 points:** For the rooted-tree family, proves identical observations, injective recovery of the tree from single interventions, the (n-1)log_2 n lower bound with its probability statement, and the matching encoding upper bound. Justifies the tree cardinality and the encoding length by a valid standard result with its applicable statement or by a derivation. The encoding must achieve the claimed remainder, not incur an unexplained linear rounding penalty.
- **3 points:** For the bipartite family, proves identical observations, neighborhood recovery from interventions, the m^2 lower bound with its probability statement, and the m^2+O(1) upper bound. The exact graph upper bound uses the fixed labeling and the fact that n determines the payload length; an unnecessary O(log n) charge does not prove this sharper claim.
- **2 points:** Derives both the displayed finite-schema parent-set encoding bound and its consequence O(nd log_2(en/d)+n log n). Accounts for the code components and decoding information, verifies exact computation of the rational answer distributions, justifies the binomial estimate over the full range 1<=d<=n-1, and proves the implication for Delta_{2|1}. Explains order optimality using suitable fixed libraries containing the two constructions, without asserting that arbitrary libraries must realize the lower bounds.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, direct counting with auxiliary input (P*,n) may replace the constant-observation transfer, and any encoding that attains the displayed upper bounds is acceptable.

The decoding arguments and counting-to-complexity deductions are theorem-critical; merely naming an encoding or a counting method is insufficient. Standard independently valid results may be used when their relevant statements and applicability are clear. Routine integer rounding and fixed interpreter overhead are acceptable when they fit the claimed remainders. Conditional fixed-length payloads do not require an unconditional self-delimiting length charge.

Treat n=1 and m=0 consistently with the asymptotic notation: these singleton families have constant-complexity answers. Part 2 has no admissible d when n=1. Do not penalize a proof for presenting asymptotic estimates for n>=2 after accounting for singleton cases.
