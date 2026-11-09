# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the affine converged-error representation from the exact residual and test-output equations using the publicly assumed stationary empirical NTK convergence. Justifies the finite-time limiting passage for the initialization-dependent random target, for example by residual norm monotonicity, tightness of the initial residual, and a variation-of-constants estimate. Takes width to infinity before time; does not assume an interchange of limits.
- **3 points:** Establishes the engineered target's conditional centered Gaussian law with the pre-final parameter-gradient Gram matrix as covariance. Justifies convergence of that matrix, for example by subtracting the concentrated final-layer contribution from the convergent full empirical NTK, and supplies a valid characteristic-function/continuity argument for the target limit.
- **3 points:** Establishes the predictor's centered initialization limit and identifies its covariance with the limiting final-layer gradient contribution for the specified affine readout. Supplies a valid joint-law argument for predictor and target, such as conditional characteristic-function factorization, and obtains the full NTK covariance for their difference. Conditional layerwise Gaussianity and empirical covariance concentration provide a self-contained route to the initialization assertion.
- **2 points:** Computes the covariance of the limiting linear Gaussian error map and identifies it with the noiseless NTK-GP posterior law after subtracting its deterministic mean. Allows degenerate posterior covariance and preserves the independence of the centered law from the labels Y.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. Stationary NTK convergence along the specified training trajectory is an explicit assumption; do not require the solver to prove a general lazy-training theorem from Lipschitz activation and initialization scaling alone. Conversely, merely naming kernel regression does not supply the remaining ODE derivation and limiting justification.

Zero cross-covariance or separate Gaussian marginal limits do not alone establish independence. Require a valid joint-Gaussian or joint-characteristic-function argument. Do not assume finite-width predictor/target independence, since they share the predictor initialization.

Do not require the full recursive NTK formula: the initialization full-NTK premise and the direct final-layer calculation suffice. Do not award credit for merely naming Gaussian-process, concentration, or characteristic-function methods without supplying their relevant application. A standard result may replace a derivation when its relevant statement is given and its hypotheses are checked.

The target concerns the iterated width-then-time limit, not the distribution obtained by converging every finite-width network first. A dependency failure should reduce downstream credit only when the downstream conclusion is not independently established. Empty lists, L=1, overlapping inputs, and singular test covariance may be handled by the natural limiting or zero-dimensional conventions; no positive test variance is required.
