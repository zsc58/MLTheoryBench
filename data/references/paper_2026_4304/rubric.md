# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** For a fixed \(k\), proves retrieved-region conditional coverage by conditioning on group memberships and using exchangeability/rank validity of the calibration scores and test score. The argument must handle the \(+\infty\) quantile case and not incorrectly assume that the pooled calibration scores are unconditionally i.i.d. from a cell.
- **3 points:** Derives the uniform comparison \(|F_k(t)-F_{A_k}(t)|\le\varepsilon_k\) from the mixture identity and the weighted KS distances, including applicability at the random calibration-measurable threshold.
- **3 points:** Correctly conditions on the calibration data to express the two conditional coverage probabilities as expectations of \(F_k(q_k)\) and \(F_{A_k}(q_k)\), transfers the retrieved-region bound to cell \(k\), and identifies the deployed threshold on \(\{b(X_{n+1})=k\}\).
- **1 point:** States both required final guarantees with the correct conditioning events, parameter conditions, and conversion from score coverage to prediction-set coverage.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
