# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (3 points):** Unrolls the online recursion and derives \(f_{\rm on}=Y(\eta^{-1}I+K^U)^{-1}k(X_n,x)\), with a valid triangular or nilpotence argument for invertibility.
- **Step 2 (3 points):** Defines \(Y^e=Y(\eta^{-1}I+K^U)^{-1}(\gamma I+K)\) and proves by matrix substitution that offline kernel ridge on \(Y^e\) equals the online predictor.
- **Step 3 (4 points):** Defines \(Y^c=Y(\gamma I+K)^{-1}(\eta^{-1}I+K^U)\), verifies the required inverses, and proves exact equality between online learning on corrected targets and offline regression on the original targets.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award the central algebraic/inversion argument only when it is actually derived, not merely named.
