# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly defines the forward and swapped pair measures and establishes, from characteristic-kernel MMD convergence (including the needed pair-law tightness/subsequence argument), that their signed difference converges weakly to zero against C_0(S^2).
- **4 points:** Establishes the central reversibility-to-target transfer: using tightness, a compact product-space cutoff, strict positivity and continuity of the transition density, and detailed balance, converts convergence of the transition-weighted antisymmetric measures into convergence of the target-weighted antisymmetric measure. The argument must control tails/cutoff errors and not merely name a lemma or method.
- **2 points:** Correctly marginalizes the target-weighted antisymmetric signed measure and proves convergence of \(\int u\,d\nu_l\) to \(\int u\,d\pi\) for every bounded continuous \(u\).
- **2 points:** States and verifies the sequential quantifiers and all required analytic hypotheses (tightness, positivity/continuity and normalization of the transition density, detailed balance, and the RKHS/MMD conditions), yielding the exact weak-convergence conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the pair-law tightness/subsequence closure, the compactness/tail argument, or an unjustified division by the transition density as a theorem-critical gap.
