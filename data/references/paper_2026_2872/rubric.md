# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derive continuity and order-(beta-1) regularity of the oracle price map, an appropriate Taylor remainder, and a positive uniform instance-wise interior local-curvature radius. Check the stated smoothness convention, including integer smoothness and utility-interval endpoints.
- **2 points:** Specify the coarse-to-fine policy sufficiently to analyze it. Prove uniform empirical concentration and coarse localization, handle incomplete and empty bins, and construct a feasible binwise polynomial comparator with loss O(eta^2+h^{2beta-2}).
- **3 points:** Derive the unbiased convex-bandit reduction with the correct analytical conditioning and learner information. State a valid independent noisy BCO result and verify its action-set, loss, Lipschitz, noise, and oracle-access hypotheses. Establish a prefix-valid learner without giving it future bin visit counts, sum bin regrets, and include localization failures to obtain the conditional decomposition.
- **1 point:** Prove unbiased uniform-price pseudo-responses, dimension-free scalar prediction confidence, pilot-side separation, and ~O(d eta^{-2}) exploration cost. Combine and optimize to obtain the integrated rate and the quantified large-horizon regime. A generic self-normalized vector-confidence invocation with an unaccounted dimension factor does not establish this step.
- **2 points:** Derive a centered localized smooth-tail family in the explicitly defined normalized class, including bounded valuations on its actual context support and geometry on its full supplied utility interval. Prove signed oracle shifts, local-regret aggregation, the paired adaptive-transcript KL bound including queries from other cells, a decoder/testing inequality, and hypercube aggregation with the stated policy/horizon/instance quantifier order.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular named BCO implementation. The existing coarse-to-fine architecture in the target must be satisfied, but exact private tuning constants need not be reproduced when equivalent choices are justified.

The upper policy is nonanticipating. Conditioning on the entire exogenous context sequence or future coarse observations is an analytical device and does not grant information to the policy. The lower bound quantifies over all admissible nonanticipating policies, not only policies with separated pilots.

The normalized context space is a subset of [0,1], and its supplied structural interval need not be [0,1]. Do not reject a valid centered hard family merely because it uses a smaller translated interval. Conversely, verify bounded valuations, mean-zero noise, common structural bounds, and the normalized radius; assertions of family membership alone earn no completed membership step.

General independent background theorems may be invoked with an explicit relevant statement and checked hypotheses. A paper-specific support lemma, specialized construction, or named method is not a substitute for its missing derivation. The reference proof now derives its internal normalization, anytime wrapper, scalar confidence, determinant count, and lower-bound mechanisms; there is no outstanding GT quality exception.

Do not require the original erroneous generic self-normalized pilot argument. Its source-grounded replacement conditions on the context-measurable exploration design and uses scalar weighted concentration. Propagate a missing pilot or lower-bound dependency only when the corresponding conclusion is unsupported. Mere optimization of the displayed rates cannot compensate for an unsupported theorem-critical reduction or converse.
