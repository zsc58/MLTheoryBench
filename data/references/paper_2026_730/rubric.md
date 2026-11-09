# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly defines and uses the piecewise-linear peaked truth, uniform treatment distribution, noiseless outcomes, and restricted population model.
- **2 points:** Computes the population OLS moments and derives `beta=(1+t_0)y_max/2`.
- **3 points:** Proves monotonicity, boundary selection `hat t=1`, and optimism `(1+t_0)y_max/2`, including its arbitrarily-large lower bound for `t_0>=1/2`.
- **2 points:** Derives the split-integral historical MSE bound for `t_0=1-epsilon`, `MSE <= 2 epsilon y_max^2 + epsilon^2 y_max^2/3`.
- **1 point:** Correctly combines the parameter choices to establish arbitrarily large optimism together with arbitrarily small MSE.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the optimizer-selection or MSE-to-zero argument as a theorem-critical gap.
