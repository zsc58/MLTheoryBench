# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Derive \(\mu=\nabla\psi(\eta)\) and \(\operatorname{Cov}(y)=\nabla^2\psi(\eta)/n\) under the stated interior exponential-family conditions, with the normalization in \(n\) correct.
2. **2 points:** Use the mean/canonical Jacobian inverse and the restricted score to obtain Fisher information \(n(V^{-1})_{EE}\), and justify the displayed MLE asymptotic normality. A correctly stated standard result applicable to this restricted exponential-family model may be used with its hypotheses checked. Alternatively, derive sufficient-statistic normality and a valid likelihood expansion. Do not silently assume consistency or finite-sample existence for every outcome. The reference proof verifies asymptotic existence, consistency, and normality by likelihood localization and the implicit-function theorem, but that particular method is not required.
3. **3 points:** Compute the control-variate covariance for deterministic coefficients, solve the normal equations or complete the square to obtain \(c^*=-D^{-1}B^\top\alpha\), and derive the exact minimized variance \(\alpha^\top(A-BD^{-1}B^\top)\alpha/n\).
4. **3 points:** Establish invertibility of the relevant nonempty blocks and identify \([(V^{-1})_{EE}]^{-1}=A-BD^{-1}B^\top\), using a correctly applied block-inverse identity or an equivalent derivation. Complete the equality for every fixed \(\alpha\), consistently with the empty-block conventions.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not award the central step for merely naming Schur complements or optimal control variates without deriving the corresponding identities. The score should reflect independently established downstream conclusions even if an earlier presentation differs.

The comparison is pointwise at a fixed true parameter. Optimal coefficients may depend on that parameter but are nonrandom in the variance calculation. An argument replacing them with empirical coefficients must justify any new claim and does not by itself establish the exact variance identity requested here.

Asymptotic variance refers to the covariance of the limiting normal distribution after multiplication by \(\sqrt n\). Do not require convergence of the MLE's finite-sample variances, and do not treat weak convergence alone as proof of such moment convergence.

The model specifies joint exponential-family densities with the same log-partition function across sample sizes; an additional independence assumption is not part of the task. The normalizer can itself establish the sufficient-statistic central limit result. A standard asymptotic theorem must actually cover the stated experiment or its applicability must be justified.

The finite-sample exceptional-event convention only makes the estimator defined. It is not an assumption of consistency or asymptotic normality. A valid proof may show that a unique restricted maximizer exists with probability tending to one, after which the convention is asymptotically irrelevant.

Explicit separate discussion of \(\alpha=0\) or empty blocks is unnecessary when the proof already handles them through the stated conventions. Do not demand a proof of the neighboring linear-reparameterization corollary or any fixed-point algorithm result.
