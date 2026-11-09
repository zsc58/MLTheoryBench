# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Constructs equal-coordinate-marginal distributions in every dimension \(d\ge2\), proves that their joint dependence differs (including the copula/MMD conclusion), and correctly scales the construction to make \(\delta(P,Q)\) arbitrarily large.
- **2 points:** Derives the population least-squares slope from the squared-error objective and uses the equal-variance covariance-matrix structure to prove the exact regression identity, including a valid opposite-sign example.
- **2 points:** Establishes the ordered-eigenvalue bound for all \(k\) by correctly relating the symmetric-matrix perturbation norm to \(\delta(P,Q)\).
- **3 points:** Proves the stated sin-principal-angle bound using the reference eigengap with applicable perturbation conditions. A valid route observes that the bound is automatic when \(\delta(P,Q)\geq\gamma/2\), even if \(C_Q\) has a tie at \(r\), and verifies separation in the remaining regime. Accept any valid alternative covering both regimes.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A mere assertion that marginal matching does not control dependence, or a bare citation of a perturbation result without verifying its applicable norm and eigengap conditions, does not establish the corresponding core step. In particular, \(\delta(P,Q)<\gamma\) alone does not imply a positive \(r\)-th eigengap for \(C_Q\); do not require or credit that inference. A correctly stated standard perturbation result that applies without a \(C_Q\) eigengap is acceptable when its hypotheses are checked.
