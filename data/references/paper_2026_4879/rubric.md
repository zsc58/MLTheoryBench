# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly defines the support, normalized magnitude distribution, Shannon/Renyi entropies, and uniform distribution, with valid parameter and nonzero-vector conditions.
- **4 points:** Derives the Shannon identity `H=log_2 k-D_KL(pi||u)`, exponentiates to the ENZ decomposition, and proves the upper bound and exact equality condition using KL nonnegativity.
- **3 points:** Derives the Renyi identity `R_alpha=log_2 k-D_alpha(pi||u)` for every `alpha>0`, `alpha!=1`, exponentiates, and proves the corresponding ENZ upper bound.
- **1 point:** Correctly establishes scale invariance and the Renyi limiting cases `alpha->1` (Shannon) and `alpha downarrow 0` (support size).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
