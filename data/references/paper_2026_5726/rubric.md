# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derive the three-periodic limiting first and second moments from the affine return maps, including the explicit M_i and V_i formulas and convergence from arbitrary initialization.
- **3 points:** Prove the characteristic drift claim: at a=2 establish the signs, zero sum of the M_i, strict ordering V_1>V_2,V_3, and hence strict negativity of the normalized sum; then use continuity to choose a=2+delta preserving all required signs.
- **3 points:** Analyze the three projected updates, prove the projection comparison for one nonpositive followed by two nonnegative increments, use the step-size ratio and divergent sum to force period-start iterates to 1, and control within-period movement to conclude x_t->1.
- **2 points:** Show the cumulative gradient is positive at every positive horizon, identify -1 as the best comparator, and establish R_T/T -> 2delta/3 > 0 via the Cesaro argument.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. Do not award credit for merely naming a contraction, continuity, projection, or concentration method without carrying out the needed inequalities and limits. A gap in the strict negative drift or in the projection-and-divergence argument is theorem-critical. The explicit formulas may be replaced by an equivalent derivation that proves the same sign and convergence claims.
