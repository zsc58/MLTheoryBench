# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Projects the positive-semidefinite cone onto the observed coordinates, proves that the projected feasible set is convex and the weighted loss is strictly convex there, and concludes that the optimal observed-entry vector is unique. Merely asserting uniqueness without addressing the projection and strict convexity does not earn full credit.
- **2 points:** Correctly proves that the entire inner minimizing set consists exactly of the positive-semidefinite completions of that one fixed observed-entry vector, and uses the assumed positive-definite inner minimizer to obtain a positive-definite completion.
- **3 points:** Establishes that the maximum-log-determinant completion exists, is positive definite, and is unique. This may be done directly using compactness and strict concavity or by correctly invoking an applicable standard covariance-completion theorem after verifying its hypotheses.
- **2 points:** Derives the inverse sparsity for every unspecified off-diagonal pair, either through feasible two-sided entry perturbations and the derivative of log determinant or through an equivalently justified completion theorem.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A citation or method name alone earns no credit unless the relevant hypotheses and conclusions are stated and correctly applied. Failure to prove uniqueness of the observed-entry vector generally leaves the reduction to a single completion problem unsupported. If that reduction or the completion theorem is independently established by another valid argument, score subsequent achievements on their own merits.
