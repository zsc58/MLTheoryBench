# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Entropy expansion and relevance/redundancy terms (2 points):** Correctly expands \(I(Y;X_j\mid X_S)\) and obtains the terms \(I(Y;X_j)\) and \(-I(X_j;X_S)\).
2. **Prediction/error bijection (3 points):** Establishes the conditional bijection for binary outputs, transfers the conditional entropy to \(H(E_j\mid E_S,Y)\), and derives the conditional error-information term.
3. **Correlation decomposition (3 points):** Uses the mutual-information chain rule in both orders to prove \(I(E_j;E_S\mid Y)=I(E_j;E_S)+\Lambda_j(S)\) with the correct label-dependence correction and completes the general identity.
4. **Label-invariant simplification (2 points):** Correctly shows joint independence of the error vector from `Y` makes both correction mutual informations vanish and states the simplified criterion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat an incorrect sign or missing correction term in the decomposition as a theorem-critical error.
