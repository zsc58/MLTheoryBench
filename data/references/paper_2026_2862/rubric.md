# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Correctly uses the smoothness, oracle, interpolation, generalized-growth, fresh i.i.d. sampling, and parameter assumptions, and derives the conditional mini-batch variance bound by eliminating centered cross terms. Handles zero smoothness constants or gives an equivalent valid boundary argument.
2. **(4 points)** For the clipped update, verifies locality and rigorously controls nonlinear clipping and the smoothness remainder under the stated batch and step-size conditions. Accept the source's event-alignment and small-gradient estimates with a valid all-regime completion, the reference proof's uniform projection/polarization estimate, or another complete valid argument. Merely asserting alignment or nonnegative conditional descent is insufficient.
3. **(2 points)** Correctly aggregates the clipped conditional estimates, places iterate-dependent regime indicators inside expectations when using regime splits, telescopes, and obtains the complete four-term bound or a stronger bound implying it, including the sigma=0 consequence. Handles empty regimes and zero objective gap without dividing by zero.
4. **(2 points)** Derives the normalized one-step estimate using variance/Cauchy-Schwarz control, verifies locality and step-size absorption including zero gradients, telescopes, and obtains 4F0/(eta N)+8sigma/sqrt(B)+6lambda.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, redundant event calculation, or stronger constants. In particular, a uniform clipping estimate can replace the event split. The objective need not decrease conditionally at every iterate in the noisy case; unsupported use of such monotonicity cannot justify telescoping. Random regime sets cannot be treated as deterministic sets of indices outside expectations. The normalized absorption must not divide by L0+L1||h|| unless positivity is separately verified. The reference proof now closes both methods; there is no outstanding private GT warning. Interpolation need not be invoked when the proof only needs the stated lower bound and growth assumptions. Propagate dependency failures only when the corresponding downstream conclusion is unsupported.
