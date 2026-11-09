# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly applies the chain rule to the trajectory and derives and solves \(\varepsilon'(t)=-\lambda\varepsilon(t)\), including the exponential score-error formula for every \(t\ge0\). The argument must cover zero initial score error and must not divide by a possibly zero gradient on the level set.
- **2 points:** Uses continuity and score convergence to prove that every omega-limit point belongs to \(B_\alpha(x)\).
- **3 points:** Under the eventual gradient lower bound, derives an integrable exponential velocity bound and uses it to establish Cauchy convergence to a limit, or supplies an equivalent valid convergence argument.
- **2 points:** Shows the limit belongs to \(B_\alpha(x)\), proves uniqueness of the limit of the given trajectory, and obtains the stated exponential distance estimate with the correct constant and range \(t\ge T\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solution must justify the scalar decay and the pointwise convergence and rate rather than merely name a gradient-flow or convergence method. Propagate a missing score-decay step to later claims only when those claims are unsupported without it.

The ODE holds almost everywhere for a locally absolutely continuous trajectory. Consequently, almost-everywhere differential identities must be integrated to obtain the claimed identities and bounds at every relevant time. A classical differentiable-trajectory argument is acceptable if it justifies its use under the stated solution convention.

The first conclusion does not require existence of an omega-limit point. The set \(B_\alpha(x)\) is the explicitly defined score level set; no equality with the topological boundary of \(C_\alpha(x)\) needs to be proved. Uniqueness concerns the limit of the given trajectory, not uniqueness of ODE solutions or equality of limits across different initializations. Do not require untied calibration scores, a compact trajectory, or a gradient lower bound before \(T\). The threshold is well-defined by the public index-domain assumption; no additional conformal coverage theorem is part of the task.
