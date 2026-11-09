# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Prove the simultaneous confidence event ||theta*-mu_n||_{Lambda_n}<=gamma_n(delta) for every n<N with probability at least 1-delta. Account for the constrained estimator and the exact radius, including the regularization bias inside the squared radius. A complete route establishes the relevant exponential supermartingales from conditional subgaussianity, integrates against a suitable fixed Gaussian measure, computes the integral, obtains a uniform crossing bound, and applies convex optimality of the constrained estimator. Equivalent complete arguments are accepted. The chosen regressors must be predictable under the stated information model, and a zero estimation error must not lead to invalid division.
2. **3 points:** Use optimism and feasibility of (u_n*,theta*), then Lipschitz continuity on the defined output set and both ellipsoid memberships, to derive r_n<=2L_z gamma_n(delta)||V^(1/2)A_n(u_n)Lambda_n^(-1/2)||_2 together with r_n<=c_r.
3. **3 points:** Convert the per-round bound into sum_n r_n^2<=2 max{c_r,2L_z gamma_N(delta)}^2 log det(Lambda_0^(-1)Lambda_N) by a valid truncation argument and a multi-output determinant/log-potential telescoping proof. Justify monotonicity of the radius, the squared operator-norm identification, the spectral-radius-to-determinant inequality, and the conformable determinant identity, or provide an equivalent valid route. Merely naming a potential method earns no credit for this step.
4. **2 points:** Apply Cauchy-Schwarz and the confidence-event probability to conclude the stated high-probability cumulative regret bound for the policy. Retain the realized information matrix and radius and the quantifier 'for each fixed delta'. Cover the empty horizon directly if needed.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular Gaussian mixture. Standard independent probability and linear-algebra results may be used when their relevant statements are explicit and their hypotheses are checked.

A bare citation to a specialized self-normalized least-squares confidence theorem does not close the confidence obligation. Neither assuming the desired confidence event nor replacing the stated radius by a larger familiar radius proves the task. If the confidence event is merely assumed or asserted without a complete justification, award appropriate partial credit for the conditional regret analysis, but the answer is incomplete and cannot receive a score above 7.

Do not require a bound on the regressor norms, compact action sets, or a closed parameter set: these are not additional hypotheses of the task. Attainment and measurable history-based selection are explicitly part of its well-definedness contract. The proof must remain valid when some or all chosen regressors vanish or when L_z=0; the reference proof's no-division truncation handles these cases.
