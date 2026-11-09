# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Affine sensitivity and operational score (2 points).** Derives the exact perturbation $L(\pi;(z_0+e,\tau_0,m_0),\lambda_0)-L(\pi;u_0,\lambda_0)=\langle w_\pi,e\rangle$ and its maximum absolute value over the catalog. The argument applies pointwise at each nominal pair and does not require common sensitivities across calibration and test blocks.

2. **Signed-hull support and minimality (4 points).** Proves $\sigma_W=\Phi$, verifies that $\Phi$ is a finite lower-semicontinuous sublinear valid certificate, and proves that every certificate protecting the actual affine Lagrangian perturbations dominates it. Establishes both directions of the equality characterization $B=\Phi$ everywhere if and only if $K_B=W$. A correctly stated polar representation or an equivalent valid argument is acceptable; its relevant hypotheses must be satisfied. Direct dominance after the affine identity is sufficient for that portion of minimality, but does not by itself establish the polar equality characterization.

3. **Conformal calibration (2 points).** Uses the stated conditional exchangeability of the block-specific scores to obtain coverage at least $1-\alpha$. Correctly treats ties, either through an appropriate standard exchangeability rank theorem or an explicit conservative rank argument, and treats $r=n+1$ using the prescribed infinite radius. Does not substitute an iid assumption or infer exchangeability after unjustified additional conditioning on realized block-specific nominal outputs.

4. **Robust selector guarantee (2 points).** Uses the assumed simultaneous component event to prove feasibility of every policy output and the regret bound relative to the realized-value maximizer over the same robust-feasible catalog. Approximate robust optimization must be compared with that policy, or with an arbitrary robust-feasible policy; redefining the comparator as a robust-objective maximizer alone does not prove the requested statement. Handles the absence of an output when the robust-feasible catalog is empty and avoids undefined infinity arithmetic. When the value-radius supremum is infinite, the regret bound is automatic because realized values are finite.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the polar equality characterization or the realized-value regret comparison as a theorem-critical gap.

The component score formulas and calibration level are definitions. Their simultaneous coverage event is an explicit assumption, so do not require a derivation of that event, a Bonferroni allocation, independence between uncertainty layers, or quantile-concentration estimates. The combined Lagrangian coverage statement does not by itself supply separate value and constraint coverage.

Do not require nonzero sensitivities, a full-dimensional signed hull, uniqueness of either optimizer, or a nonempty constraint index set. Value coverage remains required when there are no constraints. No realized-value comparator needs to be available to the selector before deployment.

The probability statement is a common-event guarantee. It is not conditional on nonempty robust feasibility or on issuance of a policy output. Merely conditioning on such an event need not preserve the stated probability.
