# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the learner history and current-row conditioning field, selected-coordinate kernel, fair selector, predictable weighting, measurable bounded losses, expectation-level risks, and conditional row exchangeability. Distinguishes scalar conditional mutual information from mutual information under a realized conditional law. Merely restating assumptions without using them does not by itself earn all of these points.
- **3 points:** Derives the sequential row-swap identity reducing the training-minus-holdout gap to twice the sum of selector-loss correlations with a consistent selector-sign convention. Shows how selector averaging and row exchangeability identify the selected and cross-evaluated branches; merely naming symmetrization is insufficient. Applies the same reasoning to the fixed-comparator signed excess losses.
- **2 points:** Establishes the evaluated-loss square-root bound through a valid variational and exponential-moment argument, or another complete valid argument. Correctly averages conditional divergences to scalar CMI, handles zero information when optimizing, and applies conditional data processing and finite-sum Jensen/Cauchy--Schwarz to obtain the state-information bound.
- **3 points:** Establishes the bounded signed-variable information/second-moment estimate and its Bernstein envelope, rather than merely naming the paper-specific conditional Bennett lemma. Uses the sign controlling holdout minus training, keeps all expectation levels correct, applies the stated second-moment assumption, and obtains the exact coefficient by rearrangement for the specified parameter range. Handles the separate b=0 case without division by b.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or sign convention. Standard variational inequalities and conditional data processing may be invoked with their hypotheses checked. A valid proof using a stronger elementary exponential-moment estimate is acceptable if it implies the exact requested conclusions.

The public I(X;U|G) is scalar CMI. A pointwise inequality given G must use the divergence under that conditional law; scalar CMI appears only after averaging. Do not accept replacing a random conditional divergence by its expectation inside a pointwise inequality without justification. Conversely, a correctly averaged argument needs no pointwise correlation bound.

Row exchangeability is conditional on the learner history, not on an already fixed ordered paired row. No independence across rounds or between the two coordinates is assumed. Ghost exclusion describes the learner's observation inputs and does not prohibit values coinciding or being inferable from selected information.

Award later steps when independently established even if an earlier auxiliary derivation is flawed; deduct for theorem-critical unsupported gaps. The reference proof has no unresolved obligations.
