# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Conditions on the directing measure, correctly applies the bounded-difference moment inequality with the stated deterministic constants, combines the conditional and mixture moment bounds, and derives the effective proxy and two-sided tail bound. Handles a zero effective proxy without division by zero.
- **2 points:** Derives the conditional mean of a linear contrast and proves exact zero-sum cancellation. For the converse, correctly justifies why a zero mixture proxy forces the centered conditional mean to vanish and is therefore impossible when the coefficient sum is nonzero and the directing mean has positive variance. Does not require an unstated second-moment assumption or use an undefined product of zero and infinite variance.
- **2 points:** Represents the subsample-minus-full statistic with the correct coefficients, verifies their zero sum, and computes their squared norm as \((N-n)/(nN)\).
- **2 points:** Correctly applies bounded differences on the bounded support and substitutes the resulting constants to obtain both the exact tail exponent and the confidence half-width. Covers \(R=0\), for which the statistic and half-width are both zero.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The independent bounded-difference moment inequality may be used as a standard result. Its precise moment constant must not be inferred solely from the corresponding two-sided tail inequality without additional justification.

Finite global bounded-difference constants imply that h is bounded on its finite product domain; no extra integrability assumption on H is needed. In the final application, restricting the state space to the almost-sure interval is legitimate, and conditional support in that interval follows from the directing law. These routine facts may be invoked concisely rather than proved at length.

Only first-moment integrability is assumed for the general linear contrast. The variance convention permits an infinite variance, and the converse remains valid in that case. Zero-sum cancellation should be obtained directly from the conditional-mean identity.

An otherwise complete proof that omits only a readily repairable zero-proxy or zero-width case belongs in the 8-9 range rather than receiving full credit. Do not require the reference proof's particular method of handling those cases.
