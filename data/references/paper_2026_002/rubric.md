# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Uses initial integrability and the pathwise identity to justify that \(G(X_t)\) is integrable for every time, then uses the derivative's integrability condition to exchange expectation and time integration, proving that \(R\) is absolutely continuous with \(R'(t)=\mathbb E[\nabla G(X_t)^\top\dot X_t]\) almost everywhere. A concise integrable-domination justification suffices; no second moment of the performance values is needed.
- **2 points:** Correctly applies Jensen's inequality and the compatibility assumption to obtain \(|R'(t)|^2\le \gamma^2\mathbb E\|J(X_t)\dot X_t\|^2\), including the needed integrability justification.
- **2 points:** Establishes the hypotheses of the mean-zero Wirtinger-Poincare inequality and applies it with the correct normalization for a uniform time variable, deriving the factor \(\gamma^2T/\pi^2\) in the general volatility bound.
- **3 points:** Substitutes the subspace-residual velocity decomposition, controls the squared sum, applies \(\|J(X_t)Sb_t\|\le\|J(X_t)S\|_F\|b_t\|\), and derives the structured bound with the correct factor of two. Nonnegative integration is valid even when a structured energy is infinite.

# Evaluator Notes

Accept any complete valid alternative proof. Merely naming Fubini, Jensen, or a Poincare inequality without verifying and using the relevant hypotheses does not earn the corresponding full credit. A failure to establish the derivative formula leaves later bounds unsupported unless the solver supplies another valid derivation. An error in the general-bound derivation need not erase credit for an independently correct decomposition estimate, and conversely. Minor notation or null-set omissions are readily repairable only when the underlying mathematical argument is correct.

Do not demand square integrability of \(G(X_0)\), any moment of \(X_0\), finite values of both structured energies, independence involving \(U\), or a use of residual orthogonality in the norm estimate. None is needed. An extended-real comparison already handles infinite structured energies without a separate case split. The initial L1 condition is explicitly available; a solver should not be required to infer it from (A)-(C), which alone do not imply it.
