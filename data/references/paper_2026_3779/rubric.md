# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulate the conditional law of the forecast given its T-value and its probability-measure barycenter, with the relevant measurability and almost-sure qualifications, or provide a rigorous equivalent argument. Standard-Borel disintegration may be used as a foundational result.
- **4 points:** Use distribution calibration to identify the barycenter with the conditional outcome law; justify equality as probability measures rather than merely making an uncountable intersection of probability-one events; establish concentration on the appropriate T-level set; and apply mixture-level-set closure to obtain conditional T-calibration. Merely naming disintegration or closure earns no credit for an absent principal derivation.
- **3 points:** Starting from conditional calibration alone, apply the two fixed-distribution identification inequalities to the conditional outcome law, justify evaluation at the X-measurable shifted endpoints, and integrate to obtain both unconditional inequalities for every epsilon greater than zero. Handle signed expectations under the stated existence conditions, without assuming additional absolute moments. A bare invocation of an 'identification bridge' or of the conditional-to-unconditional implication itself does not close this step.
- **1 point:** State the integrated implication with the correct quantifiers, almost-sure conditional conclusion, and both unconditional inequalities, without strengthening or weakening the target.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular disintegration notation. Routine foundational measure-theoretic facts may be used when their applicability is clear.

The task's identification assumption is the pair of fixed-distribution endpoint inequalities. It does not require the expected identification function to have T(R) as its exact zero set, or to vanish at either endpoint. Arguments imposing either extra condition do not prove the full task.

The source's prediction-error/expectation-form assumptions remain part of the task, but a valid proof need not use every assumption. In particular, the direct conditional-kernel argument does not require separate algebraic case analyses of the two forms.

Degenerate intervals are allowed. All positive epsilon values must be covered; there is no restricted prediction interval and no need to pass to epsilon zero. Treat omission of an endpoint inequality, an unjustified principal level-set concentration claim, or failure to prove the second implication independently of distribution calibration as theorem-critical. Distinguish these failures from a routine omitted explanation of a standard null-set or kernel-integration argument.
