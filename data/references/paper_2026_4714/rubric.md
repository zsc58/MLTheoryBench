# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly marginalizes the conditional Gaussian model and derives the hidden-state mean \(A m_t\) and covariance \(C_t=\sigma_r^2\Delta t I_k+A S_tA^\top\), including justification that the covariance is invertible.
- **3 points:** Correctly derives the multivariate Gaussian score \(\nabla_h\log p_t(h)=-C_t^{-1}(h-A m_t)\) rather than merely naming a Gaussian identity.
- **2 points:** Introduces the leakage matrix \(\Lambda_t=\sigma_r^2\Delta t\,C_t^{-1}\) and obtains the required rescaled score equation exactly.
- **2 points:** Correctly concludes linear dependence on the centered hidden state and explains the time-varying leakage representation (including dependence on time-varying process statistics and/or step size).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
