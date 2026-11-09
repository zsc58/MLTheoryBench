# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly differentiates the stated loss with the activations and targets held fixed, obtains the additive chunk update, and accumulates it over all specified prior positions. The update has coefficient lambda, with no chunk-size normalization.
- **3 points:** Expands the query logit change and validly applies finite-sum linearity of expectation and the unrelated-position assumption to isolate the matching position. Uses the fixed nature of embeddings and targets when taking their coefficients outside expectations. The stated integrability assumptions justify the expectations.
- **3 points:** For LM-aligned targets, proves the correct-logit lower bound and the epsilon bound for every incorrect logit using alignment, norm, and near-orthogonality assumptions.
- **2 points:** For reconstruction targets, applies the unrelated-position assumption to that target choice and proves the epsilon-scale bound on the correct next-token logit using $k^*\ne v^*$ and near-orthogonality.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its source-audit commentary. Treat omission of either target comparison or failure to establish the expectation reduction as theorem-critical gaps.

A proof may invoke the stated finite expectations and standard finite-sum linearity without repeating measure-theoretic details. It need not separately re-prove the asserted chunk partition or reconstruct the hidden-state distribution. An unnecessary but unused independence assertion should be distinguished from a proof that actually requires an unstated independence assumption.

The conclusions concern absolute values of expected changes, not expectations of absolute changes. Do not require an almost-sure positive alignment, and do not accept replacing the stated signed alignment mean by an unstated absolute-moment bound.

The task concerns the query evaluated after every specified prior chunk has been updated. It does not ask for the same conclusion at arbitrary positions inside an unevaluated or not-yet-updated chunk, or for an implementation with clipping, averaged losses, or additional transformations of the analytical targets.
