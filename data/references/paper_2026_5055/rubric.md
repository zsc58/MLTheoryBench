# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Handles the fixed-data ensemble expectation, centering, and well-definedness correctly, and supplies valid finite-remainder and integrability justification consistent with the public remainder definitions. The supplied ridge-resolvent error identities may be used directly; rederiving them is not required.
- **4 points:** Derives all three quadratic and all four cubic training products with the correct signs and matrix order. Establishes the fourth-order expected matrix remainder. Distinguishes the quadratic coefficient L_1 from the cubic coefficient L_2; does not assert that covariance alone determines third moments.
- **3 points:** Derives the full quadratic test correction: the three pure-kernel terms weighted by the population matrix, both kernel–population-matrix terms, the pure-kernel term weighted by the population vector, and the population-vector–kernel term. Gives correct signs and an expected remainder of the stated third insertion order.
- **1 point:** Subtracts at matching insertion order to obtain E_gen^(0) and E_gen^(1)=E_te^(1)−(γ²/N)y^TL_1y, preserving the mixed terms and absorbing only cubic and higher contributions into the stated remainder.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's interpolation, notation, derivative estimates, numerical remainder constants, or presentation choices. Symmetry-based combinations of equivalent scalar terms are acceptable.

Do not require a proof of the assumed covariance law, a derivation of that law from neural-network initialization, a numerical evaluation of the mixed expectations, or use of a specialized external result. The task asks for conditional coefficient identities, not those additional claims. Substitution of the covariance law into L_1 is valid but is not an extra required target.

Almost-sure convergence of a Neumann series alone does not justify exchanging its infinite sum with expectation. A finite expansion with an integrable remainder, or another justified expectation argument, resolves this obligation. Mere fluctuation-order labels without the stipulated expected-remainder control are insufficient for full credit.

Omitting a mixed contribution without a valid symmetry combination or a demonstrated vanishing condition is a substantive gap. Conversely, the task does not require mixed contractions to be nonzero in every model.

L_2 is required in the cubic training expansion but is not part of the quadratic gap coefficient. An auxiliary approximation that also subtracts L_2 may coexist with a cubic remainder, but does not replace the requested identification of E_gen^(1). Do not demand an unrequested cubic test or cubic gap expansion.

Do not infer uniform inverse-width error rates when resolvent factors or other deterministic coefficients are uncontrolled. No separate case calculation is necessary for zero labels, vanishing fluctuations, or singular kernels if the proof already covers them.
