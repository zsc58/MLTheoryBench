# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives gradient equivariance from loss invariance and orthogonality; proves invariance of both orbit averages using normalized-measure reindexing; and establishes that the gradient at the averaged point is fixed.
- **3 points:** Correctly identifies the centered orbit displacement and gradient outer products and uses the stipulated pointwise secant model to derive S_g=H S_z H, with H symmetric. Does not claim that differentiability alone makes the secant model exact or silently replace the gradient at the averaged point by another quantity.
- **3 points:** Derives the principal-square-root formula by congruence under S_z≻0; verifies existence, positive semidefiniteness, and uniqueness among symmetric PSD solutions, including singular S_g; and proves that the resulting solution belongs to the global commutant. Does not require H to be PSD or conclude that the PSD solution equals an indefinite H.
- **2 points:** Establishes the layer-pair decomposition into correctly typed intertwiner spaces; proves the specified diagram spanning claims for the defining representations, including the even-block signed-permutation rule, independent colors, and passive factors; handles dimension-dependent diagram dependencies; retains the GL entry as an ordinary algebraic commutant comparison; and establishes the actual represented-space coefficient count and weak monotonicity under subgroup restriction.

# Structural-Step Guidance

The structural points reward the following substantive obligations together: the block equations and their rectangular typing; valid spanning descriptions for every listed family; product and identity-factor handling; and the dimension and restriction conclusions. Merely naming a commutant, a diagram algebra, or Schur-Weyl duality without a relevant statement and valid application does not close these obligations.

It is acceptable to invoke the following standard-independent classical results without reproving them: the defining GL tensor-power commutant is spanned by tensor-factor permutations; and the defining full orthogonal tensor-power commutant is spanned by pairing diagrams. A solver must give an adequate statement and check the relevant representation and group hypotheses. These results assert spanning in arbitrary dimensions, not independence of every diagram. Accept direct alternative derivations.

For permutation and signed-permutation groups, an equality-pattern orbit argument, or an equivalent correctly stated and applicable invariant-tensor result, is sufficient. In the signed case the parity restriction must be justified or be explicitly part of the applicable result. Arbitrary representations of abstract groups with the same names do not satisfy the public diagram contract automatically.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award credit for merely naming an averaging method or square-root construction without deriving the relevant equations and claims.

Do not require positivity of S_g, independence of all abstract diagrams, a stable-dimension assumption, strict dimension growth, block diagonality of invariant matrices, or an algebra structure on a rectangular block. Do not interpret the complexity count as the minimal number of parameters for a symmetric PSD matrix or for one fixed averaged outer product.

The structural assertion does not assume the secant model or S_z≻0. Conversely, the inverse-root formula retains S_z≻0 and must not be replaced by an unrequested pseudoinverse or damped formula. A pure permutation representation having a singular centered displacement average does not invalidate the independently stated structural theorem.

The GL comparison does not authorize normalized Haar averaging over GL or replacing inverse-transpose factors by ordinary factors for a nonorthogonal action. No quantitative Hessian-approximation error bound, random-initialization result, factor-estimation algorithm, or optimizer equivalence is required.
