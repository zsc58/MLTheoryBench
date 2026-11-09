# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes a valid descent estimate for the allowed norm class, with correct gradient normalization and curvature control. In the general batch argument, this includes ||grad L_B-grad L||_sum<=2(m-1)R H and the resulting coefficient rho=gamma-4(m-1)R, with a quadratic stepsize remainder. Alternatively, after proving that rho>0 forces m=1, a complete full-batch descent argument earns the same credit without an unnecessary general mini-batch calculation.
- **3 points:** Establishes eventual low-loss entry from the stated general stepsize assumptions, obtains the decay and unnormalized-margin estimates needed for all three sums in the requested rate, and normalizes correctly while accounting for arbitrary W_0. The reference route uses H=(1/n)sum_i(1-p_{i,y_i}), H/L>=1-nL/2, the exponential loss-decay estimate, and both upper and lower weight-growth bounds. A complete alternative proof of the same rate earns full credit.
- **2 points:** Proves gamma<=2R for both entrywise and Schatten norms, including endpoint norms, and concludes that rho>0 forces the positive integer m to equal one. Explains why this identifies the guarantee as full-batch and makes the margin gap nonnegative.
- **3 points:** Verifies separability of the two-sample construction and analyzes every batch-one SignSGD realization. The reference argument proves theta_t=c_t(1,-1), obtains opposite margins, and concludes L(W_t)>=log(2)/2 for every t. The result must cover arbitrary positive stepsizes and ties in classification; a different complete argument is equally acceptable.

# Evaluator Notes

Accept a complete valid alternative proof and do not require the reference proof's ordering or incidental intermediate lemmas. In particular, proving full-batch collapse first is allowed.

Do not require a separate lower bound on ||W_t|| if a solver supplies another correct normalization argument. For example, a nonnegative margin lower bound can be combined directly with the norm upper bound in the ratio, with any needed case split. An unsupported replacement of ||W_t|| by the cumulative stepsize in the denominator of a numerator estimate is a gap, but absence of the reference proof's particular denominator repair is not itself an error.

The cross-entropy proxy used by the reference proof is H=(1/n)sum_i(1-p_{i,y_i}), not the exponential loss. Incorrect-class softmax coefficients sum to 1-p_{i,y_i}, not to one. A solver may use another proxy only if its required estimates are established correctly. Do not award completed-step credit for simply naming a paper-specific lemma or specialized method without deriving the needed result.

The stepsize assumptions in part (a) do not include polynomial decay or square summability. The low-loss starting index must support every use of the recurrence from that index, and the arbitrary initialization term must be retained or legitimately absorbed. Normalized quantities must be defined on the asserted range. Part (b) is not restricted by part (a)'s stepsize conditions.

Failure to establish the full-batch collapse or the invariant counterexample, or an unresolved substantive gap in the requested rate, is a major missing conclusion. Mere local notation errors that do not affect an otherwise complete proof should be treated as readily repairable.
