# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives uniform effective-linearity and dissipative control for the tamed drift, establishes or validly justifies the polynomial increment estimate, and combines it with Gaussian moments to prove the Lyapunov drift. Explains why the state-dependent higher-order coefficients are absorbable for alpha<1/2, treats all real q>=2 including q=2, and obtains the iterated moment bound. The admissible upper step size may depend on q.
- **2 points:** Verifies the Feller property and constructs an invariant probability measure through tight Cesaro averages or another valid argument. Proves the uniform q-th moment bound for every invariant probability measure without assuming that moment is finite beforehand. A correct bounded-truncation argument or a precisely applicable standard Lyapunov integration result is sufficient.
- **2 points:** Establishes local generator convergence (Q_eta f-f)/eta -> Lf uniformly on compact sets for f in C_c^infinity, with the correct Gaussian normalization and justified Taylor remainder. Verifies the continuity and boundedness needed for subsequent weak convergence.
- **3 points:** Uses admissibility to obtain tightness, justifies passage of stationarity to weak limits including the off-compact contribution, applies the stated identification assumption, and concludes convergence of the full family. Supplies a fixed finite admissibility threshold independent of eta, the selected family, and the test function. In the reference argument, the off-compact bound is C_f eta^(-1) exp(-c_f/eta)+C_f M eta^[Q_*(1-alpha)-1], so Q_min=2 works.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require incidental presentation choices, the particular moderate/large-displacement split, or the smallest possible admissibility threshold. A different finite threshold satisfies the public existential target if its sufficiency and allowed dependencies are proved.

Naming a method without the corresponding hypotheses or necessary estimates is incomplete. In particular, direct cancellation of potentially infinite stationary Lyapunov integrals is not valid. Do not require arbitrarily high or eta-dependent admissibility orders; if a proof uses additional uniform moments, it must derive them rather than assume them.

Compact convergence alone does not justify integrating the discrete generator against varying invariant measures. Credit a quantitative off-compact estimate, a valid global estimate, or another complete argument. Do not require convergence of integrals with a discontinuous compact-set indicator: comparing the full integral with that of the bounded continuous function Lf avoids any boundary-mass issue.

At q=2, the state-independent Gaussian contribution is O(eta), not o(eta), and is allowed in the additive drift constant. Distinguish uniqueness supplied by stationary identification for the limiting generator from uniqueness of invariant measures of a fixed-step kernel, which is not assumed or required.
