# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes Wasserstein density by finite-support approximation and an explicit coupling between each atom and its small Gaussian perturbation, with moment and nonzero trace-class covariance conditions verified.
- **3 points:** Derives the RKHS empirical-measure bound from iid sampling, the Hilbert-space variance calculation, and the probabilistic-method selection of a realization with MMD at most 1/sqrt(K).
- **2 points:** Proves that smoothing the selected atoms by Gaussian noise converges in MMD, using bounded continuity of the kernel and the kernel-expectation representation.
- **2 points:** Combines the two MMD estimates by the triangle inequality and states both conclusions with all quantifiers, every K >= 1, and exactly K indexed Gaussian components with nonzero, self-adjoint, positive-semidefinite, trace-class covariances in the rate claim.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The covariance requirement excludes Dirac components but does not require nonsingularity, injectivity, or strict positive definiteness. Singular nonzero covariances are admissible.

Exactly K components means a representation with K indexed Gaussian terms, as in the public mixture definition. The terms need not be distinct, and K need not be the minimal possible component count. Repeated sample points and repeated Gaussian components are allowed.
