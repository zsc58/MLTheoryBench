# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly defines the component losses and Jensen gap, and proves the exact decomposition of mixture log loss into weighted component loss minus Jensen gap.
2. **3 points:** Uses the stated uniform upper-tail condition to obtain the simultaneous lower bound on expected Jensen gaps, with the correct orientation and the term \(\sqrt{2ns''\log(2/\delta)}\).
3. **3 points:** Correctly derives or invokes a simultaneous PAC-Bayes inequality for the weighted component losses in the conditional probability space where the predictive densities and prior are fixed, verifying the conditional sub-Gaussian hypothesis and obtaining the KL, \(ns^2/2\), and \(\log(2/\delta)\) terms.
4. **2 points:** Combines the two inequalities by a conditional union bound, cancels the weighted component terms, and states the final uniform bound for every posterior weight vector.

# Evaluator Notes

Accept any complete valid alternative proof under the stated conditional assumptions. The confidence split may use any \(\delta_1,\delta_2>0\) with \(\delta_1+\delta_2=\delta\), provided the resulting constants are correct. Do not award credit for merely naming concentration or PAC-Bayes without a correct inequality, justified conditional applicability, and a valid combination of the bounds.
