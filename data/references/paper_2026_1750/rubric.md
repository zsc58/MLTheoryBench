# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the constrained critical points \(\pm e_i\), critical values \(\lambda_i\), and Hessian Morse index \(i-1\). For a direct proof that does not use Morse theory, award these points instead for the valid spectral-coordinate construction and estimates that replace this analysis; critical-point and Hessian calculations are not mandatory for full credit.
- **3 points:** Establishes the complete sublevel topology sequence \(\varnothing,S^0,S^1,\ldots,S^{n-1}\) by a valid argument. This includes the empty range \(c<\lambda_1\), the full-sphere range \(c\ge\lambda_n\), and the critical-level behavior needed for \(\lambda_k\le c<\lambda_{k+1}\). A handle argument must justify the resulting topology rather than rely only on handle counts.
- **3 points:** Correctly derives all persistence intervals and their endpoint conventions from the inclusion-induced maps or an equivalent valid persistence argument: the \(n-1\) finite bars \([\lambda_k,\lambda_{k+1})\) in degree \(k-1\), together with the two infinite bars and their degrees, with no missing or extra classes. Account for the degree-zero merger, persistence within each spectral range, and the final top-dimensional birth. Include \(n=1\), where both infinite bars lie in degree zero, and \(n=2\), where the degree-one infinite bar is born at \(\lambda_2\).
- **2 points:** Computes the total finite persistence by summing the bar lengths and obtains \(\lambda_n-\lambda_1\), including the empty sum when \(n=1\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or Morse theory when a direct proof closes all target obligations. In a direct proof, the first two points reward the coordinate construction and its validity, while the next three reward its complete application to the sublevel ranges and endpoints.

A method name without the corresponding derivation does not earn the associated points. Regular-level Betti numbers alone do not establish the exact persistence module: the proof must also justify the relevant inclusion maps and critical endpoints, either explicitly or through a correctly stated applicable result. Routine omissions should be assessed proportionately under the scoring guide, not treated as an automatic failure of every downstream step. Propagate a dependency failure only when it leaves the stated downstream barcode conclusion unsupported.
