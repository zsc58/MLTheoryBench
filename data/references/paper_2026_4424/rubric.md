# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the split-half cosine RDM, Spearman midrank correlation, estimator domain, and zero-half convention, and correctly distinguishes the exhaustive equipartition average from a realized finite estimator and identifies it with the partition expectation. Restating definitions already supplied in the task is not required.
- **2 points:** Supplies a valid explicit X and orthogonal Q, verifies Q^TQ=I, and derives Y=XQ.
- **2 points:** Proves XX^T=YY^T, verifies that the common centered Gram matrix is nonzero, and hence establishes that linear CKA(X,Y) is defined and equals 1.
- **4 points:** Correctly evaluates all three equipartitions for X and Y, checking that ordinary correlations are defined and applying the zero-half convention where appropriate, obtaining bar S(X)=1/2 and bar S(Y)=-1/3 and concluding non-invariance of S_30. For the reference construction, this includes the -1/2 tied-rank calculation and the degenerate-half value 0.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the particular matrices, ordering, or individual partition scores used in the reference if the claimed dissociation and calculations are correct. Correct use of supplied definitions earns credit without their verbatim reproduction.

The exact numerical targets concern the exhaustive average, equivalently the expectation over random partitions, not every realized average of 30 draws. Differing expectations of these bounded estimators establish differing distributions and suffice for the requested non-invariance. Do not require a claim of inequality for every partition sequence. Do not silently assign zero to other undefined cosine or rank correlations; only the stated identically-zero-half convention is available.
