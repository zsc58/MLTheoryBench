# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives M = c D L D from the spectral transformation and proves that every k-principal minor, and hence the normalizer, is multiplied by the same factor c^k; verifies that M remains in the k-DPP domain, concludes equality of the two k-DPP laws, and identifies all three invariances.
- **2 points:** Correctly differentiates the log determinant and finite normalizer to obtain the centered trace score, and proves that the score vanishes for every subset exactly when the trace values are constant. Award equivalent credit for another valid treatment of the differential that supports the dimension argument.
- **4 points:** Establishes that the zero-score space is a linear subspace and proves the dimension lower bound. One route constructs the linear trace map, identifies the zero-score space with the inverse image of the constant-vector line, verifies Phi(L)=k 1, and applies rank-nullity with rank(Phi) <= binom(N,k). Another route bounds the rank of the score map by binom(N,k)-1 and applies rank-nullity directly. Accept any complete valid alternative.
- **1 point:** Relates span{L} to the positive scaling tangent and correctly concludes that the strict subset-count threshold yields an additional infinitesimal, zero-score direction outside span{L}.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular auxiliary map. The dimension argument must justify the relevant rank bound and its implication for the kernel or preimage dimension; merely naming invariance, scores, or rank-nullity is insufficient.

Local non-identifiability in this problem is explicitly infinitesimal: it means membership in V_L. Do not require a construction of exact constant-law curves. Conversely, a vanishing first derivative alone does not justify an additional assertion that L+tH has the same law for nonzero t or that every H in V_L integrates to an exact constant-law curve. Eigenspace rotations commuting with Lambda leave L itself unchanged; they need not generate nonzero kernel directions.
