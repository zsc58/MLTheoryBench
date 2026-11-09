# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **4 points:** Treats the LP bound entries as independent arguments when defining partial derivatives, distinguishes the fixed-bound gap derivative from the total derivative, and applies the chain rule to the gap before averaging. Includes the forward-output contribution in the direct gap term and the factor \(1/|B|\) in the indirect term. Justifies the needed local differentiability from the stated basis regime or correctly invokes that regime's elementary smooth-basis implication.
2. **3 points:** Differentiates the normalized width definition to obtain \(N_h^{-1}\sum_{l,j}(\nabla U_j^{(l)}-\nabla L_j^{(l)})\). Understands these as total bound derivatives through the full IBP recursion, not derivatives with earlier-layer bounds artificially frozen. Handles the task's matched branch-limit convention where kinks are discussed.
3. **3 points:** Substitutes the width derivative into the definition of the surrogate, proves the displayed identity, and identifies the lower/upper coefficients as \(-\alpha/N_h\) and \(+\alpha/N_h\), replacing the batch-averaged indirect gap sensitivities. Does not identify the surrogate with the ordinary full gradient of the combined numerical regularizer or claim an unprovided approximation-error bound.

# Evaluator Notes

Accept a complete valid alternative proof. A concise chain-rule proof plus differentiation of the width definition can receive full credit. An explicit dual sensitivity formula, straight-through proxy construction, recursive componentwise IBP derivative calculation, and maximization analogue are not compulsory public targets and must not be required for full credit.

If a proof voluntarily uses the displayed Lagrangian convention \(c^Ty+\nu^T(A_{eq}y-b_{eq})+\mu^T(Gy-h)\), with \(\mu\geq0\), its value sensitivity must be \(-\nu^Tdb_{eq}+\nu^T(dA_{eq})y^*+\mu^T(dG)y^*-\mu^Tdh\). With the bounds fixed, the inequality-data derivatives vanish. Parameter-independent variable bounds may be included as fixed inequality rows; their active-feasibility derivatives contribute zero. Equivalent multiplier conventions receive credit when used consistently with stationarity and multiplier signs.

At a kink, the public identities concern common limiting branches, or convex combinations of complete matched identities. Independently selecting subgradients of separate component functions is not a valid justification of an exact chain rule. Do not demand an ordinary gradient at a nondifferentiable point.

The source's optional maximization construction is outside the required minimum-direction target. A solver need not provide it.
