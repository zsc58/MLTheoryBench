# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly applies standard backdoor adjustment and total probability to derive p_theta(y | do(H=h)) = integral p_theta(y | h,z)p_theta(z) dz on the stated observational conditional-distribution domain. Identifies the blocked backdoor paths, the no-descendant condition, and overlap. Does not claim identification at unsupported h from arbitrary observational conditional versions.
- **2 points:** Correctly expands the adjusted conditional using the conditional latent factorization over U and V and the label kernel independent of V. Formulates the joint integral or sum. Respects the almost-everywhere conditional identities and the transfer to the adjustment marginal permitted by overlap. Does not assume observational independence of Z and H.
- **4 points:** Derives the variational inequality using the product posterior and Jensen, or a complete valid alternative argument. Under only q << P, compares the full model likelihood integral with the integral restricted to variational support; does not require or assert an unjustified exact importance-sampling equality. Obtains the reconstruction expectation and all three correctly oriented KL divergences. Justifies the use of the given positivity, log-integrability, and finite-KL conditions, and avoids separately subtracting divergent expectations of log densities.
- **1 point:** States both conclusions with the prescribed conditional-distribution scope and explains why the V expectation drops from the reconstruction term while its KL penalty remains.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not require reverse absolute continuity or strictly positive variational densities on the whole model support. In discrete H, the almost-everywhere scope includes every positive-probability h satisfying overlap. In non-atomic H, the task does not require a pointwise identity at arbitrary exceptional versions. Equivalent explicit well-definedness arguments are acceptable, but a proof of the unchanged displayed inequality must cover the task's admissible domain rather than imposing additional support assumptions.
