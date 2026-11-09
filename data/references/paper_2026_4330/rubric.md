# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Population identity and estimator domains.** Derive the antiderivative identity from the weak Fokker–Planck equation with justified approximation or cutoffs, using proper parents for drift terms and inclusive parents for the Hessian. Obtain ζ_i=−J_i^*b_i^* and the population Tikhonov equation. Respect the explicit empirical estimator: ζ̂_i need not lie in H_i. Do not assume boundedness of a marginal merely from boundedness of the joint density.
- **3 points — Deviations and perturbation.** Establish the population-score, same-sample training-score, and covariance deviations, with the parent training-error terms. Verify hypotheses of any concentration result used. Derive deterministic empirical and population perturbation estimates for the explicit estimator, using correctly typed sample/population operators. Combine them into component recursions with controlled confidence logarithms. The training-score calculation must handle its shared observations, for example by conditioning on an evaluation observation or by a verified canonical U-statistic argument.
- **3 points — DAG propagation and expectation.** Propagate the training recursion through arbitrary DAGs, including graphs with multiple paths of different lengths between two vertices. Verify the sampling-depth and approximation-error exponents from the actual regularization constraints. Justify the expectation step despite dependence between fitted errors and the concentration events. If normalized empirical biases are used, handle zero denominators and show their expected values are at most one. Explain why the source-style maximum of fractional and first powers is equivalent to the requested fractional-power sum under bounded drift. Include roots and empty ancestor sets.
- **2 points — Consistency and specialization.** Prove T_i(λ)→0 from density, construct deterministic admissible schedules tending to zero, and conclude expected-norm consistency. For ε∈(0,1/(2d)), ε_i=d_iε and λ_i=n^{-2(1−ε_i)/r_i}, verify eventual admissibility and the requested polynomial rate up to logarithmic factors. At roots ε_i=0, logarithmic factors may remain and must not be discarded by invoking nonexistent positive slack.

# Evaluator Notes

Accept any complete valid alternative proof with the same assumptions, estimator, and conclusions. Exact leading constants and equivalent logarithmic-factor bounds are not required. Standard independent concentration and spectral results may be invoked when their relevant statements and hypotheses are supplied and checked; a paper-specific component theorem or a named specialized method alone does not discharge the corresponding obligation.

Do not require an H_i norm bound for ζ̂_i or assume ζ̂_i∈H_i. Do not require sample splitting: the task deliberately uses the same iid observations at every node. Do not replace empirical approximation error by deterministic population approximation error pointwise. Do not require a log-free rate at roots; the frozen target explicitly allows logarithmic factors. Constants in the main inequality must be independent of n and of the deterministic admissible regularization values, while dependence on the fixed graph and stated uniform bounds is allowed.

Equivalent max-versus-sum formulations over fixed ancestor sets and harmless logarithmic conventions are acceptable after their equivalence is justified. The reference proof closes all obligations for the frozen target; there is no private-GT completeness exception.
