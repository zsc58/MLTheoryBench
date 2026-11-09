# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly derives the incremented local posterior by conditional exponential reweighting and verifies the weighted conditional moment identity for \(T_c\). Conditional identities need hold only on supported states. The signed target is handled by coefficient-wise conditional averaging, not by assuming it is a probability vector.
- **3 points:** Reduces the objective to conditional cross-entropy against \(q^+\), establishes that its value at \(q^+\) is finite, and proves the stated almost-everywhere unique minimizer using the KL equality condition. The finite-optimum argument must justify subtracting the optimal loss when candidate losses may be infinite. A valid route uses the masked-coordinate survival probability and the finite-alphabet entropy bound; other valid bounds are equally acceptable.
- **3 points:** Converts normalized excess loss into the local-KL integral under \(\mathbb P^+\) and proves the required path-KL identity or an equally sufficient path-KL bound. Accounts for equal total exit rates, pre-jump evaluation, terminal behavior at time 1, and extended-real cases. Support conditions are understood up to true jump-exposure null sets. Merely asserting that every pointwise support failure makes path KL infinite is not correct. Positive candidate probabilities alone do not imply finite KL.
- **1 point:** Applies or proves data processing from path law to terminal law to obtain exactly the claimed terminal-KL inequality, with the stated normalization by \(Z\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular dominating measure, or its particular negative-part bound.

The rate model permits arbitrary measurable probability kernels, zero probabilities, terminal distributions without full support, and schedule intervals with zero hazard. A proof restricted to strictly positive kernels must justify its extension to the full stated domain. Likewise, a bounded-time likelihood formula must be extended to the terminal endpoint or replaced by an argument directly valid for the finite-jump path.

Establishing terminal completion and a finite optimum may be integrated into other steps rather than presented separately. Do not require a quantitative small-step assumption, nondegeneracy of the target, strict positivity of the hazard, or positivity of every terminal mass; none is part of the task.

All reference-proof obligations are closed. There is no private ground-truth completeness warning.
