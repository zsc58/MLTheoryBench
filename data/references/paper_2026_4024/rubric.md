# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly normalizes the hidden permutation, uses feasibility and optimality against the planted permutation, and derives the O(sigma sqrt(n)) commutator bound for every minimizer. The argument must work for both feasible sets and must not exclude sigma=0 by dividing by sigma.
- **3 points:** Diagonalizes A, introduces an index-band/off-band decomposition, and validly derives the lower bound relating the commutator to the squared trace deficiency. This must use the total-mass identity rather than merely assert that trace is controlled.
- **3 points:** Establishes the required uniform entrywise control of the projected all-ones matrix and uses extreme points plus convexity, or an equivalent valid argument, to prove a positive lower bound proportional to n-Tr(X). Merely naming Haar concentration or an internal lemma without deriving the relevant uniform conclusion is insufficient for full credit. A Gaussian-expansion proof must account for noncentered lower-order terms, random coefficients, both diagonal and off-diagonal entries, and failure probabilities sufficient for a union bound over all entries.
- **1 point:** Establishes the Omega((log n)^-8) separated-eigenvalue bound at the required band width. If using the source's rigidity route, the precise source-grounded error is n^(-2/3)(log n)^(C log log n), and its ratio to the chosen band width must tend to zero. The underlying nonstandard rigidity obligation must be justified rather than treated as proved merely because it is cited.
- **1 point:** Combines the estimates with the correct powers of n and log n, converts trace deficiency to Frobenius error, and proves the row-wise rounding consequence for both feasible sets, all minimizers, and arbitrary argmax tie choices on a common high-probability event.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, the use of extreme points when a direct deterministic inequality is supplied, or the exact auxiliary estimates used in the reference.

The source's threshold t=O(n eta log^2 n) does not give polynomial failure probability from its displayed quadratic-form inequality at eta=kappa/(log n)^4. A sufficient corrected threshold is K_c n(sqrt(eta log n)+eta log^2 n). Other valid estimates are acceptable. Do not penalize a solver for rejecting the incorrect threshold or for retaining noncentered terms that the original reference incorrectly described as centered.

A proof that establishes the main rate but leaves projected-matrix separation or its uniform random-matrix justification unsupported has a theorem-critical gap and cannot receive a near-complete score. Explicit statements of independent standard concentration results, together with verification of their hypotheses, are acceptable; a paper-specific projected-matrix lemma is not a substitute for its derivation.

# Private GT Quality Warning

The replacement reference closes the Gaussian/projection calculation and the deterministic deductions, but it does not derive the nonstandard rigidity input theory_013. Its Section 5 states the exact remaining assertion and proves only the implication from that assertion to the separated-gap estimate. Do not treat this citation as a completed rubric step, and do not use agreement with this conditional portion of the reference as evidence that an answer is fully proved. A correct conditional deduction may receive credit for the deduction actually established, but full proof closure requires justification of the remaining input or a valid alternative route. This limitation concerns the private GT, not the definition or source fidelity of the public task.
