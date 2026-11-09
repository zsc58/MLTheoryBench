# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Scaling correspondence (2 points):** Defines the bijection phi(x) = Lx between the two domains, respects D >= 1 and 0 < L <= 1, and uses ell_1 = c sqrt(D) and ell_L = c L sqrt(D) with c > 0.
2. **Kernel and Gram preservation (3 points):** Derives equality of normalized pairwise distances under phi and uses isotropy/stationarity to prove equality of all corresponding kernel entries and Gram matrices.
3. **Information-gain preservation (2 points):** Correctly applies the common Gaussian-noise log-determinant formula, or equivalently matching finite-dimensional Gaussian laws, to show equal information gain for every corresponding design.
4. **Maximum information gain equality (3 points):** Uses bijectivity on N-point designs to transfer the attainable information-gain sets and their suprema, concluding gamma_N(X_1,k_{ell_1}) = gamma_N(X_L,k_{ell_L}) for every N >= 1.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
