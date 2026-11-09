# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly introduce scaled coordinates and the target-centered span, and prove that every pairwise difference among target and reference inputs lies in that span. Transform gradients consistently with the input scaling.
- **4 points:** Derive the radial input-kernel covariance consequences, showing perpendicular gradient components have zero covariance with all relevant function observations and parallel gradient components. Use joint Gaussianity to obtain independence and remove the perpendicular components from the conditional law. The reasoning must remain valid at zero separation and for singular Gaussian vectors.
- **2 points:** Prove that the directional statistic carries exactly the information in the parallel gradient components, by establishing injectivity of the span map and its measurable inverse on its image, or by an equivalent argument. Use dimensionally correct block or Kronecker-product identities and account for at most \(m^2\) scalar coordinates.
- **2 points:** Handle both exact gradients and metric-matched Gaussian gradient noise, and conclude the almost-sure equality of the full-gradient and reduced-statistic conditional distributions under the stated model. Do not extend the asserted guarantee to unsupported general gradient-noise models.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A named method without the covariance and information-equivalence arguments earns no credit for the corresponding steps. Propagate a missing geometric or independence argument to the final equality when it is not independently justified.

The smoothness assumption concerns the input covariance kernel, not twice continuously differentiable sample paths. Do not require a finite \(\kappa_\theta''(0)\): the needed diagonal covariance conclusions follow from the actual twice continuously differentiable radial input kernel. A solver may use standard derivative-GP covariance identities with a valid interpretation at coincident inputs rather than reproduce the difference-quotient construction in the reference proof.

No positive-noise, distinct-coordinate, full-rank, or \(m\leq d\) assumption is present. An inverse-based argument must justify its inverses or otherwise cover singular cases. A proof whose reasoning automatically covers these cases need not list them separately. Likewise, a formulation using conditional densities is acceptable when its almost-sure conditional-law meaning, including permitted degenerate distributions, is clear; a proof restricted without justification to nonsingular cases is incomplete.

Means need not vanish. The reduced statistic is generally not itself an orthogonal projection; what matters is equivalence of the information it carries with the parallel components. The empty reference case is immediate. No counterexample for excluded noise models is requested, and a solver need not repeat the scope caveat after proving the stated result.
