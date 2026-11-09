# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the assumed measurable quotient predictor and shows that population and empirical risks factor through the quotient under the invariance assumption. Do not require a construction of a measurable quotient predictor beyond the existence assumed in the task.
- **2 points:** Correctly transfers both posterior-averaged risks by pushforward integration. These equalities are deterministic identities for each sample and posterior.
- **4 points:** Establishes absolute continuity on the quotient, disintegrates prior and posterior over fibers, and derives the KL chain rule with the nonnegative integrated conditional KL \(\Delta_\pi\), rather than merely naming it. A complete derivation may construct the quotient density and conditional posterior densities from \(dQ/dP\), or use a valid equivalent argument. It must justify the relevant almost-everywhere conditional statements and the extended-value identity without subtracting infinities. The finite-parameter-KL case permits the stated subtractive reformulation.
- **2 points:** Applies an applicable sample-independent-prior PAC–Bayes inequality on the quotient, with the stated constants or a valid stronger bound, and uses risk preservation and KL monotonicity to obtain the requested bound and no-larger certificate. The argument must permit the posterior to depend on the certification sample and cover \(n\geq1\). It must also allow a finite quotient certificate even when the parameter-space KL is infinite.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, particular conditional versions, or its independent concentration derivation. A correct statement and application of the standard bounded-loss PAC–Bayes theorem is sufficient for the external inequality, provided its hypotheses, constants, and applicability to a sample-dependent posterior are checked. Merely naming the paper-specific quotient conclusion does not establish the requested risk identities or KL decomposition.

The KL decrease equals \(\Delta_\pi\) when the parameter-space KL is finite. The numerical decrease of the square-root complexity term is generally not \(\Delta_\pi\); do not require or award credit for that incorrect assertion. The task asks for a no-larger certificate, not strict improvement.

Do not demand finite parameter-space KL as a global assumption. An unrestricted expression \(\infty-\infty\) is not a valid proof of the additive identity or comparison. A valid extended-value argument may justify integration using finite negative parts or an equivalent rigorous method. No separate \(n=1\) case split is required if the proof already applies at that value.
