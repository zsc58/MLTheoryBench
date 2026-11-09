# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the componentwise Student-t log-likelihood location score z_i=(nu+1)(y_i-f_i)/(nu s^2+(y_i-f_i)^2) and proves the uniform bound |z_i| <= (nu+1)/(2s sqrt(nu)), hence the sqrt(m) vector bound.
- **3 points:** Establishes centering and the Student-t score covariance kappa I with kappa=(nu+1)/((nu+3)s^2), and correctly factors the Fisher covariance as J^T(kappa I)J using that J is deterministic at fixed x,w. An explicit moment calculation, or an applicable precisely stated standard identity with its hypotheses checked, suffices. The reference calculation uses two integrations by parts and works for every nu>0; finite variance of Y is not required.
- **3 points:** Establishes the regularized operator bound max_sigma sigma/(kappa sigma^2+tau) <= 1/(2sqrt(kappa tau)), by SVD or an equivalent valid argument. The argument must be valid without a full-rank assumption; tau>0 ensures invertibility, and zero singular values cause no problem. Merely naming natural-gradient or SVD without the controlling inequality is insufficient.
- **2 points:** Combines the bounds and simplifies to the exact uniform conclusion (1/4)sqrt(((nu+1)(nu+3)m)/(tau nu)) for all x,w,y.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions and allocate credit for equivalent mathematical achievements. Do not require the reference proof's incidental presentation choices or its exact proof route. In a proof following that route, unsupported score covariance, deterministic-Jacobian factorization, or operator control is a theorem-critical gap; an alternative derivation that genuinely bypasses a step is not an omission.

The score is the positive log-likelihood location derivative for residual y-f. A consistent overall sign slip does not change the covariance or norm estimates and should be treated as a readily repairable local error, not as failure of the norm argument. Do not accept replacing the exact model Fisher covariance by an empirical or approximate Fisher matrix without a separate valid justification.
