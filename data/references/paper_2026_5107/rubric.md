# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs nested interior cells and a continuous ReLU-realizable recursive encoder that produces the correct level-dependent cell label on every interior cell. The construction must cover the allowed case N=1, either directly or by a separate valid argument.
- **2 points:** Establishes simultaneous finite interpolation of the residual cell averages by the two-sine decoder, with a uniform bound on the correction amplitudes sufficient for all levels. If using Kronecker approximation, states the relevant form and verifies the required rational independence. No uniform bound on the inner or outer frequency coefficients is required.
- **4 points:** Proves the cell-average translation estimate and uses it with transition-region control to close the residual induction, obtaining the stated (2d+1) times the modulus error for every prefix. This includes positive-volume cell averages, a justified positive tolerance in the nonconstant case, a common noncircular choice of the transition parameter, nested exceptional regions, and the almost-everywhere constant case. The proof must remain valid for p=1.
- **2 points:** Realizes the full recursive construction as one shared mixed-activation network of width at most 2dN+d+2, with exactly the allowed blocks and heads. Verifies that the cell label is available before the inner sine is evaluated and that the outer sine is available at the claimed readout block. An explicit affine register description or an equally checkable construction is sufficient; counting separately realizable modules without establishing their shared timing is not sufficient.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, exact hinge representation, padding convention, or particular register names.

The two sine coordinates in one activation block operate in parallel, not in series. A valid pipeline can evaluate the outer sine for one level while evaluating the inner sine for the next and advancing the encoder. Do not permit extra nonlinear operations or extra activation blocks to be absorbed into affine maps.

The correction amplitude bound controls the network values on transition regions. It is not a bound on all affine coefficients. The theorem allows large finite real coefficients and does not assert bounded-weight or finite-precision guarantees.

All maps may depend on the target and on the prescribed terminal depth. The same maps must serve every prefix within that horizon; consistency when the terminal depth changes is not required. Monotonicity of the actual approximation errors is also not required.
