# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Clipped-mean bias and variance bound (4 points).** Under the p-moment condition and the specified per-sample thresholds, derives valid bias and centered-variance bounds and combines them to obtain an estimator mean-squared error of at most $8\sigma^2 n^{-2(p-1)/p}$ (or a stronger valid bound).
2. **Smoothness descent reduction (3 points).** Applies smoothness to each clipped update, uses a correct polarization or equivalent inequality, exploits $\eta_t<1/L$, and obtains the weighted true-gradient bound in terms of the initialization gap and weighted estimator errors.
3. **Conditional-to-unconditional control (2 points).** Conditions on the iterate, uses independence/freshness of the batch and the uniform moment assumption to transfer the clipped-estimator bound to each iteration's unconditional expected error.
4. **Telescoping and final rate (1 point).** Sums over the horizon, uses the lower bound $F\ge F^*$, and divides by the total step-size weight to state exactly the required weighted average expected squared-gradient inequality.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award credit for merely naming clipping, smoothness, or concentration without deriving the corresponding inequalities.
