# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly uses the canonical ranked lists, nested top-\(M\) sets, rank score (including \(+\infty\) for an absent class), calibration order statistic, and the \(k=n+1\) infinite-threshold convention. Correct use of definitions supplied in the task suffices; verbatim repetition is unnecessary.
2. **3 points:** Proves that, for arbitrary fixed agent parameter/output law, the augmented calibration and test constructions and their rank scores are exchangeable. A sufficient justification is that, conditional on the examples, auxiliary sampling is independent with the same query-dependent rule at every index, and the score construction commutes with index permutations. Merely asserting score exchangeability without connecting it to the prescribed construction does not complete this step.
3. **3 points:** Establishes the equivalence between test-set membership and \(T_{n+1}\le M^*\), then gives a valid exchangeable rank argument yielding coverage at least \(1-\alpha\). The proof must handle ties between scores, including ties at \(+\infty\), and full-universe coverage whenever the threshold is infinite. Suitable tied-score arguments include lower-rank counting or independent auxiliary tie breaking with a proved event inclusion.
4. **2 points:** Derives the no-tie value \(k/(n+1)\) and the \(1/(n+1)\) ceiling for \(k\le n\), then explicitly concludes that the lower bound is uniform over agent biases and output distributions because it holds for every fixed agent/kernel without an agent-quality restriction.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular lower-rank notation. Treat failure to justify score exchangeability or the order-statistic membership event as a theorem-critical gap; propagate it to the final coverage claim. Give credit for any mathematically correct treatment of ties and of the \(k=n+1\) edge case.

Frequency ties within a ranked candidate list and ties between calibration/test scores are distinct. Uniform frequency-tie breaking does not make the discrete scores tie-free. An ordinary score rank is not generally uniform when scores tie. A claim that ties only increase coverage must be supported by a valid comparison, counting argument, or a correctly stated applicable exchangeable-score result; it must not rely on unconditional uniformity of tied ranks.

An infinite threshold can arise either because \(k=n+1\) or because the selected calibration order statistic is infinite. In both cases the task specifies the full canonical universe, not merely the observed candidate pool. The claim is marginal coverage for a fixed level and fixed agent/kernel; conditional-on-calibration coverage and validity after arbitrary data-dependent agent or level selection are not required.
