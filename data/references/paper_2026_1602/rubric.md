# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Kernel and target structure (2 points).** Establish the harmonic eigenspaces, multiplicities, rank r0 asymptotic to d^{k0}, leading-subspace identification, eigenvalue scaling, and degree-k0 gap. Check that the augmented scalar indicator features supply K^(0), the ReLU weights supply K^(1), and the fixed target belongs to the corresponding leading population subspace with the stated RKHS bound. Do not infer a global ordering solely from bounded-degree asymptotics.
2. **Finite-width projected dynamics (3 points).** Derive uniform initialization-kernel and activation-boundary estimates, or obtain them from a valid independently established result with its hypotheses checked. Derive the residual recursion with the exact-kernel projector, weight movement, and a closed residual induction. Retain the scalar augmented contribution in the function linearization. Establish f_t=h_t+e_t uniformly up to T, the empirical leading-subspace membership of h_t, its bounded RKHS norm, and the uniform remainder bound under the stated width. Any proof tolerance must be chosen compatibly with width; it cannot be assumed arbitrarily small. Nonexpansiveness, not strict contraction on the untrained complement, is the relevant operator property.
3. **Empirical-projection and optimization control (3 points).** Compare population and empirical covariance operators on a common RKHS, verify the gap and sample-size conditions, and derive the target's empirical-complement bound. Derive the interpolation/Bessel estimate, spectral target transient, conditional projected-noise bound, and accumulated recursion-error contribution. Keep the noise term and distinguish noisy residual from clean-label error. Establish an empirical risk bound of order gamma_0^2/(eta t)+C(gamma_0,sigma_0)log(4/delta)d^{k0}/n on events shared across time.
4. **Localized generalization and final rate (2 points).** Establish a valid localized population transfer, including its boundedness, variance/Bernstein condition, localized complexity, and fixed-point calculation. A fixed-class theorem cannot be applied to a class selected by the same sample merely by conditioning on that sample. The reference uses the source-derived deterministic population-subspace enlargement for the RKHS components and transfers the bounded residual separately; accept any valid alternative. Combine the late-iteration, width, and remainder scales, account for the shared-event probability, and prove the simultaneous C log(4/delta)d^{k0}/n risk bound and the stated sample-size consequence.

# Evaluator Notes

Accept any complete valid alternative proof under the repaired public assumptions. The projection is defined by the exact kernel Gram matrix, not by the finite-width initialization Jacobian Gram matrix. The augmented coefficient vector has dimension m, not md.

Standard independent covariance concentration and localized empirical-process theorems may be invoked when the relevant statements are supplied and their hypotheses, including operator domains and fixed-class requirements, are verified. Do not award full credit merely for naming a specialized method, citing a nonstandard paper-specific dependency, or asserting the finite-width, projection-tail, optimization, or generalization estimates. The reference independently derives the particular consequences needed from its nonstandard imported dependencies; it does not require reproduction of their unused full exact-constant statements.

The guarantee is simultaneous across the specified integer iterates. A proof that only supplies a separate probability bound for each time has not yet proved this scope unless it constructs shared events or supplies an adequate time-uniform argument. Constants may depend on all fixed parameters identified in the public task, but not on n,d,m,T,delta, or epsilon. Do not penalize a proof for using these permitted dependencies.

Zero noise and a zero target function are allowed. The positive fixed degree is an ambient bound on target degree, not a requirement that every top-degree coefficient be nonzero. The sample-complexity consequence retains the other width and horizon requirements and the same probability bound; it is not a separate assertion of confidence 1-delta alone.

Propagate a failed eigenspace or dynamics dependency only when the final risk conclusion is thereby unsupported. No unresolved reference-proof obligation is designated as an assumed or completed scoring step.
