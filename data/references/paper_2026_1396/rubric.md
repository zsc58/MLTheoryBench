# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly factors the loss through a smooth Gramian function and derives the directional derivative through \(MM^T\), including validity at rank-deficient or nonunique triangularizations.
- **2 points:** Establishes that any tangent satisfying \(\dot L L^T+L\dot L^T=\dot M M^T+M\dot M^T\) gives the exact JVP.
- **4 points:** Derives and verifies the explicit pseudoinverse/projector surrogate, including the lower-triangular column-space term and the null-space term, and proves their Gramian contributions sum to the full differential.
- **2 points:** Concludes exactness for arbitrary rank and identifies the invertible case where the null-space correction vanishes and the classical rule is recovered.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
