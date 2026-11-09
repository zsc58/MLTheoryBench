# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Adversarial family and optimality (2 points).** Defines admissible one-type, K=1 environments with bounded MNL parameters and a designated B-set, and proves that the designated set is the unique optimal full-capacity assortment. Handles the unit match-reward convention and explains why the benchmark is appropriate on these environments.
2. **Regret decomposition (2 points).** Derives a quantitative instantaneous gap proportional to the perturbation and the number of designated sellers omitted, and sums it to lower-bound cumulative regret. Covers actions of size less than B without assigning the policy unobserved feedback from artificially padded actions.
3. **Sequential information bound and aggregation (4 points).** Correctly compares neighboring environments; bounds the proposal-law KL; accounts for the observed seller decisions and the common policy kernels; accumulates information over the complete relevant history; applies Pinsker or another valid change-of-measure inequality; and quantitatively aggregates the comparison. For the reference route, the neighbors have designated-set sizes B and B-1 and the averaging uses the exact pair count. Merely citing a per-period KL bound does not justify comparing unconditional later adaptive actions. No logarithmic exploration requirement follows from admissibility alone.
4. **Parameter tuning and conclusion (2 points).** Chooses a valid horizon-dependent perturbation, maintains a positive averaged omission bound, and obtains the stated log-squared lower bound with a positive constant depending only on N and B. The reference proof uses a perturbation proportional to T^(-1/2), first obtains an N,B-dependent sqrt(T) bound, and then converts it to the requested rate. Covers the stated horizons and boundary cases.

# Evaluator Notes

Accept any complete valid alternative proof under the stated model and parameter bounds. Do not require the particular constants, coupling, family notation, or presentation used above. The final rate and permitted constant dependencies must be established quantitatively; unsupported appeals to a paper-specific lemma do not suffice.

The task does not demand a dimension-uniform constant. Do not award credit for claiming that B-dependent factors cancel unless the displayed inequalities actually establish that claim. Do not require a logarithmic lower bound on individual offer counts, an efficiency assumption on policies, or the previous GT's 1/log(NT) perturbation. A proof using such a route must independently justify it under the task's unrestricted admissibility contract.
