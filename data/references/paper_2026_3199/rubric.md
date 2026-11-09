# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Relevant ideas but no complete correct proof step.
- **3-7:** Some correct core steps, but important steps are missing.
- **8-9:** Complete and essentially correct, with minor repairable errors.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derive the lifted invariance identity from the true local martingale by taking expectations. Correctly use the push-forward joint law, the initial-law averaging, and absolute integrability for Fubini. Preserve the quantifier that the neighborhood may depend on the initial time and law.
- **3 points:** Identify the value on the closed time interval from normalization and the terminal condition. Use the law Itô formula and a short-time limit, or an equivalent valid argument, to identify the advantage for t<T at every parameter in the corresponding neighborhood. Establish the terminal base-parameter equality by continuity. Direct use of the terminal invariance identity is an acceptable alternative to a fully justified classical uniqueness argument.
- **2 points:** Establish the parameter-sensitivity identity rather than merely citing it. Justify parameter continuity of the law flow, derive the performance-difference identity for the fixed base value, and control differentiation using the continuous parameter derivative on compact flow images. An arbitrary-increment remainder argument or another proof of full differentiability is required; directional derivatives alone are not automatically enough. Do not require a common martingale neighborhood along the entire trajectory.
- **2 points:** Apply the stipulated action/joint-law chain rule with the state law and candidates held fixed. Include both the direct action term and the action-coordinate joint-law derivative term, with the correct independent-copy evaluation and Jacobian orientation. Justify the final time/expectation interchange.

# Evaluator Notes

Accept any correct alternative proof. Do not award credit for merely naming a method or invoking an unspecified audited sensitivity theorem. Standard law Itô and elementary SDE estimates may be used when their hypotheses are checked. A specialized external continuity theorem is not necessary: the stated Lipschitz assumptions allow a direct same-noise coupling proof.

The chain rule itself is an explicit hypothesis; a solver need not derive it from stronger differentiability assumptions. Do not award additional required-proof credit for proving existence or uniqueness of the local candidates: only their integrated quantities are identified.

The corrected task does not assert off-policy advantage identification at an initial time equal to T. The martingale condition is then vacuous, and continuity alone does not supply a uniform parameter neighborhood. Do not penalize a solution for restricting off-policy rate identification to t<T. Conversely, do not accept an unsupported off-policy terminal extension as a necessary proof step. The value equality and base-parameter terminal advantage equality remain part of the task.

The reference proof closes all theorem-critical obligations; no private-GT warning applies.
