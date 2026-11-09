# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the given convex subdifferential relation for the quadratic-optimal coupling to place Y_t in partial psi_t(X_1), and obtains endpoint recovery, including the singular-target setting.
- **5 points:** Establishes the exact identity nabla psi_t*(y)=prox_{(alpha_t/beta_t) phi}(y/beta_t) for every y, using proximal optimality and conjugate inversion or an equivalent complete argument. Accounts for the existence and uniqueness of the proximal minimizer and the differentiability of psi_t* under the stated properness, lower semicontinuity, convexity, and positive-coefficient hypotheses. Merely naming proximal methods is insufficient.
- **3 points:** Expresses X_0 and X_1 as functions of Y_t almost surely, obtains the correct coefficients and proximal parameter in the field formula, and verifies that the displayed everywhere-defined Borel field is a version of the conditional expectation. Integrability follows from the finite second moments. Does not assert that arbitrary conditional-expectation versions agree at every y.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular elementary derivations of standard convex-analysis facts. Precise standard results may be invoked when their hypotheses are verified.

The potential and its almost-sure subdifferential relation are supplied in the task; independently proving their existence from optimal transport is not required. The interior-time conditions alpha_t,beta_t>0 must be respected, and no density of P_1 may be assumed. Extended-valued potentials and lower-dimensional effective domains are allowed.

The field conclusion concerns an everywhere-defined Borel version. A proof may obtain the identity almost surely and then explicitly choose the displayed Borel representative. It need not prove uniqueness of extensions outside the support of the law of Y_t or justify a pointwise identity for every possible conditional-expectation version.
