# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Heat-ball source-correction identity (3 points).** Proves the forced heat-ball identity, for example by deriving the radius derivative of the weighted mean and its cancellation with the source correction. A proof using integration by parts must account for the lateral normal-derivative terms and justify the treatment of the singular time tip. A mere citation of a heat-ball method, or an unsupported assertion that differentiation produces the desired source term, is insufficient.
2. **Density, log-density, and entropy sources (3 points).** Correctly derives the equations for `h_u`, `h_v`, and `h_w`, including the nonlinear gradient and drift-divergence terms, and substitutes them into the common representation.
3. **Exact mean-value hierarchy (2 points).** Justifies normalization of the weighted mean and the small-radius limit, including vanishing of the source correction, and obtains all three representations with the correct signs, coefficients, radial integrations, quantifiers, and admissible-domain restriction. A correctly stated and applicable standard normalization result is acceptable in place of its direct calculation.
4. **Score differentiation (2 points).** Differentiates the log-density representation with respect to the anchor and justifies passage through the integrals using the available regularity, local positivity, compact bounds, and integrable weights. Obtains the exact representation for `∇log u`. Direct differentiation on the fixed scaled domain is fully sufficient; kernel symmetry and integration by parts are optional, not required.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Propagate a missing heat-ball identity to later formulas when they are unsupported, but award independently correct source computations. Merely substituting the correct sources into an unproved representation does not close the central obligation.

The positive variable `σ` in `E1` is backward time lag. Any classical caloric mean-value result invoked must respect that orientation: a sampled lag-coordinate function satisfies `∂σθ+Δθ=0`, or equivalently a physical forward-caloric function is evaluated at `τ0−r²σ`. Do not accept the incorrectly oriented standalone statement in the source as a valid theorem. Do not require a solver to discuss the source error when the solver works directly from the public definitions.

The public `C^{2,1}` regularity of `u` and second spatial derivatives of `b` suffice for the score formula: `∇h_v` involves only second spatial derivatives of `v` and `b`. No stronger regularity, global lower bound on `u`, separate existence theorem, sampling result, or additional public assumption is required.
