# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Sampling and confidence control:** Correctly uses the factorized transition and effective-context observations. Justifies concentration despite adaptive visits, for example by union-bounding over deterministic prefixes of context sample streams. Distinguishes fixed optimal-value slices from arbitrary data-dependent functions. Obtains the minimum confidence parameter for optimal slices and the support-dependent uniform bounds needed for adaptive gaps or variances. Accounts for counts zero and one.
- **3 points — Optimism:** Proves optimism for the specified conditional, individually clipped recursion at every stage, state, and episode. Handles the empirical bonus's dependence on the optimistic value function, for example through a proved monotone maximum-bonus envelope. A fixed-function Bernstein inequality applied without justification to a data-dependent value function is insufficient. Averaging over the known marginal and maximizing over actions must be justified.
- **3 points — Variance-sensitive regret analysis:** Controls the optimistic-minus-executed policy value gap, not merely the optimism gap. Derives an adequate one-step residual inequality and propagates it to an episode bound. In the reference route, this includes the negative squared-gap cancellation, explicitly defined clipped uncertainty recursions, and the H^2 bound on expected cumulative optimal-value conditional variance. A joint-transition variance bound controls the average over Y of conditional variances, not each conditional variance separately. Naming a specialized method or a paper-specific lemma does not establish these obligations.
- **2 points — Visitation control and final rate:** Correctly handles episode-start counts when a context can recur within the episode, establishes the needed high-probability conversion between conditional expectations and realized visitation contributions, and performs the final Cauchy-Schwarz and harmonic summations. Derives the requested rate with probability at least 1-delta and with logarithmic, rather than additional polynomial H or K, losses. Retains the logarithmic floor when |Y|=1.

# Evaluator Notes

Accept a complete valid alternative proof and universal constants other than the reference values. Do not require the reference proof's incidental presentation choices or exact intermediate numerical constants.

The reference visitation proof establishes the aggregate order needed for the theorem directly; an answer need not reproduce the source's sharper intermediate visitation statement. Conversely, merely citing that specialized statement without a proof or an independently justified applicable theorem does not close the visitation obligation.

Standard scalar concentration results may be cited when their relevant form and hypotheses are clear. Specialized monotonicity, visitation, and variance-recursion claims must be justified, not accepted solely because the paper cites them.

The public algorithm clips each conditional estimate before averaging over the known Y marginal and uses past episodes for its estimates and policy. An analysis of a different recursion is not automatically a proof for this algorithm. The regret is the sum of value-function differences at the observed initial states, not realized reward shortfall.

Unvisited and unreachable contexts, support bound one, and singleton X or Y are admissible. No initial coverage assumption or lower bound on positive transition probabilities may be added.

Missing concentration, optimism, squared-gap or equivalent variance control, or stale-count visitation control is theorem-critical. The replacement reference proof supplies all of these obligations; there is no unresolved private ground-truth warning.
