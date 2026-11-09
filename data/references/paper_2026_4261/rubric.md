# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly sets up the two covariance-pair comparisons, using partial-symmetric tensors or an equivalent matrix formulation, and verifies the required rank or nondegeneracy conditions. In particular, recognizes that coefficient diversity and nonnegativity make each pairwise covariance sum positive definite even though individual covariances may be singular.
- **3 points:** Derives signed representations of any competing solution in both bases. A tensor proof must correctly apply an appropriate uniqueness result and resolve scaling and permutation using the known coefficient pairs. An elementary proof may instead use orthogonal congruence with distinct normalized coefficient eigenvalues, or another valid argument establishing the same signed representations.
- **4 points:** Compares the two signed representations and uses the transverse-subspace condition through the positive eigenspaces of the signed involutions, or an equivalent argument, to prove that only one common global sign remains. Accounts for the empty and full positive-eigenspace cases.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require tensor terminology, an external uniqueness theorem, or the reference proof's incidental presentation choices. Allocate the first two core-step scores to equivalent setup and pairwise-uniqueness arguments in alternative proofs.

A bare invocation of tensor uniqueness without checking its hypotheses, or an unsupported assertion that transversality resolves signs, does not earn the corresponding core-step credit. Nonnegative eigenvalues need not be strictly positive: do not accept an argument that assumes an individual input or output covariance is invertible without justification. Invertibility of a competing solution follows from a positive-definite covariance-pair sum; another valid justification is equally acceptable.
