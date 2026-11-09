# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives E_{X~R_X}||mu_{Y|X}-mu_{Z|X}||_{H_ell}^2=Tr(Delta^*Delta C_XX), using the conditional operator representation and a justified expectation-to-trace argument or an equivalent valid method.
- **3 points:** Correctly establishes ||mu_XY-mu_XZ||_{H_k tensor H_ell}^2=||Delta C_XX||_{HS}^2 under the common reference marginal. A valid derivation through cross-covariance factorization or directly through conditional expectation is acceptable.
- **2 points:** Rigorously obtains CMMD_1^2=Tr(Delta^*Delta C_XX) and CMMD_2^2=Tr(Delta^*Delta C_XX^2), thereby connecting the family definition with both embedding discrepancies. Uses valid adjoint, trace, and self-adjointness manipulations, or an equivalent spectral argument.
- **3 points:** Proves for every real s>=s'>=0 the bound CMMD_s^2<=sigma_max^(s-s') CMMD_{s'}^2 via a valid operator or spectral argument. Covers s=s' and sigma_max=0, either explicitly or through reasoning valid in those cases.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, named cross-covariance operators, a named kernel chain rule, or a separately displayed general trace identity if the requested conclusions are proved rigorously.

The conditional and joint embedding identifications are conclusions to be proved, not assumptions granted by the setup. Merely deriving traces from the family norm definition does not establish those identifications.

Treat an unproved embedding identification or a missing eigenvalue-controlled hierarchy as a theorem-critical gap. A specialized citation alone does not replace a derivation of the kernel-chain-rule identity in this task.

For a trace-based hierarchy argument, do not accept an unrestricted assertion Tr(AB)<=||A||_{op}Tr(B), or an unsupported claim that Delta^*Delta C_XX^{s'} is positive. A positive sandwich, a valid spectral sum, or the Hilbert-Schmidt ideal inequality resolves this issue.

A solver need not rederive Hilbert-Schmidt regularity from the smoothness condition, because the public setup explicitly supplies the bounded Hilbert-Schmidt conditional mean operators. Likewise, no estimation-rate theorem is required.

Use the stated scalar convention sigma_max^0=1 even when sigma_max=0. Do not demand division by sigma_max or exclusion of zero covariance. Omission of an elementary boundary-case sentence is minor only when the actual argument remains valid at that boundary.
