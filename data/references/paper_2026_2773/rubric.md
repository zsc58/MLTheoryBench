# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Establish square integrability and the correct first-order expansion for the fixed oracle AIPW kernel on iid augmented observations. Identify its projection as h_1^mu(hat Y)+xi^*[h_1(Y)-h_1^mu(hat Y)]/pi_tau^*(X)-theta*. Justify the o_p(n^-1/2) remainder using the fixed-order square-integrable Hoeffding decomposition. Nondegeneracy is not what bounds the higher-order remainder.
2. **3 points:** Establish learned-to-oracle equivalence at the full-statistic root-n scale under the actual learned-policy dependence. A complete approach privately constructs shared fresh uniforms, derives conditional centering and the O(Delta_n) second-moment bound, and uses overlapping-tuple covariance counting to obtain O_p(n^-3/4) for the full statistic. The scalar HT comparison can then recover the learned first-order expansion. Alternatively accept any fully justified route to the required full-statistic o_p(n^-1/2) comparison. A scalar first-order comparison alone does not justify the learned-policy remainder.
3. **3 points:** Apply the iid oracle CLT and Slutsky to obtain the asserted learned-policy Gaussian limit. Verify the mean, finite variance, and variance identity by conditioning on both X and Y. Establish sigma_*^2>=r^2 Var(h_1(Y))>0.
4. **2 points:** Prove consistency of both variance components, including changes in labeling indicators as well as denominator weights. Only integrability is available for the squared projection and squared residual weights; do not assume fourth moments. Identify the sum of the limits with sigma_*^2, justify the positive-part standard error, and deduce limiting coverage 1-alpha.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its exact O_p(n^-3/4) strengthening if the needed little-o comparison is proved, or an explicit coupling if another argument establishes the same distributional conclusion.

The following are theorem-critical gaps: treating learned-policy observations as iid without justification; invoking an oracle Hoeffding expansion for a learned kernel without controlling its remainder; comparing only the first-order HT terms and never connecting that comparison to the full statistic; applying a fixed-indicator lemma without accounting for changed indicators; or requiring an unstated fourth moment to control the variance estimator.

A correct argument may replace the source's second-moment formulation of its fixed-indicator stability lemma by the elementary first-absolute-moment bound and separately control indicator mismatches. No particular named lemma is required.

The projection functions inside the variance estimator are the population functions explicitly supplied in the task. Do not require or award an additional theorem about estimating those functions. The score-building functions a and b are separate supplied functions.

The proof should cover fixed r>=1, tau in [0,1], and probabilities equal to one. Events with zero learned probabilities and a nonpositive raw variance estimate are handled by the public conventions and their asymptotically negligible probabilities. Omitting a brief verification of such a convention is readily repairable when the necessary positivity conclusions have already been proved; omitting strict positivity of the limiting variance is not automatically harmless for the coverage claim.
