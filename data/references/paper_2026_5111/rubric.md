# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the exact one-step loss change, including the triangular Hessian average, and telescopes it with a valid zero-step convention.
- **3 points:** Correctly converts the telescoping equality and the lower loss bound into the weighted-average identity and both effective-curvature forcing bounds.
- **3 points:** Proves interior-point localization of the triangular average and uses the Rayleigh quotient to derive both largest-eigenvalue forcing statements.
- **1 point:** Correctly proves convergence of the weighted effective curvature under bounded trajectory loss and diverging step energy.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A claimed localization must actually establish an interior Hessian point, and a claimed forcing result must retain the stated energy and nonzero-step conditions.
