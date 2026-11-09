# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly uses covariate shift to identify the same measurable class-posterior functions \(\eta_k(Z)\) under both domains, with the appropriate domain-specific almost-sure meaning. Recognizes that the label indicators and posterior functions are integrable.
- **4 points:** Derives both types of domain-specific conditional-expectation identities. For top-label correctness, justifies \(\mathbb E_d[\mathbf 1\{L_A=1\}\mid Z]=\eta_A(Z)\) using that \(A\) is measurable and deterministic given \(Z\), and then validly conditions on \(M\). Also derives the identity conditional on \(R_k\) for every class. The tower property applies because the score statistics are measurable functions of \(Z\). These identities initially hold almost everywhere under their respective domain score laws.
- **3 points:** Uses absolute continuity of each comparison measure with respect to both relevant score laws to transfer the two domain-specific identities outside a comparison-measure-null set. Establishes both directions of the top-label equivalence and both directions of the simultaneous class-wise equivalence for every class.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or an explicit proof of standard conditional-expectation facts when they are correctly invoked and their applicability is clear.

A complete proof must respect the stated almost-everywhere comparison. Merely fixing arbitrary versions, or saying that the conditional quantities are 'defined in both domains', does not justify pointwise identities at score-null values. A concise correct treatment of exceptional sets is sufficient; elaborate measure-theoretic machinery is unnecessary.

Do not require mutual absolute continuity, source-to-target support inclusion, continuity of conditional probabilities, positive mass at every individual score, perfect source calibration, or a sampling model. These are not assumptions of the task. Conversely, a proof that adds such a substantive restriction establishes only a special case unless it also handles the stated general setup.

No separate numerical calculation is required for ties, constant scores, boundary posterior values, or zero comparison measures when the general bounded-variable argument already covers them. If the score laws are mutually singular, their common absolutely continuous comparison measure is necessarily zero, so the relevant almost-everywhere statements are vacuous.
