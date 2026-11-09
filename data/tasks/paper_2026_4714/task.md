# Problem

## Setup

Let \(\{x_t\}\) be a jointly Gaussian target-state process, with marginal mean \(m_t\in\mathbb R^d\) and covariance \(S_t\succeq0\) at time \(t\). Let the hidden activity be \(h_t\in\mathbb R^k\). Fix a matrix \(A\in\mathbb R^{k\times d}\), a step size \(\Delta t>0\), and noise variance \(\sigma_r^2>0\). Assume the conditional hidden-state law
\[
h_t\mid x_t\sim\mathcal N(Ax_t,\,\sigma_r^2\Delta t\,I_k).
\]
Let \(p_t\) denote the marginal density of \(h_t\).

## Task

Prove that \(h_t\) is Gaussian with mean \(A m_t\) and covariance
\[
C_t=\sigma_r^2\Delta t\,I_k+A S_tA^\top,
\]
and that its score satisfies
\[
\sigma_r^2\Delta t\,\nabla_h\log p_t(h)
=-\Lambda_t\bigl(h-A m_t\bigr),
\qquad
\Lambda_t:=\sigma_r^2\Delta t\,C_t^{-1}.
\]
Conclude that the optimal activity score is linear in the centered hidden state, with leakage coefficients that may vary with time through the process statistics and step size; hence a linear leakage mechanism with time-varying coefficients exactly represents this score.
