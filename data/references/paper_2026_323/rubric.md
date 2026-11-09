# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Community and Gram concentration (3 points).** Establishes simultaneous community-count control with the stated failure budget, including a valid transfer from full community counts to the proportions excluding the focal vertex. Establishes off-diagonal adjacency Gram concentration with the stated failure budget by conditioning on the labels, checking independent centered bounded summands, and handling the exceptional columns. The reference proof retains the stronger tolerance epsilon_AP-2/n. It is not enough to quote concentration without checking these hypotheses and constants. Cases in which the requested probability lower bound is nonpositive may be disposed of directly.
2. **Data-dependent neighborhoods and population bias (2 points).** Uses the count event and the specified quantile convention to control all selected-neighbor dissimilarities. Uses the full diagonal-inclusive block matrix P. Handles equal-community pairs directly and justifies distinct-index representatives for different-community pairs from the count event. Obtains the required population-row bias estimate without invoking false diagonal Gram concentration. The reference proof retains the stronger bound 8(epsilon_AP-2/n).
3. **Centered cross-products and smoothing fluctuation (2 points).** Establishes a simultaneous distinct-row product event and expands the smoothing fluctuation with the correct number of ordered pairs. The reference proof uses conditional variance at most 1/16 to obtain M<epsilon_m/2 with failure probability at most n(n-1)exp[-n epsilon_m^2/(4(1+epsilon_m))]. The prefactor comes from a two-sided tail and unordered-pair union bound. Accounts for the exceptional columns, including the fact that A_ii-P_ii need not vanish. Justifies use of these uniform events for data-dependent neighborhoods.
4. **Correct row-wise constants (2 points).** Uses an exact noise-plus-bias decomposition and obtains 2/|N_i|+epsilon_m+2/n+16epsilon_AP simultaneously for all rows. Correctly counts |N_i|(|N_i|-1) ordered cross terms. If using the reference route, combines the half-tolerance cross-product event with the retained Gram slack. A derivation ending with larger constants does not by itself establish the requested bound.
5. **Probability and consistency (1 point).** Combines the three events without an independence assumption, obtains the exact stated failure budget, and uses |N_i|>=ceil(h(n-1)), the three exponent conditions, and the tolerance limits to establish uniform convergence in probability. Handles the stated finite-n domain, either directly or through the vacuous probability-bound cases.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental presentation choices, its particular slack allocation, or its stronger intermediate events if another argument establishes the exact target.

Do not reward an all-entry concentration claim for AA^T/n around PP^T/n: its diagonal entries generally have a Bernoulli-variance bias. Do not identify the full block matrix P with E[A | labels] on the diagonal. Do not assume a third same-community vertex without justification, or add a realized minimum community size as a hypothesis.

The source appendix's conversion of an ordered-pair sum to half as many terms is invalid. Merely invoking M<epsilon_m and then dropping the resulting factor of two is a substantive gap, not a completed constants calculation. Conversely, the sharper variance bound and exceptional-column slack supplied in the reference proof resolve this issue, so the requested constants are not unattainable.

A proof using an observed-versus-population squared-distance discrepancy instead of the public dissimilarity does not address the specified estimator unless an independent valid argument connects it to that estimator. There are no unresolved ground-truth obligations or specialized external dependencies to waive.
