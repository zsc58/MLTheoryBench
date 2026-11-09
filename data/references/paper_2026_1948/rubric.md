# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Robust static representation (2 points):** Derives the max-over-PSD-certificates quadratic transport formula using the support representation and valid minimax hypotheses. Checks finiteness, convexity, the relevant semicontinuity, and attainment of the certificate maximum. Establishes, or validly supplies, the metric properties needed later; the robust formula and trace comparison suffice.
2. **Static-dynamic equivalence (3 points):** Proves both directions. For displacement interpolation, constructs a genuine Eulerian velocity, for example by conditional expectation, and uses its covariance inequality; equality of pathwise and Eulerian covariances for arbitrary couplings is not valid. For the converse, verifies the integrability needed for superposition and applies PSD Jensen with the same endpoint coupling for all certificates. Uses the correct square-root normalization of the dynamic distance.
3. **LMO duality and local geometry (3 points):** Establishes the required primal minimization and dual-norm identities, and derives the local slope from the public differentiability hypothesis. Establishes metric absolute continuity and the speed bound from the dynamic action. It is sufficient to prove speed equality specifically for LMO solutions using the chain rule and local-slope inequality; a full tangent-space theorem is not required. Handles zero gradients, singular certificates, and possible nonuniqueness without imposing extra hypotheses.
4. **Gradient-flow identity (2 points):** Combines the chain rule, LMO identities, local-slope formula, and justified speed equality to prove the almost-everywhere energy-dissipation identity. Uses energy absolute continuity to obtain the integrated identity and the stated curve-of-maximal-slope conclusion.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation choices. Treat omission of either static-dynamic direction or the identification connecting the LMO, descending local slope, and metric speed as theorem-critical.

Do not require an inverse-certificate formula. The public LMO is a primal minimizer, and direct norm duality is valid at singular boundary cases. If a solution uses an interior inverse-trace minimizer, it must verify the saddle condition and cannot assume such a minimizer always exists. An arbitrary inverse-trace minimizing sequence need not yield primal minimizers, even if its velocities converge.

Do not accept the assertion that every continuity-equation velocity has norm equal to the metric speed. Nonminimal representatives generally only provide an upper bound. Equality for the prescribed LMO solution must be justified.

Do not accept a generic citation to metric-gradient-flow calculus as a substitute for the spectral local-slope identification. The public transport-differentiability condition supplies a direct route: optimal couplings and conditional expectation give one inequality, and deterministic perturbations give the other.

No additional ellipticity, absolute continuity of endpoint measures, strict convexity of the gauge, uniqueness of an LMO, or geodesic convexity of F is required. A proof confined to such an additional regime does not establish the full task.
