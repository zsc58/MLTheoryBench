# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes exchangeability of the k-NN calibration/test scores conditional on the independent reference sample and applies or proves the finite-sample rank bound. Handles ties for the lower bound, the infinity threshold when the calibration rank is n+1, and the stated tie-free upper slack in its optional regime. An accurately stated standard split-conformal theorem with verified hypotheses is acceptable in place of the counting proof.
- **3 points:** Justifies nesting of the neighbor-label sets and the equivalence between the rank-threshold event and membership in C_knn. Covers both finite integer thresholds and infinity, then transfers the score bounds to k-NN set coverage. The optional finite-threshold and no-tie assumptions are almost-sure assumptions on the experiment, not post-selection conditioning events.
- **3 points:** Establishes the CLR lower coverage bound using the fixed measurable score map, conditional exchangeability, and the defined extended order statistic. Correctly accommodates label-specific empty minima, tied or infinite scores, and a zero component error level. A standard split-conformal lower-bound invocation is sufficient when these hypotheses and conventions are respected; a CLR upper bound is neither required nor available from exchangeability alone.
- **2 points:** Expresses failure of the intersection as the union of component failures, applies Boole's inequality without assuming independence, and obtains coverage at least 1-alpha_knn-alpha_clr=1-alpha under the fixed allocation.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, auxiliary leave-one-out notation, or a separate analytic discussion of every elementary measurability fact. A concise explanation establishing the needed fixed-score exchangeability is sufficient.

Treat omission of the rank-to-set identification or of valid intersection composition as a theorem-critical gap unless an alternative argument supplies the same implication. Boundary cases may be handled uniformly rather than in separate paragraphs. A proof that silently replaces the rank-n+1 threshold by the largest calibration score, or that excludes all infinite scores without justification, does not establish the full task. Do not demand independence between calibration and test observations, between the component scores, or between the component failure events. Do not award the CLR step merely for asserting an unspecified 'valid calibration' assumption: the public task now gives its explicit hypotheses rather than its coverage conclusion.

The lower k-NN bound and intersection bound apply without the optional upper-bound assumptions. No proof concerning kernel training, empirical reference reuse, calibration-dependent hyperparameter selection, or a CLR upper coverage bound is required.
