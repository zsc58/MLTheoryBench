# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes the causal stochastic-kernel setup for whole structured fields, including the independent recursive DAG product and kernel-replacement intervention semantics. An iid-noise invariance and conditional-equivariance calculation is a valid supporting step, but is not mandatory in an alternative proof of the requested identification claims.
- **3 points:** Correctly applies standard do-calculus soundness to the full causal DAG with its fixed observed marginal, obtaining the stated observational functional. Explains why the stated existence and support conditions make conditional evaluations independent of arbitrary versions. Does not substitute the unavailable full endogenous joint distribution for the observational input.
- **3 points:** Transfers ordinary nonidentifiability witnesses into the index-transform model class. Verifies equivariance and noise requirements, equality of the entire structured observational laws, and preservation of a differing interventional outcome marginal at an actual coordinate of the assigned intervention. Does not require the intervention to be constant or require an intervention to preserve symmetry.
- **2 points:** Correctly invokes ordinary nonparametric do-calculus completeness and concludes the converse by the indistinguishable-model argument. Checks the scope of the external theorem or supplies the elementary latent-query reductions and empty cases needed for the task's full domain. Keeps the completeness class unrestricted by the support conditions of a chosen soundness derivation.

# Evaluator Notes

Accept any complete valid alternative proof and mathematically equivalent organization of the points. Do not require the reference proof's incidental presentation choices or a separate derivation of a supporting equivariance identity when the two target claims are already established.

The standard independent soundness and ordinary nonparametric completeness theorems may be cited without reproving them, provided their relevant statements and application hypotheses are clear. A bare appeal to completeness for an unspecified restricted model family is insufficient. A construction preserving only a one-coordinate observational marginal is insufficient unless the argument also establishes equality of the full observational input. Conditional existence at a null configuration alone does not establish identification there.

Do not demand ergodicity, mixing, locality, amenability, finite coordinate-state spaces, or finite-data estimation arguments: those are not hypotheses or targets of this task. Do not assume treatment or outcome vertices are observed unless the proof justifies that reduction. Empty outcome and empty-index cases are trivial normalization cases and must not be excluded by an additional substantive assumption.

Naming equivariance, factorization, or completeness without establishing its role in the target does not earn the corresponding points. Deduct downstream points when a missing dependency leaves a conclusion unsupported. No private GT proof obligation remains unresolved.
