# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes SCOPE unbiasedness under the stated sequential stopping and conditional-probability definitions. A conditioning proof must use the inclusive endpoint, justify prefix measurability of eligibility, and justify any exchange of expectation with an infinite nonnegative sum.
- **3 points:** Derives the exact identity \(\operatorname{Var}(\widehat\mu_{\rm SCOPE})-\operatorname{Var}(\widehat\mu_{\rm MC})=\mathbb E[U_1(U_1-1)]/n\), including iid sample-mean scaling, and derives the strict-improvement criterion.
- **4 points:** Proves that no positive prevalence threshold guarantees strict variance improvement. A counterexample proof must produce admissible models with arbitrarily small positive prevalence and establish \(\operatorname{Var}(\widehat\mu_{\rm SCOPE})\ge\operatorname{Var}(\widehat\mu_{\rm MC})\). It must verify the relevant score values, moments, or variances and explain why the construction defeats every positive threshold. The reference proof establishes the stronger strict reversal, but equality counterexamples are also sufficient for the stated target.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, vocabulary, path enumeration, or particular counterexample. Merely naming a construction without verifying its properties is insufficient. Conversely, do not require strict reversal when equality already refutes the claimed universal strict improvement. The hypotheses allow termination to be recognized from the current sampled token; a proof must not replace this with a stronger predictable-endpoint assumption. The variance identity must remain valid at prevalence zero or one, and the impossibility witnesses must have strictly positive prevalence. No result about an outcome-avoiding sampling law is required.
