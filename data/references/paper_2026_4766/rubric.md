# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Model, information structure, and density setup (2 points).** Uses the natural prior Brownian filtration and the hierarchical observation kernel, rather than assuming that the intensity-only conditional law controls an arbitrary filtration. Correctly defines a conditional density on the event-sequence space, including the empty observation, and verifies the initial-enlargement hypothesis. The density may be assumed as in the task or derived from the Poisson likelihood. A proof must not infer strict positivity of paths from Lipschitz coefficients alone.
2. **Likelihood factorization and score covariation (4 points).** Derives the past/future factorization of the conditional density for a fixed event sequence, with future factor equal to the specified prior exponential/product expectation. Computes its Brownian covariation as the past factor times c partial_v beta dt, yielding c h dt after division by the density. Handles the intervalwise nature of the calculation and explains why there is no omitted contribution at the finitely many event times. Forms original-filtration covariations with a fixed observation index before evaluating at Y. Merely naming a score or filtering method is insufficient.
3. **Enlarged Brownian decomposition (2 points).** Applies a valid initial-enlargement theorem, or an equivalent conditional change-of-measure argument with verified hypotheses. Establishes that the corrected process is a continuous local martingale with quadratic variation t, hence Brownian in the appropriate enlarged filtration. The theorem may supply the compensator's local integrability; a separate global Novikov assumption is not required.
4. **Full-horizon posterior conclusion (2 points).** Explains why the density is constant, and the correction zero, after S. Substitutes the Brownian decomposition to obtain the correction c^2 h and unchanged coefficient c. Retains v_0, handles the zero extension of h, and gives the conditional-law interpretation for the law of Y-almost every observation. Brownian independence from the initially revealed sigma-field is sufficient for this last point.

# Evaluator Notes

Accept a complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation or unit-rate-Poisson presentation. Standard SDE moment estimates, Brownian martingale representation, Itô's formula, the density-based enlargement theorem, and Lévy's characterization may be invoked with their relevant hypotheses checked; re-proving them is unnecessary.

The score need not be smooth across an observed event time. An intervalwise calculation together with continuity and absolute continuity of the density martingale's Brownian bracket closes that issue. The empty observation is covered by an empty product, and neither a nonzero diffusion coefficient nor parameter-differentiability assumptions are required.

Treat an unsupported drift assertion, a missing factorization or covariation calculation, or an actual use of p(Y) as an original-filtration martingale as a theorem-critical gap. Purely abbreviated bracket notation is not by itself a major error if the surrounding argument clearly computes at fixed y before evaluation. Do not require a claim for every deterministic observation, including observations in a conditional-law null set.
