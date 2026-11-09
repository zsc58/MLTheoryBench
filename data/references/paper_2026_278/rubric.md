# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Formulate the sitewise centered estimating equations and obtain the counting-process martingale representation at beta_0, explicitly showing cancellation of every site-specific baseline hazard. Justify predictability and the compensator under the stated censoring and hazard model.
- **2 points:** Prove the needed uniform risk-set mean convergence and convergence of the normalized information matrices to A_S, including positive definiteness and invertibility with probability tending to one. Obtain the exact affine score identity, or a valid equivalent linearization, and establish consistency without circular reasoning. Consistency may be deduced after the score CLT.
- **3 points:** Derive the sitewise predictable bracket limits Sigma_k and justify the martingale CLT, including a small-jump/Lindeberg argument. Use site independence and n_k/n->p_k to obtain the weighted score covariance Sigma_S. A complete independent-summand asymptotic-linear representation and ordinary CLT may replace the martingale-CLT route.
- **2 points:** Combine the score CLT with the information limit to obtain the stated asymptotic normal law for sqrt(n)(beta_hat_S-beta_0), allowing singular limiting covariance and accounting for the vanishing-probability singular-information outcomes.
- **1 point:** Prove convergence of each empirical Sigmahat_k and Ahat_k, then establish consistency of the weighted sandwich by continuity of inversion. Identify n^{-1}Vhat_S as the estimator-scale asymptotic covariance estimate.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Exact affine linearization is fully sufficient; do not demand an intermediate parameter or a separate preliminary consistency theorem. Do not award credit for merely naming Doob-Meyer, a generic uniform law, a martingale CLT, or a sandwich estimator without verifying the centering, weighting, and applicable limiting conditions.

For uniform convergence, bounded marks multiplied by threshold indicators 1{Y>=t}, together with the strictly positive population risk denominator, provide a valid route. An unrestricted assertion that all bounded predictable classes obey a uniform law is not sufficient. For the martingale CLT, bracket convergence plus the O(n_k^{-1/2}) jump bound closes the essential conditions. Subject score integrals within a site share the empirical risk-set mean and need not be independent; orthogonality of the driving subject martingales is sufficient. Site scores themselves are independent.

Missing baseline cancellation or the limiting site-weight aggregation is theorem-critical. Propagate a failed sitewise limit only when the global CLT or covariance conclusion is thereby unsupported. Routine omission of an empty-set or singular-event convention is minor when the argument correctly shows that it is asymptotically immaterial.

Every integral is restricted to [0,tau]. A proof using event sums must retain 1{Y_ik<=tau}, unless it explicitly administratively truncates the observations at tau. No assumption that all raw observed times are at most tau may be introduced.

The limiting covariance need not be positive definite; zero or singular Sigma_S is allowed. The target is consistency for the covariance in the normalized limiting law, with the corresponding factor 1/n on the estimator scale. Do not require convergence of finite-sample second moments or accept weak convergence alone as proving such a claim.
