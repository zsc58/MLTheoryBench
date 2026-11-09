# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly applies Itô's formula to \(\phi(X_t)\), uses both Gram equations, and derives the integrated moment equation or \(d\mathbb E[\phi(X_t)]/dt=m'_t\), hence exact moment tracking from the initial match. Taking expectations is justified by the stated integrability assumptions.
- **3 points:** Derives the correct Fokker--Planck equation and entropy derivative, including the integration-by-parts identity \(\mathbb E[\nabla\phi\,\nabla\log p_t]=-\mathbb E[\Delta\phi]\).
- **3 points:** Substitutes the Gram relation and completes the square to obtain the exact nonnegative-residual entropy identity, or supplies an equally valid derivation of the entropy inequality. The central estimate must be derived, not merely asserted by naming a method.
- **2 points:** Integrates the identity or inequality over time to establish the stated computable entropy lower bound with the correct initial and terminal entropies and parameter dependence.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Differential identities may hold almost everywhere in time; integrated identities and the conclusions must hold with the stated endpoints. The public analytic hypotheses may be used without proving additional regularity or existence results. Do not require the exact residual identity from a solver who proves the requested lower bound by another complete argument.
