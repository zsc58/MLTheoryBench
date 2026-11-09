# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the Gaussian prediction and rank-one covariance update, including preservation of the common covariance factor across output columns. Accounts for the Gaussian initial belief and independent innovations; may use the standard Gaussian-conditioning formula with its hypotheses verified. Posterior columns share a covariance but need not have identical means.
- **3 points:** Proves the exact cross-key uncertainty increment formula, its covariance-normalized form, and the positive-semidefinite contraction bounds.
- **3 points:** Analyzes the eventual repeated-key Riccati iteration, proves convergence to the unique positive root, and obtains the limiting increment (1-rho^2) ell^2 for arbitrary finite preceding write history. Does not silently assume exact diagonalization at the start of the repeated-key phase. Handles rho=+1 and rho=-1 for the variance and gain claims.
- **2 points:** Derives the steady-state scalar gain and both parameter limits. Proves the warped-probe angular limit under eventual repeated writes when |rho|<1, and proves the displayed finite-time angle identity under repeated k_A writes from initialization.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The eventual repeated-key claims and the exact finite-time angular identity have different history assumptions. A general preceding history can leave nonzero cross-covariances. An argument that uses the displayed diagonal angle formula throughout such a history is not a complete proof of the eventual angular limit. A valid proof can instead show that the cross-covariances decay and that the orthogonal covariance has the requisite linear leading growth; equivalent arguments are acceptable.

The angle target is restricted to |rho|<1. No residual-direction angle limit is required for collinear keys. The case rho=0 is included. The initial case p_0=0 is allowed and does not invalidate Gaussian conditioning, since ell and r are positive.

The gain target requires g_*~ell/r as ell/r tends to zero and g_* tends to 1 as ell/r tends to infinity. No finer large-noise expansion, memory-horizon formula, boost-boundary gain, mean-readout limit, or retrieval plateau is required.
