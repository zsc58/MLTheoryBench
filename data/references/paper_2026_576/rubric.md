# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Solves the reverse linear ODE and obtains \(X_1=e^{TL}X_0e^{TL}\), with the stated initial condition and time interval.
- **2 points:** Uses the decomposition \(X_0=\Pi+X_\perp\), proves the constant part is fixed, and establishes Frobenius orthogonality (or an equivalent norm inequality) for the propagated orthogonal part.
- **4 points:** Performs the Laplacian eigendecomposition, uses the zero row and column sums to remove all zero-eigenvalue modes, and derives the squared Frobenius expansion and spectral-gap lower bound \(\|e^{TL}X_\perp e^{TL}\|_F^2\ge e^{4T\lambda_2}\|X_\perp\|_F^2\).
- **2 points:** Combines the orthogonality inequality and square-root step to conclude \(\|X_1\|_F\ge e^{2T\lambda_2}\|X_\perp\|_F\) for all stated parameters.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The spectral-mode elimination and exponential amplification argument are theorem-critical; merely naming spectral decomposition or instability without deriving the bound earns no credit for that step.
