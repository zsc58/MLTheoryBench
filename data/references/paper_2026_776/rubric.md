# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Covariance and linear/PCA reduction (2 points).** Computes the population covariance, verifies its positive spike strength, and uses the exact linear risk and Rayleigh-Ritz characterization to identify the minimizers and their zero hidden-spike overlap. A proof restricted directly to the stated sphere is acceptable; unrestricted radial minimization is an alternative, not an additional mandatory target.

2. **Overlap reduction and coefficient structure (3 points).** Correctly connects the model to the supplied overlap expansion and establishes the coefficient facts needed by the dynamics. In particular, centering, whitening, and the zero cross-moment eliminate the linear terms and all quadratic terms except the u-square term. Distinguishes literal monomial coefficients from the named quantities C2=2C_20, C3=2C_21, C_(3,1)=6C_31, and C_(2,2)=4C_22. If deriving the Hermite representation, uses standard-normal contraction with the correct factorials and the actual whitened coordinate, includes the whitening factor in the latent-moment specialization, and justifies convergence on feasible overlaps. The task supplies the existence of the expansion, so a solver need not independently reprove the entire Hermite expansion or an unused moment identity. It must, however, justify every structural coefficient fact on which its proof relies.

3. **Overlap flow and initialization control (2 points).** Obtains the correctly projected two-dimensional equations for the d-rescaled flow. Establishes appropriate spherical initialization bounds, including anti-concentration when used. Respects the source's confidence-dependent order of choices: a fixed ratio cutoff supplies a fixed confidence bound, not a probability tending to one by itself. Uses absolute overlaps and handles both signs of initialization. Correctly relates rescaled and unrescaled times.

4. **Dynamical regimes (3 points).** Supplies explicit invariant-region, integrating-factor, or valid alternative estimates proving both forcing cases, early-stage u-recovery with the stated hidden-overlap bound in the no-direct-forcing case, and uniform non-recovery over every deterministic o(sqrt(d)) horizon when C2>=0, including C2=0. Establishes the logarithmic-time upper and lower estimates and the stated probability quantifiers. Recovery times may be trajectory-dependent times in the prescribed interval, as in the public statement.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or derivations of facts explicitly supplied by the problem.

Do not assume that C3=0 eliminates every cubic monomial. Terms such as C_12 m_u m_v^2 and C_03 m_v^3 are permitted and must be retained or bounded when relevant. In the no-forcing case, the stated coefficient inequality does not by itself imply monotonic contraction of the hidden overlap. A valid bounded-amplification estimate up to the early-stage recovery time suffices.

Do not require positive signed overlaps, probability tending to one for a fixed finite initialization-ratio cutoff, a deterministic recovery time stronger than the public target, or any claim about the dynamics after the early-stage time under consideration.

Treat omission of a whole regime, use of the wrong mixed coefficient, an incorrect normalization that changes the third condition, or unsupported theorem-critical exit/forcing/comparison bounds as a substantial gap. Merely naming a specialized method does not close an estimate needed by the proof. No unresolved reference-proof obligation is designated as an assumed or completed scoring step.
