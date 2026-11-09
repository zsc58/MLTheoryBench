# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Pseudo-posterior concentration (2 points).** Establish exponential separation of the likelihood away from the empirical mean and a subexponential lower bound for the posterior denominator using the strictly positive prior-density lower bound. Verify feasibility on the interval used for the lower bound, including when tau_n=0. Deduce concentration near the true mean and that the zero-denominator completion occurs with probability tending to zero.
2. **Vanishing tilt (2 points).** Establish uniform local curvature and root control on events where the empirical variance is bounded away from zero. Combine this with posterior concentration and convergence of the empirical mean to prove posterior concentration of the tilt at zero. A correct argument must not require continuity of the regularizer in the candidate mean.
3. **Predictive consistency (2 points).** Derive a sufficient Wasserstein comparison between a fitted distribution and the empirical law. Justify posterior averaging using boundedness of Wasserstein distance on the observation interval and a small-tilt/large-tilt split, or an equally valid argument. Combine with empirical Wasserstein convergence. Posterior convergence in probability of the tilt alone does not justify integrating an unbounded function of the tilt.
4. **Oracle log-growth (4 points).** Establish uniform convergence of the predictive log objective, uniqueness of the true-objective maximizer, and convergence of the selected coefficients, or an equivalent valid route to oracle growth. Identify the true conditional mean of each realized log increment as M evaluated at the selected coefficient, not as its predictive objective M_n. Control the martingale differences and justify averaging the true conditional means, for example through bounded L1 convergence and Cesaro summability. Prove both realized convergence in probability and expected normalized log-growth convergence, and the almost-sure realized variant under almost-sure predictive consistency.

# Evaluator Notes

Accept any mathematically valid alternative proof. The precise constants in the reference likelihood and Wasserstein bounds are not required. A direct valid oracle-value argument may replace coefficient convergence.

The prior lower bound must be strictly positive, not merely finite or nonnegative. Do not impose tau_n>0, full support of the prior, continuity of H_mu, or positivity of every finite-sample denominator. The stated initialization and zero-denominator conventions are part of the task; their asymptotic irrelevance must be justified. Empirical weights refer to the empirical component and must not absorb regularizer mass at coincident atoms.

Standard probability and Wasserstein results may be used when their relevant hypotheses are checked. Do not award credit for merely naming a specialized method or a source-specific consistency result in place of proving the requested chain. Theorem-critical gaps in concentration, tilt control, posterior averaging, or the oracle-growth bridge are major; readily repairable local slips should be treated according to the general scoring guide.
