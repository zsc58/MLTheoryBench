# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Establish a single high-probability Gram concentration event from the stated iid, independent-coordinate, covariance-normalized random-feature assumptions. Give the relevant concentration statement and verify its hypotheses. Derive sufficient spectral and inverse-Gram estimates and check that the effective-dimension assumptions make their deviations small. Do not take an infinite union over iterations.
2. **(3 points)** Verify quantitative first-step conditions and prove their induction: positive-label coordinates remain active, negative-label coordinates remain inactive through sufficiently negative frozen dual coordinates, and residual and dual-norm bounds are maintained. State the conditions actually used and derive their propagation. Check the initialization/step-size constant compatibility. Merely naming a stabilization method is insufficient.
3. **(2 points)** Reduce the fixed-pattern tail to linear least-squares gradient descent and prove parameter convergence to the projection of w^1 onto {w:X_+w=y_+}, including X_-w^infty<=0. A spectral residual contraction together with preservation of the null-space component is sufficient.
4. **(1 point)** Establish existence and uniqueness of w^star and derive its KKT/subset representation, or an equally valid comparison characterization. If using KKT, verify applicability, complementary slackness, and the precise remainder set on which the row-span coefficients vanish.
5. **(2 points)** Prove both parameter-distance bounds with the stated constants and sqrt(n_-)/sqrt(L) scaling. A prediction-space proof must justify both sides of any estimate before squaring a discrepancy and justify the conversion back to parameter space. Check the C_alpha^2 dependence of the lower-bound constant.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the public assumptions and target. Do not require the reference notation or ordering, its six-condition formulation, or separate invocations of every indexed source lemma. A single operator concentration event may supply all needed spectral and inverse estimates.

Omission of either matching bound, failure to establish activation stabilization, or an unverified replacement of the concentration/invariant argument is theorem-critical. Correct use of an independently stated standard concentration result is allowed; unexplained invocation of a paper-specific stabilization theorem is not a completed proof step.

Neither label-sign subset is assumed nonempty. Account for n_-=0, where the distance is exactly zero, and for an empty positive-label set, where the tail is constant and the projection set is the whole space. A generally valid argument using empty-block conventions suffices; do not demand a separate case split when it is unnecessary. A merely omitted routine empty-block explanation can fall in the 8-9 band, but an essential division by an undefined empty-block eigenvalue must be repaired.

The repaired reference closes all listed obligations. No private GT quality warning remains.
