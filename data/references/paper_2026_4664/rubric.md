# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly applies the multivariate chain rule through the componentwise activation and identifies the outer activation-derivative factor diag(sigma'(s_m(t))).
- **2 points:** Uses the product rule on the attention-weighted sum and derives the direct term alpha_mn(t) W_mn from differentiating the selected neighbor message with fixed matrices.
- **4 points:** Correctly uses n != m and the pairwise score dependence to establish that only e_mn varies with x_n, applies the softmax derivative alpha_mr(delta_rn-alpha_mn), and forms the resulting outer-product summation with correct indices and dimensions.
- **2 points:** Combines the direct and indirect contributions into the exact stated Jacobian block and correctly identifies their direct-influence versus softmax-competition roles.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The standard softmax derivative may be used without reproducing its quotient-rule derivation. Treat omission or incorrect handling of the indirect softmax pathway as a theorem-critical gap.

The asserted derivative is off-diagonal: n != m. Holding the receiver state fixed follows from this restriction and the meaning of the partial derivative, not merely from fixing the node label m. Scores may depend on the receiver state. Self-loop messages are allowed and must not be silently removed; their receiver-state dependence is constant with respect to the selected distinct neighbor input. Do not require an extension to diagonal blocks or a graph without self-loops.

Do not require nonzero message matrices, score gradients, or activation derivatives. A valid general calculation covers these cases. Empty or self-only neighborhoods have no asserted cross-client block, and a singleton distinct-neighbor neighborhood has zero competition term. Separate discussion of these cases is unnecessary when the argument already covers them.
