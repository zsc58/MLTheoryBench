# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates both constrained KKT/normal-cone stationarity conditions for the asymmetric objective.
- **3 points:** Subtracts the two systems, pairs with the factor difference, and handles the normal-cone terms with the correct signs.
- **3 points:** Derives the central spectral comparison. For the symmetrization route, justifies that the discarded term is one half of \(\|P_E(UV^\top-VU^\top)\|_F^2\), applies the spectral trace inequalities to symmetric matrices and the positive semidefinite factor-difference product, and bounds the symmetrized masked product by \(\|P_E(UV^\top)\|_F\) using the Frobenius triangle inequality and transpose invariance. Accept an equivalent valid derivation of the comparison.
- **2 points:** Uses the strict hypothesis to conclude \(U^*=V^*\), then establishes criticality for the symmetric objective. The gradient is \(2P_E(WW^\top-X)W\); the reduced asymmetric KKT condition is equivalent because the normal cone is invariant under positive scaling.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The spectral/masking comparison and the transfer of stationarity are theorem-critical; merely naming a penalty or symmetry argument is insufficient. Nonnegativity alone does not justify the masked symmetrization remainder's sign. Do not require a separate boundary-case discussion when the proof already works without division by a possibly zero norm. An omitted explanation of the harmless factor-of-two rescaling is a readily repairable omission, not a failure of the theorem or its stationarity conclusion.
