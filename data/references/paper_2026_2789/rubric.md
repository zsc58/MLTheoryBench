# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Relaxation and extreme points (2 points).** Defines the binary and LP programs on the same constraints, proves `P_n^01<=P_n^LP`, and establishes that an optimal LP extreme point has at most two fractional coordinates.
2. **Feasible rounding and uniform gap (3 points).** Handles all fractional-coordinate and coverage cases, constructs a feasible binary vector, and proves objective loss at most `2V_max`, yielding `0<=P_n^LP-P_n^01<=2V_max`.
3. **Per-capita equivalence (2 points).** Divides the uniform bound by `n` and concludes convergence of the normalized LP and binary optima.
4. **Threshold squeeze (3 points).** Uses threshold feasibility and the assumed `P_n^LP-o(n)` value bound together with the integrality gap to prove normalized threshold welfare is asymptotically equal to the binary optimum.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation. Merely naming linear programming, extreme points, or rounding without checking feasibility and the two-fractional-coordinate case is incomplete.
