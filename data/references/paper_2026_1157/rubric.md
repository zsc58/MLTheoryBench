# Scoring Guide

- **0:** No correct idea or no relevant valid argument.
- **1-2:** Some relevant observations, but no correctly established major conclusion.
- **3-7:** Correct progress on one or more core conclusions, with major omissions or an invalid stationary-point argument.
- **8-9:** All principal conclusions are correctly established, with only minor omissions in routine geometry or bounded-model details.
- **10:** Complete proof under the stated feasible-set, rank-cap, and limiting-subdifferential definitions.

# Core Steps

- **2 points:** Prove the rank/column-sparsity identity for every matrix of rank at most \(r\), including both the lower bound and a padded compact-SVD equality case; use it to prove equality of values, global-minimizer projection, and global SVD lifts.
- **2 points:** State and use the bounded-model hypotheses, including \(\tau\ge\|\mathcal B^Z\|_{\max}^{1/2}\) and \((\mathcal B^Z\times\mathcal B^S)\cap G_L\ne\varnothing\), to prove the bounded value equality and both global-minimizer inclusions.
- **2 points:** Prove that a padded compact-SVD lift of every local minimizer of \(L\) is locally minimizing for \(F\), using product continuity and the pointwise comparison \(F\ge L\circ(X,Y,S)\).
- **2 points:** Use the stated limiting-normal stationarity definitions to lift every stationary point of \(L\). The argument must handle both \(\lambda>0\) and \(\lambda=0\) through the appropriate rank feasible slice.
- **2 points:** For \(\lambda>0\), project factor stationarity back to original-model stationarity. The proof must use the intersection of the two active-column sets, derive the two product orthogonality relations, and identify the resulting rank-manifold normal direction.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. Do not require the source's notation. Do not award full credit for merely naming compact SVDs, normal cones, or the rank/column representation without deriving the needed comparisons and inclusions. Do not require the factor active-column sets to be equal at an arbitrary stationary point; their intersection is sufficient for the converse argument.
