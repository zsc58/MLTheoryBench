# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Identification and canonical gradient (3 points).** Establishes the observed-data interpretation of the target, represents its path derivative by the centered augmented feature, and verifies that this feature is the canonical gradient in the specified nonparametric model. Mean-zero square integrability and tangent-space membership must be addressed, explicitly or by a correct standard argument. The arm bias identity and double robustness are useful proof tools, not separate required conclusions; a valid alternative gradient derivation receives full credit.
2. **Cross-fitted fixed-location asymptotics (2 points).** Controls the nuisance mean bias by the armwise product errors and the centered empirical replacement by vanishing L2 errors, or supplies equivalent valid bounds. Uses foldwise training/validation independence with the fixed fold structure to prove the asymptotic linear representation and covariance consistency. Establishes ridge-inverse convergence as needed for the local statistic. Conditioning simultaneously on all cross-fitted nuisance estimates does not establish validation independence and is not an acceptable substitute for the foldwise argument.
3. **Local experiment and population criterion (3 points).** Verifies the QMD/LAN and joint-CLT hypotheses, transfers the null remainders and covariance convergence by contiguity in the specified n-observation experiment, and uses Le Cam's third lemma or an equivalent valid argument to obtain the shifted Gaussian law. Whitening and Slutsky yield the noncentral chi-square limit. Pathwise differentiation and covariance continuity yield the limit of n Lambda_V along the same path. Covers h=0 and zero drift without illegitimate division. A separate convolution-theorem discussion or an omnibus optimality claim is not required.
4. **Uniform location learning (2 points).** Derives a uniform bounded-Lipschitz empirical mean and covariance rate with sample-size-independent constants; derives nuisance-to-oracle moment transfer from the specified propensity and uniform scalar-regression L2 errors; and controls the ridge quadratic form for positive semidefinite covariances. Proves the asserted uniform criterion rate and the near-optimality inequality by adding and subtracting empirical values and using the optimization-gap upper bound. May use a sharper valid concentration estimate. Does not assume that covariances are nonsingular throughout the learning class.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Theorem-critical omissions in any step warrant loss of that step's substantial credit; merely naming cross-fitting, LAN, concentration, nuisance transfer, or a resolvent identity without deriving the needed bounds or stating and verifying an applicable standard result is insufficient.

Respect the source-grounded repaired contract: armwise exchangeability is sufficient; fixed-location inference does not require a globally Lipschitz kernel; learning uses the explicitly defined nuisance L2 error rather than an assumed population-moment bound. The covariance is normalized by n-1, although correctly accounting for its asymptotic equivalence to normalization by n is acceptable within a proof. The local experiment uses the same cross-fitted statistic on the n observations; no unmentioned alternative experiment for an auxiliary growing training sample may be assumed.

The source covariance argument's joint-conditioning error has a routine foldwise repair. A proof implementing that repair is fully valid. All theorem-critical obligations in the replacement reference proof are closed; there is no private GT quality exception.
