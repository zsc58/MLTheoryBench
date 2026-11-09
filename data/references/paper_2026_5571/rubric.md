# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Justifies the augmented lifted MSE and its smooth parameter dependence under the stated integrability assumptions, and establishes the equivariant quadratic and linear structure by Haar averaging. An equivalent pointwise-in-data argument followed by justified integration receives the same credit.
- **3 points:** Proves invariance of the lifted loss under every member of the stabilizer, accounting correctly for both quadratic and linear terms.
- **3 points:** Transfers the realized symmetry to left orthogonal invariance of the parameter risk and derives a valid differential or flow-equivariance consequence at every rank. Accept either a justified symmetric right-multiplier argument or the equivariance of the full coupled gradient field used in a complete uniqueness proof.
- **2 points:** Proves exact equality of the parameter ranges throughout the solution interval, including exclusion of finite-time rank loss, and concludes conservation of every stated smooth function of the range. Accept either an invertible right fundamental matrix with justified coefficient regularity or the two-sided equivariant-flow uniqueness argument.

# Evaluator Notes

Accept a complete valid alternative proof. The point allocations assess mathematical obligations, not the reference proof's incidental presentation choices. In particular, a complete reflection-and-uniqueness proof need not additionally construct a symmetric multiplier or a fundamental matrix.

For a Gram-factorization proof, equality of Gram matrices identifying orthogonal orbits establishes only set-theoretic factorization. It does not by itself establish smoothness of a quotient function at singular Gram matrices. A correctly stated applicable smooth invariant-factorization theorem with its hypotheses verified is acceptable; merely naming orthogonal invariant theory or the polynomial first fundamental theorem does not supply this regularity argument.

A pointwise identity \(\nabla_P R=PA\) without adequate time regularity of \(A\) does not by itself exclude rank loss. A fundamental-matrix proof must justify a continuous or otherwise sufficiently integrable coefficient and invertibility. An alternative uniqueness proof must establish equality of ranges, not only forward inclusion, and must account for the auxiliary parameters in the coupled flow.

Do not require a full-rank assumption, a homomorphism \(a\mapsto B_a\), or differentiability of that choice. Do not penalize a solver for declining to infer smoothness of the range map across rank strata. The consequence concerns smooth parameter functions on the open domain specified in the task. No global-in-time existence or preservation of rank at a limiting endpoint is required.

An unsupported invariance transfer, an unclosed arbitrary-rank argument, or failure to establish exact range equality is theorem-critical. Omission of a particular moment formula or fundamental matrix is not a gap when a complete valid alternative closes the same obligation.
