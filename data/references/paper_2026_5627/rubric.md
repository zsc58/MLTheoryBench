# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the covariance recursion from the Gaussian minibatch model, retains a valid positive trace-noise contribution, and rigorously uses its eigenvalue condition to establish \(\gamma\le2m/\operatorname{tr}(G)\) under strict contraction. A secular-equation approach must justify the relevant resolvent domain, continuity, and construction of an eigenmatrix from a scalar root; it must not treat a constant-factor covariance bound as an equality.
- **2 points:** Correctly compares the stochastic covariance spectral radius with the deterministic two-step dynamics on symmetric matrices and obtains the necessary deterministic stability restriction \(\gamma<2(1+\mu)/((1-\mu)\lambda_1)\).
- **3 points:** Establishes \(1-\rho(\mathcal T)\le\min\{4\gamma\lambda_d,1-\mu\}\), including the relevant real, nonreal, repeated-root, and zero-momentum cases, or an equally rigorous alternative. Distinguishes the radius of the smallest-eigenvalue coordinate block from the global deterministic spectral radius.
- **2 points:** Combines the restrictions uniformly to obtain the stated constant-8 bound, includes parameter choices with \(\rho(\mathcal T)\ge1\), takes the infimum without requiring attainment, and correctly identifies the crossover of the two terms.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

A positive trace-only comparison map is sufficient; a solver need not derive a secular equation for the entire exact stochastic operator or prove that its leading eigenmode is observable. Positive-map spectral monotonicity must be justified or invoked in an applicable standard form.

If the smallest-eigenvalue block has nonreal roots, its squared radius equals \(\mu\), but the global deterministic squared radius need only be at least \(\mu\). Do not require or endorse equality for the global radius.

Do not require an optimizing crossing in \(\mu\in[0,1)\): such a crossing need not exist. A uniform bound such as \(\min\{x,y\}\le\sqrt{xy}\) closes the parameter elimination, including well-conditioned spectra.

The target is immediate when \(\rho(\mathcal T)\ge1\). A solver need not evaluate a resolvent at a stability boundary or prove the reference proof's additional weak-stability extension of the supporting cap.

The displayed critical size is the positive real crossover of two expressions. Do not require it to be an integer, and do not require an achievability, risk-convergence, or runtime-optimality result that is absent from the public task.
