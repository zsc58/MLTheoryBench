# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the pushforward/change-of-variables identity, including its Jacobian factor, and recognizes that pi_t is a positive probability density.
- **3 points:** Correctly derives the continuity equation. For the Jacobian proof, this includes `partial_t D_xF_t=(D_yu_t)(F_t)D_xF_t` and the trace calculation giving `partial_t |det D_xF_t|=|det D_xF_t|(div u_t)(F_t)`.
- **3 points:** Uses the defined score-corrected drift and `pi_t grad log pi_t=grad pi_t` to derive the stated Fokker-Planck equation with the correct signs and factor of one half.
- **2 points:** Correctly concludes the prescribed SDE marginals on the nonexplosive positive-time interval by applying a valid forward-equation/SDE correspondence and checking its hypotheses. The explicit local regularity and square-integrability assumptions satisfy the relevant local coefficient conditions; positivity, unit mass, and nonexplosion close the marginal identification. A valid alternative identification argument earns the same credit.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require incidental presentation choices or the reference proof's killed-domain argument when another valid standard correspondence is accurately applied.

For a proof using Jacobi's formula, omission of the substantive Jacobian-to-divergence link is a core gap. This requirement does not apply to a complete alternative continuity-equation proof. Merely naming a score-based diffusion without deriving the two equations is a major gap.

Do not require a closed-form expansion of the score through F_t^{-1}; that expansion is not a public target. Do not penalize a signed determinant when positive orientation is justified: F_1 is the identity and det D_xF_t cannot change sign on the positive-time interval.

A bare assertion that SDE uniqueness is automatically equivalent to uniqueness in an unspecified Fokker-Planck solution class does not justify the final step. Conversely, a correct application of the regularity-qualified standard correspondence need not reprove that background theorem. Do not demand additional global growth, moment, or drift-integrability assumptions absent from the task.

The equations are asserted for positive times, with a left time derivative at t=1. The marginal conclusion begins at t_0>0 and concerns nonexplosive solutions, not killed or explosive laws. Zero noise is allowed; no division by sigma is valid or necessary.
