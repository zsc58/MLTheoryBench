# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Use the well-defined full-support sampling setup and projected equation; justify statewise stochastic-policy interpolation and its deterministic-policy convex-hull representation.
2. **3 points:** Derive the exact frozen-target $m$-step boundary map; under JSR $<1$, justify a common contraction bound, existence and uniqueness of the projected fixed point, boundary and within-period convergence, and the normalized upper rate. Equivalent elementary contraction or fixed-point arguments are acceptable.
3. **3 points:** Prove the period-one identity and the decomposition with $(I-\alpha G)^m$; use the step-size condition and finite-family JSR continuity to obtain the PQVI endpoint limit.
4. **2 points:** Combine strict endpoint inequalities into all four regimes. Interpret JSR $>1$ as failure of uniform convergence for arbitrary products of the abstract policy-matrix family, without claiming that an unstable product is greedy-reachable or that every realized trajectory diverges.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's particular Lyapunov construction or presentation. Do not accept an unexplained assumption that a projected fixed point exists in all endpoint cases. Deduct substantially for omitting the switched boundary map, treating an endpoint identity as an assumption, or conflating full-family switching products with realized greedy trajectories.
