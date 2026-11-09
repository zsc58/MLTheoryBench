# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Conditions on the training data, keeps the learned witness fixed as n grows, identifies the held-out scores as iid with the stated conditional mean and finite positive conditional variance, and correctly applies the finite-variance CLT and empirical-variance consistency. Uses the stated n-1 normalization, or explicitly accounts for an asymptotically equivalent normalization.
- **3 points:** Proves null centering using the zero-flow implication and the conditional-expectation tower identity. Justifies the relevant integrability from the witness's square integrability under the midpoint law and the endpoints' finite second moments. An equally valid exchangeability argument for null centering is acceptable.
- **3 points:** Uses Slutsky/studentization to obtain the centered standard-normal limit and hence the uncentered null calibration. Accounts for the zero-empirical-variance convention, noting that this event has probability tending to zero because the limiting population variance is positive.
- **2 points:** Correctly proves that power tends to one for a fixed positive alignment, and establishes the displayed Gaussian expression with an absolute o(1) error. It suffices to show that the centered term is tight, the random signal term diverges to positive infinity, and both the true power and the proposed Gaussian expression tend to one.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, ordering, or explicit proof of the already assumed null implication. Treat omission of the null-centering argument or the positive-signal consistency argument as theorem-critical gaps.

The expectation, variance, probabilities, and limits are conditional on training. The result is pointwise for a fixed learned witness; do not require uniformity over witnesses, a growing-training-sample result, local-alternative analysis, a convergence rate, or fourth moments.

Do not require or reward the unsupported assertion sqrt(n)T/sigma_hat_n=sqrt(n)T/sigma+o_p(1). Sample-standard-deviation consistency does not imply this assertion for fixed nonzero T. A proof that relies on it without an independent valid power argument has a substantive gap in the final core step. Conversely, deriving the absolute-o(1) power formula by showing that both terms tend to one is fully sufficient and must receive full credit when the other obligations are met.

The exact numerical assignment to a studentized statistic on a zero-variance event has no asymptotic effect once the event's probability is shown to vanish. A concise justification is sufficient; failure to discuss this otherwise routine convention need not be treated like omission of a central argument.
