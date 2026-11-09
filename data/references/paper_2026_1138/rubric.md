# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Covariance identification (3 points).** Condition on the supplied directing measure, compute the covariance of the mean of b conditionally independent draws, and apply total covariance. Use invariant conditional means to remove the between-measure term, justify finite unconditional moments, and obtain Cov(Pi_theta g_B(theta))=G*(theta)/b. Apply the independent fresh-batch law at the predictable iterate to obtain the martingale-difference and conditional-covariance identities.
2. **Fluid limit (2 points).** Give the martingale decomposition and prove uniform convergence to the ODE using valid localization, a maximal inequality, and Gronwall. Localization must preserve the martingale argument, for example through predictable stopping; conditioning without justification on a future high-probability event is not sufficient.
3. **Fluctuation linearization (2 points).** First establish a tight fluctuation-scale bound, or an equivalent argument sufficient for Taylor control. Linearize h along the ODE and show that the accumulated Taylor and Euler errors vanish. Control the difference between grid, step, and piecewise-linear processes at the fluctuation scale, including the final partial grid interval.
4. **Martingale FCLT and limit (3 points).** Establish uniform predictable-covariance convergence to the integral of G* along the ODE, conditional Lindeberg, and the required tightness/jump control. Apply a valid martingale FCLT. Justify joint convergence with the initial fluctuation and independence of the limiting Gaussian driver from that initial value. Pass through the linear integral equation, establish uniqueness, and conclude the requested D and C convergence.

# Evaluator Notes

Accept any complete valid alternative proof; do not require incidental presentation choices from the reference proof. Standard maximal inequalities, Gronwall, the martingale functional CLT, and standard continuous-mapping facts may be invoked with their relevant hypotheses checked.

Do not require second or fourth moments of U_0^eta: convergence in distribution supplies tightness, and this is enough. Do not require Gaussian batch noise, invertibility of G* along the entire trajectory, or continuity of Pi_theta beyond what is actually needed for measurability. The assumed continuity is that of G*.

The experiment uses independent copies of the full size-b exchangeable batch law, independent also of the initial iterate. Replacing it by blocks sharing one latent directing measure across iterations, or by reuse of a fixed dataset, is a different experiment. Merely quoting a one-batch unconditional covariance does not establish a conditional covariance for such different experiments.

Do not award completion of the Taylor-remainder step from unscaled fluid convergence alone, or completion of the limiting-SDE step from separate marginal convergence of the initial value and martingale alone. The relevant missing estimates or joint-convergence justification must be supplied. Conversely, concise use of a standard theorem that explicitly supplies those conclusions is acceptable.
