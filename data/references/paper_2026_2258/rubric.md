# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Centered decomposition and rank (2 points).** Correctly form `Y_c=PH+NH`, use projection contraction for the noise, and establish the rank-zero `K=1` case and rank `K-1` (hence zero `K`th singular value) for `K>=2`.
2. **Signal singular-value lower bound (4 points).** Derive the bound `sigma_{K-1}(PH) >= (Delta/kappa) sqrt(beta n/(2K))`, including the Gram-matrix/balance argument and the conversion from pairwise separation to `sigma_K(A)`; merely naming a lemma or method is insufficient.
3. **Noise event and asymptotics (2 points).** Apply Gaussian operator-norm concentration at `tau=sqrt(p)+sqrt(n)+s_n`, verify that the probability of a suitable noise event tends to one from `s_n -> infinity`, and transfer the bound through centering. The bound `Pr(||N|| >= tau) <= exp(-s_n^2/2)` directly supplies the strict event `||N|| < tau`.
4. **Threshold separation and conclusion (2 points).** Use the separation condition and Weyl inequalities to show exactly `K-1` singular values exceed the threshold for `K>=2`, including equality in the separation assumption, and conclude consistency. Correctly handle `K=1` without separation. A strict noise event gives `widehat sigma_{K-1} > tau` and `widehat sigma_K < tau` directly; a valid alternative treatment of threshold ties is also acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Propagate a missing signal lower bound or invalid threshold comparison to the final consistency score when it leaves the main conclusion unsupported.

A non-strict bound `widehat sigma_{K-1} >= tau` alone does not establish that the singular value is counted by the estimator. Continuity of singular values together with absolute continuity of the original data does not, by itself, prove that a specified threshold has probability zero. An otherwise complete proof with only this omitted endpoint justification has a readily repairable local gap, not a substantive failure of the theorem. Accept either a justified no-tie argument or a strict-noise-event argument. Do not require strengthening the public separation assumption to a strict inequality.
