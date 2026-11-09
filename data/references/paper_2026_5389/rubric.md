# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly differentiates \(G(t)=\|\nabla S(w_t)\|^2\) along the flow and obtains both the mixed loss-curvature term and the surrogate-curvature term with the correct signs and factors.
- **3 points:** Applies the two hypotheses when \(\|w_t\|>R\) to derive \(\dot G\le 2C\sqrt G-2\lambda\mu G\), and correctly identifies that this forces decay above a finite threshold.
- **4 points:** Handles the region \(\|w\|\le R\) using continuity and compactness, combines its finite gradient bound with a strictly enlarged decay threshold, and rigorously proves both finite-time entry and forward invariance of one bounded interval.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the particular constants chosen in the reference proof. Merely asserting that a comparison argument applies, without addressing times when the trajectory lies inside the radius-\(R\) ball or without establishing eventual forward invariance, does not complete the final core step. A flaw in differentiating \(G\) should not remove credit for a later comparison argument if the needed scalar inequality is independently established.
