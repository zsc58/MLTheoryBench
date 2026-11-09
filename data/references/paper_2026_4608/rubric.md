# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Reference-Proof Status

The reference now contains a complete proof of the public target. It does not invoke the specialized external master regret theorem recorded as theory_018. Instead, it explicitly controls the fraction of particles outside a proof-only confidence radius, compares a selected good particle with a good optimistic particle, derives the bounded martingale estimate, and sums the resulting regret inequalities.

The generic external theorem remains unproved in the supplied paper, but is no longer an unresolved dependency of this reference. A solver may use a different complete route; reproducing the reference's particular radius or event allocation is not required.

# Core Steps

- **2 points:** Correctly handles the sequential experiment and confidence bounds. Actions must not anticipate fresh perturbations. Establishes the true-parameter ridge-confidence event and perturbation self-normalization, and explains how fresh uniform selection controls selected-particle radii without introducing a log(m) factor into the final regret bound. Any additional particle-fraction events used later must have justified probability bounds.
- **4 points:** Derives the characteristic exceedance mechanism, or a valid replacement. For the Brownian route, constructs the embedding with a legitimate progressive filtration, verifies predictable coefficients and zero cross-covariations, and explains the common-clock property. Proves the time-uniform Brownian exceedance estimate using the Lamperti transition, short-interval fluctuation control, independent binomial counting across particles, Chernoff, and a union bound. Standard DDS, Knight, Gaussian concentration, and Chernoff results may be used when their relevant statements and hypotheses are clear. Merely naming a specialized mechanism does not establish it.
- **2 points:** Gives the Lipschitz estimate and deterministic sphere-net transfer from threshold 1/20 to 1/40, including the all-particle radius event. Verifies that m>=2000d log(n/delta) suffices for every allowed m, rather than merely claiming the right asymptotic order or checking one chosen ensemble size.
- **2 points:** Closes the optimism-to-regret argument and final substitution. One point concerns a valid conditional comparison that controls nonoptimistic rounds and a justified martingale summation. In the reference route, a positive fraction of particles must be both good and optimistic, and a minimum-width member of that set is compared with the selected good particle. The other point concerns the beta-radius event needed for optimism, degenerate optimal actions, potential estimates, gamma control, failure accounting, absorption into a universal constant, and the lambda=80 soft-O consequence.

# Evaluator Notes

Accept a complete valid alternative proof. The Brownian route, the good-particle-fraction argument, and the reference's numerical failure allocation are not mandatory when an alternative establishes the same public conclusion.

A theorem-critical omission of the embedding, time-uniform exceedance estimate, uniform-direction transfer, or regret reduction is a major gap when no alternative closes it. Propagate a failed dependency only when it leaves the final conclusion unsupported. The global score descriptions take precedence over mechanically adding points for steps whose dependencies have failed.

A precise citation of the specialized external master theorem can establish what a proposed application would require, but does not by itself supply its derivation under this task's proof-completeness standard. Either derive the needed reduction or give a complete alternative, as the revised reference does. The elliptical-potential calculation alone does not control nonoptimistic rounds.

Do not treat unconditional independence of a predrawn Gaussian array as independence from actions that can inspect it. Do not apply a common-time Brownian exceedance estimate to different particle-specific clocks without additional justification. Do not claim that a union bound over all particles yields a radius independent of m. Do not infer a beta-radius confidence inequality merely from membership in a larger b-radius ellipsoid.

When using the reference's replacement reduction, distinguish unconditional martingale estimates from conclusions imposed afterward on an intersection of high-probability events. Do not condition on a future good event and then assume that the original martingale differences remain centered. The action-width conditional means must be taken with respect to the pre-index history.

The source's exact auxiliary numerical prefactor is not a public target. Correct changes to numerical constants and private confidence parameters are acceptable when absorbed into the public universal C, when the public algorithm is unchanged, and when the final probability is at least 1-4delta. The earlier source-local confidence-event repair remains relevant, but the current complete reference no longer depends on its conditional invocation of the master theorem.
