# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Establishes the conditional weighted swap miscoverage bound from the prediction construction. Correctly freezes the history-measurable weights and clipped level under `F_{t-1}^+`, proves the requisite weighted failure/rank inequality, and transfers it using total variation. Accounts for ties and clipped-level endpoints. The weighted swap bound is not a public assumption.
2. **2 points:** Uses the TV-profile assumption to replace each swap discrepancy by `phi(||mu_k-mu_{N+1}||_2)` and forms the empirical weighted profile expression.
3. **3 points:** Establishes the uniform empirical-to-latent squared-distance error on the mean-concentration event, including the explicit `4D_mu epsilon+4epsilon^2` bound or a valid stronger bound.
4. **3 points:** Derives a valid normalized-exponential weight perturbation estimate, handles the sentinel coordinate when using full-vector norms, decomposes empirical weights into oracle weights plus error, and obtains the final remainder `(8N phi_max/h^2)(D_mu epsilon_{t,delta}+epsilon_{t,delta}^2)` with probability at least `1-delta`.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Stronger intermediate constants are acceptable when they imply the requested bound.

A citation to a specialized conformal theorem alone does not complete Core Step 1; the necessary specialized inequality must be justified rather than treated as a supplied assumption. The public actual score law includes the finite latent target score, not the sentinel.

The probability assertion is for each fixed `t` and `delta`, not one simultaneous event for all such choices. Full-probability conditional-law and TV exceptional sets may be intersected with the concentration event without an extra confidence penalty. Do not require independence across units or time, MCAR feedback, a concrete tolerance rate, a factor model, or a particular adaptive-level recursion.

Check clipped levels 0 and 1 and avoid assumptions excluding `epsilon=0`, `D_mu=0`, or `phi_max=0`. Do not penalize a proof for retaining the theoretical `+infinity` sentinel; replacing it by the largest finite calibration score changes the procedure.
