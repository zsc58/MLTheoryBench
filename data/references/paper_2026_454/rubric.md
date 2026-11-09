# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the normalized base joint, its marginal data density, and the support-aware importance weight. Recognizes that conditional normalization holds for prior-almost every parameter and that the marginal integrates to one.
- **2 points:** Expands the second moment under the base joint into the integral involving powers \(r^{2\beta-1}p_X^{2-2\beta}\), with appropriate support and endpoint conventions.
- **4 points:** For \(\beta\in(1/2,1)\), chooses valid conjugate Holder exponents \(u=1/(2\beta-1)\) and \(v=1/(2-2\beta)\), applies the inequality for prior-almost every parameter, and integrates the resulting unit bound over the prior.
- **2 points:** Handles \(\beta=1/2\) using the support-indicator bound and \(\beta=1\) directly, then correctly concludes finite variance from the second-moment bound.

# Evaluator Notes

Accept a complete valid alternative proof and allocate credit for equivalent mathematical achievements. Do not require the reference proof's incidental presentation choices or its particular inequality. When Holder is used, merely naming it without verifying the exponents and the normalized integrals is insufficient.

Tonelli applies to the nonnegative normalization and second-moment integrands; prior integrability of the squared weight must not be assumed. A concise use of the fact that a probability marginal integrates to one is sufficient. It is also acceptable to work with finite density versions and standard almost-everywhere conventions without reproducing the reference proof's full null-set discussion. Do not require common support, strict positivity everywhere, or bounded densities.

At \(\beta=1/2\), the second moment can be strictly below one. An assertion that it always equals one needs correction when conditional supports differ. At \(\beta=1\), the weight is one almost surely, irrespective of its assigned values on null sets.

The conclusion concerns finite variance of the importance weights. Claims about an arbitrary unbounded self-normalized estimator require a separately specified estimator and appropriate integrability analysis and are not part of this task.
