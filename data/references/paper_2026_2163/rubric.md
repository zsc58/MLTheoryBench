# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Correctly uses the DP-mixture posterior weight, identifies no-overlap clusterings with tuples of subproblem clusterings, and proves that the weight and finite normalization separate. The normalized factors must be identified as the conditional marginal posteriors, for all partition elements.
- **2 points:** Expands reverse KL against the conditional product posterior and correctly shows that the cross-entropy contribution is determined solely by the prescribed marginals, or supplies an equivalent KL decomposition.
- **3 points:** Establishes that the independent product coupling minimizes reverse KL, with a valid equality/uniqueness argument. Handles support sufficiently to justify the product coupling and the finite logarithmic calculations; zero marginal masses do not invalidate the argument.
- **1 point:** Transfers the comparison and equality condition to the full posterior, without assuming the no-overlap event has probability one, and states the supported-particle consequence. The proof must cover an arbitrary finite partition.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular inequality. In particular, a direct KL decomposition may replace the entropy presentation.

Treat an asserted conditional factorization without deriving it, or merely naming entropy subadditivity without applying it to the KL comparison, as a theorem-critical gap. Distinguish the full posterior P from the conditional posterior P_O: only P_O is asserted to factorize. A complete proof of the full-posterior consequence must justify why conditioning does not change the comparison for distributions supported on O; an explicit common-additive-constant calculation or an equivalent argument suffices. Do not require the full posterior to be supported on O, require strictly positive marginals everywhere, or require the product approximation to use only particles originally present in q.

All fixed-marginal competitors are distributions on the no-overlap product space, extended by zero to other clusterings. The task does not claim optimality over global clusterings that cross partition elements merely because their restrictions have the same marginals. Equality is equality of probability distributions, including when some marginal states have zero mass.
