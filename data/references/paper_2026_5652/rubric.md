# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **1 point:** Establishes the mean recursion, the potential identity, and the curvature inequality needed to make the target well-defined. Accounts for the positive feature scale and the zero-radius case, either explicitly or through an argument valid in that case.
- **4 points:** Proves high-probability uniform stability without assuming bounded original iterates. Localizes the recursion, constructs an adapted Poisson martingale starting at zero, derives valid deterministic increment envelopes and summation-by-parts remainder estimates, and closes the stated radius bootstrap. For the reference route, the scalar Poisson bounds are 192 m L^2 R^2 in sup norm and 224 m L^2 R times the iterate difference; these give the martingale coefficient 384 and remainder coefficients 576 and 672. Bounds on stopped iterates are needed only where the associated coefficients are nonzero. The first-exit argument must retain and control the potentially overshooting exit iterate.
- **3 points:** Derives the weighted-average residual decomposition and validly controls its telescoping, additive, and iterate-dependent multiplicative Markov terms to obtain the stated fast bound uniformly in T. For the reference route, the multiplicative remainder coefficient is 192, and collecting the additive and multiplicative bounds gives coefficients 528 and 352 in the residual numerator. A valid tighter bound also suffices. Converts residual control to the potential bound without assuming A is symmetric.
- **2 points:** Uses the energy identity, valid localized scalar-noise control, and convexity to prove the stated robust bound. Establishes stability and both rates on one event with probability at least 1-delta, uniformly over all requested times.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular internal constants when valid bounds imply the stated constants. Merely invoking mixing, a Poisson equation, or concentration without deriving the iterate-dependent localization control does not satisfy the 4-point stability step.

The standard independent Euclidean martingale maximal inequality may be cited, but its hypotheses must hold: the martingale starts at zero, the increments are adapted martingale differences, and their deterministic squared norm envelopes are summable. Concentrating after conditioning on the future event that all original iterates are bounded is not a substitute for localization. The chain need not start in stationarity.

The scalar concentration event can be reused for stability and the robust bound. Neither four distinct events nor independence is required; any valid allocation proving the requested common probability is acceptable. A discrete first-exit contradiction does not require continuity of the recursion. Do not require divergence of the sum of stepsizes, reversibility, or additional curvature-dependent stepsize restrictions.

A proof that establishes only one rate cannot receive credit for the missing final-rate step. The existing source multiplication typo is corrected to 192 throughout the reference calculation; reproducing 92 is not required or accepted as justification for that estimate.
