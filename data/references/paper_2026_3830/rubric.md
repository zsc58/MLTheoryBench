# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

The following ten-point allocation describes the reference route. Award equivalent credit for a complete valid alternative proof; the listed methods are not additional public conclusions.

- **2 points:** Correctly establishes the spectral setup used in the proof. On the reference route, expands the projector-distance penalty and obtains the equivalent trace optimization with \(M_\lambda=\overline\Sigma+2E\lambda\overline\Pi\), identifying optimizing subspaces rather than asserting that every optimizer basis already has ordered eigenvector columns. A proof working directly from the publicly defined \(M_\lambda\) need not rederive this penalty identity; award this credit for the corresponding valid spectral setup and structural justification.
- **2 points:** Establishes the hard-solution claim: identifies the eigenvalue-one eigenspace of \(\overline\Pi\) with \(S_*\), proves inclusion in every hard solution subspace, and justifies choosing a representative basis beginning with the ordered eigenvectors of the compressed operator \(A_*:S_*\to S_*\). An arbitrary optimizer's columns are not required already to have this form.
- **3 points:** Proves operator-norm convergence of the leading rank-\(m\) projector. On the reference route, establishes eventual spectral separation and applies an appropriate perturbation theorem with its hypotheses verified. Accept another complete argument establishing the same convergence without a named perturbation theorem or an explicit separation estimate.
- **3 points:** Under simple compressed spectrum, proves both the ordered shifted-eigenvalue limits and the sign-adjusted eigenvector limits. On the reference route, uses the correct complement operator \(2E\lambda(I-B)+\delta_i I-A_{22}\), controls the complement coordinates, and uses orthogonality and ordering to identify all limiting eigenpairs. Accept an alternative complete argument without this particular block equation or an explicit \(O(\lambda^{-1})\) rate.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, penalty expansion, complement-coupling method, or intermediate convergence rate when the stated conclusions have otherwise been proved.

Failure to establish the requested direction-level conclusion under its simple-spectrum hypothesis is a theorem-critical omission. Absence of a particular method is not. Merely identifying possible limiting eigenvalues without establishing their multiplicities and ordered correspondence does not complete the eigenvalue argument.

Interpret \(A_*\) as compression to \(S_*\), not as an assumption that \(\overline\Sigma\) preserves \(S_*\). Do not accept a proof that assumes vanishing cross-block covariance, strict local eigengaps, or uniqueness of the full rank-\(k\) optimizer without justification. Do not require those assumptions from a solver.

Eigenvectors may be chosen arbitrarily within finite-penalty ties; the signs used for convergence may depend on \(\lambda\). The assertions must cover \(E=1\), \(m=k\), and singular covariances. Do not require individual-vector convergence when the compressed spectrum is repeated, or the stronger unconditional eigenvalue limit proved privately. No empirical sampling or consistency result is part of this task.
