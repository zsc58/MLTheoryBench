# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Bias decomposition and cross-fitting.** Correctly derives the same-group covariance decomposition and uses independence of groups \(A\) and \(B\), together with gradient unbiasedness, to factor both cross-fitted expectations and eliminate the coupling term exactly. The factorizations must be compatible with integrability under the stated assumptions; no additional second-moment assumption on the numerator is needed.
- **2 points: Uncorrected inverse bias.** Establishes the required sample-mean moment orders, performs a justified quadratic Taylor expansion with third-order remainder, and obtains the leading term \(T_a''(\mu_k)\sigma_k^2/(2m)\) with an \(O(m^{-3/2})\) remainder. The derivative bound must apply to the possible sample-mean outcomes, as it does here because the statistics are nonnegative and damping is positive. Merely invoking a delta method without deriving or justifying the expectation remainder does not earn full credit.
- **4 points: Plug-in correction cancellation.** Proves that \(\widehat V_k\) is unbiased for \(\sigma_k^2/m\), controls its second moment under the stated fourth-moment assumption, and shows that replacing \(T_a''(\mu_k)\) by \(T_a''(\bar X_k)\) incurs only \(O(m^{-3/2})\) error in expectation. It must then explicitly cancel the order-\(m^{-1}\) Taylor term and obtain the corrected scalar rate. This is the central step.
- **2 points: Matrix lifting and update conclusion.** Correctly lifts the scalar estimates through the fixed diagonal or population-aligned basis in operator norm and combines them with independence to prove the ordinary and corrected expected-update bounds, without claiming a result for a random empirical eigenbasis.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its exact constants. For the sample-variance second moment, one sufficient elementary estimate is

\[
\mathbb E\widehat V_k^2
\leq\frac{\mathbb E|X_{1,k}-\mu_k|^4}{(m-1)^2}
=O(m^{-2}).
\]

A correctly stated standard moment bound with verified hypotheses is also acceptable. Do not require this particular estimate if another argument establishes the needed expectation-level plug-in error. A stochastic-order assertion alone does not justify an expectation bound.

Integrability follows from bounded ordinary inverse factors, finite expectation of the variance correction, and independence from the integrable numerator. An otherwise complete proof that only leaves this routine justification implicit should be treated as a readily repairable omission, not as a failure of the main bias-reduction argument.

A proof covering only the diagonal inverse case omits the aligned inverse-root case and cannot receive full credit. Treat the use of a random empirical eigenbasis as a theorem-critical scope error unless its additional rotation terms are independently controlled. Numerical clipping is not part of the estimator in this task. Do not deduct twice for a single missing scalar estimate when its matrix consequence is absent solely because of that dependency. Do not require separate discussions of zero gradients, zero variances, zero population entries, or repeated eigenvalues when the proof already covers them without division by a potentially zero quantity or an unstated eigengap assumption.
