# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the low-mass parameter bounds for η, φ, and Φ and the diffuse-prior covariance identity, including Tr(φΦHΣH^T)=D/β. Uses positive-definite matrices and valid digamma domains. The diffuse state-update limit must hold its incoming weights and updated shape factor fixed; a merely large finite covariance does not give the exact trace identity.
- **3 points:** Uses the coordinate updates and nonnegative competing intensities to derive the per-measurement association bound, then correctly aggregates it to β^+<h(β)Δ. Applies admissibility to the complete current configuration, including its incoming Gaussian moments. Merely asserting contraction or citing coordinate ascent earns no credit for this step.
- **3 points:** Establishes B h(x)<x throughout the interval defining L, with the correct Lambert-W branch analysis. Treats A<e without evaluating a real V, and includes A=e with strict exclusion of the equality point. A derivation restricted to x<B must also address x>=B when claiming an all-positive-x result. The threshold calculation is theorem-critical.
- **2 points:** Verifies that the next scores and mass are positive and finite, uses admissibility and the fixed threshold to prove the strict ratio bound and invariant monotone decrease, and supplies a valid limit argument proving convergence to zero.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or analysis of the unused upper Lambert-W interval. A later step may receive credit if its required premise is independently established, even when an earlier attempted derivation is flawed. Missing the one-round score bound or the threshold justification is a major gap because either omission leaves the claimed pruning guarantee unsupported.

No proof of absorption at exactly zero mass is required: the diffuse state update is defined here for positive mass, and positivity of the subsequent scores keeps the asserted ratios meaningful. If M=0, the theorem's premise is impossible. Do not require a proof of general CAVI convergence, an exact-inference guarantee for the unapproximated latent-existence model, invariance of other components after removal, or a guarantee for a different coordinate order or finite prior covariance.
