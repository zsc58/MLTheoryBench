# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Applies the placement-error condition to the accumulated action and uses the triangle inequality to obtain \(\|F(x_i,u,W)-g\|\le \|x_j-g\|+c_F\sum_{k=i}^{j-1}\|b_k\|\).
- **3 points:** Uses Lipschitz continuity in the correct lower-bound direction to transfer the continuation value from \(x_j\) to the shortcut endpoint, including the factor \(\delta Lc_F\sum\|b_k\|\).
- **4 points:** Substitutes the quantitative margin, cancels the \(\delta L\) placement-error term correctly, and combines the resulting lower bound with the geometric bound to establish exactly the shortcut inequality.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The distance-improving assumption need not be used in the final algebraic argument, but the proof must establish the stated result under all of the given assumptions. A proof that asserts the endpoint or value-transfer bounds without deriving them receives at most partial credit.
