# Reference Proof

## Proof Structure

1. Marginalize the Gaussian conditional law to compute the hidden-state mean and covariance.
2. Differentiate the resulting Gaussian density to obtain its score.
3. Rescale the score and identify the leakage matrix, including its time dependence and architectural interpretation.

## Complete Proof

Write q_t=\sigma_r^2\Delta t>0. The conditional law means that, in distribution, h_t=A x_t+\varepsilon_t, where \varepsilon_t\sim\mathcal N(0,q_t I_k) is independent of x_t. Since x_t\sim\mathcal N(m_t,S_t), the affine Gaussian sum h_t is Gaussian with
\[
\mathbb E[h_t]=A m_t,\qquad C_t:=\operatorname{Cov}(h_t)=q_t I_k+A S_t A^\top.
\]
Because q_t>0, C_t is positive definite even when S_t is singular, so p_t, the density of h_t, exists and is
\[
p_t(h)=(2\pi)^{-k/2}(\det C_t)^{-1/2}\exp\!\left[-\tfrac12(h-A m_t)^\top C_t^{-1}(h-A m_t)\right].
\]
Taking the gradient with respect to h gives
\[
\nabla_h\log p_t(h)=-C_t^{-1}(h-A m_t).
\]
Define
\[
\Lambda_t:=q_t C_t^{-1}=\sigma_r^2\Delta t\,(\sigma_r^2\Delta t I_k+A S_t A^\top)^{-1}.
\]
Multiplication by q_t yields
\[
\sigma_r^2\Delta t\,\nabla_h\log p_t(h)=-\Lambda_t(h-A m_t).
\]
Thus the optimal activity score is linear in the centered hidden state. Its coefficient matrix (and, when the process statistics or step size vary with t, the centering and covariance parameters) is time-dependent, so a linear leakage mechanism with time-varying coefficients represents the score exactly.
