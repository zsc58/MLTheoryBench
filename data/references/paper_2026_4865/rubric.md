# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes a deterministic family of globally Lipschitz score estimates with a universal dimension-free Lipschitz bound, chosen independently of p and T. For an interpolation construction, verifies that the branches match and includes every derivative term. Justifies well-posedness of the resulting SDE.
- **3 points:** Proves exponential-time confinement from standard-normal initialization using the inner OU dynamics and a justified stochastic-convolution supremum estimate, or an equivalent valid method. Controls both grid values and within-interval increments if using a time partition, and chooses universal constants consistently over the stated horizon.
- **3 points:** Uses an appropriate measurable event to compare the output and shifted-target masses and derives the near-maximal total-variation lower bound for all stated times, with universal constants and a universal dimension threshold.
- **2 points:** Proves exponentially small target Lp score error for every fixed finite p, including both target-tail and pointwise-error bounds, the permitted p-dependent constants and dimension threshold, and use of the same field family as for the TV conclusion.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference construction or presentation, but do not award credit merely for naming a concentration or OU method without deriving the needed conclusion.

For the reference-style construction, a cutoff that rises from zero on the inner region to one on the outer region must multiply the outer drift, not the inner drift. A derivative bound inside the shell alone does not prove global Lipschitz continuity if the branches do not match. The pointwise score error and shell derivative must account for mu.

If a Gaussian-process argument is used, standard independent concentration theorems may be invoked with their relevant hypotheses checked. A square-root-time metric requires a time mesh of order epsilon squared. Combining that mesh with a sphere bound of order (C/epsilon)^d gives an exponent d+2, or any justified looser order-d exponent. The exact entropy exponent and numerical constants are not scoring requirements.

A fixed-time distributional identity or an unsupported time-reversal assertion does not alone control a continuous-time supremum. A complete confinement proof must justify the full interval control and the exponential number of intervals. Harmless constant changes, a shorter final interval, and T=0 may be handled by any valid local argument.

Do not demand the private auxiliary lemmas in their full generality: proving the needed estimate for one sufficiently large universal contraction constant is enough. The proof must not choose a different score field for each time or each p. The TV dimension threshold is universal; the score-error threshold may depend on p. Do not require constants uniform over unbounded p.
