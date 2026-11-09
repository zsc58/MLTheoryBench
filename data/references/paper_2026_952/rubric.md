# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the conditional correlation drift and all needed lower bounds. The proof must handle the actual monotone-link assumptions, explain the local learning-phase lower bound without using either extra burn-in assumption, and treat zero tangential projection correctly. A symmetry proof or appropriate Stieltjes integration by parts is acceptable; an exact ordinary-derivative identity cannot be asserted for an arbitrary non-absolutely-continuous monotone link.
- **2 points:** Establishes conditional subexponential increment control and a scale-sensitive maximal martingale bound sufficient for the epochs. Verifies conditional centering, predictability, stopping/envelope conditions, and probability allocation. A finite-horizon maximal bound with deterministic stopped envelopes is sufficient; the specialized time-uniform theorem is not mandatory. A variance-floor-one bound alone does not establish fluctuations smaller than one.
- **2 points:** Controls normalization and combines drift, stochastic fluctuations, and normalization in valid stability and improvement arguments. Accounts for random crossings without conditioning away the martingale property. For convex burn-in, uses correct threshold-spacing fluctuation scales and correlation-proportional normalization, or another valid argument with the same guarantees.
- **2 points:** Iterates warm-start epochs to obtain both learning schedules, pure-exploration complexity, and the stated iterate-based regret bound, including truncated epochs. Distinguishes the exploration epoch duration of order d/alpha from the regret epoch duration of order d/(alpha epsilon).
- **2 points:** Establishes both burn-in guarantees. Under the derivative lower bound, uses the corrected rate Theta-tilde(1/d) and proves O-tilde(d^2) time. Under convexity, supplies a valid schedule, proves the next-threshold guarantee for every permitted starting correlation, controls total failure probability, and justifies the sum-to-integral comparison and the infinite-integral convention.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, exact logarithms, or particular stopping thresholds. All source-local corrections recorded in provenance are part of the audited reference, not errors a solver must reproduce.

Theorem-critical omissions in adaptive correlation control, concentration scaling, epoch iteration, or convex burn-in are major gaps. Merely citing a specialized concentration theorem or naming SGD earns no credit for an unverified application. In particular, the unsupported O(1/d) fluctuation estimates from the original convex appendix must not be accepted as established facts.

The source's printed Theta-tilde(1/d^2) rate for the derivative-lower-bound burn-in conclusion is corrected to Theta-tilde(1/d), as forced by its explicit supporting schedule. Do not require the erroneous rate. Do not require finite-time conclusions from an infinite complexity integral or require an algorithm to evaluate an unknown correlation. Do not substitute action regret for the public iterate-based target, although proving both is acceptable.
