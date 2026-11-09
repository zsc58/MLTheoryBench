# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Uses the correctly oriented factorization and fixed-positive-dispersion divergence on the nonnegative extended-value domain. Distinguishes inner data/reconstruction 0/0=0 from outer update 0/0=1. Recognizes that a finite current objective requires positive reconstruction only at positive data entries.
2. **3 points:** For fixed D, constructs the E auxiliary using normalized log-sum/Jensen weights at positive-data entries and the tangent inequality for log(alpha+x). Includes the constants needed for equality and proves global majorization and equality at E^t. Handles zero weights without undefined logarithmic products and treats zero-data negative-log terms as zero.
3. **3 points:** Calculates the E and D scalar auxiliary coefficients and minimizes on the nonnegative domain. Covers positive logarithmic coefficients, purely linear terms, and flat terms; proves that a zero outer denominator entails a zero outer numerator; and derives both displayed update formulas. A derivative-zero argument alone does not cover boundary or flat minimizers.
4. **2 points:** Verifies the D-side majorization and tightness, proves that the selected auxiliary minimizers have finite objective so that subsequent alternating updates are defined, and concludes MM descent. Zero reconstructions at zero data entries are allowed and must not be excluded by an open-domain minimization argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Tangency here means equality of auxiliary and objective at the current iterate, not a differentiability assertion at boundary coordinates. Flat coordinates need not have unique minimizers, but retaining them must implement the task's convention.

Deduct for treating an internal auxiliary-function result as an assumption, omitting either update direction, changing dimensions or the fixed-dispersion contract, replacing the permitted nonnegative data or factors by strictly positive ones without covering the remaining cases, or leaving either kind of quotient undefined. Do not accept a claim that the update always preserves strictly positive reconstruction at zero data entries. Neither convexity of the fixed-factor divergence nor convergence to a global optimum is required or generally justified. The point totals assess proved obligations; no specialized external algorithmic result may substitute for deriving the two auxiliaries and their minimizers.
