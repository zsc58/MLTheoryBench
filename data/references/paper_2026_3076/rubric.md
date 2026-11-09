# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establish absolute-continuity propagation, the adjoint moment identity and fixed point, and prove KL contraction using mixture convexity and Markov-kernel data processing.
- **2 points:** Derive the normalized-exponential projection objective and its first-order information-projection inequality. Prove the quadratic approximation bound, including the bounded-image and KL-curvature arguments, then iterate the population recursion.
- **3 points:** Establish the uniform fitted-loss excess bound from the four specified localized complexities. Verify curvature, self-normalized transition denominators, normalizer control, localized initial and transition processes, and peeling; explain why the event applies to every data-dependent iterate.
- **2 points:** Convert exact empirical minimization to a population excess bound and prove the approximate-projection perturbation inequality using the target lower bound. Obtain and iterate the recursion for population-normalized fitted outputs with the stated dependence on gamma.
- **1 point:** Transfer the final population-normalized bound to generalized KL for empirically normalized outputs, including K=0 and the event's simultaneous validity for all K.

# Evaluator Notes

Accept any complete valid alternative proof. Naming projection geometry or concentration tools without deriving their applicable inequalities and verifying their hypotheses does not close the corresponding steps. In particular, a recursion for population-normalized iterates cannot simply be asserted for empirically normalized generalized-KL errors; the final normalization transfer must be justified.
