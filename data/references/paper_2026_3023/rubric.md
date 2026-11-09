# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly derives the nominal-law change-of-measure/Jensen lower bound for each perturbed CTMC. Accounts for the finite-horizon likelihood-ratio compensator, its discounted integration, and the action-averaging relative-entropy-rate inequality. A valid direct derivation or a correctly stated standard finite-state likelihood formula with verified hypotheses is acceptable.
- **3 points:** Correctly introduces and uses the local cost `c`, and proves the statewise Gibbs/log-sum-exp inequality with the policy KL term. Zero policy probabilities must be allowed; a finite variational optimizer is not required.
- **3 points:** Converts the discounted-time expression to normalized nominal discounted occupancy with the factor `1/r`, applies uncertainty-set membership to obtain the `epsilon/r` penalty, and preserves all factors of `r` and the `log r` constant.
- **1 point:** Exponentiates the pointwise logarithmic bound and takes the infimum to state the exact worst-case-performance conclusion under the common-support and positivity assumptions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The policy is a probability vector on each state's available-action set, and may have zero probabilities. The reference policy, not the controlled policy, has full support on that set. Zero nominal occupancies, absorbing states, and `epsilon=0` are permitted. Do not demand irreducibility, a worst-case minimizing parameter, uniformly bounded rates or rewards over the whole parameter family, or finite attainment of an entropy-duality infimum.

A change of measure must be applied to the positive expectation before nominal-law Jensen, or justified by an equivalent valid argument. A Jensen bound under the perturbed law does not by itself authorize replacing that law by the nominal law with a relative-entropy penalty.

Because occupancy is normalized, `sum_s bar d(s)g(s)=r E_theta^pi[int_0^infty exp(-rt)g(S_t)dt]`. A missing factor `1/r` in the reverse conversion is a substantive proof error unless corrected before the conclusion.

Pointwise positivity of model rewards alone does not prove positivity of an infimum over models. Establishing the common pointwise lower bound and then taking the infimum avoids this issue. An extended-real logarithm argument is also acceptable if its conventions and inequalities are justified.
