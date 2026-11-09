# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expands both EMA-weighted Gram matrices of \(Z_t=AG_tB\), retaining the expectation and EMA operations and obtaining the two equations involving \(A\) and \(B\).
- **4 points:** Uses SPD symmetry, full-rank/positive-definiteness, and uniqueness of the SPD inverse square root to derive both coupled inverse-square-root equations, rather than merely naming whitening or a related method.
- **2 points:** Establishes the converse: the coupled equations imply both row and column time-averaged orthogonality identities.
- **2 points:** Clearly identifies the mutual dependence of the two equations and maintains all stated dimensions, identity matrices, and EMA/stochastic quantifiers.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The elementary SPD square-root theorem may be used as standard background when its hypotheses and application are clear. For example, deriving \(M=A^{-2}\) from \(AMA=I\), then identifying the positive inverse square root, is sufficient. Do not require the reference proof's explicit diagonalization. An unsupported assumption that arbitrary SPD matrices commute is not valid.

The proof must apply throughout \(0\le\beta<1\). A finite-sum argument that also works when earlier weights vanish already covers \(\beta=0\); a separate endpoint paragraph is not required. Preserve the uncorrected EMA normalization.

Do not require existence or joint uniqueness of a simultaneous pair \((A,B)\), independence or identical distribution of the gradients, or full rank of individual gradient realizations. Do not impose \(m=n\) as an additional hypothesis. The trace obstruction when \(m\ne n\) is a valid optional observation, but alone does not prove the characterization for the remaining dimensions. The private boundary checks are not additional scored targets.
