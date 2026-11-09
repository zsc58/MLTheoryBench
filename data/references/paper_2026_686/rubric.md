# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes a uniform positive radial-growth bound for the finite even coercive convex loss after bounded symmetric-noise smoothing. A correct derivation of equal asymptotic slopes is sufficient, but a direct uniform linear-growth argument is equally acceptable. Must cover superlinear losses for which the asymptotic slope is infinite; a finite attack size cannot satisfy a lower bound of infinity.
- **4 points:** Constructs an admissible attack for each prescribed p in (0,1/2), and rigorously obtains strict population separation at the true dynamics. For the alternating fully permitted construction, this includes boundedness or another valid verification of the uniform conditional attack-tail requirement, current-state measurability, fresh-noise timing, node permissions, conditional excitation, and a strictly negative population directional derivative. If using gradients, establishes population differentiability or otherwise excludes zero from the entire subdifferential. Merely exhibiting one nonzero subgradient is insufficient. Merely naming an adversarial method earns no credit for this step.
- **2 points:** Establishes almost-sure uniform convergence of the empirical objectives on the compact feasible matrix set, with valid integrability and dependence arguments. For an alternating construction, uses the correct average of its phase expectations. A claim that consecutive even losses are independent is not valid; a suitable finite-memory or residue-class argument suffices. Arbitrary finite convex losses need not have integrable envelopes merely because their arguments are sub-Gaussian.
- **2 points:** Uses the strict population separation and empirical optimality to rule out convergence to the true dynamics on a single probability-one event, simultaneously for every sequence of minimizers. Correctly handles feasibility of a descent direction, existence of minimizers, and the distinction between failure of almost-sure convergence and almost-sure exclusion of all convergent minimizer selections.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular bounded-noise distribution, a normalized attack rather than another admissible attack, an exact recession-slope identity, or KKT terminology when a direct descent argument suffices.

The noise law, tail constants, excitation constant, and attack size may be chosen as part of the existential instance. The attack probability p is prescribed arbitrarily in (0,1/2); proving the claim only for a specially selected positive p does not establish the full statement. The process must be fixed independently of T.

The public noise condition is causal: fresh noise is independent of the state and selected contemporaneous attack. Future attacks may depend on past noise through the observed trajectory. Do not impose independence of noise from all future attacks.

The adapted small-ball result cited in the source is not a prerequisite for full credit. Positivity of E||W|| for an explicitly chosen nondegenerate bounded noise law may be shown directly. A paper-specific citation without its needed statement and verified hypotheses does not close an otherwise unsupported obligation.

A theorem-critical omission in admissibility, strict population separation, empirical convergence, or the pathwise final contradiction is a major gap. Do not award complete-proof credit for a nonzero-subgradient argument without exclusion of zero. Do not double-penalize a single upstream gap merely because it propagates downstream. If all needed facts follow immediately from an explicitly bounded construction but a routine bound is omitted, treat that omission proportionately rather than demanding the reference proof verbatim.
