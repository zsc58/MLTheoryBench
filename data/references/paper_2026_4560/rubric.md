# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the invertible change-of-basis relation between any two rank-r exact factorizations and derives \(\mathbf1_r^TQ=\mathbf1_r^T\) from the simplex constraints.
- **3 points:** Uses the first scatteredness condition and the dual-cone geometry to show \(\|q_i\|_2\le s_i\), where \(q_i^T\) is row i of Q and \(s_i=q_i^T\mathbf1_r>0\). Uses \(\sum_i s_i=r\), Hadamard's inequality, and the arithmetic-geometric-mean inequality, or a valid equivalent argument, to obtain \(|\det Q|\le1\).
- **3 points:** Uses equality of the optimal determinant values and \(\det(HH^T)>0\) to obtain \(|\det Q|=1\). Correctly analyzes equality in the bounds: every row sum and row norm is one, and the rows are mutually orthogonal, so Q is orthogonal.
- **2 points:** Converts QH>=0 and orthogonality into \(\operatorname{cone}(H)\subseteq\operatorname{cone}(Q^T)\), applies the second scatteredness condition, and concludes permutation equivalence of both factors.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The dual-cone characterization and equality cases must be justified, not merely named. A proof using only the necessary dual-cone inclusion rather than the full characterization is sufficient if that inclusion is justified.

The identity \(\mathbf1_r^TQ=\mathbf1_r^T\) fixes column sums, not row sums. It does not by itself imply that every row sum or row norm is at most one. Do not award full credit for that inference unless the missing argument is supplied; the source-grounded route uses the total row sum and a product bound, followed by optimality and equality cases.

A fully correct proof must cover r=1 as well as r>=2. A uniform argument that is valid at r=1 is sufficient; a separate case is not mandatory. If a dual-cone calculation divides by \(\sqrt{r-1}\), r=1 needs separate treatment. A missing readily repairable boundary case is consistent with the 8-9 band, not with full credit. For r=1 alone, direct use of the simplex constraints proves uniqueness without cone or determinant machinery.
