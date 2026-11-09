# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Regularity, well-posedness, and invariant bounds (2 points).** Derive bounded normalized optimizer increments, the parameter support bound, and state/adjoint bounds. Establish the needed local field and gradient Lipschitz estimates from attention and the loss assumption. Justify solutions and measurable uniform suprema. If an initial-law flow is used, construct it and identify its empirical-law specialization with the finite-particle system; do not assume the paper-specific flow representation or its uniform regularity.

2. **Adaptive parameter-flow coupling (2 points).** Compare optimizer histories at a fixed depth, with the same initial head and zero initial moments. Derive normalized-history stability, including zero-variance histories, and bound continuous/discrete gradient discrepancies using the same training batches and the mixed discrete pair (x_r,a_{r+1}). Couple corresponding heads to obtain a parameter discrepancy controlled by earlier training-step path errors. Also establish the continuous parameter curve's depth-time regularity needed for quadrature. A recursion between neighboring independently initialized depth layers is not a substitute for this argument.

3. **Uniform empirical-head concentration (3 points).** Conditional on training data, use continuous-gradient images of independently initialized heads to obtain centered independent layer/head contributions and a layer martingale. Establish measurable suprema and derive the uniform maximal squared bound C(L^{-2}+L^{-2/3}H^{-1}) without an N-dependent entropy factor. For the reference route, justify the attention-ratio reduction, the integrated-denominator adjoint case, Gaussian comparison, bounded tensor coefficients including the cubic adjoint term, and the block estimate C[L^{-1}+(mH)^{-1/2}+m/(L sqrt(H))]. Choose an admissible integer m of order L^{2/3}, then supply the bounded-differences variance estimate and maximal upgrade. Merely citing a paper-specific concentration lemma does not close this step.

4. **Forward/backward and training closure (3 points).** Decompose field errors into parameter-time quadrature, hybrid concentration, and residual state/measure/parameter discrepancies. Use same-label coupling in the correct direction. First close the forward recursion, then the terminal loss discrepancy, then the backward recursion with later adjoint indices. Handle the piecewise-constant extensions and endpoints. Close the training-time induction, including tau=0, and conclude both estimates with the stated expectation/supremum order. Verify N independence and, for the specified blockwise optimizer, d,k independence with the scalar data/loss bounds fixed. Derive the L2 rate by taking square roots.

# Evaluator Notes

Accept any complete valid alternative proof; the reference concentration presentation and named tools are not mandatory. The uniformity is over the complete vector bold y in K^N, not one token with other inputs fixed or sampled. E^1 averages head initialization only, conditional on the training data. Within-vector token independence must not be imposed.

Do not treat actual discretely trained heads as conditionally independent: the independent comparison samples are the hybrid continuous-gradient images. Do not reverse the empirical Wasserstein matching inequality. Do not impose an auxiliary m<=sqrt(L) restriction when claiming the reference optimized rate. Fixed-degree tensor estimates must include the cubic adjoint term, or an equivalent valid decomposition.

The corrected source-local endpoint, quotient-extension, block-range, tensor-degree, and numerical-constant issues are not additional solver obligations beyond proving the repaired public task. Minor numerical constant changes are immaterial. The public task supplies no intermediate concentration or regularity theorem as an assumption. Naming symmetrization, an optimizer, or Gronwall without establishing the theorem-critical inequalities earns only partial credit.
