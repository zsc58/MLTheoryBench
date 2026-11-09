# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the scalar relaxation identity by variation of constants and integrations by parts, including the initial transition term, curvature integral, and valid bounds.
- **2 points:** Applies the identity to m and v and correctly computes the derivative identities for g and g^2, obtaining the normalized moment forms and controlling initial and curvature contributions.
- **4 points:** Derives the nonlinear ratio decomposition, isolates the displayed coefficient (tau_2-tau_1) multiplying logarithmic scale drift, and supplies an explicit non-tautological remainder formula and a quantitative finite compact-subinterval bound. If using Taylor's formula, verifies that its integration segments remain in the positive-denominator domain and controls the derivatives there. Constants must have justified dependencies on the stated data and normalization lower bounds; neither R nor E may be used to bound the remainder.
- **2 points:** Uses the prescribed coefficient-based definition to prove the iff condition on every nonempty interval of definition, and translates tau_1=tau_2 correctly to beta_1=beta_2 using the common positive time step.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions; the reference proof's particular notation, integral representation, or numerical constants are not mandatory. Allocate the corresponding core-step credit to mathematically equivalent work.

Do not award substantial credit for merely naming a Taylor expansion, filtering argument, or scale-invariance principle without deriving the coefficient and remainder. Merely setting E equal to R minus the asserted leading term does not meet the requested non-tautological construction. An explicit remainder derived from the ODE data, with a justified quantitative bound, does.

Do not require nonnegative initial second moments, small logarithmic drift, a small relaxation time, or a post-transient regime. The public task allows arbitrary initial moments and makes assertions only where the normalization is defined. In a Taylor-based proof, positivity along the segment follows from 1+uY=(1-u)+u(1+Y)>0; smallness of Y is unnecessary.

The iff concerns the canonical coefficients, not whether the realized drift term happens to vanish on a particular trajectory. Constant gradients do not invalidate the conclusion. No invariance characterization is asserted on an empty positivity region, and no estimate uniform up to an excluded zero-denominator endpoint is required.
