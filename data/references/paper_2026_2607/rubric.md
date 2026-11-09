# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly differentiates the integral construction to obtain \(\phi'(r)=g(r)/r\) and \(\phi'(r)+r\phi''(r)=g'(r)\ge0\), including the stated regularity and finiteness conditions.
- **3 points:** Uses the logarithmic/exponential reparameterization to prove convexity of the constructed loss in \(t\), and establishes \(\ell\ge0\) with \(\ell(1)=0\), thereby satisfying the loss definition.
- **3 points:** Correctly differentiates the loss as \(g(e^t/y)-g(y/e^t)\) and uses \(|g|\le M\) to obtain the uniform bound \(|\partial_tL|\le2M\).
- **2 points:** Applies a valid bounded-derivative argument (for example, the mean-value theorem) to conclude global \(2M\)-Lipschitz continuity, while preserving the ratio-based form and all quantifiers.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The convexity and derivative-bound arguments are theorem-critical; merely naming a reparameterization or a Lipschitz criterion without carrying out the inequalities does not earn the corresponding points.
