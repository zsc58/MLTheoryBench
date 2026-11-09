# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly works with the continuous linear program on \([0,1]^d\), objective \(\sum_jm_j|g_j|\), and sole resource constraint \(\sum_jm_jc_j\le E\). Establishes existence of an optimum, either by a valid existence argument or by constructing and proving optimality of a feasible mask. Does not import a cardinality constraint.
- **4 points:** Proves the necessary and sufficient common-threshold characterization for all optimal masks: full selection above a nonnegative threshold, zero selection below it, and arbitrary tied-coordinate values consistent with feasibility and the requirement that either the budget is exhausted or the threshold is zero. A justified KKT argument, direct certificate argument, exchange argument with a complete converse/sufficiency step, or another valid method earns credit. Merely identifying a necessary ratio ordering does not establish the whole characterization.
- **3 points:** Proves that the sorted budget-filling construction is feasible and optimal. Covers a fractional boundary coordinate, a zero boundary fraction under exact exhaustion, and ties. Tie reallocations must preserve allocated energy, not merely the unweighted sum of mask entries.
- **1 point:** Correctly treats \(E\ge\sum_jc_j\), including equality, as a case in which the all-ones mask is an optimal choice. Also correctly accommodates zero scores and slack optima: unused energy is permissible when every positive-score coordinate is fully selected, and the all-ones optimizer need not be unique.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or explicit multiplier notation.

The task asks both for an optimal sorted construction and for a characterization of all optimal masks. An existence-only construction does not automatically establish the latter; award credit for the obligations actually proved.

Do not require strict positivity of gradient magnitudes, uniqueness of an optimizer, or exhaustion of the energy budget by every optimizer. When \(g=0\), every feasible mask is optimal. When \(E\ge\sum_jc_j\), zero-score coordinates may remain unselected at an optimum.

No discrete-knapsack optimality result, fixed-cardinality claim, stochastic assumption, or expected-energy comparison is part of this task.
