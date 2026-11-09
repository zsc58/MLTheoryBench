# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the regularized confidence ellipsoid from the least-squares normal equations, a simultaneous self-normalized noise bound applicable to predictable features and conditionally sub-Gaussian noise, and \(\|\alpha^*\|_\Lambda\le C\). Verifies that the stated coefficient \(c\) dominates the resulting confidence radius.
- **2 points:** Uses the policy's maximizing property and confidence bound to obtain a two-width instantaneous-regret bound, then aggregates widths with the bounded-mean clipping, Cauchy--Schwarz, and the elliptical-potential inequality.
- **4 points:** Proves the characteristic spectral determinant bound. A valid route bounds the determinant by the product of its diagonal entries, sets coordinate masses equal to sums of squared feature coordinates, verifies their nonnegativity and total-mass budget, and applies the effective-dimension head-tail split to obtain \(\log(\det V_{T+1}/\det\Lambda)\le2d\log(1+T/\lambda)\). Handles \(d=N\) without referring to \(\lambda_{N+1}\). An equally valid alternative determinant argument receives full credit.
- **2 points:** Combines the estimates on a single event of probability at least \(1-\delta\) and substitutes the stated coefficient to obtain the exact cumulative-regret guarantee with its parameter dependence.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its order of presentation. Standard self-normalized martingale and elliptical-potential inequalities may be invoked with their relevant hypotheses checked; a needless union bound that changes the advertised confidence coefficient does not establish the stated result.

A valid argument controlling the determinant through the spectrum and effective dimension is theorem-critical. Exact axis-aligned maximization is not required and must not be treated as a valid substitute: the assertion that a jointly maximizing collection of unit-bounded updates can always be chosen along coordinate axes is false. Single-update maximization does not prove it. The continuous coordinate-mass upper bound is sufficient and does not require realizing the relaxed masses as a sequence of axis-aligned unit updates.

Do not penalize a solver for identifying and avoiding that false assertion. Conversely, a proof relying solely on it leaves the determinant step unjustified. Nonnegative, rather than strictly positive, coordinate masses are permitted. Zero noise, zero coefficient bound, the initial empty history, repeated eigenvalues, and \(N=1\) must not be excluded by added assumptions; these cases can be covered directly by the general argument.
