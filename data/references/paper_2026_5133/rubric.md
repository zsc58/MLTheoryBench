# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes conditional optimism, learner-bias control by gamma_t Q_t, and the conditional second-moment bound. Reduces the expected loss difference for each fixed comparator to estimated-loss difference plus the bias sum, with the maximum over comparators outside the expectation.
- **3 points:** Gives a valid adaptive exponential-weights analysis with the stated history-dependent rates. Handles normalization and the change in learning rate, justifies taking conditional expectations of the second-moment terms, and gives a valid summation argument obtaining R_T<=4 E[sqrt((d+sum_t Q_t) log d)]. A bare assertion of this adaptive bound or invocation of an unspecified summation lemma is insufficient.
- **3 points:** Derives the directed graph control of Q_t from the independence number. A valid discretization and graph-expansion proof, or another complete derivation of the weighted bound, is required. The standard unweighted directed harmonic inequality may be used if its relevant statement is given and its application is justified; merely citing the final weighted bound is insufficient. Any auxiliary assertion allowing zero weights must handle zero denominators or omit zero-mass vertices correctly. A proof confined to the strictly positive probabilities of this algorithm need not prove an unnecessary zero-weight extension.
- **2 points:** Uses Q_s<=d to lower-bound gamma_t, obtains the specified H_t expression with the correct ceiling and constants, and substitutes the pointwise graph bound inside the expectation to reach the exact stated conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The adversary may adapt both losses and graphs to past actions. Restricting the argument to an oblivious adversary or to deterministic graph sequences does not prove the whole task. Conditional analysis of the privately selected current graph does not authorize the learner to use it before selecting its arm.

Regret is the maximum over expected comparisons with fixed arms. Do not replace it with an expectation of a maximum or with a realized best-arm loss subtracted outside the expectation.

The final expectation is essential when the independence numbers are random. It may be omitted only under an explicitly justified deterministic special case, which alone is not a complete proof of the public task.

All theorem-critical obligations in the reference proof are closed. There is no unresolved private dependency to treat as a completed scoring step.
