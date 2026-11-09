# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Exact Kac--Rice reduction (2 points).** Defines the augmented field, applies the local theorem under the stated hypotheses, computes its block Jacobian and the adjugate determinant identity without requiring the Hessian block to be invertible, and includes the |lambda|^(-n) density factor and correct conditioning substitution. Uses a nonnegative exhaustion to obtain the global representation.
2. **Gaussian structure and kernel calculations (2 points).** Establishes joint Gaussianity of the required derivatives and obtains the covariance identities needed for the bound. For the reference route, verifies the diagonal variance, coefficient identities, and first and mixed derivative formulas, or obtains the equivalent normalized identities directly. The kernel is given, so neither a finite-width central limit theorem nor a new derivation of the network model is required.
3. **Normalization and conditional Hessian control (3 points).** Justifies preservation of the critical-pair count and use of the normalized counting integral. Derives alpha_d=d^2/(2d-1), the positive definite anisotropic gradient covariance, and the correct density. Uses Gaussian regression and fourth kernel derivatives to obtain quantitative conditional Hessian moment bounds, and controls the adjugate with degree-independent constants apart from the displayed degree factors. Merely naming regression or claiming a polynomial bound does not close these obligations.
4. **Global integral estimate and degree rate (3 points).** Carries out the multiplier integral with its hypotheses checked. For the reference route, retains D_x=||xi-x||^2+(x^T(xi-x))^2/n, obtains the distinct J_m and K_m spatial families, proves integrability both near xi and at infinity, and collects degree factors to obtain C_(n,xi)d^(n/2). Handles the m=0 exponent correctly and covers n=1 and d=1. The constant must be independent of d.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices or unused intermediate identities.

The conditional singularity assumption is an almost-everywhere statement. At x=xi the conditioned gradient vanishes, so the conditional Jacobian is singular; this measure-zero spatial set is not a contradiction. It must not be used with the positive-beta multiplier identity, and its original adjugate factor is zero.

The reference proof's exact Gaussian exponent is nq(x)D_x/(2alpha_d lambda^2). A weaker isotropic bound cannot simply be substituted while claiming the same tail estimates without a separate valid integrability argument.

The source's off-diagonal derivative expansion contains a product-rule error; its diagonal derivative statement is correct. The final B contribution uses K_m rather than J_m. In collecting degree powers, m=0 uses alpha_d<=d, whereas negative exponents may use alpha_d>=d/2. Do not require or reward the incorrect source calculations.

All reference-proof obligations are closed in the replacement proof; there is no unresolved private GT dependency.
