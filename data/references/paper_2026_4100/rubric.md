# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Proves the quadratic optimum is $\eta^2\Lambda$ and supplies an attaining vector satisfying $Au=\Lambda Bu$ and $u^TBu=\eta^2$, including the case $A=0$. Compactness and scaling, whitening, or another complete generalized-Rayleigh argument are acceptable.
- **3 points:** Derives $\sup_{u\in Q_\eta}|w^TJu|=\eta\sqrt{\sigma_w}$, supplies an attaining optimizer and its boundary-directed sign, and handles zero sensitivity. Correctly distinguishes strict sign reversal from actual binary prediction flips: the strict-crossing threshold is $>$, while the label-flip threshold is $>$ for a positive base score and $\ge$ for a negative base score under $\operatorname{sign}(0)=+1$.
- **2 points:** Proves that $T$ is symmetric positive semidefinite, that $\|T\|_{\rm op}=\Lambda$, and that $\sigma_w\le\Lambda$ for every unit $w$, using a justified spectral comparison or an equivalent operator-norm argument. Handles the zero-matrix case. A characterization of equality in $\sigma_w\le\Lambda$ is not an additional required conclusion.
- **2 points:** Derives the target remainder bound $r_{M,w}(t)\le C_Mt^2/(2\beta)$ on the stated chart region and proves both finite-radius implications. Quantifies the proxy-distance error and correctly explains its effect on exact local feasibility and sufficient flip/no-flip tests. This may use inner and outer ellipsoids or another rigorously justified local comparison; the reference proof's particular conservative radii are not mandatory.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the spectral comparison or either nonlinear direction as a theorem-critical gap; merely naming generalized eigenvalues, duality, or Taylor control without derivation earns no credit for that step.

The positive-margin hypothesis excludes a zero base score, but it does not exclude an attained perturbed score of zero. At equality, asserting that neither base sign can undergo a prediction flip is incorrect. Conversely, a solver must not be penalized for identifying the negative-to-zero label flip required by the explicit prediction convention.

The proxy comparison must respect its controlled domain. An unqualified assertion that one can add an $O(\eta^2)$ term, without explaining feasibility or controlling the points to which it is applied, does not complete that obligation. Do not require global injectivity of the proxy map or a guarantee outside $P_{\eta,\rho}$. No construction of a discrete paraphrase in $X$ is requested.
