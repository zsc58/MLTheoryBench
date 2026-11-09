# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly expand the signed-measure MMD objective with the repaired (lambda/2)||a||^2 penalty, establish invertibility of G_lambda, solve a_lambda=G_lambda^{-1}m_0, and form the reduced objective. Gaussian Gram positivity may be invoked as a standard fact; distinct particles are not required.
2. **4 points:** Justify differentiating the kernel mean integral and the reduced objective, and derive the full particle-coordinate gradient for the squared-exponential kernel. Account for both embedding and Gram derivatives and use G_lambda a_lambda=m_0 to obtain grad_Z E^{red}=sigma^{-2}D_lambda(G_lambda D_lambda Z-m_1). Differentiate K with the weights held fixed only after justifying cancellation of the optimizing-weight derivatives, or use a valid equivalent envelope argument. The identity must hold even at zero weights. No unweighted first-moment assumption is available or necessary: Gaussian localization ensures finiteness of m_1, and the Gaussian derivative is bounded.
3. **2 points:** Show that P_lambda=sigma^{-2}D_lambda G_lambda D_lambda is positive definite on the nonzero-weight domain and that the gradient factors through P_lambda there. Deduce the stated preconditioned update, equivalently (1-eta)Z+eta Phi, for every eta>0.
4. **2 points:** For mu_C=C mu with C>0 and fixed kernel and lambda, prove the scaling of m_0,m_1,a_lambda,D_lambda and the exact cancellation yielding Phi_{mu_C,lambda}=Phi_{mu,lambda}. Verify that positive scaling preserves the nonzero-weight domain.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular proof of Gaussian Gram positivity. The factor-of-two penalty normalization and the nonzero-weight domain are theorem-critical. The weights are unconstrained real numbers; neither positivity nor unit-sum normalization may be assumed. Repeated particles are allowed. The zero target satisfies the gradient identity and has an empty map domain; a proof covering this automatically need not discuss it separately. The update identity does not require proving objective decrease for arbitrary positive step sizes, convergence, or preservation of the map domain at future iterates. A merely notational fixed-weight derivative shorthand is acceptable if its meaning is clear and the preceding reduced-value differentiation is valid.
