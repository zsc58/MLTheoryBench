# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Comparison and strictness.** Proves $Q_T^\star\le2LS_T^\star$ and gives a checked smooth convex family with $Q_T^\star/(LS_T^\star)\to0$.
- **4 points: Central projected-gradient conversion.** Derives the dual smoothness inequality, inserts it into the projection recursion, and completes the square with the correct $1/(1-\eta L)$ factor.
- **2 points: Telescoping and tuning.** Derives the comparator bound and both step-size regimes yielding $\max\{2LD^2,D\sqrt{2Q_T^\star}\}$.
- **2 points: Sharp deterministic lower bound.** Establishes correct algorithm/sequence quantifiers, identifies $Q_T^\star=M^2T$, and proves $R_T(w^\star)\ge D\sqrt{Q_T^\star}/4$.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the particular strict-separation family or moment estimate, but do require the central conversion rather than merely naming a method.
