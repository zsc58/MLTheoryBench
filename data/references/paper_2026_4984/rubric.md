# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the conditional distribution of the task score given the observed concepts, obtaining conditional mean phi(alpha)^T chi_k and conditional variance psi_u^T B_temp psi_u+sigma_y^2. Correctly uses the covariance orientation and independent label noise, and recognizes that this residual variance is positive and alpha-independent. An equivalent direct residual construction earns the same credit.
- **2 points:** Establishes Bayes optimality over all measurable binary classifiers using only chi_k by comparing conditional 0-1 risks, or an equivalent valid argument. Shows that the threshold is at zero and permits the displayed choice of label 0 when the conditional mean is zero.
- **3 points:** Derives the exact arctangent accuracy formula. A sign-agreement proof must justify the Gaussian decomposition or equivalent joint law, compute the correct correlation, and apply the identity only when the observed-signal variance is positive. It must also establish accuracy 1/2 when phi(alpha)^T B_kk phi(alpha)=0. Any complete alternative calculation earns the same credit.
- **2 points:** Expands the numerator into the known-known, cross-aligned, and recoverable-unknown terms and identifies the residual denominator as independent of alpha. Correctly interprets the last two numerator terms as the only terms that can vary with alpha, not as terms that must vary for every parameter choice.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award credit for equivalent covariance orientations or notation when dimensions and transposes are handled correctly.

The task already assumes the Gaussian vector and its covariance. A separate Schur-complement or quadratic-form proof of positive definiteness is optional and must not be required for full credit. Likewise, merely restating the assumed model is not a separate proof obligation.

Correctly stated standard Gaussian conditioning, Gaussian independence, and Gaussian sign-agreement results may be used without reproving them, provided their relevant hypotheses are satisfied and their application is justified. Do not require an integration proof of the sign-agreement identity itself. An alternative derivation of the requested accuracy formula need not use that identity.

Treat an incorrect residual variance or the absence of a valid derivation of the central accuracy formula as a theorem-critical gap. Distinguish these from an isolated, readily repairable omission of the zero-signal case in an otherwise complete proof, which belongs in the 8-9 range. A proof that handles the zero-signal case separately must not be penalized for restricting correlation and ordinary sign-agreement calculations to positive observed-signal variance.
