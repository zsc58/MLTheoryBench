# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Establishes the exact-subspace truncation bound. This requires correctly using the weighted-to-Euclidean spectral reduction, the Poisson equation, and inverse control on the mean-zero subspace to obtain \(\|v-\Pi_U^Wv\|_W\le \|g\|_W/\sqrt{\lambda_2\lambda_{k+1}}\).
- **3 points:** Derives a learned-subspace projector bound from the feature objective excess and the positive cutoff eigengap. The argument must substantively relate excess energy to mass outside the bottom subspace and then to projector distance; merely citing a specialized perturbation result is insufficient.
- **3 points:** Correctly identifies the two weighted least-squares approximations as weighted orthogonal projections and combines the truncation and projector bounds to prove exactly the displayed end-to-end inequality.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
