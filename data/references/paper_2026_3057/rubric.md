# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Proves slack invariance, introduces the residual, and derives the exponential time change and dual rescaling.
- **4 points:** Derives the active-set residual system and establishes the common quadratic dissipation margin, including control of Jacobian variation. Merely naming a Lyapunov method earns no credit for this step.
- **2 points:** Applies scalar comparison to obtain the rescaled residual and dual decay with the stated exponent \(\alpha\).
- **2 points:** Converts back to \(t\), bounds \(\operatorname{ReLU}(h(x_t))\) using \(s_t\ge0\), and concludes feasibility and both rates.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the private proof's presentation choices or notation.
