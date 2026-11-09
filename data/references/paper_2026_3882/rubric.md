# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes task-level rank-set coverage. Correctly assigns the directional composite nulls, obtains family-wise error at most alpha_task/2 for each family, and explains why absence of false rejections implies L_j(t)<=l_j(t) and U_j(t)>=u_j(t), including tied true scores. A precise statement and valid application of the standard Holm FWER result is acceptable; reproving that standard result is not mandatory.
- **3 points:** Correctly uses the stated ascending-order construction, verifies 1<=k_l<=k_u<=N under the given parameter range, and justifies the common-law processing of complete task-data records. An auxiliary future evaluation record may be introduced for analysis, but must not be used to construct the reported interval. Merely repeating the two index formulas does not establish all of this step.
- **3 points:** Establishes both finite-sample endpoint inequalities, P(L_j*<L_j)<=k_l/(N+1)<=alpha_leader/2 and P(U_j*>U_j)<=(N+1-k_u)/(N+1)<=alpha_leader/2, or equivalent sufficient bounds. The argument must be valid with ties. A leave-one-out counting proof, justified independent tie-breaking argument, or correctly stated and justified equivalent order-statistic argument is acceptable.
- **2 points:** Proves the final event inclusion and applies the three-event union bound to obtain total miscoverage at most alpha_task+alpha_leader, giving the claimed marginal guarantee for every fixed model.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award credit for merely naming Holm, exchangeability, or conformal calibration without explaining how the relevant hypotheses and conclusions yield the required inequalities.

Within-task p-values may be dependent. The lower and upper endpoint arrays, and the three final error events, need not be independent. Do not require a simultaneous guarantee across models or a guarantee conditional on the observed records.

The endpoint values are discrete, so equality of unrandomized ranks with a uniform distribution cannot be assumed. In particular, replacing the strict endpoint failures by non-strict events is not justified: constant endpoint arrays are allowed. Explicit randomized tie-breaking is one valid proof device, not an additional assumption on the data or the procedure.

The boundary alpha_leader=2/(N+1) is admissible and gives k_l=1, k_u=N. Full-width intervals and tied true scores are allowed. No condition alpha_task+alpha_leader<1 is required; the asserted bound may be vacuous outside that range. The proof need not guarantee nonempty reported intervals on error events.

All theorem-critical obligations in the reference proof have explicit closure. There is no unresolved specialized external dependency and no GT quality warning.
