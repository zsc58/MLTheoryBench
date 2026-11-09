# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Bayes conditional risks and routing rule (2 points).** Defines measurable conditional probabilities \(\pi_k=\Pr(Y=k\mid X)\) and \(\rho_j=\Pr(M_j=Y\mid X)\). Correctly computes individual class and expert risks as \(1-\pi_k\) and \(1-\rho_j\), compares their minima, and justifies that a measurable finite-action selector attains the population Bayes infimum. Policies use only \(X\); expert predictions need not be deterministic functions of \(X\).
2. **Exact surrogate-excess decomposition (3 points).** Conditions on \(X\), derives the entropy-plus-KL identities with the correct \(\lambda/J\) factor, and obtains the exact population excess as the expectation of categorical KL plus weighted Bernoulli KL terms. Justifies that the entropy baseline is finite and equals the population infimum, attained by the conditional probabilities in the closed probability domains. Handles zero probabilities and expert endpoints through the stated extended-real conventions rather than imposing positivity of the true probabilities.
3. **Plug-in regret control (3 points).** Establishes the four action-type comparisons, including cross-type cases and true-utility ties, or gives an equivalent general argument covering them. Obtains the \(2\max\{e_c,e_e\}\) estimate or another sufficient bound. Applies Pinsker correctly: its Bernoulli form first bounds \(|u_j-\rho_j|\), after which the maximum expert error is bounded using the maximum or sum of the expert KL divergences. Derives the pointwise calibration inequality with a constant no larger than the requested one.
4. **Population transfer and consequences (2 points).** Handles infinite surrogate risk, and in the finite-risk case applies Jensen or an equivalent valid inequality to obtain the population bound with \(\max\{2\sqrt2,\sqrt{2J/\lambda}\}\). States Bayes consistency for fixed problem parameters and explains independence from \(J\) when \(\lambda/J\) is fixed.

# Evaluator Notes

Accept a complete valid alternative proof, including a stronger calibration bound that implies the requested one. Do not require the reference proof's incidental presentation choices or a literal four-case split if another argument covers all cases.

Do not accept a proof only for deterministic expert functions, independent experts, strictly interior true probabilities, or finite-risk estimates without an argument covering the omitted source-admissible cases. Distinguish an easily corrected notation slip from an unclosed theorem-critical inference. In particular, the inequality \(e_e\le\sqrt{B_j/2}\) for every \(j\) is not a valid application of Pinsker; the valid coordinatewise inequality concerns \(|u_j-\rho_j|\). Missing routing cases not covered by another argument, an incorrect weighting factor, or an unsupported calibration constant are theorem-critical gaps when they leave the conclusion unproved.

The source proof's strict true-utility comparison in the Bayes-predicts case is corrected to a non-strict comparison. No extra strict-margin assumption is allowed. Endpoint log losses are defined in the public task, and all reference-proof obligations are closed.
