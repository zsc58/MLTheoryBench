# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Identification and certificate transfer (2 points).** Derives the target inverse-propensity identity, or an equivalent conditional-expectation argument, from consistency, conditional ignorability, and overlap. Uses nonnegativity of the target reward to obtain R* >= (R-U)_+, proves policy-wise domination, and extends it to the population mixture at the realized posterior. The proxy inverse-propensity identity is optional and is not an additional scored requirement.
2. **Exact weighted-classification reduction (3 points).** Establishes the conditional mean of each action score and its connection to certified value, proves V_ell(d)=C_alpha^sharp-R_01^alpha(d), and obtains the Bayes action rule over measurable policies. The proof must respect the fixed-alpha scope of the optimization equivalence, handle zero advantage consistently, and justify the required measurability and integrability.
3. **Uniform fixed-temperature PAC-Bayes lower bound (3 points).** Proves the score range, obtains the stated loss normalization, and constructs a common high-probability event supporting the bound for all absolutely continuous posteriors, including sample-dependent choices. Derives the correct upper tail for population loss, with the stated K_epsilon, KL coefficient, log(1/delta), and eta/8, and transfers the result to latent target value. Infinite-KL competitors are vacuous. The requested event is uniform in Q, not in eta or n.
4. **Exact variational optimizer (2 points).** Solves the stated KL-regularized objective over probability measures Q<<Pi_0. Gives a positive finite normalizer and the normalized density, establishes the equivalence of the value and loss exponential forms, and proves uniqueness of the probability measure up to density null sets. A relative-entropy identity with an equality condition is sufficient; uniqueness of a policy parameter is neither required nor generally true.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Standard scalar concentration or entropy results may be used when their relevant statements and hypotheses are supplied and correctly checked; merely naming a PAC-Bayes bound or Gibbs optimizer does not establish the requested central steps. Do not require sample splitting, correct specification of nuisance regressions, finite parameter spaces, density assumptions on the prior, or a temperature-uniform result. Do not treat the displayed theorem conclusions as available assumptions. Deduct substantially for omitting the exact reduction, using the wrong concentration direction, replacing population-mixture value by an average over learning samples, or allowing a data-fitted certificate or hypothesis family outside the public setup. Boundary cases need not be discussed separately when the proof already covers them. No rubric step depends on an unresolved private proof obligation.
