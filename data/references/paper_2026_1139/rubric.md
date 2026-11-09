# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Exchangeability of adaptive residuals (3 points):** Correctly establishes that applying the common measurable map \((x,y)\mapsto s(x,y)-\psi(\omega(x))\) to exchangeable pairs yields an exchangeable residual sequence, using the calibration-independent fixedness of the score, feature map, and regressor.
2. **Finite-sample rank and quantile argument (4 points):** Defines the adjusted order statistic with the appended \(+\infty\), handles the relevant index and ties (or gives an equivalent valid rank argument), and derives probability at least \(\lceil(n+1)(1-\alpha)\rceil/(n+1)\ge 1-\alpha\) for the test residual threshold event. If randomized tie-breaking is used, establishes the exchangeability and almost-sure distinctness needed for rank symmetry; independent identically distributed continuous tie-breakers independent of the data suffice. Independent continuous tie-breakers without identical distribution do not suffice by themselves. Handles \(k=n+1\), for which the threshold is \(+\infty\), and uses the correct inclusion from randomized rank at most \(k\) to the residual threshold event rather than an unjustified equivalence in the presence of ties.
3. **Translation to graph prediction-set coverage (2 points):** Shows exactly that the residual inequality is equivalent to \(Y_{n+1}\in\Gamma(X_{n+1})\), yielding the stated marginal coverage.
4. **Assumptions and parameter fidelity (1 point):** Maintains the stated measurable spaces, \(n\ge1\), \(\alpha\in(0,1)\), exchangeability, and calibration-independent fixed components without adding or dropping conditions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, including auxiliary randomization; a direct exchangeable order-statistic argument is equally acceptable. A solver that merely names conformal prediction or exchangeability without deriving the residual exchangeability and rank bound should not receive credit for those steps. Propagate a missing residual-exchangeability argument to the rank step when the rank symmetry is thereby unsupported. An otherwise complete randomized-rank proof that omits identical distribution of its independent continuous tie-breakers has a readily repairable local omission, not a counterexample to the public coverage claim, and should be evaluated consistently with the 8-9 category. Auxiliary proof randomization is not an additional assumption on the observed data.
