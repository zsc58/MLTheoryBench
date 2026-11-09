# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (2 points):** Rewrites the density equation with the actual solution's linear velocity \(u_t(x)=C_tx\), where \(C_t=(\int\nabla\Phi_t(y)y^\top\rho_t(y)\,dy)A\), with correct matrix orientation and sufficient justification that its coefficients are well-defined and continuous.
- **Step 2 (3 points):** Obtains the linear characteristic pushforward, justifies invertibility of its matrix, proves preservation of the elliptically contoured density with the same generator, preserves positive definiteness of the scatter matrix, and derives the mean and scatter ODEs.
- **Step 3 (3 points):** Establishes that the given potential is purely quadratic, not merely that a quadratic ansatz is consistent. A characteristic argument for the actual solution's linear transport equation, with uniqueness justified for the stipulated damping and initial trace, is sufficient. Derives the symmetric equation \(\dot P_t=-\alpha_tP_t-(C_t^\top P_t+P_tC_t)+V\) and \(P_0=0\). If a polynomial ansatz with linear and constant terms is used, explains both why the actual solution lies in that class and why those lower-order terms vanish.
- **Step 4 (2 points):** Establishes the elliptic moment identity \(\int yy^\top\rho_t(y)\,dy=\kappa_g\Sigma_t+m_tm_t^\top\), including the correct generator normalization, and obtains \(C_t=P_t(\kappa_g\Sigma_t+m_tm_t^\top)A\), closing the complete system and final claim.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its finite-point construction of a quadratic coefficient matrix, or the introduction of unnecessary lower-order coefficients.

An unproved quadratic ansatz establishes at most consistency of an invariant subclass. Award correct coefficient-algebra credit where earned, but do not award quadratic-preservation credit unless the proof identifies the given solution with that subclass. No unproved uniqueness assertion for the full coupled nonlinear PDE can substitute for this obligation.

Damping is nonnegative and is specified at positive times. It need not have a finite value at zero or an integrable singularity there. A proof using integrating factors must justify the initial-time limit; scalar dissipative uniqueness also suffices. Do not require a differential equation at time zero.

The parameter \(\Sigma_t\) is the scatter matrix; the covariance is \(\kappa_g\Sigma_t\). The matrix ODEs must retain their order of multiplication. No commutation assumption on A, V, P, or \(\Sigma\) is available.

The result is conditional on the supplied solution and does not require a global-existence theorem for the PDE or the closed ODE. The case T=0 is the initial statement. Centered laws, V=0, and zero damping remain within scope.

A named method without an applicable statement, verified hypotheses, or a supporting derivation does not close a theorem-critical step. Gaps in the characteristic pushforward, positive definiteness, preservation of quadratic potentials, coefficient comparison, or moment closure must be assessed accordingly. The formal Hamiltonian derivation of the already-given PDE and a claim of genuine metric invertibility are not additional tasks.
