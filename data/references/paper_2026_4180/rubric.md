# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Rescaling and valid transformation:** Correctly rescales time, the dual/primal variables, and the mirror potential. Derives a suitable convex subgradient-flow formulation. For a pseudoinverse transformation, justifies reconstruction of the dual trajectory when M is singular, using the Lipschitz trajectory's displacement in Span M; does not infer reconstruction from the pseudoinverse definition alone.
- **3 points — Mosco convergence:** Establishes both liminf and recovery inequalities for the moving translated/composed energies. Correctly uses the relative-interior and affine-hull assumptions. Handles zero translation errors and targets outside the limiting effective domain. A direct conjugate-supremum bound combined with the relative-interior recovery construction is sufficient; the source's conjugate-infimum proof is also acceptable. Merely citing the paper-specific convergence lemma does not complete this step.
- **3 points — Existence, uniqueness, and evolutionary convergence:** Verifies properness and the relevant initial subdifferential-domain and chain-rule conditions. Obtains existence and uniqueness in the Lipschitz dual solution class, identifies the indicator-potential limit, and proves uniform dual convergence and weighted L2 gradient convergence. The standard independent subgradient-flow existence/minimal-norm and evolutionary-convergence theorems may be invoked with their hypotheses checked.
- **2 points — Loss, minimization, and accumulation:** Derives weighted L1 loss convergence from the quadratic identity and weighted derivative convergence, or by another valid argument. Derives instantaneous minimization, for example from the minimum-norm subgradient property. For a single sequence converging almost everywhere to an accumulation function, proves limiting subdifferential membership and equality of the limiting loss, hence the argmin inclusion. Either a justified graph-convergence theorem or the direct scaled subgradient inequality is acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular order of the steps.

The following are theorem-critical obligations: the moving-energy recovery argument; validity of reconstruction for singular M; the initial-domain hypotheses of the flow theorems; instantaneous minimization; and the accumulation-function conclusion. Do not award full credit for replacing a paper-specific obligation by an unexplained citation to that same paper's lemma or theorem.

Uniqueness is required only for Lipschitz dual solutions. The primal trajectory need not be unique. Do not require M to be invertible or nonzero, C to have full dimension or be bounded, or h to be smooth or strictly convex.

The accumulation statement quantifies over an entire function obtained along one sequence converging almost everywhere. It does not require a common exceptional set for all such sequences, nor a conclusion for independently chosen pointwise subsequences. Weighted L1 convergence alone does not imply convergence at every time; a correct argument must use the assumed almost-everywhere convergence along the sequence, possibly with a further subsequence or uniqueness of limits in measure.

No separate convergence theorem for energy values is needed for the loss conclusion. The squared transformed-derivative identity and Cauchy–Schwarz suffice. There are no unresolved reference-proof obligations.
