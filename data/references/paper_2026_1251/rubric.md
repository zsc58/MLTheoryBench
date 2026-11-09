# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Buffered private-search rank guarantee (2 points).** Correctly analyzes the noisy binary search, establishes the simultaneous Gaussian good event with probability at least 1-beta_n, and proves qhat >= S_(r+m_n).
2. **Finite-sample conformal rank transfer (3 points).** Uses exchangeability of ideal scores for the 1-alpha rank event and rigorously controls test-score flips and excessive training down-crossings via Lipschitz stability, anti-concentration, no ties, and the Markov buffer, obtaining the stated lower bound with all correction terms.
3. **Synchronized projected-DP-SGD stability (3 points).** Derives the one-step coupled recurrence, including clipping, projection, extra-sample gradient and noise-normalization effects, then unrolls it to the explicit E_n bound.
4. **Asymptotic recovery (2 points).** Chooses u_n, delta_n, m_n, and beta_n as specified, verifies the scaling and admissibility conditions, and proves convergence of the lower bound to 1-alpha.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
