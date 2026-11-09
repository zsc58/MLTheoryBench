# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly represents classifiers by measurable class-0 regions and reduces the loss minimization to maximizing `F_0(A)` subject to the mixture constraint `pi_0F_0(A)+pi_1F_1(A)<=b pi_0`.
- **4 points:** Proves the characteristic likelihood-ratio ordering argument, showing that the superlevel region `{f_0/f_1>gamma*}` dominates every feasible competing region and is therefore optimal.
- **2 points:** Uses the threshold choice and no-atom boundary condition to establish exact capacity attainment and the stated optimal classifier.
- **2 points:** Constructs normalized modified priors with ratio `pi'_1/pi'_0=gamma*` and proves that the corresponding Bayes rule has the same likelihood-ratio decision region (up to a null boundary).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The likelihood-ratio optimization and prior-reweighting identification are theorem-critical; merely naming Neyman-Pearson or Bayes classification without verifying the inequalities earns no credit for those steps.
