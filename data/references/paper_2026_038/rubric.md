# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the exact pairwise Gaussian formula for $C(p_\theta)$, including the determinant and Mahalanobis-distance expression, from the squared mixture density.
- **3 points:** Establishes the KL-controlled overlap comparison, for example by rewriting $O-C$, applying Hölder with the $L^1$/$L^\infty$ norms, and using Pinsker with the correct constant. Covers infinite KL by observing that the comparison then has an infinite right-hand side and a finite left-hand side.
- **2 points:** Proves the explicit LDA sup-norm bound $(2\pi)^{-d/2}(\det\Sigma)^{-1/2}$ and substitutes it into the comparison inequality. Justifies that both overlap integrals are finite, explicitly or through an equivalent valid argument.
- **2 points:** Correctly derives the stated mechanisms: for fixed dimension and class count, covariance collapse makes the unweighted comparison coefficient and diagonal overlap contribution diverge; with covariance and positive weights fixed, each off-diagonal contribution decreases strictly as its pairwise Mahalanobis separation increases. States the weighted comparison for every $\lambda\geq0$, including the zero-weight boundary.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The public setup uses strictly positive class weights, as in the selected source analysis. There is no off-diagonal obligation when $C=1$. A proof may establish a stronger uniform diagonal lower bound, but it is sufficient to prove divergence with the weights fixed.

Distinguish divergence of the comparison coefficient from divergence of the entire KL-dependent upper bound. Do not require or credit an unsupported claim that the data-distribution overlap necessarily diverges, that a zero-weight penalty prevents collapse, or that decreasing an objective necessarily decreases the intrinsic overlap. The statement concerns population overlap integrals, not a finite-sample concentration bound.

Omitting only the immediate infinite-KL or zero-penalty case is a readily repairable omission rather than failure of the main comparison argument.
