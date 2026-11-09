# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly inserts the clipped and exact population objectives and derives the three-term triangle-inequality decomposition.
2. **3 points:** Proves the prompt and rollout sampling deviation with the stated range width, confidence parameter, and separate \(n\) and \(nK\) rates, combining them by a valid union bound.
3. **2 points:** Derives the KL-clipping mismatch bound \(\beta\mathbb E_Q|\ell_\theta-\ell_\theta^\tau|\) by cancellation of reward terms and absolute-value domination.
4. **3 points:** Transfers reward MSE from \(P\) to \(Q\) using the density ratio and Cauchy-Schwarz, obtaining \(C(\theta)\sqrt{L_{\rm train}^{(2)}}\), and combines all terms into the claimed high-probability inequality.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The score should reflect established mathematics; a named concentration or change-of-measure method without the required bounds earns no credit for that step.
