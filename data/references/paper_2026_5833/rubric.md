# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Proves the blind-fiber conditional invariance. One route factors the posterior-sample mixture as \(\rho(r,b)g(r)\), with \(g\) independent of \(b\), and cancels it to conclude \(q_\rho(b\mid r)=\rho(b\mid r)\) almost everywhere. The argument must justify normalization and cancellation on a full-measure set, or provide an equivalent valid conditional-distribution argument.
- **3 points:** Establishes the relevant conditional Gaussian laws with positive conditional variances and derives the exact truth conditional coverage formula with \(\delta\), \(s_\rho/s_*\), and \(z\). Standard Gaussian conditioning may be used with its hypotheses verified; an explicit matrix formula is not required if the conditional-law argument is otherwise complete. The result concerns conditional, not blind-marginal, intervals.
- **1 point:** Establishes that, at zero mean gap, coverage is below nominal exactly when \(s_\rho<s_*\), and proves that coverage decreases as \(|\delta|\) increases at fixed width ratio. Symmetry and differentiation, or another valid argument, suffice.
- **3 points:** Demonstrates non-identifiability using distinct positive-definite Gaussian truths with identical measurement laws. The argument must show actual changes in the claimed scalar quantities, including coverage or its deficit, rather than merely assert that different blind conditionals necessarily have different coverage. It must establish the measurement-statistic and fixed deterministic-archive consequences, holding the known likelihood, regularizer, and archive rule fixed. A pair with nominal coverage under one truth and undercoverage under the other directly proves the detection claim.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular perturbation witnesses. Do not award credit for merely naming posterior invariance, Gaussian conditioning, or non-identifiability without deriving the corresponding claims.

The allowed operator may have rank zero. A complete proof must remain valid when conditioning on the resolved coordinate is absent; this may be handled by an explicit case or a clearly applicable zero-dimensional convention. Do not require full row rank, covariance alignment, or positive rank.

Non-identifiability is a statement about the Gaussian parameter class with all known objects fixed. It does not mean that every pair of distinct blind conditionals has different coverage, nor that a diagnostic can never output an undercoverage flag. Identical laws under a nominal-versus-undercovering pair establish the absence of discriminating information.

The private reference proof has no unresolved theorem-critical obligations.
