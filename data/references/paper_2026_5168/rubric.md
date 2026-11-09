# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly identifies \(X_a-X_b\) as \(\mathcal N(m_a-m_b,2C)\), including the role of independence and the fact that positive semidefiniteness permits an orthogonal diagonalization.
- **5 points:** Correctly evaluates the kernel-overlap expectation, coordinatewise or by an equivalent valid multivariate calculation, obtaining both \(\det(I+C/\varepsilon)^{-1/2}\) and the exact exponent \(-q_{ab}\). The derivation must remain valid when \(C\) is singular; deterministic zero-variance coordinates or another valid treatment of degeneracy are acceptable.
- **3 points:** Correctly substitutes the affinity formula into the mean-field row normalization, cancels the positive common prefactor, and obtains the displayed transition formula. Correctly concludes that the transition matrix depends solely on \((q_{ab})\), while the affinities are determined by \((q_{ab})\) only up to their common prefactor.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Merely citing a Gaussian-overlap formula without establishing the determinant and exponent is insufficient for the central step. A correctly stated standard identity with its hypotheses checked and parameters explicitly substituted is acceptable; reproducing its scalar integral derivation is not mandatory.

For \(a=b\), the affinity uses two independent draws from the same class, not a self-comparison of one random draw. Do not exclude singular covariance, coincident means, or \(K=1\).

Do not credit an unqualified assertion that the unnormalized affinity matrix is determined by \((q_{ab})\) alone: its common determinant prefactor retains covariance and bandwidth dependence. Assess such an overstatement within the final three-point component without discarding otherwise correct calculations. The task concerns row normalization of averaged affinities; no identification with an expectation of pointwise normalized transitions is required or justified.
