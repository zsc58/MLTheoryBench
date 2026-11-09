# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly compute the radial spherical divergence and prove both directions of equivalence between the spherical continuity equation and the one-dimensional flux equation, including the induced density factor and its negative derivative term.
- **3 points:** Justify the vMF normalization derivative and its relation to the publicly defined Bessel ratio, correctly differentiate the flux terms, and derive the stated singular scalar ODE with the right coefficient and forcing.
- **3 points:** Solve the singular ODE, impose interior boundedness, justify the cancellation needed at the opposite endpoint, establish continuous endpoint limits with the stated values, and prove uniqueness in C([-1,1]).
- **2 points:** Transfer the solution through the radial equivalence and rigorously justify the continuity equation at the poles. Establish the spatial regularity or an equivalent valid divergence argument needed for the continuous pole extension.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular integral substitutions. Standard Bessel or vMF identities may be used when their relevant statements and applicability are made clear; a derivation from the defining series is also acceptable. All equation assertions concern t in I=(0,1); the schedule is defined on [0,1].

Treat omission of endpoint boundedness, continuous endpoint limits, opposite-end cancellation, or uniqueness as a theorem-critical gap. Naming an integrating-factor method without deriving or otherwise establishing the required solution is insufficient. The ODE is imposed on (-1,1), so independently assigned endpoint values are not constrained without continuity.

Boundedness of psi and vanishing of P_x(w) prove continuity of the velocity, not continuity of its divergence. Do not award the pole-extension step solely for that observation. A valid proof may establish smooth endpoint extensions of psi, sufficient derivative control together with differentiability of the spherical field, or another rigorous argument establishing the stated classical identity at the poles. Substitution into the singular ODE requires justification that the derivative term has the claimed limiting behavior.

The proof must cover d=2 and allow dot{kappa}_t=0; strict increase of a C^1 schedule does not imply its derivative is everywhere positive. Do not require flow-of-measures equivalence, marginal-velocity machinery, or any result outside the frozen theorem.
