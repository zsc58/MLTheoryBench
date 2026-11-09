# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Two-level decomposition (2 points):** Correctly defines the augmented and orbit-averaged risks and decomposes the expected gap into distribution shift, orbit-loss generalization, and finite-augmentation approximation terms. Takes expectations of legitimate differences rather than subtracting potentially infinite uncentered expectations. Handles an infinite right-hand side directly, or provides an equivalent valid treatment.
2. **Distribution shift control (2 points):** Uses a correctly oriented relative-entropy inequality with the stated sub-Gaussian assumption to obtain the uniform bound R sqrt(2 D_KL(D||D_G∘D)) in both directions. Uses positive parameters separately for the loss and its negative, or an equivalent valid two-sided argument; includes zero divergence by a limit or another valid argument.
3. **Orbit-loss information bound (3 points):** Derives the orbit-averaged loss's R-sub-Gaussian property under D, for example by Jensen's inequality; identifies its population mean as L_Q and the output channel as the existing marginal P_{W|S}; and proves or correctly applies the per-sample information inequality to obtain the stated data-information term. If using product-law decoupling, verifies its hypothesis for a suitably centered loss rather than assuming that mixing fixed-w uncentered sub-Gaussian losses preserves sub-Gaussianity.
4. **Conditional augmentation decoupling (3 points):** Conditions on Z_i=z, with all other training examples marginalized; identifies the product reference law D_G⊗P_{W|Z_i=z}; verifies the exponential-moment hypothesis using Assumption 2 and fixed-w centering, or an equivalent valid conditional entropy argument; obtains the exact stated single-example disintegrated-information term; justifies averaging and combines the three bounds with the stated constants and expectation placement.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular notation for centered residuals. The conditional information may be expressed in equivalent regular-conditional-law notation, but its conditioning variable must be Z_i, not the entire training sample S. A bound involving only full-sample-conditioned information does not establish the specified right-hand side without a further valid argument yielding that exact right-hand side.

The theorem does not assume finite expectations of L_D(W), L_Q(W), or the empirical loss separately. An argument that subtracts two infinite expectations is not valid; centering, justified truncation, or an equivalent method is needed when relevant. Finite expected square-root conditional information does not imply finite expected conditional information. A proof must not silently impose the latter stronger condition when justifying integrability. The reference proof's bound on the absolute centered residual is one sufficient argument, not a mandated presentation.

Do not require distribution invariance, Haar-uniform augmentation, a finite hypothesis space, a geometric regularity condition, or an additional product-law sub-Gaussian assumption. No independence of all mn transformed observations is available. All theorem-critical reference-proof obligations are resolved; there is no private ground-truth exception to scoring.
