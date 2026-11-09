# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the finite product state space, positive scan weights, random-scan kernel, and unique full-support stationary distribution. Restating the setup or reproving the stationary-distribution facts already supplied in the setup is not required.
- **2 points:** Proves the forward implication by using the common joint law and verifying detailed balance for distinct one-coordinate transitions, with zero transitions and self-transitions handled, or by an equivalent valid argument. Identifies the common joint with the stationary distribution by uniqueness.
- **4 points:** Completes the reverse implication. For the one-coordinate proof, selects distinct states with equal complements, eliminates all other update terms, cancels the scan weight, and derives the cross-multiplied relation. Extends that relation to equal component values tautologically and uses normalization to identify the conditional distributions without unjustified division by a possibly zero modeled probability. An equivalent valid proof earns the same credit.
- **2 points:** Concludes joint consistency and explicitly identifies every modeled conditional with the corresponding stationary conditional, establishing the integrated equivalence for every component and complement.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its private source-contract discussion. The substantive reverse implication and conditional identification are theorem-critical, but the particular one-coordinate proof route is not mandatory.

In the one-coordinate route, the claim that all other scan terms vanish applies only when the two component values are distinct. For equal states, the desired cross-multiplied relation is an identity even though other scan terms may contribute to the self-transition. This distinction also covers singleton component spaces. A normalization argument that automatically covers singleton components does not need a separate case discussion.

Do not accept division by a modeled conditional probability unless its positivity has first been justified. Summing the cross-multiplied relation is sufficient and does not require initially positive modeled probabilities. A readily repairable omitted diagonal case should be assessed under the scoring guide rather than treated as failure of the entire reverse implication.
