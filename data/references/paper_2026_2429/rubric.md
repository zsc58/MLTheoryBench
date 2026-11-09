# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expands the CPD response, establishes the fixed-core linear representation, and differentiates the regularized least-squares loss to obtain `H_{kk}=beta A^(k)^T A^(k)+gamma I`.
- **3 points:** Derives the cross-core derivatives componentwise for `k != m`, including the residual derivative, the derivative of the design factor when `r=p`, and the index pairing `Z^(k)_:r Z^(m)_:p`.
- **4 points:** Correctly forms `D^(k,m,r,p)=diag([Z^(k) odot_R Z^(m)]_:(r,p))`, the residual-dependent `E^(k,m,r)=diag(f-y)diag([Z^(k,m)]_:r)`, and combines them as `T=D+delta_{rp}E` for every distinct pair of cores.
- **1 point:** Assembles the component blocks into the stated cross-core Hessian formula with the correct beta, feature-matrix factors, indices, and scope `k != m`.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A theorem-critical omission in the componentwise cross-core derivation is a major gap even if the final formula is stated. Award full credit only when the D index pairing is consistent with the requested block convention.
