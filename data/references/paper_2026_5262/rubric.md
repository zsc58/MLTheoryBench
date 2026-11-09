# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly uses the componentwise exact update \([T(h)]_j=h_{j+1}\) for \(j<M\) and \([T(h)]_M=F(h)\).
- **3 points:** Substitutes those components into the defined loss and derives the full decomposition for an arbitrary admissible predictor \(Q\), including the separate final-slice term.
- **4 points:** Substitutes \(B_g\), establishes that every copied-coordinate residual is identically zero, and concludes exactly that its loss is \(\mathbb E[a_M\|g(Z)-F(Z)\|_2^2]\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A response that merely states that copied coordinates are exact, without deriving the resulting loss identity, does not earn the final core step.
