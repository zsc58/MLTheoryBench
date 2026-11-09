# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly conditions on an aliased summary and derives the conditional KL decomposition, identifying the finite regime-aware Bayes term and the excess sum_z pi_z KL_epsilon(u_z||q). Handles the specified common smoothing convention and unsmoothed boundary forecasts, allowing infinite forecast risk without an infinity-minus-infinity subtraction.
- **3 points:** Minimizes the common-forecast term over the simplex, proves the minimizer is bar_u=sum_z pi_z u_z, obtains the weighted Jensen-Shannon divergence in the selected loss convention, and justifies strict positivity when the positive-weight regime successors differ. An equivalent direct convexity or optimization argument is acceptable.
- **2 points:** Uses regime-identifying causal information together with the memory, convex-retrieval, gate, and transport-head realization assumptions to implement one joint regime-dependent choice. Respects strictly causal memory and establishes the anchor retrieval, including anchors in the convex hull of stored successor values.
- **2 points:** Substitutes the realized anchor, bounded strength, and correctly interpreted stochastic transport to obtain u_Z and zero oracle excess risk. Also proves the permitted finite-softmax case has outputs converging to u_Z and conditional expected excess risk converging to zero. The final 2 points may be allocated as 1 point for exact realization and its risk conclusion and 1 point for the limiting-case justification.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular finite-softmax approximation.

The theorem-critical conditional-risk decomposition, Jensen-Shannon minimization and positivity, and joint causal representability must be established rather than merely named. The retrieval and head-realization capabilities are assumptions: do not require a separate universal-approximation theorem for a neural architecture, and do not accept regime identification alone as proving retrieval capability.

A forecast with a zero coordinate in the unsmoothed version can have infinite risk. Correct extended-real treatment is acceptable and required where relevant. Interior successors do not make every simplex forecast's risk finite.

For common normalized additive smoothing, the conditional mean and mixture relationships must be used consistently. A proof must not silently change the loss convention or compare differently smoothed oracle and forecast risks.

Output convergence alone is not a justification for convergence of conditional expected KL risk. Accept a valid uniform logarithmic estimate, a verified domination argument, or another complete argument. In the unsmoothed case, the proposed approximations need sufficient positivity control; in the smoothed case, the fixed coordinate floor provides such control.

Do not apply the fixed-summary decomposition to an arbitrary random history-dependent approximate forecast without verifying the necessary conditioning argument. A direct comparison of its loss with the loss at u_Z avoids that issue.

Zero oracle excess risk means equality with the regime-aware Bayes risk. It does not require zero total KL to a stochastic target. No claim about training success, finite-sample estimation, optimization, or rollout performance is required.
