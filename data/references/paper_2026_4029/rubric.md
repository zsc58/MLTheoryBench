# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the exact telescoping identity `(1/T) sum M_t = q + (a_1-a_{T+1})/(lambda T)` from the adaptive recursion.
- **4 points:** Correctly establishes by induction the invariant `a_t in [-lambda,1+lambda]`, including the cases `a_t <= 0` and `a_t >= 1` and the corresponding whole-space/empty-set implications for `M_t`.
- **3 points:** Uses the invariant and the initial-range assumption to bound `|a_1-a_{T+1}|` by `1+lambda` and concludes the stated deterministic deviation bound for every `T >= 1`.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The result must remain pathwise and must not introduce independence or stationarity assumptions.
