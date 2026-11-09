# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Exact average, noise, and drift control.** Derives the exact identity $\bar x^{r+1}=\bar x^r-\eta G_r$ from the corrected merge and establishes the worker-averaged variance bound and the $\Phi_H,S_T,S_O$ local-drift bounds. Obtains the needed conditional bounds from the global oracle assumptions and fresh-sample independence, or supplies sufficient unconditional bounds in a consistently unconditional proof. Merely asserting that averaging or concentration applies is insufficient.
- **3 points: Sparse delayed disagreement contraction.** Starting from the actual merge, computes the shared-mask expectation and obtains $\mathbb E[X_{r+1}\mid x^r]\le\rho X_r+\eta^2G^2(C_TS_T+C_OS_O)$, or a sufficient unconditional or stronger version, with the stated constants. Uses mask independence jointly with the starting and local-trajectory states when conditioning. Correctly solves and sums the recursion under common initialization and $\rho<1$. This is the characteristic central bottleneck.
- **3 points: One-round descent.** Uses smoothness, conditional unbiasedness, local drift, and different-time noise orthogonality to derive the one-round inequality with the correct dependence on $X_r$, $\Phi_H$, $\sigma^2$, $H_{\max}$, and $\bar H$. Justifies the heterogeneous gradient-sum bound and preserves the leading $1/n$ variance reduction. A theorem name or an unsupported appeal to standard SGD analysis does not earn this step.
- **2 points: Telescoping and final constants.** Uses the stepsize condition to obtain the factors $\bar H/4$ and $3/2$, telescopes the objective, applies lower boundedness and accumulated disagreement, and recovers all four terms of the stated rate with their constants.

# Evaluator Notes

Accept a complete valid alternative proof, including tighter intermediate bounds that imply the displayed conclusion. Do not require the reference proof's incidental presentation choices or auxiliary notation. Award later-step credit when its required conclusion is independently proved, even if an earlier attempted derivation was flawed.

A conditional inequality does not follow merely from its unconditional counterpart. A proof using round-conditioned estimates must justify their conditioning; a consistently unconditional proof is equally acceptable. In a mask calculation, conditioning jointly on the starting and local-trajectory states supplies a legitimate nested tower argument. An isolated omitted conditioning symbol is a readily repairable notation error only when the intended conditioning and its justification are otherwise clear.

Different-time noise terms are orthogonal by the martingale-difference property. This does not justify discarding cross terms between the full gradient sum and the full noise sum, because later gradients can depend on earlier noise; a valid upper bound or another justified argument is required.

Missing control of worker disagreement, or treating it as an assumption, is theorem-critical. Likewise, a descent argument that loses the leading $1/n$ variance reduction does not establish the stated result. The argument must cover the admitted boundary cases, including full communication and zero overlap, but separate case splits are unnecessary when all formulas remain valid. Do not require assumptions beyond the public task.
