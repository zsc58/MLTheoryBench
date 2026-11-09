# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Definitions and level-set comparison (2 points):** Correctly use the empirical losses, level sets, and the inclusions available at every good tolerance. The sandwich may be invoked directly from the public good-tolerance assumption; proving it again is not required. If derived from bounded loss and minimizers, the derivation must respect the empty-set convention for negative tolerances.
2. **Single-tolerance control (3 points):** Apply aggregation stability, the sandwich, and the local measure-growth ratio to derive \(\sum_i\ell(\widehat y_{t,i},y_i)\leq cC_g(L_*+t+\Delta)\) for every good tolerance. Correctly compare denominators and enlarge integration domains using nonnegative losses and finite positive measures.
3. **Median-majority bottleneck (3 points):** Use the strict majority of good grid levels and the permitted loss monotonicity to show that at least \((\rho-1/2)|T|\) good predictions per index incur loss at least the final median loss. Cover distance monotonicity and one-sided monotonicity with the appropriate side of the median; the latter direction may depend on the fixed response. Ties and even grid cardinality must not invalidate the counting argument.
4. **Final comparison (2 points):** Sum the good-level bounds, compare with the median lower bound, and obtain the exact multiplicative oracle inequality with factor \(2cC_g/(2\rho-1)\) and normalization by \(n\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a redundant derivation of an assumed inclusion. A proof that establishes the inequality for every median also establishes it for the specified smallest median. A gap in the median-majority argument or in the measure-denominator comparison is theorem-critical. The task is deterministic and requires no distributional, independence, or concentration argument. No proof obligation is deferred to an external result.
