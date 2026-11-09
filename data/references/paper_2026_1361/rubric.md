# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establish that the defining terms are finite apart from the allowed infinite entropy value, prove properness and a lower bound, obtain sufficient entropy/moment control and compactness, justify the limiting argument, and prove existence of a minimizer. A valid alternative existence argument receives equal credit.
- **2 points:** Derive absolute continuity and strict positivity of a minimizer, compute the first variations, and obtain the normalized nonlinear Gibbs equation with finite positive normalizer.
- **3 points:** Prove uniqueness of the minimizer and of every Gibbs solution in the stated domain, and establish the drift estimates needed by the chosen dynamical proof. Strong displacement convexity and its transport-support inequality are one valid route; another complete route is acceptable. Merely showing that a Gibbs solution is mixture-critical and asserting that it must minimize is insufficient without a valid implication. Quadratic growth is an optional private consequence, not a separately required public conclusion.
- **2 points:** Prove global strong well-posedness with the stated initial-variable/noise interpretation, finite second moments and W2 continuity, derive the weak Fokker-Planck formulation, identify the regular-density Wasserstein gradient-flow structure and energy dissipation under the public qualification, and prove stationarity and invariance of the minimizer.
- **1 point:** Use a valid coupling argument and Gronwall, or another complete argument, to prove contraction at the stated rate delta and convergence to the invariant minimizer.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's order, incidental estimates, displacement-convexity presentation, or optional quadratic-growth conclusion. The fixed public constant is L_mu=m L_H sqrt(m-1)+eta L_q. A solver may establish a sharper intermediate bound, but must recover the public estimate under its stated delta>0 hypothesis. A coupling proof must control both state and law dependence and start from an optimal initial coupling, or explicitly take the infimum over initial couplings.

The parameter range includes eta=0 and m=1; empty products and vanishing interaction constants must not be excluded. The gradient-flow claim is the smooth-density continuity-equation identification, not an additional demand for EVI or maximal-slope identification of arbitrary weak solutions. The dissipation identity is required only in the stated regular setting and for almost every positive time. Equivalent analytic justifications of the differentiations and integration by parts are acceptable.

A stationary weak PDE calculation must also justify preservation of that law by the SDE. Pathwise uniqueness alone does not identify a stationary weak PDE solution with the SDE law. A valid route is uniqueness for the frozen linear forward equation in a class containing both the constant Gibbs curve and the frozen SDE law. This may be proved by the reference proof's mollified-drift duality argument, by another complete argument, or by a precisely stated standard-independent theorem with its hypotheses checked. Do not require uniqueness in a larger weak-solution class than the argument needs.

The audited standard entropy variational inequality and entropy displacement-convexity/transport-support results may be cited with their relevant hypotheses checked. If an optimal transport map is used, its existence must be justified. The standard quadratic-cost Brenier theorem is applicable when both laws lie in P_2 and the source law is Lebesgue absolutely continuous; a Gibbs law's positive C2 density verifies the latter condition. A valid coupling-based alternative need not introduce an optimal map. Routine application of a correctly identified standard theorem need not reproduce that theorem's proof.

A bare paper-specific theorem name or unspecified specialized method does not replace a missing proof obligation. The private reference proof has no outstanding quality warning.
