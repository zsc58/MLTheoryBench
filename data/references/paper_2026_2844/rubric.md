# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Group-quantile calibration and size disparity (3 points).** Establish exact conditional coverage at each q_g, define lambda_g, and use monotonicity plus (A2) to prove lambda_g-lambda_r>=c_g>0, yielding positive maximum/RMS size disparity and impossibility of simultaneous exact coverage and equalized size.
2. **Threshold displacement under equalized size (2 points).** For a common lambda strictly between two distinct lambda_g values, correctly infer the strict orderings of tau_g and q_g from monotonicity and the equal-size equations.
3. **Coverage-error lower bounds (4 points).** On each relevant threshold-quantile segment, use absolute continuity, |ell'_g|<=V_g, and f_{S|g}>=m_g to derive the two opposite-signed bounds with factors kappa_g=m_g/V_g, and combine them into a strictly positive pairwise (hence maximum) coverage disparity.
4. **Integrated incompatibility conclusion (1 point).** State clearly that equalized expected size at an intermediate common level necessarily entails group-wise coverage disparity, completing the bidirectional structural trade-off while allowing the degenerate all-lambda_g-equal case.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award credit only for deriving quantitative inequalities; merely naming monotonicity, regularity, or a calibration method is insufficient.
