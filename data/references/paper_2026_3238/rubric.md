# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Introduces the relative orthogonal matrix and correctly expresses each recovered coordinate as a unit linear combination of the independent standardized sources.
- **2 points:** Constructs the product coupling with independent standard Gaussians, proves the weighted Wasserstein bound, and sums it using orthogonality to obtain the global upper bound.
- **4 points:** Proves strictness for every unit mixture with at least two nonzero coefficients. For the reference route, shows that equality makes the induced coupling optimal; applies uniqueness of optimal transport from the absolutely continuous Gaussian to obtain a graph relation; obtains a Lebesgue-almost-everywhere functional equation; uses Fubini and nonzero coefficient changes of variables to obtain a two-variable Pexider equation; and concludes that two participating source laws are Gaussian, contradicting the hypothesis. The almost-everywhere measurable Pexider theorem may be invoked as a standard independent result if its relevant affine conclusion is stated and its measurability and almost-everywhere hypotheses are verified. A valid direct derivation is also acceptable. Merely naming an optimal-transport or functional-equation method is insufficient.
- **2 points:** Shows non-signed-permutation relative matrices have a strict row and that signed permutations attain the bound, yielding exactly the stated argmax set.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

No absolute continuity or smoothness of the source laws is assumed. In the reference route, absolute continuity belongs to the Gaussian first marginal of the optimal transport problem. Atomic source laws must remain covered. Negative nonzero coefficients are allowed, and the two-variable reduction must preserve the almost-everywhere meaning of the equation. Unit source variance rules out degenerate affine Gaussian images. A proof need not separately establish continuity or compactness of the objective once it explicitly supplies the attained upper bound and all equality cases.
