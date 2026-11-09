# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses AA^dagger Y=Y for Y in range(A) and A(I-A^dagger A)=0 to prove zero consistency risk for the stated family. Explains why rank(A)<n permits distinct nullspace components with unchanged measurements and loss.
- **3 points:** Derives the split loss as the quadratic risk weighted by Q(A1)=E[A^T A|A1], retaining 1/m. Justifies averaging over A while holding f(Z)-X fixed, for example by conditioning on (X,A1) and using independence of X from (A,A1). An equivalent correct conditional-factorization argument is acceptable.
- **3 points:** Conditions on Z=(Y1,A1), completes the square around E[X|Z], and proves the complete almost-sure minimizer characterization. Establishes that the conditional mean has finite split risk by comparison with a finite-risk competitor, and that zero excess risk is equivalent to Q(f-E[X|Z])=0 almost surely. Obtains both directions of the measurable pseudoinverse/nullspace parametrization.
- **2 points:** Correctly proves that almost-sure invertibility of Q removes the nullspace term and yields the unique minimizer E[X|Y1,A1] up to almost-sure equality. Does not assume an unnecessary uniform eigenvalue lower bound or additional estimator access to A or Y.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the complete nullspace characterization or of the weighted-risk equivalence as a theorem-critical gap.

Conditioning only on Z is acceptable if the proof also establishes the conditional independence of A and X given Z needed for the quadratic calculation. The identity E[A^T A|Z]=Q(A1) alone is not sufficient to replace A^T A inside a product involving X.

The optimization domain is the nonempty class of measurable functions with finite split risk. Do not require f or the arbitrary nullspace component to have a finite unweighted second moment. Recognized measurability of the finite-dimensional pseudoinverse may be used without reproducing its limit formula. Routine integrability details may be concise, but a proof must not subtract infinite risks or assume that finite conditional Gram entries imply an unconditional operator second-moment bound.

All minimizer identities are almost sure. Singular Q, including Q=0, is allowed before the final specialization. No extra credit requirement is imposed for discussing empty or full row selections; the argument must remain valid for them when they occur.

The source normalization and function-domain slips are already corrected in the public task. Score the normalized statement given to the solver, not the uncorrected source displays. All reference-proof obligations are closed; no GT quality warning applies.
