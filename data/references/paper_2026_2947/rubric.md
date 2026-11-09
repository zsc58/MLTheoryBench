# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Restrict to rectangular diagonal inputs and use stabilizer sign symmetries to prove the image is diagonal, with zero output in every zero-singular-value coordinate and no unmatched rectangular entries.
- **3 points:** Use permutation/sign symmetries and continuity to construct a well-defined continuous absolutely symmetric singular-value map, including repeated and zero coordinates. Continuity at zero-coordinate boundaries must be justified, for example by the coordinate formula and vanishing property, by compatible continuous orthant formulas, or by direct continuous restriction to signed diagonal inputs.
- **3 points:** Reassemble an arbitrary SVD to derive the spectral representation of every equivariant map, with independence of the SVD choice justified. When using the full stabilizer argument, justify preservation of the distinct positive singular-value spaces and the complete null spaces, equality of the paired positive blocks, and invariance of the output under these actions.
- **2 points:** Prove the converse equivariance and continuity for every map defined by a continuous absolutely symmetric singular-value transformation. Verify the zero-coordinate and repeated-coordinate properties needed for well-definedness. In a compactness-based continuity proof, identify the limiting factors as an SVD of the limit matrix and justify convergence of the whole output sequence, not just one subsequence.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A response that merely names spectral calculus or representation theory without establishing the relevant stabilizer or equivalent well-definedness arguments and SVD-independence does not earn the corresponding core-step credit.

The added details identify mathematical obligations, not mandatory formulas or a required proof organization. In the necessary direction, equality of the displayed formula with the already-defined equivariant map for every SVD establishes SVD-independence directly. A separate stabilizer classification is not required there if well-definedness in the converse is correctly established by another argument.

Well-definedness of a signed extension alone does not prove its continuity. In a stabilizer proof, the Gram-matrix commutation identities provide an elementary way to exclude mixing of distinct positive blocks with each other or with null spaces. In a limiting-SVD proof, pass to the limit in the input factorization before identifying the output limit, and apply the every-subsequence criterion or an equivalent contradiction argument.

The ordinary finite-dimensional SVD, uniqueness of ordered singular values, compactness of orthogonal groups, and continuity of singular values may be used as standard background. No continuous choice of singular vectors is required. Apply the scoring guide proportionately to local omissions; do not impose an automatic score cap merely because a solver uses a different complete argument.
