# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly works in the conditional experiment at an arbitrary history, justifies well-defined release conditioning, and derives the Bayes mixture formula for 0<q<1. Handles q=1 directly or by another well-defined argument that does not leave a probability conditional on an impossible exclusion event undefined.
- **3 points:** Uses a valid coupling or equivalent argument to compare batches with and without the record. Uses conditional Poisson independence, applies the sensitivity shift to the threshold distance, and passes correctly from pointwise acceptance bounds to averaged acceptance probabilities.
- **3 points:** Justifies the required Gaussian survival-ratio control over the clipped domain and obtains the stated endpoint constant. A correctly applied standard Gaussian hazard-monotonicity result, its elementary derivation, or an equivalent valid argument is acceptable.
- **2 points:** Converts the acceptance comparison into the claimed inflation bound, obtains the probability cap where needed, and states the history-independent minimum bound and the effective-rate bound using q_cond=q*rho.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, separate p1>=p0 and p1<p0 cases, or a literal supremum calculation if an equivalent argument establishes the claimed constant.

The proof must cover the full stated range 0<q<=1. Defining p0 as a probability conditional on exclusion and using it at q=1 without a separate case or a valid independent definition leaves an endpoint gap. If the rest of the proof is correct, this is ordinarily a readily repairable omission consistent with the 8-9 band, not grounds for rejecting the general argument.

The claimed minimum must be justified throughout the parameter range. This can be done by establishing both upper bounds, by a stronger estimate implying the minimum, or by a correct parameter-regime split. At q=1, the result is immediate and no Gaussian-ratio argument is required. Likewise, do not demand an unnecessary bound in another regime where a proved bound already equals or improves on the claimed minimum. Missing Gaussian-tail control in a regime where it is needed, or failure to obtain the probability cap when it is the smaller term, is a substantive gap.

Do not accept an identification of the mixture acceptance probability q*p1+(1-q)*p0 with a single-state Gaussian tail. A pointwise comparison must be averaged using the same law of the remaining sampled records. The sensitivity bound need not be attained, and the final bound need not be sharp.

The Gaussian hazard fact is standard independent background, with positive noise scale. Solvers need not reproduce its elementary proof if they state and correctly apply it. No differential-privacy composition theorem, selective-Gaussian privacy theorem, or convergence argument is required.
