# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Entropy dissipation, coercivity, and entropy rate (3 points).** Establishes entropy dissipation for the stated solution class, including nonnegative densities; proves comparison of dissipation with the negative Sobolev discrepancy with correct zero-mode handling; derives the entropy-power lower bound by interpolation; and integrates it on a controlled-regularity interval with the stated constant dependencies.
2. **High-order energy estimate (2 points).** Derives a valid high-order differential inequality, including the dissipative linear term, the lower-order linear remainder, and the nonlinear transport estimates. Correctly verifies the multiplier and commutator hypotheses. Any interpolation estimate essential to the nonlinear term must be stated with appropriate exponents and justified, rather than replaced by a citation to an unspecified specialized method.
3. **Bootstrap and global continuation (3 points).** Proves the entropy-powered bound on the integrated Lipschitz coefficient with a strictly positive exponent for the entire stated parameter range. Controls the additive dissipation remainder after absorption, closes a strict bootstrap with constants depending only on the allowed data, and justifies continuation from a uniform Sobolev bound. Separates the stationary case before divisions by entropy or the discrepancy norm.
4. **Sobolev decay conclusion (2 points).** Uses the uniform density upper bound, the lower entropy comparison, and interpolation to obtain every claimed Sobolev rate, including the initial-discrepancy factor and both endpoints beta=0 and beta=gamma.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular interpolation exponent, or its numerical bootstrap threshold.

The source and corrected reference estimate lead to X'<=C L X+C I, not merely X'<=C L X. Discarding the additive term or declaring it part of C L X without a valid estimate is an important gap. It can be controlled by entropy dissipation and H(0)<=c X(0), using a sufficiently large fixed multiple of X(0) as the bootstrap threshold. A different valid treatment earns full credit.

Small absolute initial entropy does not by itself imply H(0)/X(0) is small. Do not require or reward a bootstrap closure that makes this unsupported inference. A first-exit argument must obtain a strict improvement.

A positive lower bound on the evolving density is not an assumption of the problem. A proof that needs such a bound must derive it or explain a valid approximation argument that removes it. Multiplication by a nonconstant function does not preserve zero mean; homogeneous-norm arguments must account for the resulting constant mode.

Local existence is assumed, but the implication from the uniform norm bound to extension beyond a finite maximal time must be justified by an applicable continuation result or a local lifespan argument. The paper-specific well-posedness citation alone is not a completed derivation in the reference proof.

Treat omission of the bootstrap closure, the explicit entropy rate, or the requested Sobolev conclusion as theorem-critical. Restoring the initial-discrepancy factor only requires the uniform estimate X(t)<=C X(0); the reference proof supplies this estimate. No unresolved reference-proof obligation is being assigned credit by citation alone.
