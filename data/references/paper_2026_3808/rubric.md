# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs a recurrent non-goal state, a nonzero direction, and an improper deterministic stationary policy with the properties needed for the subsequent argument. For a reachability construction, justifies the Bellman relation and the positive-time return boundary at the selected state. Establishes improperness rather than assuming arbitrary greedy choices preserve the original recurrent class.
- **3 points:** Derives the max-translation identity on the selected greedy region, verifies that nonnegative translates remain in that region, and proves invariance of every Bellman residual and hence of the likelihood for all positive scales and all finite datasets.
- **3 points:** Constructs a full-dimensional positive-volume neighborhood in the greedy region, obtains a strictly positive likelihood lower bound for fixed data and scale, and uses explicitly disjoint equal-likelihood translates to prove infinite mass. Handles states with only one admissible action without taking a minimum over an empty set.
- **2 points:** For complete expected-reward data and any proper policy, identifies the square residual matrix, proves its nonsingularity from absorption, including an arbitrary prescribed first action, and deduces finite Gaussian mass on the proper-policy region.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation choices, discounted attainment argument, or particular cube construction. A proof using a supremum reachability vector need not establish attainment if it derives all identities needed for the existential target without using attainment.

Award credit for independently established conclusions, but not for merely naming reachability, translation invariance, or Gaussian integrability without the needed derivations. In particular, a positive-time return probability must not silently be replaced by a time-zero hitting probability at the selected recurrent state.

The policy and direction must be chosen independently of theta, epsilon, and D. The positive likelihood lower bound used for divergence may depend on epsilon and D. Ties are allowed in the public greedy regions. Finite datasets may contain repetitions or be empty.

Do not assume a common admissible action set, existence of a proper policy, or the negative-infinite-return condition for improper policies. These are not hypotheses of the repaired task. If no proper policy exists, the universally quantified proper-policy conclusion is vacuous. The finite-mass conclusion requires the specified complete dataset; no such conclusion is requested for arbitrary partial data.

The local corrections to other results grouped under theory_009 are not additional solver obligations. Only the proper-policy fixed-point argument from that record is relevant to the selected task.
