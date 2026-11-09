# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes existence and almost-sure weak convergence of the limiting predictive kernel under the compactness, equicontinuity, and signed-drift assumptions. Correctly handles the martingale's pathwise, rather than deterministic, boundedness, extends from countably many covariates and thresholds, and uses continuity of the mean limiting CDF to identify the finite-grid limits.
- **4 points:** For finite linear projections, constructs a uniformly integrable martingale after subtracting cumulative conditional drift, checks terminal L1 convergence, verifies both domination and vanishing of the maximal tail-array increments, and proves convergence of the realized squared increments. Establishes conditional negligibility of the scaled drift remainder using the stated domination, not just its almost-sure convergence. Applies an appropriate conditional martingale CLT with the conditioning sigma-algebra G_n and obtains multivariate conditional convergence on one probability-one event, for example by rational projections and tightness.
- **2 points:** Proves R_n->V and V_n->V almost surely using the fourth-moment condition and the assumed U_n->V. Supplies the weighted-law hypotheses and normalizations or an equivalent valid argument, aligns increment indices with their filtrations, handles the single-term tail shift, and upgrades scalar quadratic-form limits to matrix limits. Recognizes that U_n convergence is an assumption rather than an additional estimation theorem.
- **2 points:** Uses G_n-measurability of either covariance estimator, its almost-sure positive-definite limit, and eventual invertibility to justify conditional studentization. Derives exact limiting conditional coverage for the defined ellipsoids, scalar-normal marginal intervals, and exact-quantile studentized maximum bands. Gives the stated conservative coverage conclusion for ellipsoid coordinate projections and does not identify them with nominally calibrated marginal intervals when m>1.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its order of steps. Merely naming a martingale CLT or a weighted strong law without checking the relevant hypotheses does not earn the corresponding step. Realized quadratic variation must not be silently replaced by predictable quadratic variation without justification.

Almost-sure convergence of a future-dependent remainder alone does not justify transfer of an almost-sure conditional limit. A valid argument must establish its conditional negligibility; the integrable tail-envelope argument in the reference proof is one option.

Convergence of characteristic functions on a dense set requires a valid tightness or equivalent extension argument. Matrix convergence can be obtained from finitely many polarization directions; no unproved uniformity in all directions is necessary.

All limits concern the fixed finite evaluation grid and the conditional law of the random limiting predictive vector given G_n. Do not require exchangeability, independence of future covariates from past responses, uniform bands over an infinite covariate set, or frequentist coverage of an unrelated fixed data-generating parameter.

U_n means the exact conditional expectation in the problem. The theorem does not assert consistency of a Monte Carlo approximation, an empirical substitution for the covariate law, or a fixed-size simulated Gaussian quantile. The covariance matrices may be singular initially; the explicitly allowed convention before positive definiteness is sufficient.

Ellipsoid coordinate projections have limiting conditional coverage at least 1-alpha, generally strictly larger for m>1. Exact nominal marginal coverage belongs to the intervals calibrated with z_{1-alpha/2}. The simultaneous bands use the maximum of coordinate-standardized Gaussian errors and the corresponding exact quantile.

All reference-proof obligations are closed. The private source corrections are a limiting-CDF symbol correction and an initial-value normalization of the martingale; neither changes the public assumptions or mathematical target.
