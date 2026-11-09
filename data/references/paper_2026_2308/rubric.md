# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the evidences and posterior definitions and rewrites each evidence-weighted IPM utility as the integral of a supremum of centered likelihood functionals. Handles zero evidence and disregards infinite evidence only after justifying its reference-measure-null status.
- **3 points:** Correctly compares the two suprema by the reverse triangle inequality or equivalent two-sided inequalities. Justifies the subtractions on the domain where they are used rather than subtracting two infinite quantities.
- **3 points:** Derives the growth-profile bound uniformly over the test class, obtaining the terms \(\int\omega(x)|\ell-\widetilde\ell|\,d\mu\) and \(\bar\omega|z-\widetilde z|\), and controls the evidence difference by \(\int|\ell-\widetilde\ell|\,d\mu\). An equivalent direct derivation of the combined weighted bound earns the same credit.
- **2 points:** Integrates with justified measurability and integrability and concludes the exact inequality on the full stated domain. Accounts for an infinite right-hand side and for the case of infinite \(\bar\omega\) with finite right-hand side, either explicitly or through a valid unified argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the growth-profile weighting or failure to account for the evidence-error contribution as a theorem-critical gap unless an alternative argument validly absorbs that contribution.

The public task does not assume \(\bar\omega<\infty\), nor does it assume that the right-hand side is finite. It excludes only the undefined difference of two infinite utilities. In the reference route, finite \(\bar\omega\) gives integrable envelopes and finite utilities by Tonelli. If \(\bar\omega=\infty\) while the right-hand side is finite, the likelihoods agree almost everywhere, and equality of the utilities finishes that case. An infinite right-hand side is immediate. These are routine cases: omitting them from an otherwise correct proof normally warrants the 8-9 range, not treating the main mechanism as absent. An unqualified use of infinity minus infinity is not valid.

No separate measurability assumption on a supremum of differences is necessary if the proof directly bounds the measurable difference of the utility integrands by a measurable uniform majorant. Symmetry is retained as a source assumption, but no use of symmetry beyond the given absolute-value IPM definition is required.
