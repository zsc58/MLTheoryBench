# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Correctly represents the three directions using the orthogonal vectors and reduces their cosine (or squared cosine) to the weighted expression with positive squared norms.
2. **(3 points)** Defines the interpolation weights and proves, from \(\eta>1/2\), that \(p\mapsto p\sigma((-\log p)/\eta)^t\) is strictly increasing while the corresponding gate logarithm is strictly decreasing.
3. **(4 points)** Differentiates the squared-cosine proxy and derives a valid antisymmetrized pairwise expression, showing every unequal-probability pair contributes positively and hence the derivative is strictly positive.
4. **(1 point)** Correctly concludes strict improvement from \(t=0\) to \(t=1\), and passes from squared cosines to cosines using positivity.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
