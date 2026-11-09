# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Anytime validity (3 points).** Establish attainment of a null competitor, fixed-competitor mixture supermartingale validity, runner-up monotonicity, and the three-event epsilon/3 decomposition including the simultaneous unseen-category union bound. Handle p_r=0 without evaluating M_t(0), and respect the empty-observed-competitor convention. The covering failure events need not be disjoint.
2. **Category-size-free upper rate (3 points).** Prove the conservative runner-up reduction, maximal-count/concentration control, growth of the pairwise mixture, target LCB growth and unseen-threshold decay, and sum fixed-time failure tails to obtain the stated expectation and almost-sure stopping with universal constants. Verify the empirical-frequency restriction when inverting M_t(q), and retain the positive logarithmic normalization log(3/epsilon), including p_r=delta=1 and epsilon approaching one. Do not combine nonmonotone conditions by taking only the maximum of their first hitting times.
3. **Hidden-competitor lower bound (2 points).** Construct a feasible null/alternative pair differing by a target-mass split, compute the stopped KL, and derive the log(1/epsilon)/p term by data processing. Verify label availability, alternative-class membership, and use the same certifier under both laws. Null nontermination is permitted and must not invalidate the stopped-experiment argument. An alternative argument proving this contribution receives the same credit.
4. **Close-competitor lower bound and combination (2 points).** Construct a feasible adjacent-mode pair, compute the stopped KL and its p/delta^2 consequence, and combine the delta<=p/2 and delta>p/2 regimes to obtain the full minimax lower bound. Equivalent information comparisons or a single construction establishing the entire stated lower rate are acceptable.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular lower-bound constructions. Failure to control unseen competitors, or failure to establish either contribution to the stated lower rate, is theorem-critical unless a valid alternative argument supplies the missing conclusion. Naming concentration or change of measure without verifying the necessary bounds earns only partial credit. Standard independent inequalities may be cited with their relevant hypotheses checked; paper-specific intermediate results cannot simply be assumed. The public upper bound includes an explicit source-local logarithmic normalization repair, recorded privately in provenance. All reference-proof obligations are closed; there is no GT quality warning.
