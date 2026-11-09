# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **DKW p-value construction and validity (2 points).** Defines the Kolmogorov statistic and truncated exponential p-value, and proves its super-uniformity under each true CDF using DKW. A nonstrict DKW tail bound may be used directly or obtained from the strict bound by a limiting argument. Do not require a proof of the standard DKW inequality itself.
2. **E-value calibration and band containment (3 points).** Uses the fixed e-calibrator's monotonicity and integral condition to establish null e-value expectation at most one. Correctly relates the generalized-inverse threshold to the displayed clipped bands, including the zero-inverse convention. Establishing that the closed band contains the strict e-value acceptance region, or directly proving that band miscoverage implies threshold rejection, is sufficient. Exact equality of the closed band with the strict acceptance region is not required and need not hold at the boundary.
3. **Post-selection aggregation (3 points).** Derives the miscoverage indicator bound by the e-value divided by the random threshold and sums over the data-dependent selected set, enlarging to all candidates without assuming selection independence. The required indicator relationship is an inequality, not equality.
4. **FCR conclusion and edge cases (2 points).** Takes unconditional expectations to obtain FCR<=delta and correctly handles empty selection and any zero-inverse/trivial-band case.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, do not insist on explicit candidate confidence-set construction if the needed miscoverage implication is proved directly.

Do not penalize a solver for rejecting an exact strict-inversion identification: the reported bands are closed. An erroneous equality at the boundary is a local proof error when the needed one-sided implication follows from the solver's argument; assess it under the usual readily repairable-error category rather than treating exact inversion as a required step.

The theorem concerns each fixed calibrator, not a calibrator chosen adaptively from the observed data. Arbitrary dependence between configurations and arbitrary measurable full-data selection are allowed. No continuity, moment, or selection-independence assumption should be demanded.
