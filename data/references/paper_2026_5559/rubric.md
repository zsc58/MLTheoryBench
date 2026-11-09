# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(3 points)** Correctly analyzes the explicit PTQ setting: verifies existence of the Hessian at the prescribed reference and identifies the proxy; constructs one open interval containing scale 1; places the good codeword inside the specified Euclidean basin; and excludes every proxy minimizer from that basin, uniformly for every integer bitwidth B>=2. A lattice comparison must cover all indices, not just five nearby points or one fixed finite codebook. In the reference approach, both the finite strict comparisons and the uniform estimate for the remaining indices require justification.
2. **(1 point)** Derives the precise stated true-loss lower bound. The bound supplies an affine-in-sharpness lower bound in the admissible fixed-parameter regime; exact linear behavior under arbitrary parameter variation is not required.
3. **(2 points)** Establishes valid weighted normal-distance calculus and discrepancy estimates under the general setting's assumptions. In the reference approach, this includes the gradient identity using normal-space preservation, its Lipschitz bound, and the quantized normal-distance estimate when both arguments are in U.
4. **(3 points)** Proves the positive drift margin and the per-step decrease with the exact stated constants and step-size restrictions, including locality and latent-basin invariance. The argument must establish that deployed gradient evaluations and update segments stay in U before applying assumptions that are available only there. An induction must not assume the next latent iterate is in the basin in order to prove its descent.
5. **(1 point)** Proves finite entry and obtains the explicit bound for the actual first deployed-entry index. A sufficient distance threshold must not be identified with the first entry without justification; earlier deployed entry is allowed. Preserves the exact initialization and positive step-size conditions.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's comparison codeword, auxiliary strip, five-index set, or presentation choices. The two settings are separate: do not require the explicit example to satisfy the recovery setting's bounded-gradient or width conditions, and do not impose Hessian existence or stationarity on the general recovery initialization.

A theorem-critical missing drift estimate, invalid projection control, unsupported uniform PTQ minimizer comparison, or circular locality argument is a major gap. Propagate a failed dependency only when the downstream conclusion is thereby unsupported. Correctly observing that a displayed radius or scale is fixed in one setting does not authorize transferring its assumptions to the other setting. No credit-bearing obligation depends on a specialized external result or an unresolved reference-proof step.
