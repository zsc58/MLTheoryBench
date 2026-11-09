# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Rank and change of basis (2 points).** Derives the two embedded factorizations. Explains why scattering gives full policy rank, for example because the contained cone has nonempty interior, and obtains rank $k$ of the observable family. Establishes equality of the latent spans and an invertible $S$ with $\bar T=T^*S$ and $\Pi=S^{-1}\Pi^*$. Uses linearity and injectivity of the embedding to transfer the change-of-basis identity to signed measures before taking total mass, or gives another valid argument for $S^T\mathbf1=\mathbf1$.
2. **Minimum-volume determinant bottleneck (4 points).** Shows that rows of $S^{-1}$ lie in the policy cone's dual and obtains the cone norm bound from the displayed cone geometry. Applies Hadamard and AM--GM with the correct column-sum normalization to show $|\det S^{-1}|\le1$. Tracks equality to prove that the inverse change of basis, and hence the change of basis, is a permutation. Uses the Gram determinant transformation, positivity of the true objective, and feasibility of the true factorization to conclude pointwise optimal recovery up to permutation.
3. **Measure and policy identification (2 points).** Correctly transfers embedded equality back to transition measures via injectivity of $\Phi$ and states the policy relation with the prescribed permutation convention.
4. **Global alignment and anchoring (2 points).** Uses continuity and pairwise separation to prove that the unique pointwise permutation is locally constant. Uses connectedness to obtain one global permutation. At a point of the nonempty known-label anchor, uses distinctness and agreement to force the identity. The empty observation space, if considered, has a vacuous first conclusion and cannot have a nonempty anchor.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The elementary duality formula for the displayed second-order cones may be justified directly or invoked as standard cone duality with the correct dimension and convention; do not require the particular calculation in the reference proof. Likewise, accept standard Hadamard and AM--GM inequalities and their equality conditions. A citation to a specialized minimum-volume identification result alone does not establish the determinant and equality characterization required here.

Penalize as theorem-critical an unproved determinant/equality characterization or unsupported globalization step. Treat omission of the vacuous empty-space case as a readily repairable omission, not a failure of the main identification argument. No continuity of the true policy matrix needs to be assumed or proved to establish the conclusion. No finite-sample, compactness, or optimizer-existence argument is required: the task supplies a family of attained minimizers.
