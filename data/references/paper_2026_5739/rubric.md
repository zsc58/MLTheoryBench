# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Reparameterizes with `epsilon = 1-lambda` and `delta = p-u`, notes `sum_i delta_i = 0`, and establishes positivity of the shrunken coordinates near `lambda = 1`.
- **3 points:** Applies a valid Taylor expansion of each logarithm about `1/K` with a controlled remainder of order at least `O(epsilon^2)` (a sharper `O(epsilon^3)` remainder is acceptable).
- **3 points:** Averages the coordinate expansions, explicitly uses the zero-sum constraint to cancel the first-order average, and subtracts this average in the CLR so that the leading term is `K epsilon delta`.
- **2 points:** Converts back to `lambda`, controls the remainder componentwise or in a fixed vector norm, and states the required asymptotic for every fixed interior `p`.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The central Taylor expansion, zero-sum cancellation, and resulting first-order coefficient must be mathematically justified; merely naming a Taylor or CLR argument is insufficient.
