# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Coverage of the intervention conditions (2 points):** Correctly proves that Condition II supplies the marginal preservation and conditional independence required by Condition I, or directly proves the conclusion under Condition II with those properties justified. Marginal preservation must use unchanged assignments outside the affected descendants. The graph condition must be used to remove every edge from Y into an original forbidden child. Interventions are independent-noise replacements, not a claim that their outputs are independent of their descendants.
2. **Common-version and conditional-mean identification (3 points):** Justifies a common stable-blanket conditional-law version valid under every fixed environment, including environments with zero observational probability. A direct structural argument is acceptable, as is a precisely stated applicable kernel result with its hypotheses checked. The reference construction uses the fixed kernels at Y and the retained children and observes every other parent of those children; its exact presentation is not required. Also proves the additional-variable separation or an equivalent argument giving E_e[Y|X_(D^c)]=f_S(X), then uses Condition I's conditional independence to identify E_e'[Y|X]=f_S(X). Merely applying augmented-law global Markov and declaring an observational version valid for every e does not close this step. Invariance of D^c is not separately required when the necessary identities are established environmentwise.
3. **Conditional risk comparison (3 points):** Conditions on the full covariate vector and applies strict mean consistency to the conditional law, checking integrability and the finite-expectation domain. Derives R_e'(f)>=R_e'(f_S). When competitor risk is infinite, recognizes that the comparison is immediate; no subtraction of infinities is permitted. Strictness is not needed to claim uniqueness of a minimax predictor, and no such uniqueness is required.
4. **Risk transfer and worst-case conclusion (2 points):** Uses the common conditional law of Y given X_S valid under the two selected environments and equality of their X_S marginals to obtain equality of the joint laws of (Y,X_S), hence equality of stable-blanket risks. Takes suprema in the correct order and concludes optimality over all measurable predictors. Does not assume that a supremum is attained or that the family of environments is finite.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's ordering, an explicit reduction lemma, its posterior-recursion presentation, or invariance of the complement when unnecessary to the alternative argument. The proof must cover both alternatives in the public assumption; a proof only under Condition I does not cover the full task unless the Condition II branch is also justified.

Graph sets are computed in the fixed augmented deployment graph. The stable blanket contains covariate indices only; another parent of a retained child does not include Y as an observed feature.

Ordinary conditional independence is an almost-sure distributional statement. Neither the common SCM's existence nor environmentwise Markovness alone permits upgrading an arbitrary observational conditional-law version to every fixed e. A proof can construct a suitable common version without claiming that every observational version is suitable. Do not require positivity, common densities, or discrete environments as a substitute.

Deduct substantially for omitting the common-version or conditional-mean identification bottleneck or the environment-by-environment risk transfer. The failure of a particular observational version is not, by itself, a counterexample to existence of a suitable common version or to the minimax conclusion. Empty intervention sets, an empty stable blanket, and infinite worst-case suprema require no additional nondegeneracy assumptions. No faithfulness, training-graph restriction, sampling model, or follower utility condition is required.
