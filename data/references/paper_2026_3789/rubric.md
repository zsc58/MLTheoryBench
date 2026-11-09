# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly expand the mode contractions into planted and subset-indexed noise terms. Derive the coordinate-product lower and difference bounds, the one-point noise estimate of size `K_d[L(1+delta)+Theta delta^2]`, and a uniform two-point noise estimate of size `K_d[L+Theta r/beta]d_loc`. Respect the event's sums of operator norms and maxima. Its individual norm consequences may be used, but they must not be asserted to define the identical event in the reverse direction.
- **2 points:** Establish a positive scalar coefficient at least `beta/2`, nonzero normalization denominators, and positive output planted coordinates. Derive `delta(A(U))<=b_beta+kappa_aff delta(U)` with a consistent dimension-only choice of constants, and use the assumed radius inequality to prove the basin self-map property.
- **3 points:** Establish the genuine two-point contraction in `d_loc`. Control both the orthogonal-noise difference and the scalar-coefficient difference, including the signal-product contribution. Justify the normalization estimate and explicitly absorb its scalar-sensitivity term into `C_d L/beta+C_d Theta r/beta^2` under the stated assumptions. The displayed constant must be chosen consistently, independently of the parameters, rather than changed after it has entered the assumptions.
- **2 points:** Iterate the affine inequality to obtain the exact finite-time geometric-sum bound, including `t=0`. Verify nonemptiness and completeness of the positive-chart basin, apply the self-map and strict-contraction result to obtain the unique fixed point and geometric convergence, and derive the fixed-point error bound by applying the affine inequality at the fixed point. The infinite-time noise-floor consequence is justified by the already-established all-time self-map property.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. The proof need not use the particular auxiliary constants, subset notation, or normalization parametrization in the reference proof. It may prove a sharper bound or show that some of the supplied sufficient conditions are unnecessary.

The normalization estimate may be established directly from its formula or by a correct derivative argument. If a version requiring a common lower scalar bound and common upper noise bound is invoked, check those hypotheses for both inputs. Banach's theorem may be invoked as standard background without reproving it, provided its nonempty complete metric-space, self-map, and strict-contraction hypotheses are verified.

Do not award credit for merely naming multilinear expansion, normalization, or Banach's theorem without carrying out the required bounds or checking the relevant hypotheses. The two-point contraction is theorem-critical: an affine one-point recursion alone, or a plausible proof architecture with an unproved scalar-normalization contribution, is incomplete. Do not treat a paper-specific local contraction theorem as an available premise.

The source's detailed contraction expression and the public `kappa_ctr` are not definitionally identical; it is sufficient to prove that the actual Lipschitz coefficient is bounded by the public expression. A coherent common enlargement of constants depending only on `d` is allowed.

The requested floor is exactly `b_beta/(1-kappa_aff)`. Do not require, or accept as an unconditional deduction, a uniform `O(1/beta)` floor without control of `L` and the contraction margin. No probability estimate, fourth-moment hypothesis, initializer construction, KKT conclusion, singular-value estimate, or uniqueness outside the positive local basin is required.
