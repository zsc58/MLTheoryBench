# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly derives from \(e_t\le(0.9/2)^3\) (including the zero-error case or an equivalent limiting argument) that the controller multiplier is exactly the upper cap \(\phi_t=2.0\) at every step.
- **3 points:** Derives the clipped doubling recursion, proves \(h_t=\min\{2^t h_0,h_{\max}\}\), and establishes fixation at \(h_{\max}\) by \(\lceil\log_2(h_{\max}/h_0)\rceil\).
- **3 points:** Proves that two tolerances satisfying the uniform bound generate the same step-size sequence and, by a valid determinism/induction argument with tolerance-independent updates, identical iterates.
- **1 point:** States and uses the required parameter ranges and common-initialization/determinism conditions without adding or omitting substantive assumptions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
