# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Score perturbation control and empirical coupling (3 points).** Derives average calibration absolute score error and pointwise test score error at most a=4B delta_T/lambda from the stated feature-error assumptions and k(z,z)<=B^2. Establishes a valid empirical-CDF or quantile perturbation argument, such as F_T(u-h)-h<=F-hat_T(u)<=F_T(u+h)+h with h=sqrt(a), including a=0. Do not award full credit for the false assertion that the two empirical CDFs differ uniformly by at most h without further terms.

2. **Dependence transfer and valid concentration (2 points).** Shows measurable scores inherit stationarity and mixing. Supplies a valid quantitative estimate sufficient for the final coverage bound. The reference proof derives Var(F_T(u))<=2M/T at fixed thresholds and applies Chebyshev at two population quantiles. A valid alternative empirical-process argument is acceptable. The mixing sum must include lag zero. Merely citing the exact uniform-CDF inequality in the former reference proof is not a completed step: that asserted finite-sample inequality is false as stated.

3. **Quantile coupling and unconditional coverage (3 points).** Handles the conformal index ceil((1-alpha)(T+1)), its possible value T+1, ties, and population-quantile boundary cases. Combines calibration control and test-score perturbation to prove the displayed marginal bound with coefficient 16 and score contribution 4(L+1)(sqrt(a)+a). Uses unconditional event inclusions or another valid dependence-aware argument; marginal uniformity cannot be promoted to uniformity conditional on calibration data or a calibration event. A stronger deterministic bound on the unconditional coverage probability fully satisfies the advertised probability assertion. Small sample sizes may be handled by the trivial error bound.

4. **Rate regimes (2 points).** With B, M, and L fixed along lambda=T^(-beta), obtains h=O(T^((beta-rho)/2)) and a=O(T^(beta-rho)), and proves both requested regimes. In the second regime, recognizes the strict exponent gap when beta>0, including rho=2/3, so the logarithmic factor is absorbed.

# Evaluator Notes

Accept a complete valid alternative proof; do not require the reference proof's incidental presentation or a uniform empirical-CDF theorem when fixed-threshold control suffices. The target is unconditional marginal coverage, not calibration-conditional or input-conditional coverage. The test-input independence assumption from the former task is not present and must not be invented. The source's redundant outer probability wording does not require conditioning the marginal coverage probability on the calibration sample. Do not require an invalid conditional probability-integral-transform argument or insist on two endpoint applications when a valid quantile argument proves the same bound. No unresolved private proof obligation remains.
