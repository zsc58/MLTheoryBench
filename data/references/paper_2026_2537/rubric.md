# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly states the closed setup for the finite label universe, positive integer dimensions, nonempty label sets, and every-label-occurs condition; derives T_ml=sum_i k_i(x_i-mu)(x_i-mu)^T, the residual formula R=T_ml-T>=0, its vanishing criterion, and 0<=B<=T_ml.
- **3 points:** For uniform cardinality, proves T_ml=kT, reduces TD to the Ky Fan eigenspace of 2B-kT, proves TR maximization using the hypersimplex and the stated aggregate subset-ratio hypothesis, analyzes RT and DR through generalized Ritz values, and verifies the stated commutativity and strict boundary separations give one common optimizer. The proof must not infer uniqueness of TR solely from individual generalized ratios.
- **3 points:** For variable cardinalities, identifies the TD eigenspace of 2B-T_ml, explains with a valid multilabel witness why RT generally need not coincide, and proves the PSD-specialized Davis--Kahan bound ||sin Theta||_2<=||R||_2/gamma using the full Sylvester residual argument under the stated gap and residual condition.
- **2 points:** Establishes the spectral residual estimate using the multiply labelled subset, explicitly handles K empty, and correctly interprets the single-label case R=0.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the determinant or trace-ratio optimization argument, failure to state the spectral gap hypothesis, failure to close the label and dimension domains, an invalid optimizer-mismatch example, or replacing the full-residual perturbation proof by an unsupported off-diagonal-residual assertion as theorem-critical gaps.
