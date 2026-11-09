# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly treats the gate as the specified scalar function with independent arguments and positive denominators, and connects its sensitivities to evaluations at the ensemble statistics. Correctly distinguishes the scalar asymptotic from an impossible divergence of probability means. Equivalent notation is acceptable; introducing `r` or explicitly writing `1-F=exp(-r)` is not mandatory.
- **3 points:** Derives `partial F/partial u=exp(-u/(w v))/(w v)>0`, establishes strict increase in the first argument, gives the right-hand boundary value `1/(w v)` at `u=0`, and establishes gate saturation and vanishing mean sensitivity for fixed positive `v,w`.
- **3 points:** Derives `partial F/partial v=-u exp(-u/(w v))/(w v^2)`, establishes nonpositivity, and distinguishes strict negativity for `u>0` from the zero derivative and constant gate at `u=0`.
- **2 points:** Derives `partial F/partial w=-u exp(-u/(w v))/(w^2 v)`, establishes its sign and zero-mean boundary behavior, and completes the vanishing limits for spread and scale sensitivities in the stated fixed-parameter regime. A valid justification of `r exp(-r)->0`, or an equivalent elementary exponential-decay argument, suffices.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, auxiliary notation, or particular exponential estimate.

At the ensemble evaluation, the zero-mean sensitivities are `1/(kappa_c sigma_c)`, `0`, and `0`. Since zero empirical mean forces `sigma_c=epsilon`, the equivalent first value `1/(kappa_c epsilon)` is also correct. Do not require both equivalent forms.

Partial derivatives are taken in the independent arguments of `F`, not through the ensemble-statistic formulas. Do not require a derivative of empirical standard deviation with respect to member predictions, including at consensus or when `C=1`.

The final asymptotic is for each fixed positive pair `v,w` in the declared scalar domain. An argument that treats actual probability means as unbounded without distinguishing this scalar interpretation does not correctly address the domain. Conversely, pointing out that empirical means are bounded does not by itself discharge the explicitly stated scalar-limit obligation.

Treat claims of strict negativity at `u=0` as a theorem-critical error unless the boundary is explicitly corrected. A common exponential factor alone does not justify limits with uncontrolled varying prefactors; the fixed-parameter condition must be respected.

Do not require or reward an additional claim that mean sensitivity decreases globally with spread, or that all sensitivity magnitudes are globally decreasing in spread or scale. Those claims are not part of the task. The private source-repair calculation is not an additional scored obligation.
