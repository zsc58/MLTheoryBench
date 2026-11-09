# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Setup and algorithm (2 points):** States the scalar-response observations, separable convex K-smooth losses, sign-symmetric bounded scalar learners, coordinatewise compact prediction sublevels, initialization g_0=0, infinitely recurring coordinate schedule, greedy scalar fit, multidimensional exact line search, shrinkage, and vector-span comparator.
2. **Coordinatewise intermittent convergence (4 points):** For each coordinate derives the smoothness quadratic decrease at recurring greedy iterations, establishes nonincrease at intervening iterations, telescopes to vanishing greedy alignment, uses compactness and continuity on the pre-update selected subsequence to obtain first-order optimality, and concludes convergence of that coordinate loss to its scalar-span minimum. Merely naming a convergence theorem without these arguments is insufficient.
3. **Span identification (3 points):** Proves both inclusions between the rank-one vector-learner span and the Cartesian product of scalar spans, and correctly combines the coordinate minima using separability.
4. **Global conclusion (1 point):** Concludes convergence of total empirical risk to the minimum over the induced vector-valued span (and hence to the stated comparator's risk).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
