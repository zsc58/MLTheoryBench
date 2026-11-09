# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the Gaussian posterior and the matrix identities needed for the proof. Accounts correctly for the evidence normalization and, when used, the determinant and quadratic augmentation identities. Equivalent direct derivations receive full credit; unnecessary identities need not be reproduced.
- **3 points:** Derives both EM second moments and minimizes the correctly signed expected negative complete-data log likelihood. Obtains the feature-precision update and residual-plus-posterior-variance noise update. Justifies positive feature denominators and handles zero noise second moments by the stated boundary convention.
- **3 points:** Differentiates the evidence correctly and derives both stationarity equations. Obtains MacKay's quotient on its nonzero-mean domain and explicitly distinguishes fixed-point equivalence from equality of finite-iterate maps, through algebra or a valid example. Does not assert quotient-based equivalence at undefined 0/0 coordinates.
- **2 points:** Constructs and verifies the specified tight Fenchel majorization jointly in feature precisions and inverse noise variances. Derives the old-scale ridge minimizer and the subsequent separable scale minimizers with the old tangent held fixed, proving equality with the EM maps. An equivalent fully justified MM construction receives full credit.

# Evaluator Notes

Accept any mathematically valid alternative proof. Do not require the reference notation or ordering. Do not award credit for merely naming EM, MacKay, or IRLS.

The decisive MM obligation is not closed by asserting the desired scale terms or by deriving a stationarity equation alone. The proof must justify an upper bound that is tight at the current parameters and must retain its dependence on the noise scales. A feature-only conjugate cannot be treated as independent of the noise variances without justification. Likewise, an affine bound on the data-covariance log determinant is not automatically the particular posterior-precision MM procedure defined in the task.

A proof claiming that MacKay's quotient equals the EM update at arbitrary nonstationary iterates has a substantive error. At a zero posterior mean the quotient is outside its stated domain; zero feature columns remain allowed and must not be excluded by an added assumption.

For a zero noise second moment there is no minimizer over strictly positive variances: the coordinate objective tends to minus infinity as the variance decreases to zero. Accept the stated limiting-update interpretation, but not substitution of a singular B into formulas requiring B^{-1}. No proof of convergence, global optimality of the evidence, robustness, or cited specialized SBL optimization properties is required.
