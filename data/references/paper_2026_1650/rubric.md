# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** States and correctly uses the partition, squared-size sum, leave-one-out baselines, agreement factors, MAS, zero-sized-cluster handling, and one-cluster convention. Justifies the agreement-factor range used in the proof and avoids evaluating the undefined occupied-cluster baseline in a one-cluster state.
- **3 points:** Derives the one-point perturbation bounds between states with at least two nonempty clusters, including `Delta Q=2(b-a+1)`, the bystander bounds on `S_i`, and the endpoint bounds on `S_A,S_B`. Provides valid endpoint estimates, allowing `a=e=N-b` rather than assuming the false restriction `a<=e-1`.
- **3 points:** Performs a valid bystander/endpoint decomposition of `U'-U`, bounds the agreement-factor contribution by `2(N-1)/N^2`, the endpoint-weight contribution by `1/N`, and obtains the strict `<3/N` single-move estimate.
- **1 point:** Handles transitions both into and out of a one-cluster state, using the `(N-1,1)` score `2/N` and the one-cluster score zero. Also notes that a no-op has zero score change if such moves are included.
- **1 point:** Telescopes the single-move estimate over `m=epsilon N` moves, including possible one-cluster intermediate states, obtains strict `<3epsilon` for positive move count, and treats `epsilon=0` correctly.

# Evaluator Notes

Accept a complete valid alternative proof and award the corresponding credit without requiring the reference proof's incidental presentation choices or its particular decomposition. The reassignment count is discrete (`epsilon N` integer), and the strict inequality is required only for positive move count. A proof must establish its estimate for every state needed by its argument; an alternative argument that validly avoids particular intermediate states need not reproduce their case analysis. The non-strict bound alone is weaker than the stated positive-move target and must not be treated as logically equivalent to it.
