# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (2 points):** Correctly sets up the pointwise decomposition through the nearest training-grid point and uses the Hölder seminorm assumptions to bound both spatial increments, obtaining a bound of the form $e_y\le 2e_{\operatorname{nn}(y)}+8c^2\beta^{2\alpha}$ for unseen points. Justifies the elementary square estimate, either directly or by a standard two-term square inequality.
- **Step 2 (3 points):** Correctly aggregates unseen-point bounds by nearest-neighbor assignments and shows each training error is reused at most $\nu-1$ times among unseen points. Recognizes that each training point is uniquely assigned to itself. It is valid to use either the individual count bound or the exact identity that the maximum unseen assignment count equals $\nu-1$.
- **Step 3 (3 points):** Combines unseen and training-grid contributions with the correct cardinality normalization and integrates over the fresh test input to derive
  $E_\mu(\widehat F_n,G,Y_{\mathrm{test}})\le (|Y_{\mathrm{train}}|/|Y_{\mathrm{test}}|)(2\nu-1)E_\mu(\widehat F_n,G,Y_{\mathrm{train}})+(1-|Y_{\mathrm{train}}|/|Y_{\mathrm{test}}|)8c^2\beta^{2\alpha}$.
- **Step 4 (2 points):** For fixed grids and a common $\alpha,c$ across $n$, correctly concludes that training-grid error tending to zero gives a limsup test-grid error bounded by the coverage term. Explains that this term is at most $8c^2\beta^{2\alpha}$ and becomes arbitrarily small as $\beta$ decreases, with the $c=0$ case immediate.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The risk is a population error on an output grid, not empirical error on the training dataset. The learned operator is held fixed when taking the expectation over the independent fresh input. Do not require an outer expectation over training data.

Measurability is supplied by the task. Nonnegative extended expectations are allowed; do not impose extra finite-moment assumptions. A proof using integration of the nonnegative pointwise inequality is sufficient.

The exact maximum-count equality used in Step 2 is correct, not a source error. Optimization of the tie-breaking rule need not be analyzed separately once the prescribed assignment and its $\nu$ are fixed.

The conclusion must not claim that the test risk equals the coverage term, nor that finite-$n$ test risk is bounded by that term alone merely because training risk tends to zero. A uniform sample threshold across changing training grids is not required and does not follow from fixed-grid convergence alone.

Equal grids, singleton training grids, $c=0$, and $\alpha=1$ are valid cases. A general proof covering them need not discuss each case separately.
