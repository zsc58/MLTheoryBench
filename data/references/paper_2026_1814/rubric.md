# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly differentiates both preconditioners with T held fixed, obtaining d(K^{-1})=-K^{-1}(dK)K^{-1} and d(2T-TKT)=-T(dK)T.
- **3 points:** Establishes equality of preconditioner values and differentials at the numerical choice T=K^{-1}, and propagates it through predictive means, variances, and expected log-likelihoods. The likelihood comparison must accommodate direct dependence on eta; recognizing that this dependence is identical on both sides suffices.
- **3 points:** Compares all penalty terms, including both occurrences of P in m^T P K_{uu} P m, the trace term, the shared -log|S| term, and the log-determinant versus fixed-T trace differential. Concludes equality for every ordinary-parameter gradient, with S differentiated in its diagonal coordinates.
- **2 points:** Gives a valid noncancellation argument or an admissible example showing that the explicitly defined naive objective fails to match a full objective gradient. Observing only that dT=0 whereas d(K^{-1}) generally differs is useful but is not by itself a complete proof of objective-gradient failure.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation, its particular counterexample, or its domain-check identities.

T is assigned the inverse value at the comparison point and then held fixed during differentiation. Differentiating through that assignment changes the comparison and is incorrect.

The expected log-likelihood is a function of (mu_n,sigma_n^2,eta). A proof may invoke the public differentiability condition directly and need not justify differentiation under an integral. Do not require a Gaussian likelihood for the equality claim. A Gaussian likelihood is an admissible choice for a counterexample to the naive claim.

The inverse-based penalty has no -M term. Its omission or addition as a constant does not affect a gradient calculation, but a proof must not omit the preconditioners in the quadratic mean terms. Do not give full credit for proving equality only for the old, unpreconditioned quadratic expressions.

The public naive objective substitutes T for every occurrence of P_free. A counterexample solely for a different replacement rule must be connected to the public definition before it closes that obligation. Failure in general means failure for at least one admissible setting; it does not mean failure for every parameter direction or every dataset.

Zero predictive variances are permitted under the stated point-mass and relative-differentiability conventions. No extra strict-variance assumption, source-specific representation, or additional intermediate identity should be imposed on a solver.
