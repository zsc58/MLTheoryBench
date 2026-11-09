# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Define the empirical CDF of the true iid innovations and establish its uniform convergence to the innovation CDF, or invoke and correctly apply an equivalent empirical-process result. The fixed initial offset does not change the iid experiment.
2. **3 points:** Derive quantitative control of the normalized-residual error \(\Delta_t=\widehat\eta_t-\eta_t\). Account for inverse-volatility stability on an event of probability tending to one, the bounded-gradient control of volatility-argument perturbations, mean and volatility estimator errors, and the fitted-residual identity. Conclude that the sample-average error is \(o_p(1)\), or establish another sufficient empirical perturbation control, such as a vanishing fraction of errors exceeding each fixed positive threshold. Merely naming a normalization or consistency method earns no credit for this step.
3. **3 points:** Obtain a uniform two-sided comparison between the fitted-innovation empirical CDF and translated true-innovation empirical CDFs. For the smooth-cutoff route, control the product difference by a constant times \(\psi\|\Delta_t\|_1\), using correct indices and absolute values, and establish both sandwich directions. Award equivalent credit for a correct direct indicator comparison or another valid uniform transfer argument; smooth cutoffs are not mandatory.
4. **2 points:** Combine the comparison with empirical-CDF convergence and uniform translation continuity of the continuous multivariate CDF, taking limits in a justified order to conclude \(\sup_y|\widehat P_T(y)-P(y)|\to_p0\). Continuity must provide uniform, not merely pointwise, control over thresholds.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the particular cutoff formula, norm, constants, index notation, or source proof organization. Equivalent arguments should receive the corresponding core-step credit.

For example, a direct comparison may use the empirical fraction of indices with \(\|\Delta_t\|_\infty>\delta\), together with translations by \(\pm\delta\) in every coordinate. A proof need not separately establish the average-error bound if it rigorously establishes another sufficient perturbation criterion. Treat the absence of any sufficient perturbation control, or of a valid two-sided uniform transfer, as a theorem-critical gap.

The iid multivariate Glivenko–Cantelli theorem and the law of large numbers may be invoked with their hypotheses checked. Uniform translation continuity may be justified directly or by a correctly stated standard result applicable to continuous joint CDFs. Do not assume that an arbitrary continuous function on an unbounded domain is uniformly continuous; the CDF structure is relevant.

Do not require independence between the fitted functions and the innovations, coordinate independence, a density, stationarity of the observed process, an upper bound on the true volatility, or moments of the observations or residuals. These are not task assumptions. The evaluated inverse exists almost surely by the public definition's explicit domain condition; its uniform lower bound on a high-probability event must still be established for quantitative error control. The correct bounds are \(g_i\ge c\) and \(\widehat g_i>c/2\) on that event, not the reverse.

For a smoothing proof, holding the smoothing parameter fixed while taking \(T\to\infty\), then removing smoothing, is sufficient. Letting it grow with \(T\) requires additional justification from the proved error control. A proof that only cites a named specialized method without deriving or validly establishing the required estimates should not receive the corresponding step credit.
