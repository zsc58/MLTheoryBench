# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly uses the base and perturbed classes, support agreement, nonnegative-radius uncertainty, eta, rho, and the source-faithful signed-difference perturbation cost. Mere repetition of the setup is not necessary.
2. **4 points:** Proves the first inequality by comparing with a support context and obtaining TV control by 2 eta. A valid kernel-contraction argument or an arbitrary-event signed-measure argument is sufficient. A supremum over individual output atoms alone does not establish TV control.
3. **4 points:** Proves the second inequality using the actual signed-difference cost. At each positive-mass perturbation output, bounds a support-agreeing comparison pair by base uncertainty at rho, controls the remaining signed residual by its comparison infimum and then E, and combines this with mixture convexity and the outer suprema. Equivalent valid arguments receive full credit. The comparison infimum is pointwise in the output; an unjustified interchange with an output supremum or mixture is not acceptable.

# Evaluator Notes

Accept a complete valid alternative proof and any rigorously established stronger bound. Do not require the reference proof's incidental notation or presentation choices. Infimum attainment need not be proved, because taking an infimum of inequalities with a comparison-independent left side suffices; an epsilon argument is also acceptable.

The radius rho can equal zero, and the definition of uncertainty includes that case. Do not require discussion of infinite or empty optimization sets: the repaired setup makes all relevant sets nonempty and all quantities finite.

Support identifiability is not a public assumption. A proof that invokes it without justification does not prove the general second bound. Showing E=0 under an additional identifiability assumption is an optional corollary, not a requirement for full credit and not a substitute for the requested unconditional decomposition. A sum of distances between perturbed comparison laws is a different cost and cannot replace the cost in the task.
