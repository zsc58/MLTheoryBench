# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs the smoothed function, Hermite truncation, and squared polynomial; proves pointwise non-negativity and degree at most twice the truncation degree.
- **4 points:** Derives the central inequality $\|q-\mathbf1_H\|_1\le\|p-g\|_2+\|f-g\|_1$ using the insertion of $(g+1)/2$, the stated algebraic identity, norm contraction/projection bounds, Cauchy--Schwarz, and $f^2=1$.
- **2 points:** Correctly applies the Gaussian smoothing and truncation estimates to obtain $\|q-\mathbf1_H\|_1\le\rho^{t+1}+2\sqrt\pi\Gamma(H)\sqrt{1-\rho}$.
- **2 points:** Chooses $\rho$ and $t$ (including the zero-surface-area case), splits the error into two halves, and obtains the claimed $O(\Gamma_{\mathcal H}^2\varepsilon^{-2}\log(1/\varepsilon))$ degree bound uniformly over the class.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
