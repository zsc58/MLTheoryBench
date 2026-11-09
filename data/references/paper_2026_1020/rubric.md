# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines the fixed prototype-based score, calibration scores, quantile index (including the +infinity edge convention), and prediction set exactly as required.
- **2 points:** Correctly conditions on the training fit and establishes exchangeability of the m calibration scores together with the test score.
- **5 points:** Carries out the finite-sample rank/order-statistic argument, handling ties for the lower bound and pairwise-distinct scores for the exact rank calculation; derives both 1-alpha and the 1-alpha + 1/(m+1) upper bound.
- **1 point:** Correctly removes the conditioning and states the probability mode and all alpha cases, including k > m.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award credit for merely naming exchangeability or a conformal method without deriving the rank implication.
