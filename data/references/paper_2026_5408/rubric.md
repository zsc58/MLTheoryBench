# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Limiting propensity.** Derives the aggregate queue workload limit from the finite-horizon law of large numbers and deterministic budget condition, obtains the terminal treated proportion in each queue, and correctly converts this to `e_n(x)->e_infty(x)`. Accept either the correctly conditioned focal-member treated-fraction argument or the exchangeability identity `P(D_i=1|G_i=k)=E[T_{k,n}/n]/p_k`, together with independence of the focal covariate after its queue is fixed. An unconditional expectation of `T_{k,n}/N_{k,n}` is not a valid replacement for the focal-member conditional expectation. Zero-probability queues must be handled without dividing by zero. Merely asserting the limiting propensity formula earns no credit for this step.
- **3 points: Queue-dependence bound.** Proves bounded sensitivity of every cell's treated count to replacing one unit's queue-arrival coordinate. Establishes the conditional uniform-subset structure within cells, reciprocal-binomial count control, and the bounded-difference variance bound for treated fractions with the focal cells fixed. Also controls mixing over the focal cells and the shift from conditioning on both covariates to centering by `e_n(X_i)`. The focal-cell argument must distinguish potentially order-one own-cell effects from order-`1/n` effects of changing the other focal cell. These components must yield a centered-treatment bound uniform in the focal covariates, with constants depending only on the fixed design and positive cell probabilities. This is the central bottleneck; naming Efron–Stein or exchangeability without deriving the required estimates is insufficient.
- **3 points: Negligible nuisance remainder.** Gives the correct oracle-minus-remainder decomposition and conditional centering of the remainder. Uses eventual positivity and conditional L2 nuisance consistency to bound the squared remainder weight. Shows that the total diagonal contribution to `n Var(R_n|T)` is at most `E[g(X)^2|T]` and that the summed off-diagonal contribution has the same order using the pairwise bound or a valid substitute. Concludes `n Var(R_n|T)=o_P(1)` without imposing an additional nuisance rate or an unconditional training-sample moment condition.
- **2 points: Oracle variance and conclusion.** Verifies the conditional centering and cross-unit independence of potential-outcome residuals given the full design, obtains exactly zero oracle cross-unit covariances, computes the diagonal variance, and passes it to the limit by propensity convergence and dominated convergence. Controls the oracle-remainder covariance and proves convergence in probability of the conditional variance. Correctly identifies the resulting expression as the standard iid ATE efficiency benchmark.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation, its particular sensitivity constant, or its choice of conditioning notation. The pairwise dependence estimate must be derived rather than assumed unless a valid alternative directly supplies the needed remainder control. A flaw in one attempted derivation should not erase credit for later steps when the necessary estimate is independently established correctly. Conversely, without that estimate or a valid substitute, the nuisance-remainder conclusion is unsupported.

The reference proof now explicitly closes the reciprocal-count estimates, Efron–Stein application, focal-cell covariance term, and conditional-mean shifts. Do not treat any of these paper-specific dependence conclusions as supplied assumptions in the public task.

Identification need only be shown to the extent required for the conditional means, variances, and residual centering used in the proof. Unconditional independence alone is not a justification for independence after conditioning on the design; the product structure and exogeneity assumptions provide that justification here.

The experiment has deterministic period budgets and serves exactly the arrived, previously unserved units according to the stated priorities. It does not permit outcome-dependent budgets, additional eligibility restrictions, or data-dependent changes of the fixed queue policy. The estimator need only be analyzed for `n>=n_0`.

Zero-probability arrival cells can be omitted after showing they are null almost surely. Do not require all queue or period probabilities to be positive, exclude `beta=c_k`, or assume the limiting variance is strictly positive. The dependence argument can handle `n=2` directly or absorb finitely many small sample sizes into its constant.

The conclusion concerns variance conditional on training and convergence in probability over training. Do not demand convergence of the unconditional variance averaged over the training distribution. The iid efficiency interpretation is a standard comparison result, not a request to establish a new efficiency lower bound for the dependent queue experiment. No asymptotic-normality or experimental-design optimization result is part of this task.
