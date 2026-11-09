# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Establishes the smoothness-based directional preconditioned descent inequality under the prescribed step choice, including the zero-gradient case. Correctly uses positive diagonal metrics; their preservation follows directly from the metric recursion.
2. **3 points:** Derives a valid Lyapunov one-step decomposition starting from the previous auxiliary point \(z_k^+\), and proves the objective/momentum bound with remainder \(\alpha_k^2\|\nabla f(x_{k+1})\|_{P_k^{-1}}^2/2\). In the reference route, the identity \(x_{k+1}-x_k^+=\alpha_k(y_k-x_{k+1})\), convexity, and cancellation of the squared momentum increment justify this bound.
3. **3 points:** Controls the adaptive metric forcing using \(\|y_{k+1}-x^*\|_\infty\le R\), and obtains the residual coefficient \(\alpha_k^2+\alpha_k\gamma_kR^2-\eta_{k+1}(1+\alpha_k)\). Accounts for both descent contributions: the auxiliary next step and the additional contribution when replacing the uncorrected next energy in its negative multiple. Uses \(\gamma_kR^2=\alpha_k\) and the consistency inequality to prove that the residual quadratic is nonpositive.
4. **2 points:** Concludes \((1+\alpha_k)E_{k+1}\le E_k\) and correctly iterates from \(0\) through \(k\) to obtain the stated product bound and initial auxiliary energy.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its decomposition labels, or the introduction of the matrix \(M_{k+1}\). A proof valid for every step below the directional threshold also covers the prescribed equality choice. Treat omission of the adaptive-forcing cancellation or the parameter-consistency argument as a theorem-critical gap. Merely asserting the final residual without accounting for the additional \(-\alpha_k\eta_{k+1}/2\) contribution is likewise a gap unless an alternative valid argument supplies it. Expanding from \(z_k\) rather than \(z_k^+\) requires explicitly accounting for their difference. An omitted one-line positivity verification is readily repairable when all subsequent weighted calculations are valid; treating a negative-semidefinite quadratic form as an actual norm is unnecessary and should be avoided.
