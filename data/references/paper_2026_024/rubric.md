# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the conditional Gaussian mean and variance under the common covariance, and identifies the predictive-oracle score from the baseline conditional density.
- **4 points:** Equates the conditional means for every \(x\), uses the common covariance to reduce the condition, and derives the exact affine mean-shift relation \(\mu_{1Y}-\mu_{0Y}=r(s_Y/s_X)(\mu_{1X}-\mu_{0X})\), including its regression-line interpretation. This is the central bottleneck.
- **2 points:** Establishes that the conditional/residual representation makes the conformity-score distribution unchanged (and IID across the change), then correctly obtains IID uniform smoothed conformal p-values.
- **2 points:** Applies the definition of an \(A\)-cryptic pair/change-point and the p-value-filtration martingale setup to conclude that every conformal test martingale remains blind and has no post-change signal.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award the central algebraic points for merely naming a regression line or crypticity without deriving the equality for all \(x\). A dependency error in the conditional-law or score-invariance argument propagates to the p-value and blindness conclusions only when those conclusions are thereby unsupported.
