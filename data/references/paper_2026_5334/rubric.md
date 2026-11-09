# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly computes the first variation of `F`, up to an irrelevant additive constant, and applies the standard Wasserstein gradient identity to derive `v=a(u)s`, including the factor `u^2 f''(u)`.
- **2 points:** Correctly identifies the first-order derivative of the frozen Euler density and obtains the scalar expansion of `H`. Uses the stated local and weighted L1 regularity, handles the positive-part threshold using its null-level-set assumption, and justifies the integrated remainder rather than merely integrating a pointwise `o(h)`.
- **4 points:** Derives the compression-elasticity integral identity by a valid flux calculation, with the necessary product and chain rules or an equivalent derivation. Justifies derivative domains, treats the zero-score set almost everywhere, and handles the null zero-weight set without evaluating `E` where its denominator vanishes. No extra C1 assumption on `s` may be imposed; the inherited regularity of `v` suffices.
- **1 point:** Establishes finiteness and strict positivity of `G` under the stated comparison and strictness assumptions, then uses the scalar remainder to obtain strict decrease for every sufficiently small positive step.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The standard first-variation characterization of the Wasserstein gradient may be invoked; a separate global flow-existence theorem is neither required nor asserted.

A merely asserted flux factorization, without a valid derivation, does not earn the central four points. Failure of the flux identity leaves the final improvement conclusion unsupported unless it is independently established. Do not require the zero-score flux to vanish at every individual critical point: almost-everywhere vanishing is sufficient and is the correct claim. The zero-set argument may use the C1 velocity or another valid method.

The difference-quotient convergence assumptions specify the first-order integration regime; they do not give the density derivative's formula or the requested expansion of `H`. A proof must still identify that derivative and justify differentiation of the deficit functional. Do not demand a quantitative threshold separation, a step-size bound uniform over densities, or a global convergence result. Empty active regions and null positive-prefactor sets simply make the strictness premise unavailable.
