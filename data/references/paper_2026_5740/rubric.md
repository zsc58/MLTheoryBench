# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Variance derivative and common-space representation (2 points).** Correctly differentiates the centered variance, justifies the centering cancellation or an equivalent calculation, and uses the common sensitive-attribute marginal to interpret the outer derivative in H.
2. **Hessian and explicit adjoint (3 points).** Derives the inner functional derivatives, identifies the Hessian as 2I or establishes an equivalent operator identity, and proves the almost-everywhere adjoint formula with the correct sign and factor.
3. **Direct and mixed parameter derivatives (3 points).** Computes the direct prediction-error derivative and the mixed inner derivative with the correct factors, signs, probability laws, and parameter gradient. Award equivalent credit for a direct calculation of the implicit fairness derivative that supplies the same mathematical justification without introducing a mixed-derivative symbol.
4. **Total-gradient assembly (2 points).** Derives and applies the necessary task-specific adjoint identity from differentiated stationarity, or gives another valid complete differentiation argument, and obtains the full exact total-gradient formula under the explicit public hypotheses.

# Evaluator Notes

Accept a complete valid alternative proof, including direct differentiation through the conditional-mean solution when the necessary differentiation is justified. Do not require the reference proof's intermediate notation or presentation. Missing justification of a centering calculation, common-space identification, Hessian action, or adjoint sign is a gap when the proposed proof relies on that fact without an equivalent argument; omission of a particular reference-proof calculation is not by itself a gap.

The public assumptions specify first-parameter-derivative interchange for the inner squared loss at every fixed h and for the outer prediction-error loss. They also specify H-valued differentiability of the inner minimizer. A proof may obtain the mixed derivative by a quadratic-loss difference identity or an equivalent argument. Do not demand stronger analytic hypotheses such as domination, continuous derivatives, or L2 differentiability of the entire predictor map.

Naming the specialized functional implicit-differentiation or adjoint method without deriving the identity needed here does not close that proof obligation. The reference proof closes it directly by differentiating inner stationarity, testing against the adjoint, and applying the outer chain rule. An equally justified alternative earns full credit.

The inner minimizer is supplied in the setup; a separate existence proof is not required for full credit. Both the adjoint formula and the total-gradient formula must be proved. The argument must cover alpha = 0 and degenerate A-laws, but separate case discussions are unnecessary when the derivation already covers them. Do not require finite-sample, estimator, or algorithmic claims, which are outside this population task.
