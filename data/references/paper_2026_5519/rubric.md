# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Masked/full error derivation (3 points):** Expands the expected squared errors under the explicit Gaussian noises, obtains the discarded-energy plus active-noise formula, and proves the exact iff criterion.
2. **Score moments (2 points):** Proves score unbiasedness and computes the Gaussian score variance.
3. **Pairwise misranking (3 points):** Derives the difference mean/variance and applies Chebyshev to the stated bound.
4. **TopK recovery (2 points):** Uses the boundary-pair union bound and obtains the \(1-\delta\) consequence under the sufficient gap condition.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation. Do not award full credit for merely naming concentration or a ranking method without the moment and union-bound derivations.
