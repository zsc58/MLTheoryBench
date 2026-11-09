# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly uses the common record-local feature rule and independent record masks. Justifies that MAR makes the probability of an entirely missing record independent of its value, and hence that the observation probability `p` is one constant for all datasets and positions, not merely equal for one neighboring pair.
2. **3 points:** Establishes the common output component and the correctly normalized observed components. Constructs or rigorously justifies both required comparisons: between the two observed components and between an observed component and the all-missing component. For a coupling proof, verifies the marginals and explains why paired incomplete datasets agree outside the differing record. Equivalent direct finite-mixture arguments receive full credit.
3. **3 points:** Derives a valid amplified mixture calculation. For the reference route, sets `alpha=exp(epsilon)`, `alpha'=1+p(alpha-1)`, and `beta=alpha'/alpha`; checks `beta∈[0,1]`; and derives `D_{alpha'}(P||Q) ≤ p[(1-beta)D_alpha(R||C)+beta D_alpha(R||R')]`, or the equivalent event-wise identity and inequality. Both comparison terms must be controlled; no named amplification theorem may replace this theorem-critical derivation without an equivalent complete argument.
4. **2 points:** Applies the base DP guarantee to both comparisons and concludes the uniform algorithm-wide parameters `(log(1+p(exp(epsilon)-1)),p delta)` for all ordered neighboring pairs. Correctly covers identical inputs and the cases `p=0` and `p=1` without undefined conditioning, and obtains the larger-delta and MCAR conclusions. The proof must also remain valid for `n=1` and `delta=0` or `1`.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, divergence notation, or coupling terminology when the same obligations are established directly.

The inequality `D_{alpha'}((1-p)C+pR || (1-p)C+pR') ≤ p D_alpha(R||R')` is false for unrestricted components. A proof that relies on it without supplying a valid replacement has an important mathematical gap, not a cosmetic omission, and does not qualify as essentially complete. Correct preliminary work should still receive its corresponding credit. Bounding only the observed-to-observed comparison does not close the missing obligation involving the common component.

A coupling need not be maximal or optimal. A common residual mask together with independent draws from the two conditional record-mask laws is sufficient, provided its marginals and neighboring-input property are justified. The observed-to-all-missing comparison must also be justified.

Do not require conditioning on an event of probability zero. Direct treatment of the endpoints, or a construction defining unused components without such conditioning, is valid. For identical datasets no differing index is needed. The source model already requires the same feature rule at every position; replacing it by arbitrary record-specific rules and retaining an unexplained single global `p` is not a proof of the stated contract.
