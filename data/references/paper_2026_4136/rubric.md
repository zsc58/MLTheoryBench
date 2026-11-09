# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines or correctly uses the normalized restricted components and verifies that the proposed weights, including zero weights on unselected components, form a valid simplex mixture satisfying the fallback floor. Recognizes that the retained-mass assumption makes the denominator positive.
- **3 points:** Derives the density ratio and correctly obtains the exact TV identity plus both forward- and reverse-KL bounds, including their parameter dependence. For reverse KL, supplies an actual upper-bound argument; monotonicity in retained mass alone is not the complete logarithmic-bound argument.
- **2 points:** Computes the expected reporting cost from the component-label mixture weights and region masses, using mixture-average rather than displayed-list cost.
- **3 points:** Correctly interprets C* as a class of binary support vectors, justifies the product count, and proves the uniform-law truncation TV identity for every admissible nonempty A. Deduces the atom-budget lower bound and contrasts it with the zero-distortion single-region report.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, a derivative calculation, or a particular route to the reverse-KL bound. Do not require a quantitative cost separation for arbitrary declared component costs: the converse concerns the number of individually retained support atoms.

The converse assumes uniformity directly; no derivation from likelihood or prior symmetry is required. It concerns conditional truncations, not atom mixtures supplemented by unrestricted fallback. The formulas must remain valid for retained mass one, epsilon=0, singleton groups, and an empty active group set. For an empty active group set, C* contains only the zero vector and the empty product is one. An atom budget M=0 admits no nonempty truncation. Separate discussion of these cases is unnecessary when the proof already covers them. Integer rounding may be stated but is not required beyond the displayed real-valued lower bound.
