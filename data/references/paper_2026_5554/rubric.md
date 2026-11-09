# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Singular-value dynamics and contraction (2 points).** Uses the supplied ideal field and the simple-positive-singular-value differential to derive dot sigma_i=-eta alpha_i, establishes alpha_i=||P_perp u_i||_2^2 in [0,1], and proves Frobenius-norm contraction. Deriving the projected Euler construction is optional because the vector field is supplied in the task.

2. **Normalized spectral derivative (3 points).** Correctly differentiates the normalized singular values and pairwise functional, proves sum_i tilde sigma_i S_i=C, and obtains the exact (2eta/rho)sum_i alpha_i q_i formula and its iff sign criterion. Flattening means nonpositivity of this derivative, not an unstated majorization, entropy, or convergence assertion.

3. **Measurement-geometry ordering (1 point).** Establishes strict opposite ordering across unequal coordinates by a valid comparison, such as cancellation of the mutual-pair term followed by the reciprocal-denominator calculation. Merely naming monotonicity without justification is insufficient.

4. **Fixed-radius variational conclusion (2 points).** Supplies a valid convexity/symmetrization and radial argument, or another correct proof, establishing both attainment and uniqueness of the flat spectrum c/sqrt(r). Handles the domain of all positive rank-r spectra, including repeated values. Does not impose interpolation or the trajectory's simple-spectrum restriction on this separate optimization problem. Includes the permutation/frame qualification.

5. **Approximate-alignment stability and exactness (2 points).** Bounds the field error by eta delta_P at the same current W; propagates it to both requested derivative estimates with admissible uniform constants; proves the compact-polar perturbation bound or invokes a correctly stated, applicable standard result; and establishes exactness when the polar factors coincide. A complete proof of the normalized-functional estimate must justify a bound of the form C(r)/sigma_min, rather than merely asserting smoothness on a noncompact stratum.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The estimates can be proved with C_1=1 and C_2=sqrt(r)(r-1). Constants depending only on r are admissible; a solver need not introduce artificial dependence on Delta, delta_W, or delta_G. The public simple-spectrum, constant-rank, and positivity hypotheses provide the domain for differentiation, but a solver need not restate each hypothesis at every use. Do not treat the absence of a numerical gap factor as a gap in a valid first-derivative proof.

The stability trajectory is a separate near-manifold trajectory. Its G is the specified driving matrix, not necessarily G_ls(W). The source's positive lower bound is an assumed condition, not a probability statement to be proved. The time interval is likewise assumed to preserve the stated rank, positivity, and gap conditions; neither automatic rank preservation nor a quantitative lower bound for T is a requested conclusion.

A bound for square invertible polar factors alone does not automatically cover the permitted rectangular, rank-deficient matrices. A cited standard result must have the relevant compact-polar domain and hypotheses. The direct symmetric-matrix verification in the reference proof is one acceptable way to close this obligation.

Equality of left and right subspaces alone is not equality of polar factors. Shared compact singular frames are sufficient for equality of polar factors, but the task's exactness condition does not require the converse.

Treat omission of a substantive normalized-derivative calculation, the strict q-ordering argument, fixed-radius attainment/uniqueness, either required stability estimate, or the polar perturbation bound as an unclosed requested obligation. Assess the resulting score by its mathematical importance; do not penalize a solver for declining to prove an unrequested projection construction, horizon guarantee, or stochastic-model claim.
