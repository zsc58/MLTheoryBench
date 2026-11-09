# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the exponential-family expression for \(D_{\mathrm{KL}}(p_\eta\|q_{\mathrm{ref}})\), with expectation under \(p_\eta\) and the correct cancellation structure.
- **4 points:** Performs the local Taylor expansions, identifies \(\nabla^2A(\eta_{\mathrm{ref}})=F_{\mathrm{ref}}\) using the natural-parameter score differentiated before reference evaluation, and obtains \(D_{\mathrm{KL}}=\tfrac12\delta^{\mathsf T}F_{\mathrm{ref}}\delta+R_3(\delta)\) with a uniform bound \(|R_3(\delta)|\le C\|\delta\|^3\) throughout \(\|\delta\|<r\). Merely naming Taylor expansion or Fisher information without carrying out the cancellation earns substantially less.
- **2 points:** Applies the minimum and maximum eigenvalue Rayleigh bounds to prove both sides of the quadratic KL sandwich with the cubic error term.
- **2 points:** Correctly characterizes equality of the upper leading quadratic coefficient by membership in the dominant eigenspace, including repeated maximal eigenvalues, and handles the zero-displacement case appropriately.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental presentation choices, the particular value \(C=2M/3\), or separate expansions if an alternative argument proves the same uniform remainder bound. The standard exponential-family Fisher/Hessian identity and standard spectral equality characterization may be invoked with their applicable hypotheses; reproducing their elementary derivations is not mandatory. Differentiating the already fixed distribution \(q_{\mathrm{ref}}\) as a constant is not the reference score. Equality concerns the leading quadratic coefficient, not necessarily equality in the full KL upper bound containing its remainder. A gap in the Taylor remainder or Fisher/Hessian identification is theorem-critical; propagate it to the sandwich only when the sandwich is not independently justified.
