# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **3 points:** Correctly represents each leaf as a conjunction of ancestor split outcomes and derives the mixed-intervention leaf probability as the product of the selected P/Q conditional factors and branch complements, with coherent treatment of all path nodes. An equivalent recursive routing argument receives the same credit. Where normalization is addressed, it must follow from valid routing or mass conservation, not from an arbitrary rescaling.
2. **2 points:** Uses the factorized leaf probabilities and fixed leaf predictions to derive every interventional mean as the weighted sum over leaves, without introducing an unlicensed normalization or changing the tree model. Recognizing that this is the expectation under the publicly defined leaf law is sufficient; no additional representation of an input-space distribution is required.
3. **2 points:** Establishes that the all-P and all-Q interventions recover mu_P and mu_Q respectively, using the conditional chain rule and the fact that the leaf events cover the input space without overlap.
4. **3 points:** Applies the Shapley weighted marginal-difference formula, or a valid equivalent argument, to establish efficiency for the defined game and concludes that the sum of split-node attributions equals mu_Q-mu_P. A correct application of the standard finite-game efficiency theorem is acceptable when the game and endpoint values are identified and its hypotheses hold; alternatively, permutation counting and telescoping or direct coefficient cancellation may be used. Merely naming Shapley efficiency without connecting it to the defined game earns at most partial credit.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The mixed intervention is defined on split-node conditional factors; arbitrary interventions on joint leaf probabilities or omitted path factors do not establish the target.

The source's literal containment-based pseudocode has a local empty-leaf defect, corrected privately under theory_004. The public task already uses the intended structural node construction. Do not require a solver to identify, discuss, or reproduce that source defect. Structural ancestry and actual branch choices correctly identify path factors even for empty leaf regions. A proof that instead infers a leaf's ancestors or branch choices solely from set containment must handle empty leaf regions correctly; empty-set containment alone does not identify either.

The assumption that all split conditionals are defined excludes null conditioning events under P or Q. Do not require all branch probabilities to lie strictly between 0 and 1, do not require positive probability for every leaf, and do not introduce independence of the input tests. Zero mixed mass at a node is harmless in the finite routing construction.

Full credit requires an argument that covers the stated domain, including a tree with no split nodes. That case has a constant prediction and an empty attribution sum. An explicit case split is not mandatory when the proof's conventions and argument already cover it. Likewise, do not demand separate discussions of p_c=q_c, zero prediction shift, or branch probabilities 0 and 1 when the proof remains valid for them. A genuinely omitted but immediately repairable boundary case falls within the 8-9 category rather than invalidating the main argument.
