# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **3 points:** Uses equivariance under permutations fixing a target index to establish symmetry in the other rows, and uses row relabeling to obtain one common target-row function for all output coordinates. A valid continuous target-row/multiset factorization is acceptable, but an abstract quotient construction is not required.
2. **3 points:** Establishes the required invariant sum-of-row-features representation rather than merely naming a specialized method. For approximation, the reference route averages a polynomial approximant and expresses invariant coefficient polynomials through aggregated row monomials, with a valid orbit-sum argument. For scalar exactness, power sums must be shown to determine the remaining multiset, including multiplicities. Any alternative valid construction is acceptable.
3. **2 points:** Establishes the uniform approximation with the correct quantifier order and finite dimensions, and completes scalar exactness with continuous maps on the domains stated in the task. In the scalar construction this includes continuity of the inverse on the compact encoded image and extension of the outer map to the ambient latent domain, or another valid way to obtain that domain. Standard polynomial approximation and real-valued continuous extension results may be used with their hypotheses satisfied.
4. **2 points:** Assembles all coordinates using the same maps and explicitly verifies the resulting vector's permutation preservation with a consistent index convention.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation, its particular feature dimensions, or its polynomial construction. A construction giving exact representation in more than the scalar case is also acceptable, provided it is justified.

Treat omission of scalar exactness, uniformity, or the equivariance verification as substantive gaps. Do not regard a bare appeal to a specialized invariant-representation theorem as establishing an unspecified finite-dimensional multiset encoder. If an external theorem is used, its relevant statement and applicability must actually justify the construction.

An otherwise complete proof that defines the scalar outer map only on its compact encoded image but omits the routine continuous-extension step has a readily repairable omission rather than a substantive failure of scalar encoding. The empty-domain case is vacuous under the task's zero-error convention; do not require a separate lengthy discussion of it.
